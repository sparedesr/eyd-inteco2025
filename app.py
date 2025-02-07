import pandas as pd
import os
import glob
import datetime
import threading
from unidecode import unidecode
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, jsonify, send_file, session
from flask_session import Session

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'goku'
app.config['SESSION_TYPE'] = 'filesystem'  # Guarda la sesión en archivos temporales
Session(app)  # Activa Flask-Session

# Tabla de operatividad

# Función para generar la tabla después de procesar el archivo
from flask import session




curico_diccionario_operativos = {'curico' : []}
curico_diccionario_inoperativos = {'curico' : []}
curico_diccionario_semi = {'curico' : []}

talca_diccionario_operativos = {'talca' : []}
talca_diccionario_inoperativos = {'talca' : []}
talca_diccionario_semi = {'talca' : []}

linares_diccionario_operativos = {'linares' : []}
linares_diccionario_inoperativos = {'linares' : []}
linares_diccionario_semi = {'linares' : []}

cauquenes_diccionario_operativos = {'cauquenes' : []}
cauquenes_diccionario_inoperativos = {'cauquenes' : []}
cauquenes_diccionario_semi = {'cauquenes' : []}

curico_operativos = 0
curico_inoperativos = 0
curico_semioperativos = 0

talca_operativos = 0
talca_inoperativos = 0
talca_semioperativos = 0

linares_operativos = 0
linares_inoperativos = 0
linares_semioperativos = 0

cauquenes_operativos = 0
cauquenes_inoperativos = 0
cauquenes_semioperativos = 0


columna_de_interes1 = "BODEGAS_PNAC"
hospital_diccionario_operativos = {f'bodega hospital': []}
hospital_diccionario_no_operativos = {f'bodega hospital': []}
hospital_diccionario_semi_operativos = {f'bodega hospital': []}

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
      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_no_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_semi_operativos+=1



      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_operativos+=1
 

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_no_operativos+=1
 

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_semi_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_no_operativos+=1
        
      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_semi_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_no_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_semi_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_no_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_semi_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_no_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_semi_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'NO_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_no_operativos+=1

      elif raw[f'{columna_de_interes1}'] == 'SEMI_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_semi_operativos+=1

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
  diccionario = {}
  tabla_html = tabla.to_html(classes="table table-striped", index=False)
  diccionario['principalBodegas'] = tabla_html
  return diccionario


def crear_tabla_provincia(archivo):
  pd.set_option('display.max_rows', None)  # Muestra todas las filas
  pd.set_option('display.max_columns', None)  # Muestra todas las columnas
  data = []

  def separacion_instalaciones(tipoDeInstalacion):
      data = {
          'ID_EDAN': [],
          'NOMBRE_ESTABLECIMIENTO': [],
          'COMUNA': [],
          'OPERATIVIDAD_ESTABLECIMIENTO': [],
      }
      for _, raw in archivo.iterrows():

          edan = raw['ID_EDAN']
          nombre = raw['NOMBRE_ESTABLECIMIENTO']
          comuna = raw['COMUNA']
          operatividad = raw['OPERATIVIDAD_ESTABLECIMIENTO']
          tipo = tipoDeInstalacion

          if tipo in nombre:
              data['ID_EDAN'].append(edan)
              data['NOMBRE_ESTABLECIMIENTO'].append(nombre)
              data['COMUNA'].append(comuna)
              data['OPERATIVIDAD_ESTABLECIMIENTO'].append(operatividad)

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
      'Provincias': [],
      'Operativos': [],
      'Inoperativos': [],
      'Semioperativos': [],
  }





  def recolectar_datos_establecimientos(nombre):
    global curico_operativos, curico_inoperativos, curico_semioperativos
    global talca_operativos, talca_inoperativos, talca_semioperativos
    global linares_operativos, linares_inoperativos, linares_semioperativos
    global cauquenes_operativos, cauquenes_inoperativos, cauquenes_semioperativos

    global curico_diccionario_operativos, curico_diccionario_inoperativos, curico_diccionario_semi
    global talca_diccionario_operativos, talca_diccionario_inoperativos, talca_diccionario_semi
    global linares_diccionario_operativos, linares_diccionario_inoperativos, linares_diccionario_semi
    global cauquenes_diccionario_operativos, cauquenes_diccionario_inoperativos, cauquenes_diccionario_semi
    for _, raw in nombre.iterrows():

      if raw['COMUNA'] == "CURICO" or raw['COMUNA'] == 'ROMERAL' or raw['COMUNA'] == 'TENO' or raw['COMUNA'] == 'MOLINA' or raw['COMUNA'] == 'SAGRADA_FAMILIA' or raw['COMUNA'] == 'RAUCO' or raw['COMUNA'] == 'HUALAÑE' or raw['COMUNA'] == 'HUALANE' or raw['COMUNA'] == 'LICANTEN' or raw['COMUNA'] == 'VICHUQUEN' :

        if raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'INOPERATIVO':
          curico_inoperativos += 1
          curico_diccionario_inoperativos['curico'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'SEMIOPERATIVO':
          curico_semioperativos += 1
          curico_diccionario_semi['curico'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'OPERATIVO':
          curico_operativos += 1
          curico_diccionario_operativos['curico'].append(raw['NOMBRE_ESTABLECIMIENTO'])


      if raw['COMUNA'] == "TALCA" or raw['COMUNA'] =='EMPEDRADO' or raw['COMUNA'] =='PELARCO' or raw['COMUNA'] =='PENCAHUE' or raw['COMUNA'] =='RIO_CLARO' or raw['COMUNA'] =='SAN_CLEMENTE' or raw['COMUNA'] =='SAN_RAFAEL' or raw['COMUNA'] =='CONSTITUCION' or raw['COMUNA'] =='CUREPTO' or raw['COMUNA'] =='MAULE' :
        if raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'INOPERATIVO':
          talca_inoperativos += 1
          talca_diccionario_inoperativos['talca'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'SEMIOPERATIVO':
          talca_semioperativos += 1
          talca_diccionario_semi['talca'].append(raw['NOMBRE_ESTABLECIMIENTO'])
        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'OPERATIVO':
          talca_operativos += 1
          talca_diccionario_operativos['talca'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      if raw['COMUNA'] =="LINARES" or raw['COMUNA'] =='COLBUN' or raw['COMUNA'] =='LONGAVI' or raw['COMUNA'] =='PARRAL' or raw['COMUNA'] =='RETIRO' or raw['COMUNA'] =='SAN_JAVIER' or raw['COMUNA'] =='VILLA_ALEGRE' or raw['COMUNA'] =='YERBAS_BUENAS':
        if raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'INOPERATIVO':
          linares_inoperativos += 1
          linares_diccionario_inoperativos['linares'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'SEMIOPERATIVO':
          linares_semioperativos += 1
          linares_diccionario_semi['linares'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'OPERATIVO':
          linares_operativos += 1
          linares_diccionario_operativos['linares'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      if  raw['COMUNA'] =="CAUQUENES" or raw['COMUNA'] =='CHANCO' or raw['COMUNA'] =='PELLUHUE':
        if raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'INOPERATIVO':
          cauquenes_inoperativos += 1
          cauquenes_diccionario_inoperativos['cauquenes'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'SEMIOPERATIVO':
          cauquenes_semioperativos += 1
          cauquenes_diccionario_semi['cauquenes'].append(raw['NOMBRE_ESTABLECIMIENTO'])

        elif raw['OPERATIVIDAD_ESTABLECIMIENTO'] == 'OPERATIVO':
          cauquenes_operativos += 1
          cauquenes_diccionario_operativos['cauquenes'].append(raw['NOMBRE_ESTABLECIMIENTO'])
    return None

  recolectar_datos_establecimientos(hospital)
  recolectar_datos_establecimientos(sur)
  recolectar_datos_establecimientos(sar)
  recolectar_datos_establecimientos(sapu)
  recolectar_datos_establecimientos(centro)
  recolectar_datos_establecimientos(comunitario)
  recolectar_datos_establecimientos(psr)
  datos['Provincias'].append('Curicó')
  datos['Operativos'].append(curico_operativos)
  datos['Inoperativos'].append(curico_inoperativos)
  datos['Semioperativos'].append(curico_semioperativos)

  datos['Provincias'].append('Talca')
  datos['Operativos'].append(talca_operativos)
  datos['Inoperativos'].append(talca_inoperativos)
  datos['Semioperativos'].append(talca_semioperativos)

  datos['Provincias'].append('Linares')
  datos['Operativos'].append(linares_operativos)
  datos['Inoperativos'].append(linares_inoperativos)
  datos['Semioperativos'].append(linares_semioperativos)

  datos['Provincias'].append('Cauquenes')
  datos['Operativos'].append(cauquenes_operativos)
  datos['Inoperativos'].append(cauquenes_inoperativos)
  datos['Semioperativos'].append(cauquenes_semioperativos)

  tabla = pd.DataFrame(datos)
  diccionario = {}
  tabla_html = tabla.to_html(classes="table table-striped", index=False)
  diccionario['principalProvincia'] = tabla_html
  return diccionario

def crear_tabla_vias_acceso(archivo):
    # Configuración para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Cargar el archivo Excel


    # Filtrar los datos por el rango de horas especificado




    # Crear columna para clasificar los tipos de establecimientos
    archivo['TIPO_ESTABLECIMIENTO'] = archivo['NOMBRE_ESTABLECIMIENTO'].str.extract(
        '(HOSPITAL|POSTA|SUR|SAR|SAPU|CENTRO|MODULO)', expand=False)

    # Diccionarios para almacenar los establecimientos por estado de vías de acceso
    diccionario_vias_normales = {}
    diccionario_vias_con_danos_acceso = {}
    diccionario_vias_con_danos = {}

    for _, row in archivo.iterrows():
        tipo = row['TIPO_ESTABLECIMIENTO']
        nombre = row['NOMBRE_ESTABLECIMIENTO']
        vias = row['VIAS_DE_ACCESO']
        detalle = row['DETALLE_VIAS_DE_ACCESO'] if pd.notna(row['DETALLE_VIAS_DE_ACCESO']) else "NO INFO"
        
        if tipo not in diccionario_vias_normales:
            diccionario_vias_normales[tipo] = []
            diccionario_vias_con_danos_acceso[tipo] = []
            diccionario_vias_con_danos[tipo] = []
        
        if str(vias).strip().lower() == "VIAS_CON_DAÑOS_CON_ACCESO":
            diccionario_vias_con_danos_acceso[tipo].append(f"{nombre} - Detalle: {detalle}")
        elif str(vias).strip().lower() == "VIAS_CON_DAÑOS":
            diccionario_vias_con_danos[tipo].append(f"{nombre} - Detalle: {detalle}")
        else:
            diccionario_vias_normales[tipo].append(nombre)

    # Crear DataFrame para la tabla principal
    datos = []
    for tipo in archivo['TIPO_ESTABLECIMIENTO'].unique():
        datos.append({
            "Tipo de Instalación": tipo,
            "Vías Normales": len(diccionario_vias_normales[tipo]),
            "Vías con Daños con Acceso": len(diccionario_vias_con_danos_acceso[tipo]),
            "Vías con Daños": len(diccionario_vias_con_danos[tipo]),
        })

    df_vias_acceso = pd.DataFrame(datos)
    diccionario = {}
    tabla_html = df_vias_acceso.to_html(classes="table table-striped", index=False)
    diccionario['principalViasDeAcceso'] = tabla_html
    return diccionario

def crear_tabla_gases(archivo):
    # Configuración para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)  # Muestra todas las filas
    pd.set_option('display.max_columns', None)  # Muestra todas las columnas

    # Cargar el archivo Excel




    # Crear un DataFrame filtrado


    # Crear columna para clasificar los tipos de establecimientos
    archivo['TIPO_ESTABLECIMIENTO'] = archivo['NOMBRE_ESTABLECIMIENTO'].str.extract(
        '(HOSPITAL|POSTA|SUR|SAR|SAPU|CENTRO|MODULO)', expand=False)

    # Función para filtrar según el estado de gases clínicos
    def separacion_gases_clinicos(estado_gases):
        data = {
            'ID_EDAN': [],
            'NOMBRE_ESTABLECIMIENTO': [],
            'TIPO_ESTABLECIMIENTO': [],
            'GASES_CLINICOS': [],
        }
        for _, raw in archivo.iterrows():
            edan = raw['ID_EDAN']
            nombre = raw['NOMBRE_ESTABLECIMIENTO']
            tipo = raw['TIPO_ESTABLECIMIENTO']
            gases = raw['GASES_CLINICOS']

            if estado_gases in gases:
                data['ID_EDAN'].append(edan)
                data['NOMBRE_ESTABLECIMIENTO'].append(nombre)
                data['TIPO_ESTABLECIMIENTO'].append(tipo)
                data['GASES_CLINICOS'].append(gases)

        datos = pd.DataFrame(data)
        return datos

    # Filtrar los datos para las dos categorías de gases clínicos
    gases_normal = separacion_gases_clinicos('SERVICIO_NORMAL')
    gases_sin_servicio = separacion_gases_clinicos('NO_APLICA')

    # Crear los diccionarios para almacenar las instalaciones por tipo de establecimiento y estado de gases
    diccionario_servicio_normal = {}
    diccionario_sin_servicio = {}

    # Llenamos los diccionarios con las instalaciones por tipo de establecimiento y estado de gases
    for tipo in archivo['TIPO_ESTABLECIMIENTO'].unique():
        diccionario_servicio_normal[tipo] = gases_normal[gases_normal['TIPO_ESTABLECIMIENTO'] == tipo]['NOMBRE_ESTABLECIMIENTO'].tolist()
        diccionario_sin_servicio[tipo] = gases_sin_servicio[gases_sin_servicio['TIPO_ESTABLECIMIENTO'] == tipo]['NOMBRE_ESTABLECIMIENTO'].tolist()

    # Preparar los datos para la tabla
    datos = {
        'TIPO_DE_INSTALACION': [],
        'GASES_CLINICOS_NORMAL': [],
        'SIN_GASES_CLINICOS': [],
    }

    # Contadores globales
    gases_normal_total = 0
    gases_sin_servicio_total = 0

    # Llenamos los datos con los totales por tipo de instalación
    for tipo in archivo['TIPO_ESTABLECIMIENTO'].unique():
        gases_normal_tipo = len(diccionario_servicio_normal[tipo])
        gases_sin_servicio_tipo = len(diccionario_sin_servicio[tipo])

        datos['TIPO_DE_INSTALACION'].append(tipo)
        datos['GASES_CLINICOS_NORMAL'].append(gases_normal_tipo)
        gases_normal_total += gases_normal_tipo
        datos['SIN_GASES_CLINICOS'].append(gases_sin_servicio_tipo)
        gases_sin_servicio_total += gases_sin_servicio_tipo

    # Convertir los datos a un DataFrame
    df_gases = pd.DataFrame(datos)
    diccionario = {}
    tabla_html = df_gases.to_html(classes="table table-striped", index=False)
    diccionario['principalGases'] = tabla_html
    return diccionario

def crear_tabla_energia(archivo):
    # Configuración para mostrar todas las filas y columnas
    pd.set_option('display.max_rows', None)  # Muestra todas las filas
    pd.set_option('display.max_columns', None)  # Muestra todas las columnas

    # Cargar el archivo Excel


    # Filtrar los datos por el rango de horas especificado




    # Crear columna para clasificar los tipos de establecimientos
    archivo['TIPO_ESTABLECIMIENTO'] = archivo['NOMBRE_ESTABLECIMIENTO'].str.extract(
        '(HOSPITAL|POSTA|SUR|SAR|SAPU|CENTRO|MODULO)', expand=False)

    # Función para filtrar según el estado de energía
    def separacion_energia(estado_energia):
        data = {
            'ID_EDAN': [],
            'NOMBRE_ESTABLECIMIENTO': [],
            'TIPO_ESTABLECIMIENTO': [],
            'ENERGIA': [],
        }
        for _, raw in archivo.iterrows():
            edan = raw['ID_EDAN']
            nombre = raw['NOMBRE_ESTABLECIMIENTO']
            tipo = raw['TIPO_ESTABLECIMIENTO']
            energia = raw['ENERGIA']

            if estado_energia in energia:
                data['ID_EDAN'].append(edan)
                data['NOMBRE_ESTABLECIMIENTO'].append(nombre)
                data['TIPO_ESTABLECIMIENTO'].append(tipo)
                data['ENERGIA'].append(energia)

        datos = pd.DataFrame(data)
        return datos

    # Filtrar los datos para las dos categorías de energía
    energia_normal = separacion_energia('SERVICIO_NORMAL')
    energia_sin_servicio = separacion_energia('SIN_SERVICIO')

    # Crear los diccionarios para almacenar las instalaciones por tipo de establecimiento y estado de energía
    diccionario_servicio_normal = {}
    diccionario_sin_servicio = {}

    # Llenamos los diccionarios con las instalaciones por tipo de establecimiento y estado de energía
    for tipo in archivo['TIPO_ESTABLECIMIENTO'].unique():
        diccionario_servicio_normal[tipo] = energia_normal[energia_normal['TIPO_ESTABLECIMIENTO'] == tipo]['NOMBRE_ESTABLECIMIENTO'].tolist()
        diccionario_sin_servicio[tipo] = energia_sin_servicio[energia_sin_servicio['TIPO_ESTABLECIMIENTO'] == tipo]['NOMBRE_ESTABLECIMIENTO'].tolist()

    # Preparar los datos para la tabla
    datos = {
        'Tipo de Instalación': [],
        'Energía Normal': [],
        'Sin Energía': [],
    }

    # Contadores globales
    energia_normal_total = 0
    energia_sin_servicio_total = 0

    # Llenamos los datos con los totales por tipo de instalación
    for tipo in archivo['TIPO_ESTABLECIMIENTO'].unique():
        energia_normal_tipo = len(diccionario_servicio_normal[tipo])
        energia_sin_servicio_tipo = len(diccionario_sin_servicio[tipo])

        datos['Tipo de Instalación'].append(tipo)
        datos['Energía Normal'].append(energia_normal_tipo)
        energia_normal_total += energia_normal_tipo
        datos['Sin Energía'].append(energia_sin_servicio_tipo)
        energia_sin_servicio_total += energia_sin_servicio_tipo

    # Convertir los datos a un DataFrame
    df_energia = pd.DataFrame(datos)
    diccionario = {}
    tabla_html = df_energia.to_html(classes="table table-striped", index=False)
    diccionario['principalEnergia'] = tabla_html
    return diccionario
columna_de_interes = "PABELLONES"




hospital_diccionario_operativos = {f'{columna_de_interes} hospital': []}
hospital_diccionario_no_operativos = {f'{columna_de_interes} hospital': []}
hospital_diccionario_semi_operativos = {f'{columna_de_interes} hospital': []}

centro_diccionario_operativos = {f'{columna_de_interes} centro': []}
centro_diccionario_no_operativos = {f'{columna_de_interes} centro': []}
centro_diccionario_semi_operativos = {f'{columna_de_interes} centro': []}

comunitario_diccionario_operativos = {f'{columna_de_interes} comunitario': []}
comunitario_diccionario_no_operativos = {f'{columna_de_interes} comunitario': []}
comunitario_diccionario_semi_operativos = {f'{columna_de_interes} comunitario': []}

psr_diccionario_operativos = {f'{columna_de_interes} psr': []}
psr_diccionario_no_operativos = {f'{columna_de_interes} psr': []}
psr_diccionario_semi_operativos = {f'{columna_de_interes} psr': []}

csmc_diccionario_operativos = {f'{columna_de_interes} csmc': []}
csmc_diccionario_no_operativos = {f'{columna_de_interes} csmc': []}
csmc_diccionario_semi_operativos = {f'{columna_de_interes} csmc': []}

sur_diccionario_operativos = {f'{columna_de_interes} sur': []}
sur_diccionario_no_operativos = {f'{columna_de_interes} sur': []}
sur_diccionario_semi_operativos = {f'{columna_de_interes} sur': []}

sar_diccionario_operativos = {f'{columna_de_interes} sar': []}
sar_diccionario_no_operativos = {f'{columna_de_interes} sar': []}
sar_diccionario_semi_operativos = {f'{columna_de_interes} sar': []}

sapu_diccionario_operativos = {f'{columna_de_interes} sapu': []}
sapu_diccionario_no_operativos = {f'{columna_de_interes} sapu': []}
sapu_diccionario_semi_operativos = {f'{columna_de_interes} sapu': []}

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
def crear_tabla_pabellones(archivo):
  pd.set_option('display.max_rows', None)  # Muestra todas las filas
  pd.set_option('display.max_columns', None)  # Muestra todas las columnas

  data = []


  def separacion_instalaciones(tipoDeInstalacion):
      data = {
          'ID_EDAN': [],
          'NOMBRE_ESTABLECIMIENTO': [],
          'COMUNA': [],
          f'{columna_de_interes}': [],
      }
      for _, raw in archivo.iterrows():

          edan = raw['ID_EDAN']
          nombre = raw['NOMBRE_ESTABLECIMIENTO']
          comuna = raw['COMUNA']
          operatividad = raw[f'{columna_de_interes}']
          tipo = tipoDeInstalacion

          if tipo in nombre:
              data['ID_EDAN'].append(edan)
              data['NOMBRE_ESTABLECIMIENTO'].append(nombre)
              data['COMUNA'].append(comuna)
              data[f'{columna_de_interes}'].append(operatividad)

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

      if raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_operativos+=1
        hospital_diccionario_operativos[f'{columna_de_interes} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_no_operativos+=1
        hospital_diccionario_no_operativos[f'{columna_de_interes} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'HOSPITAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        hospital_contador_semi_operativos+=1
        hospital_diccionario_semi_operativos[f'{columna_de_interes} hospital'].append(raw['NOMBRE_ESTABLECIMIENTO'])


      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_operativos+=1
        centro_diccionario_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_no_operativos+=1
        centro_diccionario_no_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'CENTRO_DE_SALUD_FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_semi_operativos+=1
        centro_diccionario_semi_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'CENTRO COMUNITARIO DE SALUD FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_operativos+=1
        comunitario_diccionario_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'CENTRO COMUNITARIO DE SALUD FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_no_operativos+=1
        comunitario_diccionario_no_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'CENTRO COMUNITARIO DE SALUD FAMILIAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_semi_operativos+=1
        comunitario_diccionario_semi_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_operativos+=1
        psr_diccionario_operativos[f'{columna_de_interes} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_no_operativos+=1
        psr_diccionario_no_operativos[f'{columna_de_interes} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'POSTA_DE_SALUD_RURAL' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_semi_operativos+=1
        psr_diccionario_semi_operativos[f'{columna_de_interes} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_operativos+=1
        sur_diccionario_operativos[f'{columna_de_interes} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_no_operativos+=1
        sur_diccionario_no_operativos[f'{columna_de_interes} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'SUR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sur_contador_semi_operativos+=1
        sur_diccionario_semi_operativos[f'{columna_de_interes} sur'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_operativos+=1
        sar_diccionario_operativos[f'{columna_de_interes} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_no_operativos+=1
        sar_diccionario_no_operativos[f'{columna_de_interes} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'SAR' in raw['NOMBRE_ESTABLECIMIENTO']:
        sar_contador_semi_operativos+=1
        sar_diccionario_semi_operativos[f'{columna_de_interes} sar'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_operativos+=1
        sapu_diccionario_operativos[f'{columna_de_interes} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_no_operativos+=1
        sapu_diccionario_no_operativos[f'{columna_de_interes} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'SAPU' in raw['NOMBRE_ESTABLECIMIENTO']:
        sapu_contador_semi_operativos+=1
        sapu_diccionario_semi_operativos[f'{columna_de_interes} sapu'].append(raw['NOMBRE_ESTABLECIMIENTO'])
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
  diccionario = {}
  tabla_html = tabla.to_html(classes="table table-striped", index=False)
  diccionario['principalPabellones'] = tabla_html
  return diccionario

def tabla_operatividad(archivo):
    try:
        tipos_operatividad = ['OPERATIVO', 'SEMIOPERATIVO', 'INOPERATIVO']
        df_operativos = archivo[archivo['OPERATIVIDAD_ESTABLECIMIENTO'].isin(tipos_operatividad)]

        # Generar la tabla resumen
        conteo_establecimientos = (
            df_operativos.groupby(['TIPO_ESTABLECIMIENTO', 'OPERATIVIDAD_ESTABLECIMIENTO'])
            .size()
            .unstack(fill_value=0)
        )

        for tipo in tipos_operatividad:
            if tipo not in conteo_establecimientos.columns:
                conteo_establecimientos[tipo] = 0

        conteo_establecimientos = conteo_establecimientos[['OPERATIVO', 'SEMIOPERATIVO', 'INOPERATIVO']]
        conteo_establecimientos = conteo_establecimientos.reset_index()
        conteo_establecimientos = conteo_establecimientos.rename_axis(None, axis=1)

        # Convertir la tabla en HTML
        conteo_establecimientos_html = conteo_establecimientos.to_html(classes="table table-striped", index=False, escape=False)

        # Marcar celdas clicables con un atributo "data-clickable"
        conteo_establecimientos_html = conteo_establecimientos_html.replace(
            r'<td>([1-9][0-9]*)</td>',
            r'<td data-clickable="true" style="cursor: pointer;">\1</td>'
        )

        # Usar un diccionario en lugar de una lista
        tablas_Operatividad = {}

        # Almacenar la tabla resumen
        tablas_Operatividad['principalOperatividad'] = conteo_establecimientos_html

        # Para cada tipo de operatividad, crear una tabla con los datos filtrados
        for operatividad in tipos_operatividad:
            for tipo_establecimiento in archivo['TIPO_ESTABLECIMIENTO'].unique():
                # Filtrar el DataFrame por tipo de establecimiento y operatividad
                df_filtrado = archivo[(archivo['TIPO_ESTABLECIMIENTO'] == tipo_establecimiento) & 
                                (archivo['OPERATIVIDAD_ESTABLECIMIENTO'] == operatividad)]
                
                # Si el DataFrame no está vacío, proceder
                if not df_filtrado.empty:
                    columnas = ['NOMBRE_ESTABLECIMIENTO', 'OPERATIVIDAD_ESTABLECIMIENTO']
                    # Añadir la columna 'DESCRIPCION_SITUACION' si la operatividad es SEMIOPERATIVO o INOPERATIVO
                    if operatividad in ['SEMIOPERATIVO', 'INOPERATIVO']:
                        df_filtrado['DESCRIPCION_SITUACION'] = df_filtrado.get('DESCRIPCION_SITUACION', 'SIN_DESCRIPCION')
                        columnas.append('DESCRIPCION_SITUACION')

                    # Convertir la tabla filtrada en HTML
                    table_name = f"{tipo_establecimiento}_{operatividad}".upper()
                    tablas_Operatividad[table_name] = df_filtrado[columnas].to_html(classes="table table-striped", index=False)

        # Asegurarse de que las tablas HTML se devuelvan correctamente
        return tablas_Operatividad

    except Exception as e:
        raise ValueError(f"Error al generar la tabla: {e}")


def tablaAfectacionComuna(archivo):
    try:
        # Crear lista con los tipos de establecimientos únicos
        tipos_establecimiento = archivo['TIPO_ESTABLECIMIENTO'].unique()
        
        # Crear un diccionario para almacenar los resultados de cada tipo de establecimiento
        resultado = {'COMUNA': []}
        
        # Añadir las columnas de tipo S (semioperativo) e I (inoperativo)
        for tipo in tipos_establecimiento:
            resultado[f'{tipo}_S'] = []
            resultado[f'{tipo}_I'] = []
        
        # Diccionario para almacenar las tablas individuales
        tablasAfectacionC = {}
        
        # Agrupar los datos por COMUNA
        for comuna, grupo in archivo.groupby('COMUNA'):
            resultado['COMUNA'].append(comuna)
            
            # Para cada tipo de establecimiento, contar los semioperativos e inoperativos
            for tipo in tipos_establecimiento:
                # Filtrar los establecimientos con el tipo y operatividad correspondientes
                semioperativos = grupo[(grupo['TIPO_ESTABLECIMIENTO'] == tipo) & (grupo['OPERATIVIDAD_ESTABLECIMIENTO'] == 'SEMIOPERATIVO')]
                inoperativos = grupo[(grupo['TIPO_ESTABLECIMIENTO'] == tipo) & (grupo['OPERATIVIDAD_ESTABLECIMIENTO'] == 'INOPERATIVO')]
                
                # Contar los registros y agregarlos a las listas de resultados
                resultado[f'{tipo}_S'].append(semioperativos.shape[0])
                resultado[f'{tipo}_I'].append(inoperativos.shape[0])
                
                # Crear tablas individuales para semioperativos
                if not semioperativos.empty:
                    # Obtener el primer valor de la fila (comuna) y columna (tipo de establecimiento)
                    comuna_valor = semioperativos.iloc[0]['COMUNA']
                    operatividad = 'S'  # Para semioperativo
                    table_name = f"{comuna_valor}_{tipo}_{operatividad}".upper()
                    tablasAfectacionC[table_name] = semioperativos[['COMUNA', 'TIPO_ESTABLECIMIENTO', 'NOMBRE_ESTABLECIMIENTO']].to_html(classes="table table-striped", index=False)
                
                # Crear tablas individuales para inoperativos
                if not inoperativos.empty:
                    # Obtener el primer valor de la fila (comuna) y columna (tipo de establecimiento)
                    comuna_valor = inoperativos.iloc[0]['COMUNA']
                    operatividad = 'I'  # Para inoperativo
                    table_name = f"{comuna_valor}_{tipo}_{operatividad}".upper()
                    tablasAfectacionC[table_name] = inoperativos[['COMUNA', 'TIPO_ESTABLECIMIENTO', 'NOMBRE_ESTABLECIMIENTO']].to_html(classes="table table-striped", index=False)
        
        # Crear el DataFrame final con los resultados
        df_resultado = pd.DataFrame(resultado)
        
        # Convertir el DataFrame final a una tabla HTML
        principalAfectacionC = df_resultado.to_html(classes="table table-striped", index=False)
        tablasAfectacionC['principalAfectados por comuna'] = principalAfectacionC
        
        # Incluir las tablas individuales en la variable de retorno
        return tablasAfectacionC

    except Exception as e:
        raise ValueError(f"Error al generar la tabla: {e}")


# Funciones de procesamiento
def remove_accents(text):
    return unidecode(text) if isinstance(text, str) else text

def convert_to_string(value):
    if pd.api.types.is_number(value):  # Si es un número, conviértelo a cadena
        return str(value)
    elif isinstance(value, pd.Timestamp):  # Si es datetime, formatea como fecha y hora
        return value.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, pd.Timedelta):  # Si es un timedelta, conviértelo a cadena
        return str(value)
    elif isinstance(value, (datetime.time)):  # Si es un objeto de tiempo, formatea como hh:mm:ss
        return value.strftime('%H:%M:%S')
    return value  # Devolver el valor tal cual si no aplica ninguna condición


def eliminar_guiones_bajos(texto):
    if isinstance(texto, str):
        return texto.strip('_')
    return texto

def limpiar_df(_df_):
    _df_ = _df_.fillna('NOINFO')  
    _df_.columns = [col.upper() for col in _df_.columns]  
    _df_.columns = _df_.columns.map(remove_accents)  
    _df_ = _df_.map(remove_accents)  
    _df_ = _df_.map(lambda x: x.upper() if isinstance(x, str) else x)  
    _df_ = _df_.map(convert_to_string)  
    _df_ = _df_.replace(' ', '_', regex=True)  
    _df_.columns = _df_.columns.str.replace(' ', '_', regex=False)  
    _df_ = _df_.map(eliminar_guiones_bajos)  
    _df_.columns = _df_.columns.str.strip('_')  
    return _df_

def obtener_provincia(Nombre_Comuna):
    if Nombre_Comuna in ['CAUQUENES', 'CHANCO', 'PELLUHUE']:
        return 'CAUQUENES'
    elif Nombre_Comuna in ['COLBUN','LINARES', 'LONGAVI', 'PARRAL', 'RETIRO', 'SAN_JAVIER', 'VILLA_ALEGRE', 'YERBAS_BUENAS']:
        return 'LINARES'
    elif Nombre_Comuna in ['CONSTITUCION', 'CUREPTO', 'EMPEDRADO', 'MAULE', 'PELARCO', 'PENCAHUE', 'RIO_CLARO', 'SAN_CLEMENTE', 'SAN_RAFAEL', 'TALCA']:
        return 'TALCA'
    elif Nombre_Comuna in ['CURICO', 'HUALAÑE', 'HUALANE', 'LICANTEN', 'MOLINA', 'RAUCO', 'ROMERAL', 'SAGRADA_FAMILIA', 'TENO', 'VICHUQUEN']:
        return 'CURICO'
    else:
        return 'NOPROVINCIA'

def obtener_tipo(NOMBRE_ESTABLECIMIENTO):
    if 'HOSPITAL' in NOMBRE_ESTABLECIMIENTO:
        return 'HOSPITAL'
    elif 'POSTA' in NOMBRE_ESTABLECIMIENTO:
        return 'POSTA'
    elif 'CENTRO_DE_SALUD_FAMILIAR' in NOMBRE_ESTABLECIMIENTO:
        return 'CENTRO_DE_SALUD_FAMILIAR'
    elif 'SUR' in NOMBRE_ESTABLECIMIENTO:
        return 'SUR'
    elif 'SAR' in NOMBRE_ESTABLECIMIENTO:
        return 'SAR'
    elif 'SAPU' in NOMBRE_ESTABLECIMIENTO:
        return 'SAPU'
    elif 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR' in NOMBRE_ESTABLECIMIENTO:
        return 'CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR'
    elif 'MODULO_DENTAL' in NOMBRE_ESTABLECIMIENTO:
        return 'MODULO_DENTAL'
    else:
        return 'TIPO_NO_ESPECIFICADO'
    
def delete_uploaded_files():
    upload_folder = 'uploads'
    files = glob.glob(os.path.join(upload_folder, '*'))
    for file in files:
        try:
            os.remove(file)  # Elimina el archivo
            print(f'Archivo eliminado: {file}')
        except Exception as e:
            print(f'Error al eliminar el archivo {file}: {e}')

# Hook para ejecutar antes de cada solicitud
@app.before_request
def before_request():
    # Eliminar archivos solo si la solicitud es GET o HEAD
    if request.method in ['GET', 'HEAD']:
        delete_uploaded_files()

# Cargar y preparar los datos al iniciar la aplicación
custom_df = pd.DataFrame()  # Variable para almacenar la tabla filtrada
custom_df_original = pd.DataFrame()  # Variable para almacenar la tabla original

# Rutas generales

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subida')
def subida():
    return render_template('Tablas/subida.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/mapa')
def mapa():
    return render_template('mapa.html')

@app.route('/maule')
def maule():
    return render_template('mapa_maule.html')

@app.route('/changelog')
def changelog():
    return render_template('changelog.html')

# ////////////////////// Rutas de la pagina de subida //////////////////////

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_files = request.files.getlist('files[]')
        print("Archivos subidos:", uploaded_files)  # Agrega esto para ver el contenido de uploaded_files
        if not uploaded_files or all(file.filename == '' for file in uploaded_files):
            return jsonify({'error': 'No se subieron archivos.'}), 400

        global custom_df, custom_df_original
        custom_df = pd.DataFrame()

        tablaOperatividad = False
        tablaAfectacionC = False    

        for file in uploaded_files:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            df = pd.read_excel(filepath)
            df = limpiar_df(df)

            if 'NOMBRE_COMUNA' in df.columns:
                df['PROVINCIA'] = df['NOMBRE_COMUNA'].apply(obtener_provincia)

            if 'COMUNA' in df.columns:
                df['PROVINCIA'] = df['COMUNA'].apply(obtener_provincia)
                # df = df.drop(columns={'COMUNA'})

            if 'NOMBRE_ESTABLECIMIENTO' in df.columns:
                df['TIPO_ESTABLECIMIENTO'] = df['NOMBRE_ESTABLECIMIENTO'].apply(obtener_tipo)

            reqTablaOperatividad = ['TIPO_ESTABLECIMIENTO', 'OPERATIVIDAD_ESTABLECIMIENTO', 'NOMBRE_ESTABLECIMIENTO']
            if all(columna in df.columns for columna in reqTablaOperatividad):
                tablaOperatividad = True

            reqTablaAfectacionC = ['COMUNA', 'OPERATIVIDAD_ESTABLECIMIENTO', 'TIPO_ESTABLECIMIENTO', 'NOMBRE_ESTABLECIMIENTO']
            if all(columna in df.columns for columna in reqTablaAfectacionC):
                tablaAfectacionC = True

            custom_df = pd.concat([custom_df, df], ignore_index=True)

        custom_df_original = custom_df.copy()

        # Generar tablas y almacenarlas en la sesión
        tablas_Operatividad = tabla_operatividad(custom_df) if tablaOperatividad else {}
        tablasAfectacionC = tablaAfectacionComuna(custom_df) if tablaAfectacionC else {} #({}, {})
        tabla_pabellones = crear_tabla_pabellones(custom_df) if tablaAfectacionC else {}
        tabla_energia = crear_tabla_energia(custom_df) if tablaAfectacionC else {}
        tabla_gases = crear_tabla_gases(custom_df) if tablaAfectacionC else {}
        tabla_vias = crear_tabla_vias_acceso(custom_df) if tablaAfectacionC else {}
        tabla_provincia = crear_tabla_provincia(custom_df) if tablaAfectacionC else {}
        tabla_bodegas = crear_tabla_bodegas(custom_df) if tablaAfectacionC else {}
        
        
        session['tablas'] = (tabla_pabellones)
        session['tablas'].update(tabla_energia)
        session['tablas'].update(tabla_gases)
        session['tablas'].update(tabla_vias)
        session['tablas'].update(tabla_bodegas)
        session['tablas'].update(tablasAfectacionC)
        session['tablas'].update(tabla_provincia)
        session['tablas'].update(tablas_Operatividad)
        session.modified = True  # 🔥 Fuerza a Flask a guardar la sesión
        listaTablas = [tablaOperatividad,tablaAfectacionC,tabla_pabellones, tabla_energia, tabla_gases, tabla_vias, tabla_provincia, tabla_bodegas]
        tablaContainer = any(listaTablas)
        tablasPrincipales = [clave for clave in session.get('tablas',{}).keys() if 'principal' in clave]
        # print(tablasAfectacionC.keys())

        return jsonify({
            'message': 'Archivo(s) subido(s) exitosamente!',
            'tablasPrincipales': tablasPrincipales,
            'tablaContainer': tablaContainer
        }), 200

    except Exception as e:
        return jsonify({'error': f'Ocurrió un error al procesar los archivos: {str(e)}'}), 500

@app.route('/get_table', methods=['GET'])
def get_table():
    try:
        table_name = request.args.get('table_name')
        # print("Tablas en sesión:", session.get('tablas', {}).keys())  # 🔥 Ver qué tablas existen
        if not table_name:
            return jsonify({"error": "Nombre de la tabla no proporcionado."}), 400

        tablas = session.get('tablas', {})

        if table_name not in tablas:
            return '', 200
            # return jsonify({"error": f"La tabla '{table_name}' no existe."}), 404

        return jsonify({"table": tablas[table_name]}), 200

    except Exception as e:
        return jsonify({"error": f"Error al obtener la tabla: {str(e)}"}), 500

@app.route('/filtro')
def filtro():
    global custom_df
    if custom_df is None or custom_df.empty:
        return "No hay datos disponibles para filtrar. Suba un archivo primero.", 400

    columnas = custom_df.columns.tolist()
    return render_template('Tablas/filtro.html', columnas=columnas)

@app.route('/obtener_valores', methods=['POST'])
def obtener_valores():
    global custom_df
    columna = request.json.get('columna')
    if columna and columna in custom_df.columns:
        valores = custom_df[columna].dropna().unique().tolist()
        return jsonify({'valores': valores})
    return jsonify({'valores': []})

@app.route('/filtrar', methods=['POST'])
def filtrar():
    global custom_df
    columna = request.json.get('columna')
    valor = request.json.get('valor')
    columnas_seleccionadas = request.json.get('columnas_seleccionadas')

    if columna and valor and columna in custom_df.columns:
        custom_df = custom_df[custom_df[columna] == valor]

    if columnas_seleccionadas:
        df_filtrado = custom_df[columnas_seleccionadas]
    else:
        df_filtrado = custom_df.copy()

    df_html = df_filtrado.to_html(classes='table table-striped', index=False)
    return jsonify({'tabla': df_html})

@app.route('/reset_filters', methods=['POST'])
def reset_filters():
    global custom_df, custom_df_original
    if custom_df_original.empty:
        return jsonify({'error': 'No hay datos originales para reiniciar.'}), 400

    # Restaurar custom_df a su estado original
    custom_df = custom_df_original.copy()

    # Obtener las columnas seleccionadas
    columnas_seleccionadas = request.json.get('columnas_seleccionadas', [])
    if columnas_seleccionadas:
        df_reseteado = custom_df[columnas_seleccionadas]
    else:
        df_reseteado = custom_df.copy()

    df_html = df_reseteado.to_html(classes='table table-striped', index=False)
    return jsonify({'tabla': df_html})


@app.route('/download_filtered', methods=['GET'])
def download_filtered():
    try:
        global custom_df
        if custom_df is None or custom_df.empty:
            return "No hay datos filtrados para descargar.", 404

        columnas_seleccionadas = request.args.get('columnas', '')
        columnas_seleccionadas = columnas_seleccionadas.split(',') if columnas_seleccionadas else custom_df.columns.tolist()

        df_seleccionado = custom_df[columnas_seleccionadas]

        output_filename = 'datos_filtrados.xlsx'
        output_path = os.path.join(app.root_path, output_filename)
        df_seleccionado.to_excel(output_path, index=False)

        response = send_file(output_path, as_attachment=True, download_name="datos_filtrados.xlsx")

        @response.call_on_close
        def remove_file():
            try:
                os.remove(output_path)
                print(f"Archivo {output_filename} eliminado.")
            except Exception as e:
                print(f"Error al eliminar el archivo {output_filename}: {e}")

        threading.Timer(2, remove_file).start()
        return response
    except Exception as e:
        return f"Error al generar el archivo: {str(e)}", 500

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)