from unicodedata import name
import pandas as pd
import sys
from ruamel.yaml import YAML
import time
import xlrd

def multipleReplace(text):
    return ''.join(['' if char in '.()-_/\&;:!?,\'' else char for char in text])

teste = pd.read_csv('./carta.csv')     
 
yaml = YAML()

curlyaml = open('./tests/test_stories.yml', 'r', encoding='utf-8')
data = yaml.load(curlyaml)
cont = 0
cont2= 0

vetor = ['crlv digital', 'central de serviços', 'certificado de conclusão de curso', 'administração do domínio', 'segunda via de documentos', 'bolsa de pesquisador', 'ultrassonografia']

for row in vetor:
  nameRow = row
  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao ' + nameRow + ' está disponivel semanalmente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao ' + nameRow + ' está disponivel semanalmente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')
  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber se o '+ nameRow +' atua diaramente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'É verdade que o '+ nameRow +' permite atividades de segunda a sexta?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Existe um '+ nameRow +' que permite acesso diarimente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Estou em duvida sobre quanto ao '+ nameRow +' estão disponiveis de semanalmente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber se '+ nameRow +' está em funcionamento de segunda a sexta?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Necessito me informar '+ nameRow +' que podem ser acessados diariamente.'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Não tenho ideia quanto ao '+ nameRow +' se permite funcionamento 24 horas?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como posso saber se o'+ nameRow +' que abre semanalmente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Preciso saber quanto '+ nameRow +' possui funcionamento diariamente.'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de ser informado ' + nameRow + ' que abrem 24h?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia auxiliar-me sobre se '+ nameRow +' serviços que devem abrir semanalmente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como posso saber se um '+ nameRow +' que está em funcionamento semanamente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao '+ nameRow +' estão funcionando diariamente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'estou com dúvidas sobre o '+ nameRow +' funcionam diariamente?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber onde vejo se o '+ nameRow +' que atuam semanalmente.'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me dizer quanto os '+ nameRow +' possui funcionamento 24h?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'o serviço '+ nameRow +' permite funcionamento 24h?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber quanto ao '+ nameRow +' possuem funcionamento segunda a sexta?'
  newLookup['steps'][0]['intent'] += 'hor_func'
  newLookup['steps'][1]['action'] += 'action_hor_func'

  data['stories'].append(newLookup)
  data['stories'].append('\n')
  #FORMA ACESSO
  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Em relação ao '+ nameRow + ' permite acesso local ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Determinado servico de '+ nameRow +' permite acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o '+ nameRow +' está disponível para acesso presencial ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De que maneira o '+ nameRow +' estão disponíveis para acesso local ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Existe '+ nameRow +' que possuem acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o '+ nameRow +' em andamento, o mesmo possui acesso presencial ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber se '+ nameRow +' que está em funcionamento, possui acesso local ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'poderia me informar sobre '+ nameRow +' que possuem acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar sobre o '+ nameRow +' disponibiliza acesso fisicamente ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' possuí funcionamento acesso presencial ou remoto, quais permitem?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' de acesso presencial ou remoto, quais permitem?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar quanto '+ nameRow +' possui acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com o '+ nameRow +' disponível qual permite acesso presencial ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O '+ nameRow +', gostaria de informar-me quanto ao acesso local ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber '+ nameRow +' que possibilita acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Estou em dúvida sobre '+ nameRow +' possui acesso presencial ou online?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' de acesso presencial ou remoto'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' possibilita acesso presencial ou remoto'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' que permite acesso fisicamente ou online'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Está disponivel o '+ nameRow +' e permite acesso presencial ou remoto?'
  newLookup['steps'][0]['intent'] += 'forma_acesso'
  newLookup['steps'][1]['action'] += 'action_acesso'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  #req_serv

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quais requisitos para solicitar '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quero realizar '+ nameRow +', o que é preciso?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quais são os requisitos necessários para solicitar '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')\

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Requisitos para '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar quais são os requisitos para solicitar '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como sei o que é preciso para realizar '+ nameRow+'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber o que preciso para realizar '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O que se faz necessario para solicitar '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber os quesitos para '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o '+ nameRow +', quais as condições para ser executado?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com o '+ nameRow +', quais os quesitos ser realizado?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o '+ nameRow +' onde posso saber os quesitos para realiza-lo?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia informar-me sobre quais requisitos são necessarios para o '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n') 

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Para o  '+ nameRow +', Qual o quesito para realiza-ló?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quais quesitos necessario para efetuar um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Desse modo, quais os requisitos para um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto as exigências para solicitar um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quais as clausulas para solicitar um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com os dados o que é necessário para um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual a necessidade para realiza um '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'req_serv'
  newLookup['steps'][1]['action'] += 'action_req_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O rg é um documento necessario para serviços da '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Preciso do cnh para solicitar '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber se é necessário identidade para os '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar sobre os '+ nameRow +' que precisam de identidade?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os documentos necessários, o cnh é um deles para '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'carteira de motorista é necessario para '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Os '+ nameRow +' precisam do cpf para serem realizados?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O CTPS é um requisito comum aos '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto a '+ nameRow +', o Cartão de Saúde é um requisito comum para requer?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Ao requer um '+ nameRow +', é preciso do Título de Eleitor?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O Titulo de Eleitor é um documento necessario para serviços da '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'É preciso do RG para solicitar '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia de saber se é necessário cpf para os '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de informar-me se o '+ nameRow +' que precisa de identidade?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Para os documentos necessários, o cpf é obrigatoriedade para solicitar um '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O RG é necessario para solicitar um '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Os '+ nameRow +' faz-se necessário de cartão de Saúde para serem realizados?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'A Certidão de nascimento é um Documento comum ao '+ nameRow
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto a '+ nameRow +', o CNPJ é um documento comum para solicitar?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o '+ nameRow +', é necessário um CNPJ?'
  newLookup['steps'][0]['intent'] += 'doc_neces'
  newLookup['steps'][1]['action'] += 'action_doc_neces'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços gratis, o '+ nameRow +' quais oferecem o serviço 24h?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar se os serviços gratuitos, o '+ nameRow +' está aberto diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber sobre o '+ nameRow +' que permitem funcionamento de segunda a sexta?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao serviço ao '+ nameRow +' oferecido gratuitamente, pode atender 24 horas?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços gratuitos, o '+ nameRow +' atende todo dia?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como saber se o '+ nameRow +' é oferecido de graça e atende todo dia?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dos serviços requeridos gratuitamente, o '+ nameRow +' possibilita funcionamento diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' é gratuito e tem funcionamento 24h?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' disponivel 24h e gratis.'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar se os '+ nameRow +' é um serviço gratuito fornecido diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de informar me se '+ nameRow +' é um serviço gratuito e funciona diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'É possível descobrir sobre o '+ nameRow +', é oferecido gratuitamente e possibilita atuação diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços grátis, '+ nameRow +' atua diariamente?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao '+ nameRow +' que funciona gratuitamente e de segunda a sexta'  
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Posso saber se o '+ nameRow +' possui funcionamento semanalmente e continua gratuitamente disponível?'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como posso saber se '+ nameRow +' é disponivel gratuitamente e funciona diariamente'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao  '+ nameRow +' é acessível de graça e atua semanalmente'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De fato como posso descobri se '+ nameRow +' é gratis e ainda está disponível segunda a sexta'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Há possibilidade do '+ nameRow +' é disponivel de graça e funciona 24h'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Desse modo o '+ nameRow +' possibilita acessibilidade gratuita e funciona de mensalmente'
  newLookup['steps'][0]['intent'] += 'serv_gratis'
  newLookup['steps'][1]['action'] += 'action_serv_gratis'

  data['stories'].append(newLookup)
  data['stories'].append('\n')
  #novo

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao '+ nameRow +' é efetuado presencial permite ser acompanhado remotamente?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber se meu serviço '+ nameRow +' pode ser realizado presencialmente pode ser acompanhado de caso.'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar se o serviço '+ nameRow +' que realizei presencialmente é possível ser acompanhado em casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'é possível acompanhar '+ nameRow +' remotamente este serviço realizado presencialmente?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Solicitei um '+ nameRow +' serviço presencial, posso acompanhalo de casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços presenciais o '+ nameRow +', quais podem ser assistidos de casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber sobre os serviços presencias '+ nameRow +' que podem ser averiguado remotamente?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O serviço presencial '+ nameRow +', quais permitem acompanhamento remoto?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre os serviços presenciais o '+ nameRow +', permite acompanhar online?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' é um serviço presencial de acompanhamento online.'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os oferecidos de modo presencial o '+ nameRow +' permite acompanhamento remotamente?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia saber se o serviço '+ nameRow +' presencial pode ser acompanhado de caso.'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de me informar  quanto a possibilidade do '+ nameRow +' que realizei presencialmente é possível ser acompanhado em casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' é verídico que pode-se acompanhar remotamente este serviço presencial?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' solicitei o serviço presencialmente, posso acompanhalo de casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' presencialmente efetuado, pode ser assistido de casa?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')  

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria ser informado se há uma possibilidade de averiguar remotamente '+ nameRow +' o serviço presencial?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com os serviços presencias '+ nameRow +', é permitido acompanhamento remoto?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Executei localmente o '+ nameRow +', ele permite acompanhar online?'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' é um serviço presencial para acompanhamento de casa.'
  newLookup['steps'][0]['intent'] += 'serv_pres_on'
  newLookup['steps'][1]['action'] += 'action_pres_on'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O serviço '+ nameRow +' online, qual seu site e principais requisitos?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de sobre meu '+ nameRow +', onde encontro o site e o que é preciso, para realizar o serviço online?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar quanto, aos serviço '+ nameRow +' online, onde acesso seu site e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços onlines quanto ao '+ nameRow +', onde podem ser encontrados seus sites e seus principais requisitos.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual site e requisitos para o serviço '+ nameRow +' online.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como saber o que é preciso e qual site sobre os dados do serviços '+ nameRow +' remotos.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Tudo que é requerido para o serviço '+ nameRow +' online e onde posso encontrar seu site?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços que podem ser online o '+ nameRow +', posso conferir seus requisitos e seu site?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber onde acesso o site do serviço '+ nameRow +' online e o que preciso?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' online, onde acesso o site e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' online,  como posso saber seu site e seus principais requisitos?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Onde busco informações sobre o site e o que é preciso, para realizar um serviço '+ nameRow +' online?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia situar quanto ao '+ nameRow +' ao serviços online, onde acesso seu site e quais quesitos necessarios?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Por meio dos serviços onlines quanto ao '+ nameRow +', onde posso encontrar seu site e seus principais quesitos.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao site e requisitos para um '+ nameRow +' online.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre o que preciso e qual site sobre o '+ nameRow +' remotos.'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Onde encontro o site e o que deve ser requerido para o serviço '+ nameRow +' online?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Com base no '+ nameRow +' disponível online, onde posso conferir seus quesitos e seu site?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber quanto a disponibilidade do '+ nameRow +' classificado como online, como acessa-ló no site o que preciso?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com a '+ nameRow +' classificado como online, onde acesso o site e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_online_desc'
  newLookup['steps'][1]['action'] += 'action_online_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dos serviços presencias o '+ nameRow +', qual seu endereço e principais requisitos?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')


  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar quanto ao '+ nameRow +', é classificado como presencial, onde acesso e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços presenciais '+ nameRow +', sua rua e seus principais requisitos.'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como saber o que é preciso e onde localiza-se dados sobre o serviço '+ nameRow +' presencial.'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Tudo que é requerido para o serviço '+ nameRow +' presencial e onde posso acessar seu endereço e quesitos principais?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços o '+ nameRow +' pode ser presencial, onde posso conferir seus requisitos e seu endereço?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber onde localiza-se o serviço '+ nameRow +' presencial e o que preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O serviço '+ nameRow +' presencial, onde localiza-se e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dos serviços presencias o '+ nameRow +', qual seu endereço e principais requisitos?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria me informar quanto '+ nameRow +' onde acessar e o que é preciso, para um serviço '+ nameRow +' presencial?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia saber sobre o '+ nameRow +' definido como presencial, onde localiza-se e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Pré-definido como presencial o '+ nameRow +', qual endereco e seus principais requisitos.'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Endereço e Requisitos dos serviço '+ nameRow +' presencial.'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como saber o que é preciso e onde acesso dados para o '+ nameRow +' presencialmente.'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Tudo que é requerido para o serviço '+ nameRow +' presencial e onde posso acessa-lo?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre as informações do '+ nameRow +' definido como presencial, onde posso conferir seus requisitos e seu endereço?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De fato onde localiza-se o serviço '+ nameRow +' presencial e o que preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' qual localização do serviço presencial e o que é preciso?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Informações sobre '+ nameRow +' onde localiza-se o serviço presencial e o que necessário?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +' o serviço presencial, onde acesso e o que é requisitado?'
  newLookup['steps'][0]['intent'] += 'serv_pres_desc'
  newLookup['steps'][1]['action'] += 'action_pres_desc'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual o tempo mímino para ser atendido para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual o prazo de atendimento para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'A respeito do tempo de atendimento para '+nameRow+', qual o prazo?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber quanto tempo custa para ser atendido para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Tempo de atendimento minimo para '+nameRow+'.'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar em quanto tempo eu serei auxiliado para o '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Dentre os serviços disponiveis, qual o tempo de atendimento para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre os serviços, qual o prazo para ser ajudado para o '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber qual o tempo de atendimento para '+nameRow+' para o serviço?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Serviços disponiveis, qual prazo para ser atendido para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao prazo para ser atendido no '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto ao tempo de espera ao atendimento para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo ao prazo pra ser auxiliado '+nameRow+', qual o prazo?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Onde posso saber quanto ao tempo que custa para ser atendido no '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De que maneira posso saber sobre o tempo de atendimento minimo para '+nameRow+'.'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual o prazo para ser ajudado para o '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Prazo para atendimento para '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Os serviços, onde encontro qual o prazo pra ser ajudado ao '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de descobrir sobre o prazo de atendimento para '+nameRow+' para o serviço?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'De acordo com os serviços disponiveis, qual prazo de auxilio de '+nameRow+'?'
  newLookup['steps'][0]['intent'] += 'temp_serv'
  newLookup['steps'][1]['action'] += 'action_temp_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Descrição o serviço de '+ nameRow+'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como descrever a '+ nameRow + '?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual a finalidade da '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de saber qual a finalidade da '+ nameRow+'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Descrição a '+ nameRow + '?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como saber Descrição a '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Poderia me informar sobre a finalidade da '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +', Descrição?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre a '+ nameRow +', qual sua finalidade?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Qual a finalidade do serviço de '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Descrição o propósito do '+ nameRow+'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como posso saber o proposito do '+ nameRow + '?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Quanto o propósito da '+ nameRow +'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'O que seria, de acordo com a finalidade do '+ nameRow+'?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Como posso saber sober a descrição do '+ nameRow + '?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre Descrição o '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Gostaria de me informar sobre a descriçao da '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += nameRow +', Como pode ser descrito?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'Sobre a '+ nameRow +', qual sua descrição?'
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

  data['stories'].append(newLookup)
  data['stories'].append('\n')

  newLookup = {'story': '', 'steps': [{'user': '', 'intent': ''}, {'action': ''}]}
  cont+=1
  newLookup['story'] += 'question ' + str(cont)
  newLookup['steps'][0]['user'] += 'como pode-se descrever o serviço de '+ nameRow
  newLookup['steps'][0]['intent'] += 'desc_serv'
  newLookup['steps'][1]['action'] += 'action_desc_serv'

print(data)

with open('./tests/test_stories.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f) # Also note the safe_dump
