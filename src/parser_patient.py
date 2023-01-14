import re

from parser_generic import MedicalDocParser

class PatientParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'phone_number': self.get_field('phone_number'),
            'hepatitis_b_vaccination': self.get_field('hepatitis_b_vaccination'),
            'medical_problem': self.get_field('medical_problem')
        }

    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Birth Date\n\n(.*)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) ([1-9]|[1-2][0-9]|3[0-1]) ((20)[0-9]{2}|(19)[0-9]{2})', 'flags': 0},
            'phone_number': {'pattern': 'Patient Medical Record(.*?)(\(\d{3}\) \d{3}-\d{4})', 'flags': re.DOTALL},
            'hepatitis_b_vaccination': {'pattern': 'Hepatitis B vaccination\?\n\n(.*?)(No|Yes)', 'flags': 0},
            'medical_problem': {'pattern': 'List any Medical Problems .*?:(.*)', 'flags': re.DOTALL}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if (len(matches) > 0) and (field_name == 'patient_name'):
                return ''.join(matches[0][0]).strip()
            elif (len(matches) > 0) and (field_name == 'phone_number'):
                return matches[0][1].strip()
            elif (len(matches) > 0) and (field_name == 'hepatitis_b_vaccination'):
                return ''.join(matches[0][1]).strip()
            elif(len(matches) > 0) and (field_name == 'medical_problem'):
                return matches[0].strip()

if __name__ == '__main__':
    text = '''
Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

- eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?

‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020
    '''
    PD = PatientParser(text)
    print(PD.parse())
    print(PD.get_field('hepatitis_b_vaccination'))