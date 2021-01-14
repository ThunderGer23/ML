'''
    En este archivo podrás obtener algunos ejemplos
    así como caracteristicas de matplotlib que te serán
    de ayuda durante tu aprendizaje de ML
'''
import matplotlib.pyplot as plt


def Init():
    print("Matplotlib es una libreria de trazado utilizada para\n"
          "greficos en 2D, es muy flexible y sirve de mucho en la\n"
          "mayoria de los casos de uso durante tu trabajo en el ML\n"
          "veamos algunos ejemplos")

    vecA = [1, 2, 3, 4]
    vecB = [11, 22, 33, 44]
    plt.plot(vecA, vecB, color='blue', linewidth=3, label='linea de prueba')
    plt.legend()
    plt.show()
    print("Si no puedes/quieres o has compilado puedes ver un ejemplo de\n"
          "las lineas anteriores en la carpeta de Imagenes Fig(Matplotlib_Ejemplo1_lineadeprueba)")


if __name__ == '__main__':
    Init()