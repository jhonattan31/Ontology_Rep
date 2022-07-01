import pandas as pd
import sys
from ruamel.yaml import YAML
import time

teste = pd.read_csv('./carta.csv')     
 
yaml = YAML()

curlyaml = open('./tests/test_nlu.yml', 'r', encoding='utf-8')
data = yaml.load(curlyaml)

newLookup = {'lookup': 'nomServico', 'examples': ''}

for index, row in teste.iterrows():
    nameRow = row['nom_servico'].lower()
    nameRow = '- ' + nameRow + '\n'
    newLookup['examples'] += nameRow

for idx, (key, example) in enumerate(data['nlu']):
    if(key == 'lookup' and data['nlu'][idx][key] == 'nomServico'):
        print("entrou no if")
        data['nlu'][idx][example] += newLookup['examples']

with open('./tests/test_nlu.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f) # Also note the safe_dump

#print(nameRow)