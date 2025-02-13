import pandas as pd
def crear_tabla_consultas(archivo):
    try:
        consultas = ['NUMERO_PACIENTES_ACTUALES_HOSPITALIZADOS','NUMERO_PACIENTES_FALLECIDOS','NUMERO_ATENCIONES_ULTIMO_REPORTE'
                     ,'NUMERO_ATENCIONES_ACUMULADOS']
        datos = {'TIPO_ESTABLECIMIENTO' : ['CENTRO_COMUNITARIO_DE_SALUD_FAMILIAR','CENTRO_DE_SALUD_FAMILIAR'
                                           ,'HOSPITAL','MODULO_DENTAL','POSTA_DE_SALUD_RURAL'
                                           ,'SAPU','SAR','SUR'],
                 'NUMERO_PACIENTES_ACTUALES_HOSPITALIZADOS' : [],
                 'NUMERO_PACIENTES_FALLECIDOS' : [],
                 'NUMERO_ATENCIONES_ULTIMO_REPORTE' : [],
                 'NUMERO_ATENCIONES_ACUMULADOS' : []}
        # Convertir la columna a números (reemplazando valores no convertibles por 0)
        archivo[consultas] = archivo[consultas].apply(
            lambda valor: float(valor) if str(valor).replace('.', '', 1).isdigit() else 0
        )

        


        # Filtrar solo los hospitales
        df_hospitales = archivo[archivo['TIPO_ESTABLECIMIENTO'] == 'HOSPITAL']
        
        # Sumar las columnas
        hospitalizados_hospital = df_hospitales['NUMERO_PACIENTES_ACTUALES_HOSPITALIZADOS'].sum()
        fallecidos_hospital = df_hospitales['NUMERO_PACIENTES_FALLECIDOS'].sum()
        
    except Exception as e:
        return f'Error: {e}'
    
    datos['NUMERO_PACIENTES_ACTUALES_HOSPITALIZADOS'].append(hospitalizados_hospital)
    tabla = pd.DataFrame(datos)
    tabla_html = tabla.to_html(classes="table table-striped", index=False, escape=False)
    tablas_Operatividad = {}
    tablas_Operatividad['principalCONSULTAS'] = tabla_html
    return tablas_Operatividad