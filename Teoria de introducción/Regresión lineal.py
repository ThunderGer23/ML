'''
                    Qué es la Varianza?

En teoria de probabilidad, la varianza de una variable aleatoria
es una medida de dispersión definida como la esperanza del
cuadrado de la dessviacion de dicha variable respecto a su medida.

Hay que tener en cuenta que la varianza puede verse muy influida
por los valores atipicos y no se aconseja su uso cuando las
distribuciones de las variables aleatorias tiene colas pesadas.


                    Qué es una Bia/Sesgo?

El sesgo es un peso desproporcionado a favor o en contra de una cosa,
persona o grupo en comparación con otra, generalmente de una manera
que se considera injusta.

Los sesgos pueden aprender observando diferentes contextos culturales.
Las personas pueden desarrollar sesgos hacia o en contra de un individuo,
un grupo étnico, una identidad sexual o de género, una nacion o religión.

En ciencia e ingenieria, un sesgo es un error sistematico. El sesgo
estadistico resulta de un muestreo injusto de una población, o de un
proceso de estimacion que no da resultados precisos en promedio.


            Tipos de errores presentes en la programacion de una IA

Existen tres tipos de errotes que pueden presentarse en nuestro sistema:

        Error de Bias:
            Esta es la diferencia entre la predicción esperada de nuestro
            modelo y los valores verdaderos que hemos conseguido durante la
            ejecución.

            Los algoritmos paramétricos tienen un alto Bias que los hace
            más rápidos de aprender y más fácil de entender, pero que
            generalmente también los vuelve menos flexibles y un menor
            rendimiento predictivo en problemas más complejos.

        Error de Varianza:

            Este se refiere a la cantidad que la estimación de la función
            cambiara si se utiliza diferentes datos de entrenamiento, este
            se estima a partir de los datos obtenidos para la programacion
            de nuestro algoritmo de ML.

            Idealmente no deberia cambiar demasiado de un conjunto de datos
            de entrenamiento a otro.

        Error irreducible:
            Este ultimo no se puede evitar independientemente del algoritmo
            que se utilice, también se le nombra ruido y por lo general
            proviene de variables desconocidas que interfieren en el mapeo de
            las variables de entrada o de salida.

            También puede provenir de Caracteristicas incompletas en nuestro
            sistema o un problema no detectado dentro del mismo, cabe resaltar
            que no importa cúan bueno sea el modelo que hemos elaborado, todos
            nuestros datos tendran cierta cantidad de ruido o error irreducible.


                                Compensación BIAS-VARIANZA
        El objetivo del ML es lograr un bias bajo y una varianza baja, a su vez,
        el algoritmo debe lograr un buen rendimiento de predicción.

        El bias frente a la varianza se refiere a la precision frente a la consistencia
        de los modelos entrenados por su algoritmo.
'''

#Regresión lineal simple

import numpy as np
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def Init():
    boston = datasets.load_boston()
    print(boston)
    print()
    ###Y estoy viendo?###
    input("Enter para obtener más detalles de la variable")
    print()
    print("Información de el dataset:")
    print(boston.keys())
    print()
    input("Enter para obtener sus caracteristicas:")
    print("Caracteristicas del dataset:")
    print(boston.DESCR)
    print()
    input("Enter")
    print("Nombres de columnas")
    print(boston.feature_names)

    ##Preparando la data de regresión lineal simple##

    #Seleccionamos una columna solamente
    x = boston.data[:, np.newaxis, 5]
    #Definimos los datos correspondientes a las etiquetas
    y = boston.target

    plt.scatter(x, y)
    plt.xlabel('Numero de habitaciones')
    plt.ylabel('valor medio')
    plt.show()

    #Separamos los datos del train en entrenamiendo y prueba para probar algoritmos
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    #Definimos el algoritmo a utilizar
    lr = linear_model.LinearRegression()

    #Entrenamiento del modelo
    lr.fit(x_train, y_train)

    #Predicción del sistema
    y_pred = lr.predict(x_test)

    #Resultados
    print(y_test)
    print("###################################")
    print(y_pred)

    #Grafica
    """
            De la siguiente grafica podemos observar que la linea roja
            es el resultado obtenido, mientras que los puntos azules son
            los datos que fueron utilizados para su entrenamiento. 
            
            Si recuerdan su curso de metodos nuemricos, para que una regresión
            de este tipo sea satisfactoria la mayor cantidad de puntos debería
            estar sobre la linea. Por ende podemos entender que no es un buen
            modelo ya que los datos estan muy dispersos.    
    """
    plt.scatter(x_test, y_test)
    plt.plot(x_test, y_pred, color='red', linewidth = 3)
    plt.title("Regresión Lineal Simple")
    plt.xlabel('Numero de habitaciones')
    plt.ylabel('Valore medio')
    plt.show()

    input("Enter para ver la precision del modelo")
    print()
    print('precision:')
    print(lr.score(x_train, y_train))



if __name__ == '__main__':
    Init()