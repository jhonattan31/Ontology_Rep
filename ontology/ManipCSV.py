from os import name
import pandas as pd
import math
from pandas.core.frame import DataFrame
import re

TAG_RE = re.compile(r'<[^>]+>')

def multipleReplace(text):
    return "".join(["" if char in ".()-_/\&;:~!?,\"" else char for char in text])

def processamento(nameRow):
    if(type(nameRow) == str):
        if(nameRow.isdigit()):
            nameRow = int(nameRow)
        else:   
            nameRow = nameRow.lower()
            nameRow = multipleReplace(nameRow)
            nameRow = nameRow.replace('https', ' ')
            nameRow = nameRow.replace('http', ' ')
            nameRow = nameRow.replace('ccedilatildeo', 'ção')
            nameRow = nameRow.replace('ccedil', 'ç')
            nameRow = nameRow.replace('atildeo', 'ão')
            nameRow = nameRow.replace('otilde', 'õ')
            nameRow = nameRow.replace('acirc', 'â')
            nameRow = nameRow.replace('ocirc', 'ô')
            nameRow = nameRow.replace('ecirc', 'ê')
            nameRow = nameRow.replace('ndash', '')
            nameRow = nameRow.replace('aacute', 'á')
            nameRow = nameRow.replace('eacute', 'é')
            nameRow = nameRow.replace('iacute', 'í')
            nameRow = nameRow.replace('oacute', 'ó')
            nameRow = nameRow.replace('uacute', 'ú')
            nameRow = nameRow.replace('ordf', 'ª')
            nameRow = nameRow.replace('capitalinterior', 'capital e interior')
            nameRow = nameRow.replace('\\ ', '')
            nameRow = nameRow.replace('\"', '')
            nameRow = nameRow.replace('  ', ' ')
            nameRow = nameRow.replace('\x96', '')
            nameRow = TAG_RE.sub('', nameRow)
    elif(math.isnan(nameRow)):
        nameRow = str(nameRow)
        nameRow = 'não consta'
        
    return nameRow

teste = pd.read_excel('./rel_atend_131393.xls')

for index, row in teste.iterrows():
    nameRow = processamento(row['nom_servico'])
    teste['nom_servico'].loc[index] = nameRow

    nameRow = processamento(row['cod_servico'])
    teste['cod_servico'].loc[index] = nameRow

    nameRow = processamento(row['nom_categoria'])
    teste['nom_categoria'].loc[index] = nameRow

    nameRow = processamento(row['sgl_orgao'])
    teste['sgl_orgao'].loc[index] = nameRow

    nameRow = processamento(row['nom_orgao'])
    teste['nom_orgao'].loc[index] = nameRow

    nameRow = processamento(row['nom_area_responsavel'])
    teste['nom_area_responsavel'].loc[index] = nameRow

    nameRow = processamento(row['sgl_secretaria'])
    teste['sgl_secretaria'].loc[index] = nameRow

    nameRow = processamento(row['nom_secretaria'])
    teste['nom_secretaria'].loc[index] = nameRow

    nameRow = processamento(row['nom_unidade_prestadora'])
    teste['nom_unidade_prestadora'].loc[index] = nameRow

    nameRow = processamento(row['dsc_finalidade'])
    teste['dsc_finalidade'].loc[index] = nameRow

    nameRow = processamento(row['dsc_requisitos'])
    teste['dsc_requisitos'].loc[index] = nameRow

    nameRow = processamento(row['dsc_servico'])
    teste['dsc_servico'].loc[index] = nameRow

    nameRow = processamento(row['dsc_servicos_relacionados'])
    teste['dsc_servicos_relacionados'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_telefone'])
    teste['dsc_acesso_telefone'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_presencial'])
    teste['dsc_acesso_presencial'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_online'])
    teste['dsc_acesso_online'].loc[index] = nameRow

    nameRow = processamento(row['dsc_servico_gratuito'])
    teste['dsc_servico_gratuito'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_outros'])
    teste['dsc_acesso_outros'].loc[index] = nameRow

    nameRow = processamento(row['dsc_tempo_atendiment'])
    teste['dsc_tempo_atendiment'].loc[index] = nameRow

    nameRow = processamento(row['dsc_tempo_atendimento_priori'])
    teste['dsc_tempo_atendimento_priori'].loc[index] = nameRow

    nameRow = processamento(row['dsc_horario_atendimento'])
    teste['dsc_horario_atendimento'].loc[index] = nameRow

    nameRow = processamento(row['dsc_etapas_atendimento'])
    teste['dsc_etapas_atendimento'].loc[index] = nameRow

    nameRow = processamento(row['dsc_endereco_mapa'])
    teste['dsc_endereco_mapa'].loc[index] = nameRow

    nameRow = processamento(row['flg_publico_alvo'])
    teste['flg_publico_alvo'].loc[index] = nameRow

    nameRow = processamento(row['dsc_site_oficial'])
    teste['dsc_site_oficial'].loc[index] = nameRow

    nameRow = processamento(row['flg_ativo'])
    teste['flg_ativo'].loc[index] = nameRow

    nameRow = processamento(row['flg_servico_digital'])
    teste['flg_servico_digital'].loc[index] = nameRow

    nameRow = processamento(row['dsc_poder'])
    teste['dsc_poder'].loc[index] = nameRow

    nameRow = processamento(row['dsc_solicitante'])
    teste['dsc_solicitante'].loc[index] = nameRow

    nameRow = processamento(row['flg_servico_gratuito'])
    teste['flg_servico_gratuito'].loc[index] = nameRow

    nameRow = processamento(row['dsc_doc_necessarios'])
    teste['dsc_doc_necessarios'].loc[index] = nameRow

    nameRow = processamento(row['dsc_prazo_entrega'])
    teste['dsc_prazo_entrega'].loc[index] = nameRow

    nameRow = processamento(row['flg_acesso_online'])
    teste['flg_acesso_online'].loc[index] = nameRow

    nameRow = processamento(row['flg_acesso_telefone'])
    teste['flg_acesso_telefone'].loc[index] = nameRow

    nameRow = processamento(row['flg_acesso_presencial'])
    teste['flg_acesso_presencial'].loc[index] = nameRow

    nameRow = processamento(row['dsc_banco_palavra'])
    teste['dsc_banco_palavra'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_online_acomp'])
    teste['dsc_acesso_online_acomp'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_presencial_acomp'])
    teste['dsc_acesso_presencial_acomp'].loc[index] = nameRow

    nameRow = processamento(row['dsc_acesso_telefone_acomp'])
    teste['dsc_acesso_telefone_acomp'].loc[index] = nameRow

    nameRow = processamento(row['dsc_endereco'])
    teste['dsc_endereco'].loc[index] = nameRow

    nameRow = processamento(row['dsc_legislacao'])
    teste['dsc_legislacao'].loc[index] = nameRow

print(teste.count())
#teste.to_csv('./dados.csv')

teste.to_excel('./dados.xls')