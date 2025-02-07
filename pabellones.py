import pandas as pd
from dash import Dash, html, dash_table, Input, Output, State
import dash_bootstrap_components as dbc
import matplotlib.pyplot as plt
from pandas.plotting import table

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
def crear_tabla_pabellones(edan):
  pd.set_option('display.max_rows', None)  # Muestra todas las filas
  pd.set_option('display.max_columns', None)  # Muestra todas las columnas

  data = []
  global columna_de_interes
  columna_de_interes = "PABELLONES"
  archivo = pd.read_excel(edan)




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


      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'Centro de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_operativos+=1
        centro_diccionario_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'Centro de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_no_operativos+=1
        centro_diccionario_no_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'Centro de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        centro_contador_semi_operativos+=1
        centro_diccionario_semi_operativos[f'{columna_de_interes} centro'].append(raw['NOMBRE_ESTABLECIMIENTO'])

      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'Centro Comunitario de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_operativos+=1
        comunitario_diccionario_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'Centro Comunitario de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_no_operativos+=1
        comunitario_diccionario_no_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'Centro Comunitario de Salud Familiar' in raw['NOMBRE_ESTABLECIMIENTO']:
        comunitario_contador_semi_operativos+=1
        comunitario_diccionario_semi_operativos[f'{columna_de_interes} comunitario'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'OPERATIVO' and 'Posta de Salud Rural' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_operativos+=1
        psr_diccionario_operativos[f'{columna_de_interes} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'NO_OPERATIVO' and 'Posta de Salud Rural' in raw['NOMBRE_ESTABLECIMIENTO']:
        psr_contador_no_operativos+=1
        psr_diccionario_no_operativos[f'{columna_de_interes} psr'].append(raw['NOMBRE_ESTABLECIMIENTO'])
      elif raw[f'{columna_de_interes}'] == 'SEMI_OPERATIVO' and 'Posta de Salud Rural' in raw['NOMBRE_ESTABLECIMIENTO']:
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
  return tabla
tabla= crear_tabla_pabellones('EDAN.xlsx')
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1(f"{columna_de_interes}"),
    dash_table.DataTable(
        id='tabla',
        columns=[{"name": i, "id": i} for i in tabla.columns],
        data=tabla.to_dict('records'),
        editable=True,
        row_deletable=True,
        style_cell={'textAlign': 'center'},
    ),
    dbc.Modal(
        [
            dbc.ModalHeader("Información"),
            dbc.ModalBody(id='modal-body'),
            dbc.ModalFooter(
                dbc.Button("Cerrar", id="close-modal", className="ms-auto", n_clicks=0)
            ),
        ],
        id="info-modal",
        is_open=False,
    ),
])

@app.callback(
    Output('info-modal', 'is_open'),
    Output('modal-body', 'children'),
    [Input('tabla', 'active_cell'),
     Input('close-modal', 'n_clicks')],
    [State('info-modal', 'is_open')]
)
def display_click_data(active_cell, n_clicks, is_open):
    if active_cell:
        row = active_cell['row']
        column = active_cell['column_id']
        fila = tabla.iloc[row]
        info = []

        # Obtener la información según la columna
        if column == "Operativos" and fila['Tipo de Establecimientos'] == 'Hospital':
            info = hospital_diccionario_operativos[f'{columna_de_interes} hospital']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'Hospital':
            info = hospital_diccionario_no_operativos[f'{columna_de_interes} hospital']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'Hospital':
            info = hospital_diccionario_semi_operativos[f'{columna_de_interes} hospital']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'Centro de Salud Familiar':
            info = centro_diccionario_operativos[f'{columna_de_interes} centro']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'Centro de Salud Familiar':
            info = centro_diccionario_no_operativos[f'{columna_de_interes} centro']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'Centro de Salud Familiar':
            info = centro_diccionario_semi_operativos[f'{columna_de_interes} centro']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'Centro Comunitario de Salud Familiar':
            info = comunitario_diccionario_operativos[f'{columna_de_interes} comunitario']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'Centro Comunitario de Salud Familiar':
            info = comunitario_diccionario_no_operativos[f'{columna_de_interes} comunitario']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'Centro Comunitario de Salud Familiar':
            info = comunitario_diccionario_semi_operativos[f'{columna_de_interes} comunitario']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'Posta de Salud Rural':
            info = psr_diccionario_operativos[f'{columna_de_interes} psr']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'Posta de Salud Rural':
            info = psr_diccionario_no_operativos[f'{columna_de_interes} psr']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'Posta de Salud Rural':
            info = psr_diccionario_semi_operativos[f'{columna_de_interes} psr']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'SUR':
            info = sur_diccionario_operativos[f'{columna_de_interes} sur']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'SUR':
            info = sur_diccionario_no_operativos[f'{columna_de_interes} sur']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'SUR':
            info = sur_diccionario_semi_operativos[f'{columna_de_interes} sur']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'SAR':
            info = sar_diccionario_operativos[f'{columna_de_interes} sar']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'SAR':
            info = sar_diccionario_no_operativos[f'{columna_de_interes} sar']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'SAR':
            info = sar_diccionario_semi_operativos[f'{columna_de_interes} sar']
        elif column == "Operativos" and fila['Tipo de Establecimientos'] == 'SAPU':
            info = sapu_diccionario_operativos[f'{columna_de_interes} sapu']
        elif column == "No Operativos" and fila['Tipo de Establecimientos'] == 'SAPU':
            info = sapu_diccionario_no_operativos[f'{columna_de_interes} sapu']
        elif column == "Semi Operativos" and fila['Tipo de Establecimientos'] == 'SAPU':
            info = sapu_diccionario_semi_operativos[f'{columna_de_interes} sapu']


        # Crear una lista de párrafos para cada nombre
        nombres = [html.P(nombre) for nombre in info]

        # Mostrar modal con información
        return True, nombres

    # Cerrar modal si se hace clic en el botón "Cerrar"
    if n_clicks and is_open:
        return False, ""

    return is_open, ""

if __name__ == '__main__':
    app.run_server(debug=True)