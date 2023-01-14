import os
import sys

fpath = os.path.join(os.path.dirname(__file__), 'src')
sys.path.append(fpath)

from src.parser_patient import PatientParser
import pytest


@pytest.fixture()
def doc_1_Kathy():
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine
'''
    return PatientParser(document_text)


@pytest.fixture()
def doc_2_empty():
    return PatientParser('')


def test_get_name(doc_1_Kathy, doc_2_empty):
    assert doc_1_Kathy.get_field('patient_name') == 'Kathy Crawford'
    assert doc_2_empty.get_field('patient_name') == None


def test_get_phone_number(doc_1_Kathy, doc_2_empty):
    assert doc_1_Kathy.get_field('phone_number') == '(737) 988-0851 or emergency (990) 375-4621'
    assert doc_2_empty.get_field('phone_number') == None


def test_get_hepatitis_b_vaccination(doc_1_Kathy, doc_2_empty):
    assert doc_1_Kathy.get_field('hepatitis_b_vaccination') == 'No'
    assert doc_2_empty.get_field('hepatitis_b_vaccination') == None


def test_get_medical_problem(doc_1_Kathy, doc_2_empty):
    assert doc_1_Kathy.get_field('medical_problem') == 'Migraine'
    assert doc_2_empty.get_field('medical_problem') == None


def test_parse(doc_1_Kathy, doc_2_empty):
    record_Kathy = doc_1_Kathy.parse()
    assert record_Kathy['patient_name'] == 'Kathy Crawford'
    assert record_Kathy['phone_number'] == '(737) 988-0851 or emergency (990) 375-4621'
    assert record_Kathy['hepatitis_b_vaccination'] == 'No'
    assert record_Kathy['medical_problem'] == 'Migraine'

    record_empty = doc_2_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'phone_number': None,
        'hepatitis_b_vaccination': None,
        'medical_problem': None
    }
