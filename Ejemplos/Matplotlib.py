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

    input("Presiona enter para desplegar las graficas")

    vecA = [1, 2, 3, 4]
    vecB = [11, 22, 33, 44]
    plt.plot(vecA, vecB, color='blue', linewidth=3, label='linea de prueba')
    plt.title('Diagrama de lineas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()
    print("Si no puedes/quieres o has compilado puedes ver un ejemplo de\n"
          "las lineas anteriores en la carpeta de Imagenes")

    x1 = [0.25, 1.25, 2.25, 3.25, 4.25]
    y1 = [10, 55, 80, 32, 40]
    x2 = [0.75, 1.75, 2.75, 3.75, 4.75]
    y2 = [46, 26, 10, 29, 66]
    plt.bar(x1, y1, label='Datos 1', width=0.5, color='black')
    plt.bar(x2, y2, label='Datos 2', width=0.5, color='orange')
    plt.title('Grafica de barras')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()

    vecC = [22, 55, 62, 45, 21, 22, 34,
            42, 4, 2, 102, 95, 85, 55,
            110, 120, 70, 65, 55, 111,
            115, 80, 75, 65, 54, 44,
            43, 42, 48]
    binds = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.hist(vecC, binds, histtype='bar', rwidth=0.8, color='lightgreen')
    plt.title('Histograma')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()

    plt.scatter(x1, y1, label='Datos1', color='red')
    plt.scatter(x2, y2, label='Datos2', color='purple')
    plt.title('Gráfica de dispersión')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()

    #Dormir = [7, 8, 6, 11, 7]
    #Comer = [2, 3, 4, 3, 2]
    #Trabajar = [7, 8, 7, 2, 2]
    #Recreaciones = [8, 5, 7, 8, 13]
    divisiones = [7, 2, 2, 13]
    actividades = ['Dormir', 'Comer', 'Trabajar', 'Recreaciones']
    Colores = ['red', 'green', 'yellow','purple']
    plt.pie(divisiones,labels=actividades, colors=Colores,startangle=90,
            shadow=True, explode=(0.1, 0.5, 0, 0), autopct='%1.1f%%')
    plt.title('Gráfica de pastel')
    plt.show()


if __name__ == '__main__':
    Init()