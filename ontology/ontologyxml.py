import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace 
from rdflib.namespace import XSD, SKOS, OWL, RDFS
from unidecode import unidecode
              
def multipleReplace(text):
    return "".join(["_" if char in ". ()-/\&;:!?,\"" else char for char in text])

def multipleReplace2(text):
    return "".join(["" if char in "_.()-/\&;:!?,\"" else char for char in text])

teste = pd.read_excel('C:\\Users\\jh0nn\\Documents\\TesteRasas\\rasa_ontologias_exemplo-master\\rel_atend_131393.xls')
g = Graph()
g = g.parse('C:\\Users\\jh0nn\\Documents\\TesteRasas\\rasa_ontologias_exemplo-master\\OntoServiceCEXML.owl', format="application/rdf+xml")
serv = Namespace("http://servicos.gov.ce.br/")
g.bind("skos", SKOS)
g.bind("serv", serv)

for index, row in teste.iterrows():
  nameRow3 = "" + serv + multipleReplace(unidecode((row['dsc_poder']).lower()))
  g.add((URIRef(nameRow3), RDF.type, OWL.Class))
  g.add((URIRef(nameRow3), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow3), RDF.type, URIRef(serv+'Poder')))
  g.add((URIRef(nameRow3), URIRef(serv+'administra'), Literal(row['nom_orgao'])))
  g.add((URIRef(nameRow3), URIRef(serv+'nomPoder'), Literal(row['dsc_poder'], datatype=XSD.string) ))

for index, row in teste.iterrows():
  nameRow2 = "" + serv + multipleReplace(unidecode((row['nom_orgao']).lower()))
  g.add((URIRef(nameRow2), RDF.type, OWL.Class))
  g.add((URIRef(nameRow2), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow2), RDF.type, URIRef(serv+'Orgao')))
  g.add((URIRef(nameRow2), URIRef(serv+'administrado'), Literal(row['dsc_poder'])))
  g.add((URIRef(nameRow2), URIRef(serv+'organiza'), Literal(row['nom_secretaria'])))
  g.add((URIRef(nameRow2), URIRef(serv+'realiza'), Literal(row['nom_servico'])))
  g.add((URIRef(nameRow2), URIRef(serv+'siglaOrg'), Literal(row['sgl_orgao'], datatype=XSD.short) ))
  g.add((URIRef(nameRow2), URIRef(serv+'nomeOrg'), Literal(row['nom_orgao'], datatype=XSD.string) ))

for index, row in teste.iterrows():
  nameRow1 = "" + serv + multipleReplace(unidecode((row['nom_secretaria']).lower()))
  g.add((URIRef(nameRow1), RDF.type, OWL.Class))
  g.add((URIRef(nameRow1), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow1), RDF.type, URIRef(serv+'Secretaria')))
  g.add((URIRef(nameRow1), URIRef(serv+'siglaSec'), Literal(row['sgl_secretaria'], datatype=XSD.short) ))
  g.add((URIRef(nameRow1), URIRef(serv+'nomeSec'), Literal(row['nom_secretaria'], datatype=XSD.string) ))
  g.add((URIRef(nameRow1), URIRef(serv+'organizado'), Literal(row['nom_orgao'], datatype=XSD.string)))

for index, row in teste.iterrows():
  nameRow4 = "" + serv + multipleReplace(unidecode((row['nom_categoria']).lower()))
  g.add((URIRef(nameRow4), RDF.type, OWL.Class))
  g.add((URIRef(nameRow4), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow4), RDF.type, URIRef(serv+'Categoria')))
  g.add((URIRef(nameRow4), URIRef(serv+'categoria'), Literal(row['nom_categoria'], datatype=XSD.string) ))
  g.add((URIRef(nameRow4), URIRef(serv+'pertencido'), Literal(row['nom_servico'])))

for index, row in teste.iterrows():
  nameRow = "" + serv + multipleReplace(unidecode((row['nom_servico']).lower()))
  g.add((URIRef(nameRow), RDF.type, OWL.Class))
  g.add((URIRef(nameRow), RDF.type, OWL.NamedIndividual))
  g.add((URIRef(nameRow), RDF.type, URIRef(serv+'Servico')))
  g.add((URIRef(nameRow), URIRef(serv+'possui'), Literal(row['nom_categoria'])))
  g.add((URIRef(nameRow), URIRef(serv+'realizado'), Literal(row['nom_categoria'])))
  g.add((URIRef(nameRow), RDFS.label, Literal(multipleReplace2((row['nom_servico']).lower().capitalize()), datatype=XSD.string)))
  g.add((URIRef(nameRow), URIRef(serv+'codigo'), Literal(row['cod_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'unidPres'), Literal(row['nom_unidade_prestadora'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'finalidade'), Literal(row['dsc_finalidade'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'requisitos'), Literal(row['dsc_requisitos'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), SKOS.notation, Literal(row['dsc_servico'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), SKOS.broader, Literal(row['dsc_servicos_relacionados'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'areaRespon'), Literal(row['nom_area_responsavel'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'telefone'), Literal(row['dsc_acesso_telefone'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoPresencial'), Literal(row['dsc_acesso_presencial'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoOnline'), Literal(row['dsc_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoValor'), Literal(row['dsc_servico_gratuito'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'outrosAcessos'), Literal(row['dsc_acesso_outros'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempoAtendimento'), Literal(row['dsc_tempo_atendiment'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'horarioAtendimento'), Literal(row['dsc_horario_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'etapasAtendimento'), Literal(row['dsc_etapas_atendimento'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'enderecoMapa'), Literal(row['dsc_endereco_mapa'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'publicoAlvo'), Literal(row['flg_publico_alvo'], datatype=XSD.short) ))
  g.add((URIRef(nameRow), URIRef(serv+'siteOficial'), Literal(row['dsc_site_oficial'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'servAtivo'), Literal(row['flg_ativo'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'servDigital'), Literal(row['flg_servico_digital'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'solicitante'), Literal(row['dsc_solicitante'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'servGratuito'), Literal(row['flg_servico_gratuito'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'docNeces'), Literal(row['dsc_doc_necessarios'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'tempAtendPriori'), Literal(row['dsc_tempo_atendimento_priori'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'prazoEntrega'), Literal(row['dsc_prazo_entrega'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoOnline'), Literal(row['flg_acesso_online'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoPres'), Literal(row['flg_acesso_presencial'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoTelefone'), Literal(row['flg_acesso_telefone'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'bancoPalavra'), Literal(row['dsc_banco_palavra'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoOnAcompa'), Literal(row['dsc_acesso_online_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoPresAcompa'), Literal(row['dsc_acesso_presencial_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'acessoTelAcompa'), Literal(row['dsc_acesso_telefone_acomp'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'endereco'), Literal(row['dsc_endereco'], datatype=XSD.string) ))
  g.add((URIRef(nameRow), URIRef(serv+'legislacao'), Literal(row['dsc_legislacao'], datatype=XSD.string) ))

g.serialize('C:\\Users\\jh0nn\\Documents\\TesteRasas\\rasa_ontologias_exemplo-master\\OntoServiceTEsteXML.rdf', format="application/rdf+xml")