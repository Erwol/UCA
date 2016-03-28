# -*- coding: iso-8859-1 -*-
import numpy as np
import matplotlib.pyplot as plt
__author__ = 'Antonio Ruiz Rondán; Juan José García Beza; Ernesto Wulff Olea'

def generar_grafica_seguidores (siguiendo, seguidores):
    partidos = ("psoe", "PPopular", "ahorapodemos", "CiudadanosCs")

    for x in range(len(partidos)):
        print "%s" % (partidos[x].upper())
        print "\tSiguiendo: %s" % (siguiendo[x])
        print "\tSeguidores: %s" % (seguidores[x])
        print "\tTFF: %.2f" % (seguidores[x] / float(siguiendo[x]))
    ind = np.arange(len(partidos))
    width = 0.5
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, siguiendo, width, color='r')
    rects2 = ax.bar(ind + width, seguidores, width, color='y')

    ax.set_ylabel(u'Número de personas')
    ax.set_title(u'Presencia en Twitter de partidos políticos')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(partidos)
    ax.legend((rects1[0], rects2[0]), ('Siguiendo', 'Seguidores'))

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%d' % int(height), ha='center', va='bottom')
    autolabel(rects1)
    autolabel(rects2)
    # Generamos la imagen en PNG
    plt.savefig('seguidores')



def generar_grafica_tff(siguiendo, seguidores):
    partidos = ("psoe", "PPopular", "ahorapodemos", "CiudadanosCs")
    tff = []
    for x in range (len(partidos)):
        tff.append(siguiendo[x] * 100 / float(seguidores[x]))
    print tff
    ind = np.arange(len(partidos))
    width = 1
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, tff, width, color='r')

    ax.set_title(u'Relación Seguidores / Siguiendo (Menos = Mejor)')
    ax.set_ylabel('Porcentaje seguidores / siguiendo')
    ax.set_xticks(ind + 0.5)
    ax.set_xticklabels(partidos)

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, '%f' % float(height), ha='center', va='bottom')

    autolabel(rects1)
    plt.savefig('tff')

def generar_grafica_cadiz(cadiz):
    labels = 'PSOE', 'PP', 'Podemos', 'Ciudadanos'
    sizes = cadiz
    colors = ['red', 'blue', 'mediumpurple', 'orange']
    explode = (0, 0, 0, 0)  # proportion with which to offset each wedge
    fig, ax = plt.subplots()
    plt.pie(sizes,  # data
            explode=explode,  # offset parameters
            labels=labels,  # slice labels
            colors=colors,  # array of colours
            autopct='%1.1f%%',  # print the values inside the wedges
            shadow=True,  # enable shadow
            startangle=70  # starting angle
            )
    plt.savefig('cadiz')
