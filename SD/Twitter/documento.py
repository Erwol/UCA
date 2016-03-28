# -*- coding: iso-8859-1 -*-
from pylatex import *
from pylatex.utils import italic, NoEscape
import sys
__author__ = 'Antonio Ruiz Rond�n; Juan Jos� Garc�a Beza; Ernesto Wulff Olea'

def generar_documento():
    reload(sys)
    sys.setdefaultencoding('iso-8859-15')
    doc = Document()
    doc.packages.add(Package('inputenc', options=['utf8']))
    doc.packages.add(Package('babel', options='spanish'))
    doc.preamble.append(Command('title', 'Sistemas Distribuidos\nSeminario I'))
    doc.preamble.append(Command('author', "Antonio  Ruiz Rond�n\nErnesto Wulff Olea\nJuan Jos� Garc�a Beza"))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    doc.append(NoEscape(r'\tableofcontents'))
    doc.append(NoEscape(r'\newpage'))

    with doc.create(Section('Funci�n de la aplicaci�n')):
        doc.append("La aplicaci�n realiza un an�lisis de la situaci�n de los cuatro partidos pol�ticos m�s influyentes de la actualidad (PP, PSOE, Podemos y Ciudadanos). En concreto genera tres gr�ficas, en la primera (figura 1) se compara el n�mero de seguidos y seguidores de cada partido. En la segunda (figura 2) se muestra la relaci�n entre seguidos y seguidores en forma de porcentaje. A menor sea este n�mero, m�s 'popular' ser� la cuenta del partido. A continuaci�n realiza un an�lisis de los �ltimos 100 tweets emitidos en un radio de 100 kil�metros desde la capital de la provincia de C�diz en funci�n del partido al que estos hagan referencia. Por �ltimo emite un tweet (figura 4) que informa de los resultados obtenidos en el an�lisis.")
        with doc.create(Figure(position='h!')) as grafico1:
            grafico1.add_image("seguidores.png", width='420px')
            grafico1.add_caption('Relaci�n entre seguidos y siguiendo de cada partido.')
        with doc.create(Figure(position='h!')) as grafico2:
            grafico2.add_image("tff.png", width='420px')
            grafico2.add_caption('TFF Twitter Following Follower ratio.')
        with doc.create(Figure(position='h!')) as grafico3:
            grafico3.add_image("cadiz.png", width='420px')
            grafico3.add_caption('Interacci�n de los usuarios a 100KM de C�diz capital.')
        with doc.create(Figure(position='h!')) as grafico4:
            grafico4.add_image("twitter.png", width='420px')
            grafico4.add_caption('Mensaje emitido por la aplicaci�n.')
    with doc.create(Section('Manual de uso')):
        doc.append("Para ejecutar la aplicaci�n simplemente introduzca el comando python seminario1.py y espere a que se generen las tres gr�ficas y el documento PDF. Previamente deber� haber introducido sus credenciales de Twitter en el fichero api.py.")

    with doc.create(Section('Librer�as empleadas')):
        with doc.create(Enumerate()) as enum:
            enum.add_item("NumPy: es una extensi�n de Python, que le agrega mayor soporte para vectores y matrices, constituyendo una biblioteca de funciones matem�ticas de alto nivel para operar con esos vectores o matrices. El ancestro de NumPy, Numeric, fue creado originalmente por Jim Hugunin con algunas contribuciones de otros desarrolladores. En 2005, Travis Oliphant cre� NumPy incorporando caracter�sticas de Numarray en NumPy con algunas modificaciones. NumPy es open source.")
            enum.add_item("Matplotlib: es una biblioteca para la generaci�n de gr�ficos a partir de datos contenidos en listas o arrays en el lenguaje de programaci�n Python y su extensi�n matem�tica NumPy. Proporciona una API, pylab, dise�ada para recordar a la de MATLAB.")
            enum.add_item("M�dulo sys: El m�dulo provee acceso a funciones y objetos mantenidos por del int�rprete.")
            enum.add_item("Python-twitter: Es usado para gestionar algunas de las aplicaciones que podemos crear en una cuenta de Twitter.")
            enum.add_item("PyLaTex: Permite generar documentos LaTex y PDF nativos desde aplicaciones escritas en python.")
    with doc.create(Section('Problemas hallados')):
        doc.append("Hemos tenido que adaptarnos a la sintaxis de m�ltiples librer�as para lograr el resultado obtenido. A la hora de generar el PDF con LaTex tuvimos problemas con la codificaci�n de la terminal que tuvimos que cambiar de la forma: sys.setdefaultencoding('iso-8859-15'). Nos encontramos una vez con el l�mite de llamadas a la API, lo cu�l nos hizo esperar en un par de ocasiones para poder seguir desarrollando.")

    doc.generate_pdf('seminario1as')