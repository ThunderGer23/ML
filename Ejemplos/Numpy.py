'''
    En este archivo podrás obtener algunos ejemplos
    así como caracteristicas de numpy que te serán de
    ayuda durante tu aprendizaje de ML
'''
import numpy as np
import sys
import time
SIZE = 1000000

def UseNumpyNow():
    #Crear una matrices
    print("Matriz de unos: ")
    unos = np.ones((3,4))
    print(unos)
    input()
    print("Matriz de ceros:")
    ceros = np.zeros((3,4))
    print(ceros)
    input()
    print("Matriz de numeros aleatorios:")
    aleatorios = np.random.random((3,4))
    print(aleatorios)
    input()
    print("Matriz vacia:")
    vacia = np.empty((3,4))
    print(vacia)
    input()
    print("Matriz con un solo valor especifico:")
    num = np.full((3, 4), 8)
    print(num)
    input()
    print("Tambien podemos crear/tener vectores con np.array\n"
          "aunque no es la unica manera de hacerlo, por ejemplo\n"
          "si lo que buscamos es crear un vector cuyos valores\n"
          "sean de incremento constante podemos usar:")
    inc = np.arange(0, 50, 5)
    print(inc)
    input()
    print("Así mismo podemos crear matrices identidad de dos\n"
          "maneras bastante sencillas")
    identidad = np.eye(4,4)
    print(identidad)
    print()
    identidad2 = np.identity(4)
    print(identidad2)
    input()
    #Trabajando con matrices de numpy
    print("Para trabajar con cualquiera de estas podemos utilizar\n"
          "alguno de los siguientes metodos que nos ofrece por default\n"
          "el compilador.")
    print("Dimensiones de la matriz unos:")
    print(unos.ndim)
    print("Tipos de datos de la matriz ceros:")
    print(ceros.dtype)
    print("Longitud de la matriz aleatorios:")
    print(aleatorios.size)
    print("Forma de la matriz vacia:")
    print(vacia.shape)
    input()
    #Cambiando forma
    print("Así mismo podemos cambiar la forma de una matriz")
    redi = np.array([(8, 9, 10), (11, 12, 13)])
    print(redi)
    print("Forma de la matriz:")
    print(redi.shape)
    redi = redi.reshape(3, 2)
    print(redi)
    print("Forma de la matriz:")
    print(redi.shape)
    input()
    print("Ahora bien, para acceder u obtener alguno o todos los datos\n"
          "de una matriz podemos acceder de la siguiente manera:")
    print(identidad[0:, 1])
    input()
    print("Por otro lado, las operaciones con matrices es una de las\n"
          "mayores simplicidades de esta libreria, ya que podemos obtener\n"
          "el minimo, la suma, el maximo, entre otros de esta solo con una linea")
    print("Minimo de la matriz Num "+ str(num.min())+"\nMaximo de la matriz Num"
          + str(num.max())+"\nSuma de la matriz Num "+ str(num.sum())+"\nRaiz de la"
            "matriz Num"+ str(np.sqrt(num))+"\nDesviación estandar de la matriz Num"
          + str(np.std(num)))








def Init():
    L1 = range(SIZE)
    L2 = range(SIZE)
    A1 = np.arange(SIZE)
    A2 = np.arange(SIZE)

    print("Diferencias entre los objetos de numpy y\n"
          "y los objetos por default en python.")
    print(input())
    print("numpy.array es un potente objeto de tipo\n"
          "matriz N-dimensional y las ventajas sobre\n"
          "una matriz normal de python es la memoria\n"
          "y también su velocidad.")
    input()
    s = range(1000)
    print("Tamaño de la lista de python: " + str(sys.getsizeof(5)*len(s)))
    print()
    MatA = np.arange(1000)
    print("Tamaño de la lista de numpy: " + str(MatA.size*MatA.itemsize))

    input()
    start = time.time()
    result = [(x, y) for x, y in zip(L1, L2)]
    print("Tiempo de la lista de python " + str((time.time()-start)*1000))
    print()
    start = time.time()
    result = A1 + A2
    print("Tiempo de la lista de numpy " + str((time.time()-start)*1000))
    input()
    UseNumpyNow()

if __name__ == '__main__':
    Init()