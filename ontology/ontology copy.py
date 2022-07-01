from os import name
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import XSD, SKOS, OWL, RDFS
from unidecode import unidecode
import xlrd

def multipleReplace(text):
    return "".join([" " if char in "  " else char for char in text])

teste = pd.read_csv('./carta.csv')
g = Graph()
g = g.parse('C:\\Users\\jh0nn\\Documents\\TesteRasas\\rasa_ontologias_exemplo-master\\OntoServiceCE.ttl', format='turtle')
serv = Namespace("http://servicos.gov.ce.br/")
g.bind("skos", SKOS)
g.bind("serv", serv)

for index, row in teste.iterrows():
  nameRow3 = "" + serv + unidecode(str(row['dsc_poder']).replace(" ", "_").replace('\"', ''))
  g.add((URIRef(nameRow3), RDF.type, OWL.Class))
  g.add((URIRef(nameRow3), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow3), RDF.type, URIRef(serv+'Poder')))
  g.add((URIRef(nameRow3), URIRef(serv+'administra'), Literal(row['nom_orgao'])))
  g.add((URIRef(nameRow3), URIRef(serv+'nomPoder'), Literal(row['dsc_poder'], datatype=XSD.string) ))

for index, row in teste.iterrows():
  nameRow2 = "" + serv + unidecode(str(row['nom_orgao']).replace(" ", "_").replace('\"', ''))
  g.add((URIRef(nameRow2), RDF.type, OWL.Class))
  g.add((URIRef(nameRow2), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow2), RDF.type, URIRef(serv+'Orgao')))
  g.add((URIRef(nameRow2), URIRef(serv+'administrado'), Literal(row['dsc_poder'])))
  g.add((URIRef(nameRow2), URIRef(serv+'organiza'), Literal(row['nom_orgao'])))
  g.add((URIRef(nameRow2), URIRef(serv+'nomeOrg'), Literal(row['nom_orgao'], datatype=XSD.string) ))

for index, row in teste.iterrows():
  nameRow1 = "" + serv + unidecode(str(row['nom_orgao']).replace(" ", "_").replace('\"', ''))
  g.add((URIRef(nameRow1), RDF.type, OWL.Class))
  g.add((URIRef(nameRow1), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow1), RDF.type, URIRef(serv+'Secretaria')))
  g.add((URIRef(nameRow1), URIRef(serv+'nomeSec'), Literal(row['nom_orgao'], datatype=XSD.string) ))
  g.add((URIRef(nameRow1), URIRef(serv+'organizado'), Literal(row['nom_orgao'], datatype=XSD.string)))
  g.add((URIRef(nameRow2), URIRef(serv+'realiza'), Literal(row['nom_servico'])))

"""for index, row in teste.iterrows():
  nameRow4 = "" + serv + unidecode((row['nom_categoria']).replace(" ", "_"))
  g.add((URIRef(nameRow4), RDF.type, OWL.Class))
  g.add((URIRef(nameRow4), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow4), RDF.type, URIRef(serv+'Categoria')))
  g.add((URIRef(nameRow4), URIRef(serv+'categoria'), Literal(row['nom_categoria'], datatype=XSD.string) ))
  g.add((URIRef(nameRow4), URIRef(serv+'pertence'), Literal(row['nom_servico'])))
"""
for index, row in teste.iterrows():
  nameRow = row['nom_servico'].replace("  ", "_")
  nameRow = nameRow.replace(" ", "_")
  nameRow = nameRow.replace('\"', '')
  nameRow = nameRow.replace("\e", "e")
  nameRow = nameRow.replace("(", "")
  nameRow = nameRow.replace(")", "")
  nameRow = "" + serv + unidecode(nameRow)
  g.add((URIRef(nameRow), RDF.type, OWL.Class))
  g.add((URIRef(nameRow), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow), RDF.type, URIRef(serv+'Servico')))
  #g.add((URIRef(nameRow), URIRef(serv+'possui'), Literal(row['nom_categoria'])))
  g.add((URIRef(nameRow), URIRef(serv+'realizado'), Literal(row['nom_orgao'])))
  g.add((URIRef(nameRow), RDFS.label, Literal(row['nom_servico'], datatype=XSD.string)))
  g.add((URIRef(nameRow), URIRef(serv+'codigo'), Literal(row['cod_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'unidPres'), Literal(row['nom_unidade_prestadora'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'requisitos'), Literal(row['dsc_requisitos'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), SKOS.notation, Literal(row['dsc_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'areaRespon'), Literal(row['nom_area_responsavel'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoOnline'), Literal(row['dsc_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoValor'), Literal(row['dsc_servico_gratuito'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempoAtendimento'), Literal(row['dsc_tempo_atendiment'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'horarioAtendimento'), Literal(row['dsc_horario_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'etapasAtendimento'), Literal(row['dsc_etapas_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'publicoAlvo'), Literal(row['publico_alvo'], datatype=XSD.short) ))
  g.add((URIRef(nameRow), URIRef(serv+'servDigital'), Literal(row['dsc_servico_digital'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'solicitante'), Literal(row['dsc_solicitante'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'servGratuito'), Literal(row['dsc_servico_gratuito'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'docNeces'), Literal(row['dsc_doc_necessarios'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempAtendPriori'), Literal(row['dsc_tempo_atendimento_priori'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'prazoEntrega'), Literal(row['dsc_prazo_entrega'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoOnline'), Literal(row['dsc_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'endereco'), Literal(row['dsc_endereco'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'legislacao'), Literal(row['dsc_legislacao'], datatype=XSD.string) ))

g.serialize('C:\\Users\\jh0nn\\Documents\\TesteRasas\\rasa_ontologias_exemplo-master\\OntoService.ttl', format='turtle')