import pandas as pd
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc

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
    return df_vias_acceso
