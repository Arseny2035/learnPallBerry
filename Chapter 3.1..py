import pprint

people = dict()
people['Ford'] = {'Name': 'Ford Prefect',
                  'Gender': 'Male',
                  'Occupation': 'Researcher',
                  'Home Planet': 'Betelgeuse Seven'}

people['Arthur'] = {'Name': 'Arthur Dent',
                    'Gender': 'Male',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}

people['Trillian'] = {'Name': 'Tricia McMillan',
                      'Gender': 'Female',
                      'Occupation': 'Mathematical',
                      'Home Planet': 'Earth'}

people['Robot'] = {'Name': 'Bender',
                   'Gender': 'Unknown',
                   'Occupation': 'Paranoid Android',
                   'Home Planet': 'Unknown'}

pprint.pprint(people)

print(people['Arthur']['Occupation'])
