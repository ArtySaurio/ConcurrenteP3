import multiprocessing
import threading
from multiprocessing import Pool

def fibonacci(n):

    #Definicion de los numeros que se usaran
    numerocores = multiprocessing.cpu_count()
    primernum = 0
    segundonum = 1
    n = int(n)

    #Condicion si el num fibonacci es 0 o 1 el numero sera 0 y 1
    if n in (0, 1):
        print('Su numero de cores es de {} y el Fibonacci del {} es: {}'.format(numerocores, n, n))
    else:
        for i in range(2, n):
            nuevonum = primernum + segundonum
            primernum = segundonum
            segundonum = nuevonum
        print('Su numero de cores es de {} y el Fibonacci del {} es: {}'.format(numerocores, n, segundonum))

if __name__ == '__main__':

    #Pregunta a usuario su número de expediente
    numeroescogido = input('Introduzca el número de expediente: ')
    segmentdata = map(int, numeroescogido.split())

    #Pool para introducir los procesos
    pool = Pool()
    result = pool.map(fibonacci, segmentdata)
    pool.close()
    pool.join()
