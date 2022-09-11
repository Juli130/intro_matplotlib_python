# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
from audioop import add
from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    x = list(np.linspace(-4, 4, 20))

    #y1 = x**2
    #y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
   
    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)
    fig = plt.figure()
    ax = fig.add_subplot()
    
    ax.plot(x, y1, color="c", label="fig1")
    ax.plot(x, y2, color= "r", label="fig2")
    ax.set_facecolor("whitesmoke")
    ax.legend()
    plt.show()



    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico

    print("terminamos")
