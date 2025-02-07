import pandas as pd
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc

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
    return df_energia