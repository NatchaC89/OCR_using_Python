from parser_prescription import PrescriptionParser

def test_get_name():
    PD = PrescriptionParser(document_text1)
    assert PD.get_field('patient_name') == 'Marta Sharapova'

    # PD = PrescriptionParser(document_text2)
    # assert PD.get_field('patient_name') == 'Natcha Cota'

def test_get_address():
    PD = PrescriptionParser(document_text1)
    assert PD.get_field('patient_address') == '9 tennis court, new Russia, DC'


document_text1 = '''
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

# document_text2 = '''
# Dr John Smith, M.D
# 2 Non-Important Street,
# New York, Phone (000)-111-2222

# Name: Natcha Cota Date: 5/11/2022

# Address: 8 badminton court, new Thai, AC

# K

 

# Prednisone 20 mg
# Lialda 2.4 gram
# Dolly 2 kg

# Directions:

# Prednisone, Taper 5 mg every 3 days,
# Finish in 2.5 weeks a
# Lialda - take 2 pill everyday for 1 month
# Dolly - eat every one

# Refill: 20 times
# '''

if __name__ == "__main__":
    print("test")