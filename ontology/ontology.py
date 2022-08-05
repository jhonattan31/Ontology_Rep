from os import name
import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import XSD, SKOS, OWL, RDFS
from unidecode import unidecode
import xlrd
import argparse

parser = argparse.ArgumentParser(description='Gerador de Ontologia.')
parser.add_argument("-e", type=str, help="Digite o nome do Estado a ser adicionado na ontologia.",required=True)
parser.add_argument("-c", type=str, help="Digite o endereço de origem do csv a ser adicionado na ontologia.",required=True)
parser.add_argument("-d", type=str, help="Digite o endereço do destino da ontologia gerada.",required=True)
args = parser.parse_args()
ESTADO = args.e
ORIGEM_CSV = args.c
DESTINO_ONTO = args.d


def multipleReplace(text):
    return "".join([" " if char in "  " else char for char in text])

ontodados = pd.read_csv(ORIGEM_CSV)
g = Graph()
g = g.parse('ontology\OntoServiceCE.owl', format='turtle')
serv = Namespace("http://servicos.gov.ce.br/")
g.bind("skos", SKOS)
g.bind("serv", serv)

for index, row in ontodados.iterrows():
  nameRow3 = "" + serv + unidecode(((row['dsc_poder']).replace(" ", "_")))
  g.add((URIRef(nameRow3), RDF.type, OWL.Class))
  g.add((URIRef(nameRow3), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow3), RDF.type, URIRef(serv+'Poder')))
  g.add((URIRef(nameRow3), URIRef(serv+'administra'), Literal(row['nom_orgao'])))
  g.add((URIRef(nameRow3), URIRef(serv+'nomPoder'), Literal(row['dsc_poder'], datatype=XSD.string) ))

for index, row in ontodados.iterrows():
  nameRow2 = "" + serv + unidecode((row['nom_orgao']).replace(" ", "_"))
  g.add((URIRef(nameRow2), RDF.type, OWL.Class))
  g.add((URIRef(nameRow2), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow2), RDF.type, URIRef(serv+'Orgao')))
  g.add((URIRef(nameRow2), URIRef(serv+'administrado'), Literal(row['dsc_poder'])))
  g.add((URIRef(nameRow2), URIRef(serv+'organiza'), Literal(row['nom_secretaria'])))
  g.add((URIRef(nameRow2), URIRef(serv+'nomeOrg'), Literal(row['nom_orgao'], datatype=XSD.string) ))

for index, row in ontodados.iterrows():
  nameRow1 = "" + serv + unidecode((row['nom_secretaria']).replace(" ", "_"))
  g.add((URIRef(nameRow1), RDF.type, OWL.Class))
  g.add((URIRef(nameRow1), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow1), RDF.type, URIRef(serv+'Secretaria')))
  g.add((URIRef(nameRow1), URIRef(serv+'nomeSec'), Literal(row['nom_secretaria'], datatype=XSD.string) ))
  g.add((URIRef(nameRow1), URIRef(serv+'organizado'), Literal(row['nom_orgao'], datatype=XSD.string)))
  g.add((URIRef(nameRow2), URIRef(serv+'realiza'), Literal(row['nom_servico'])))

for index, row in ontodados.iterrows():
  nameRow4 = "" + serv + unidecode((row['nom_categoria']).replace(" ", "_"))
  g.add((URIRef(nameRow4), RDF.type, OWL.Class))
  g.add((URIRef(nameRow4), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow4), RDF.type, URIRef(serv+'Categoria')))
  g.add((URIRef(nameRow4), URIRef(serv+'categoria'), Literal(row['nom_categoria'], datatype=XSD.string) ))
  g.add((URIRef(nameRow4), URIRef(serv+'pertence'), Literal(row['nom_servico'])))

for index, row in ontodados.iterrows():
  nameRow = row['nom_servico'].replace("  ", " ")
  nameRow = nameRow.replace(" ", "_")
  nameRow = "" + serv + unidecode(nameRow)
  g.add((URIRef(nameRow), RDF.type, OWL.Class))
  g.add((URIRef(nameRow), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow), RDF.type, URIRef(serv+'Servico')))
  g.add((URIRef(nameRow), URIRef(serv+'possui'), Literal(row['nom_categoria'])))
  g.add((URIRef(nameRow), URIRef(serv+'realizado'), Literal(row['nom_secretaria'])))
  g.add((URIRef(nameRow), RDFS.label, Literal(row['nom_servico'], datatype=XSD.string)))
  g.add((URIRef(nameRow), URIRef(serv+'codigo'), Literal(row['cod_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'estado'), Literal(ESTADO, datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'unidPres'), Literal(row['nom_unidade_prestadora'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'finalidade'), Literal(row['dsc_finalidade'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'requisitos'), Literal(row['dsc_requisitos'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), SKOS.notation, Literal(row['dsc_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), SKOS.broader, Literal(row['dsc_servicos_relacionados'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'areaRespon'), Literal(row['nom_area_responsavel'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoPresencial'), Literal(row['dsc_acesso_presencial'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoOnline'), Literal(row['dsc_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempoAtendimento'), Literal(row['dsc_tempo_atendiment'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'horarioAtendimento'), Literal(row['dsc_horario_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'etapasAtendimento'), Literal(row['dsc_etapas_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'publicoAlvo'), Literal(row['flg_publico_alvo'], datatype=XSD.short) ))
  g.add((URIRef(nameRow), URIRef(serv+'solicitante'), Literal(row['dsc_solicitante'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'servGratuito'), Literal(row['flg_servico_gratuito'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'docNeces'), Literal(row['dsc_doc_necessarios'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempAtendPriori'), Literal(row['dsc_tempo_atendimento_priori'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'prazoEntrega'), Literal(row['dsc_prazo_entrega'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoOnline'), Literal(row['flg_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoPres'), Literal(row['flg_acesso_presencial'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoOnAcompa'), Literal(row['dsc_acesso_online_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoPresAcompa'), Literal(row['dsc_acesso_presencial_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoTelAcompa'), Literal(row['dsc_acesso_telefone_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'legislacao'), Literal(row['dsc_legislacao'], datatype=XSD.string) ))

g.serialize(DESTINO_ONTO, format='turtle')