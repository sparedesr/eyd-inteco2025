import pandas as pd
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
from pandas.plotting import table
global columna_de_interes1
columna_de_interes1 = "BODEGAS_PNAC"
hospital_diccionario_operativos = {f'{columna_de_interes1} hospital': []}
hospital_diccionario_no_operativos = {f'{columna_de_interes1} hospital': []}
hospital_diccionario_semi_operativos = {f'{columna_de_interes1} hospital': []}

centro_diccionario_operativos = {f'{columna_de_interes1} centro': []}
centro_diccionario_no_operativos = {f'{columna_de_interes1} centro': []}
centro_diccionario_semi_operativos = {f'{columna_de_interes1} centro': []}

comunitario_diccionario_operativos = {f'{columna_de_interes1} comunitario': []}
comunitario_diccionario_no_operativos = {f'{columna_de_interes1} comunitario': []}
comunitario_diccionario_semi_operativos = {f'{columna_de_interes1} comunitario': []}

psr_diccionario_operativos = {f'{columna_de_interes1} psr': []}
psr_diccionario_no_operativos = {f'{columna_de_interes1} psr': []}
psr_diccionario_semi_operativos = {f'{columna_de_interes1} psr': []}

csmc_diccionario_operativos = {f'{columna_de_interes1} csmc': []}
csmc_diccionario_no_operativos = {f'{columna_de_interes1} csmc': []}
csmc_diccionario_semi_operativos = {f'{columna_de_interes1} csmc': []}

sur_diccionario_operativos = {f'{columna_de_interes1} sur': []}
sur_diccionario_no_operativos = {f'{columna_de_interes1} sur': []}
sur_diccionario_semi_operativos = {f'{columna_de_interes1} sur': []}

sar_diccionario_operativos = {f'{columna_de_interes1} sar': []}
sar_diccionario_no_operativos = {f'{columna_de_interes1} sar': []}
sar_diccionario_semi_operativos = {f'{columna_de_interes1} sar': []}

sapu_diccionario_operativos = {f'{columna_de_interes1} sapu': []}
sapu_diccionario_no_operativos = {f'{columna_de_interes1} sapu': []}
sapu_diccionario_semi_operativos = {f'{columna_de_interes1} sapu': []}

hospital_contador_operativos = 0
hospital_contador_no_operativos = 0
hospital_contador_semi_operativos = 0

centro_contador_operativos = 0
centro_contador_no_operativos = 0
centro_contador_semi_operativos = 0

comunitario_contador_operativos = 0
comunitario_contador_no_operativos = 0
comunitario_contador_semi_operativos = 0

psr_contador_operativos = 0
psr_contador_no_operativos = 0
psr_contador_semi_operativos = 0

csmc_contador_operativos = 0
csmc_contador_no_operativos = 0
csmc_contador_semi_operativos = 0

sur_contador_operativos = 0
sur_contador_no_operativos = 0
sur_contador_semi_operativos = 0

sar_contador_operativos = 0
sar_contador_no_operativos = 0
sar_contador_semi_operativos = 0

sapu_contador_operativos = 0
sapu_contador_no_operativos = 0
sapu_contador_semi_operativos = 0
def crear_tabla_bodegas(archivo):
  pd.set_option('display.max_rows', None)  # Muestra todas las filas
  pd.set_option('display.max_columns', None)  # Muestra todas las columnas


  data = []





  def separacion_instalaciones(tipoDeInstalacion):
      data = {
          'ID_EDAN': [],
          'NOMBRE_ESTABLECIMIENTO': [],
          'COMUNA': [],
          f'{columna_de_interes1}': [],
      }
      for _, raw in archivo.iterrows():

          edan = raw['ID_EDAN']
          nombre = raw['NOMBRE_ESTABLECIMIENTO']
          comuna = raw['COMUNA']
          operatividad = raw[f'{columna_de_interes1}']
          tipo = tipoDeInstalacion

          if tipo in nombre:
              data['ID_EDAN'].append(edan)
              data['NOMBRE_ESTABLECIMIENTO'].append(nombre)
              data['COMUNA'].append(comuna)
              data[f'{columna_de_interes1}'].append(operatividad)

      datos = pd.DataFrame(data)
      return datos
  hospital=separacion_instalaciones('HOSPITAL')
  centro=separacion_instalaciones('CENTRO_DE_SALUD_FAMILIAR')
  comunitario=separacion_instalaciones('CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR')
  psr=separacion_instalaciones('POSTA_DE_SALUD_RURAL')
  csmc=separacion_instalaciones('CENTRO_DE_SALUD_MENTAL_COMUNITARIO')
  sur=separacion_instalaciones('SUR')
  sar=separacion_instalaciones('SAR')
  sapu=separacion_instalaciones('SAPU')

  datos = {
      'Tipo de Establecimientos': [],
      'Operativos': [],
      'No Operativos': [],
      'Semi Operativos': [],
  }


  def recolectar_datos_establecimientos(nombre):
    global hospital_contador_operativos, hospital_contador_no_operativos, hospital_contador_semi_operativos, hospital_diccionario_operativos, hospital_diccionario_no_operativos, hospital_diccionario_semi_operativos
    global centro_contador_operativos, centro_contador_no_operativos, centro_contador_semi_operativos, centro_diccionario_operativos, centro_diccionario_no_operativos, centro_diccionario_semi_operativos
    global comunitario_contador_operativos, comunitario_contador_no_operativos, comunitario_contador_semi_operativos, comunitario_diccionario_operativos, comunitario_diccionario_no_operativos, comunitario_diccionario_semi_operativos
    global psr_contador_operativos, psr_contador_no_operativos, psr_contador_semi_operativos, psr_diccionario_operativos, psr_diccionario_no_operativos, psr_diccionario_semi_operativos
    global csmc_contador_operativos, csmc_contador_no_operativos, csmc_contador_semi_operativos, csmc_diccionario_operativos, csmc_diccionario_no_operativos, csmc_diccionario_semi_operativos
    global sur_contador_operativos, sur_contador_no_operativos, sur_contador_semi_operativos, sur_diccionario_operativos, sur_diccionario_no_operativos, sur_diccionario_semi_operativos
    global sar_contador_operativos, sar_contador_no_operativos, sar_contador_semi_operativos, sar_diccionario_operativos, sar_diccionario_no_operativos, sar_diccionario_semi_operativos
    global sapu_contador_operativos, sapu_contador_no_operativos, sapu_contador_semi_operativos, sapu_diccionario_operativos, sapu_diccionario_no_operativos, sapu_diccionario_semi_operativos



    for _, raw in nombre.iterrows():

      if raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_operativos+=1
        hospital_diccionario_operativos[f'{columna_de_interes1} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_no_operativos+=1
        hospital_diccionario_no_operativos[f'{columna_de_interes1} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_semi_operativos+=1
        hospital_diccionario_semi_operativos[f'{columna_de_interes1} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])


      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_operativos+=1
        centro_diccionario_operativos[f'{columna_de_interes1} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_no_operativos+=1
        centro_diccionario_no_operativos[f'{columna_de_interes1} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_semi_operativos+=1
        centro_diccionario_semi_operativos[f'{columna_de_interes1} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_operativos+=1
        comunitario_diccionario_operativos[f'{columna_de_interes1} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_no_operativos+=1
        comunitario_diccionario_no_operativos[f'{columna_de_interes1} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_semi_operativos+=1
        comunitario_diccionario_semi_operativos[f'{columna_de_interes1} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_operativos+=1
        psr_diccionario_operativos[f'{columna_de_interes1} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_no_operativos+=1
        psr_diccionario_no_operativos[f'{columna_de_interes1} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_semi_operativos+=1
        psr_diccionario_semi_operativos[f'{columna_de_interes1} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_operativos+=1
        sur_diccionario_operativos[f'{columna_de_interes1} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_no_operativos+=1
        sur_diccionario_no_operativos[f'{columna_de_interes1} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_semi_operativos+=1
        sur_diccionario_semi_operativos[f'{columna_de_interes1} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_operativos+=1
        sar_diccionario_operativos[f'{columna_de_interes1} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_no_operativos+=1
        sar_diccionario_no_operativos[f'{columna_de_interes1} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_semi_operativos+=1
        sar_diccionario_semi_operativos[f'{columna_de_interes1} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_operativos+=1
        sapu_diccionario_operativos[f'{columna_de_interes1} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_no_operativos+=1
        sapu_diccionario_no_operativos[f'{columna_de_interes1} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_semi_operativos+=1
        sapu_diccionario_semi_operativos[f'{columna_de_interes1} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
    return None
  recolectar_datos_establecimientos(hospital)
  print(hospital_contador_operativos)
  recolectar_datos_establecimientos(centro)
  recolectar_datos_establecimientos(comunitario)
  recolectar_datos_establecimientos(psr)
  recolectar_datos_establecimientos(sur)
  recolectar_datos_establecimientos(sar)
  recolectar_datos_establecimientos(sapu)
  datos['Tipo de Establecimientos'].append('Hospital')
  datos['Operativos'].append(hospital_contador_operativos)
  datos['No Operativos'].append(hospital_contador_no_operativos)
  datos['Semi Operativos'].append(hospital_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('Centro de Salud Familiar')
  datos['Operativos'].append(centro_contador_operativos)
  datos['No Operativos'].append(centro_contador_no_operativos)
  datos['Semi Operativos'].append(centro_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('Centro Comunitario de Salud Familiar')
  datos['Operativos'].append(comunitario_contador_operativos)
  datos['No Operativos'].append(comunitario_contador_no_operativos)
  datos['Semi Operativos'].append(comunitario_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('Posta de Salud Rural')
  datos['Operativos'].append(psr_contador_operativos)
  datos['No Operativos'].append(psr_contador_no_operativos)
  datos['Semi Operativos'].append(psr_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('SUR')
  datos['Operativos'].append(sur_contador_operativos)
  datos['No Operativos'].append(sur_contador_no_operativos)
  datos['Semi Operativos'].append(sur_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('SAR')
  datos['Operativos'].append(sar_contador_operativos)
  datos['No Operativos'].append(sar_contador_no_operativos)
  datos['Semi Operativos'].append(sar_contador_semi_operativos)
  datos['Tipo de Establecimientos'].append('SAPU')
  datos['Operativos'].append(sapu_contador_operativos)
  datos['No Operativos'].append(sapu_contador_no_operativos)
  datos['Semi Operativos'].append(sapu_contador_semi_operativos)
  tabla = pd.DataFrame(datos)
  return tabla

