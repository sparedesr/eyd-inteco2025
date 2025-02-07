import pandas as pd
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc

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
    return df_gases
