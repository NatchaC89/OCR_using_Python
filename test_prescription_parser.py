import os
import sys

fpath = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(fpath)

from src.parser_prescription import PrescriptionParser
import pytest


@pytest.fixture()
def doc_1_maria():
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K



Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_2_natcha():
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Natcha Cota Date: 5/11/2022

Address: 8 badminton court, new Thai, AC

K



Prednisone 20 mg
Lialda 2.4 gram
Dolly 2 kg

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month
Dolly - eat every one

Refill: 20 times
'''
    return PrescriptionParser(document_text)


@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')


def test_get_name(doc_1_maria, doc_2_natcha, doc_3_empty):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
    assert doc_2_natcha.get_field('patient_name') == 'Natcha Cota'
    assert doc_3_empty.get_field('patient_name') == None


def test_get_address(doc_1_maria, doc_2_natcha, doc_3_empty):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
    assert doc_2_natcha.get_field('patient_address') == '8 badminton court, new Thai, AC'
    assert doc_3_empty.get_field('patient_address') == None


def test_get_medicine(doc_1_maria, doc_2_natcha, doc_3_empty):
    assert doc_1_maria.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_natcha.get_field('medicines') == 'Prednisone 20 mg\nLialda 2.4 gram\nDolly 2 kg'
    assert doc_3_empty.get_field('medicines') == None


def test_get_directions(doc_1_maria, doc_2_natcha, doc_3_empty):
    assert doc_1_maria.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_natcha.get_field('directions') == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month\nDolly - eat every one'
    assert doc_3_empty.get_field('directions') == None

def test_get_refill(doc_1_maria, doc_2_natcha, doc_3_empty):
    assert doc_1_maria.get_field('refills') == '2'
    assert doc_2_natcha.get_field('refills') == '20'
    assert doc_3_empty.get_field('refills') == None

def test_parse(doc_1_maria, doc_2_natcha, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] == 'Marta Sharapova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['medicines'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert record_maria['directions'] == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert record_maria['refills'] == '2'

    record_natcha = doc_2_natcha.parse()
    assert  record_natcha == {
        'patient_name': 'Natcha Cota',
        'patient_address': '8 badminton court, new Thai, AC',
        'medicines': 'Prednisone 20 mg\nLialda 2.4 gram\nDolly 2 kg',
        'directions': 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month\nDolly - eat every one',
        'refills':'20'
    }

    record_empty = doc_3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'directions': None,
        'refills': None
    }