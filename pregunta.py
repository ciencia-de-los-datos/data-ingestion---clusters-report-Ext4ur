"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():

    #
    # Inserte su código aquí
    #

    with open('clusters_report.txt') as f:

        data = f.readlines()

    columnas_1 = data[0].split('  ')
    columnas_2 = data[1].split('  ')

    columnas = [columnas_1[0], columnas_1[1] + columnas_2[4], columnas_1[3] + ' ' + columnas_2[5], columnas_1[4]]
    
    columnas = [c.lower().replace('\n', ' ').strip().replace(' ', '_') for c in columnas]

    data = data[4:]

    data_rows = []

    row = ''

    for r in data:

        if r.strip() == '':

            values = [v for v in row.replace('\n', '').split('  ') if v != '']

            data_rows.append((
                int(values[0].replace(' ', '')),
                int(values[1].replace(' ', '')),
                float(values[2].replace(' ', '').replace('%', '').replace(',', '.')), 
                ' '.join(values[3:]).replace(',', ', ').replace(',  ', ', ').replace('  ', ' ').replace('.', '')
                .strip()))

            row = ''

        else:

            row += r

    df = pd.DataFrame(data_rows, columns=columnas)

    return df

ingest_data()