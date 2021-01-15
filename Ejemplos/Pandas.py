'''
    En este archivo podrás obtener algunos ejemplos
    así como caracteristicas de pandas que te serán
    de ayuda durante tu aprendizaje de ML
'''

import numpy as np
import pandas as pd

def Init():
    #Declaración e implementación de un objeto numpy con pandas
    data = np.array([['', 'Col1', 'Col2'], ['Fila1', 11, 22], ['Fila2', 33, 44]])
    print(pd.DataFrame(data=data[1:, 1:], index=data[1:, 0], columns=data[0, 1:]))

    print("Así mismo contamos con metodos que nos serán de gran ayuda\n"
          "a la hora de trabajar con estas librerias")

    data = pd.Series({"Argentina": "Buenos Aires",
                      "Chile": "Chile",
                      "Colombia": "Bogota",
                      "Peru": "Lima"})

    print("Forma del frame")
    print(data.shape)

    print("Forma del frame")
    print(len(data.index))

    print("Estadisticas del frame")
    print(data.describe())

    print("Conteo de datos del frame")
    print(data.count())

    print("Valor maximo de la columna")
    print(data.max())

    print("Valor minimo del frame")
    print(data.min())

    print("Así mismo podemos obtener su mediana con")
    #print(data.median()) aunque en este ejemplo no es posible
    #ya que tenemos un conjunto de datos de tipo string, no numerico

    print("Desviación estandar del frame")
    #print(data.std()) aunque en este ejemplo no es posible
    #ya que tenemos un conjunto de datos de tipo string, no numerico

if __name__ == '__main__':
    Init()