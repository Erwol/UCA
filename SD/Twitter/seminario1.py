# -*- coding: iso-8859-1 -*-
from api import *
from graficos import *
from documento import *
__author__ = 'Antonio Ruiz Rondán; Juan José García Beza; Ernesto Wulff Olea'

if __name__ == '__main__':
    # Realizamos consultas
    siguiendo, seguidores, cadiz = consultas()

    generar_grafica_seguidores(siguiendo, seguidores)
    generar_grafica_cadiz(cadiz)
    generar_grafica_tff(siguiendo, seguidores)

    generar_documento()

    mandar_tweet(cadiz)