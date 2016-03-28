# -*- coding: iso-8859-1 -*-
from pylatex import *
from pylatex.utils import italic, NoEscape
import sys
__author__ = 'Antonio Ruiz Rondán; Juan José García Beza; Ernesto Wulff Olea'

def generar_documento():
    reload(sys)
    sys.setdefaultencoding('iso-8859-15')
    doc = Document()
    doc.packages.add(Package('inputenc', options=['utf8']))
    doc.packages.add(Package('babel', options='spanish'))
    doc.preamble.append(Command('title', 'Sistemas Distribuidos\nSeminario I'))
    doc.preamble.append(Command('author', "Antonio  Ruiz Rondán\nErnesto Wulff Olea\nJuan José García Beza"))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\tableofcontents'))
    doc.append(NoEscape(r'\newpage'))

    with doc.create(Section('Función de la aplicación')):
        doc.append("La aplicación realiza un análisis de la situación de los cuatro partidos políticos más influyentes de la actualidad (PP, PSOE, Podemos y Ciudadanos). En concreto genera tres gráficas, en la primera (figura 1) se compara el número de seguidos y seguidores de cada partido. En la segunda (figura 2) se muestra la relación entre seguidos y seguidores en forma de porcentaje. A menor sea este número, más 'popular' será la cuenta del partido. A continuación realiza un análisis de los últimos 100 tweets emitidos en un radio de 100 kilómetros desde la capital de la provincia de Cádiz en función del partido al que estos hagan referencia. Por último emite un tweet (figura 4) que informa de los resultados obtenidos en el análisis.")
        with doc.create(Figure(position='h!')) as grafico1:
            grafico1.add_image("seguidores.png", width='420px')
            grafico1.add_caption('Relación entre seguidos y siguiendo de cada partido.')
        with doc.create(Figure(position='h!')) as grafico2:
            grafico2.add_image("tff.png", width='420px')
            grafico2.add_caption('TFF Twitter Following Follower ratio.')
        with doc.create(Figure(position='h!')) as grafico3:
            grafico3.add_image("cadiz.png", width='420px')
            grafico3.add_caption('Interacción de los usuarios a 100KM de Cádiz capital.')
        with doc.create(Figure(position='h!')) as grafico4:
            grafico4.add_image("twitter.png", width='420px')
            grafico4.add_caption('Mensaje emitido por la aplicación.')
    with doc.create(Section('Manual de uso')):
        doc.append("Para ejecutar la aplicación simplemente introduzca el comando python seminario1.py y espere a que se generen las tres gráficas y el documento PDF. Previamente deberá haber introducido sus credenciales de Twitter en el fichero api.py.")

    with doc.create(Section('Librerías empleadas')):
        with doc.create(Enumerate()) as enum:
            enum.add_item("NumPy: es una extensión de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de funciones matemáticas de alto nivel para operar con esos vectores o matrices. El ancestro de NumPy, Numeric, fue creado originalmente por Jim Hugunin con algunas contribuciones de otros desarrolladores. En 2005, Travis Oliphant creó NumPy incorporando características de Numarray en NumPy con algunas modificaciones. NumPy es open source.")
            enum.add_item("Matplotlib: es una biblioteca para la generación de gráficos a partir de datos contenidos en listas o arrays en el lenguaje de programación Python y su extensión matemática NumPy. Proporciona una API, pylab, diseñada para recordar a la de MATLAB.")
            enum.add_item("Módulo sys: El módulo provee acceso a funciones y objetos mantenidos por del intérprete.")
            enum.add_item("Python-twitter: Es usado para gestionar algunas de las aplicaciones que podemos crear en una cuenta de Twitter.")
            enum.add_item("PyLaTex: Permite generar documentos LaTex y PDF nativos desde aplicaciones escritas en python.")
    with doc.create(Section('Problemas hallados')):
        doc.append("Hemos tenido que adaptarnos a la sintaxis de múltiples librerías para lograr el resultado obtenido. A la hora de generar el PDF con LaTex tuvimos problemas con la codificación de la terminal que tuvimos que cambiar de la forma: sys.setdefaultencoding('iso-8859-15'). Nos encontramos una vez con el límite de llamadas a la API, lo cuál nos hizo esperar en un par de ocasiones para poder seguir desarrollando.")

    doc.generate_pdf('seminario1as')