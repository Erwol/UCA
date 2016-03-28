# -*- coding: utf-8 -*-
import twitter
import io
import json
__author__ = 'Antonio Ruiz Rondán; Juan José García Beza; Ernesto Wulff Olea'

def oauth_login():
    CONSUMER_KEY = 'rIlJerpf16IWgzZ8gCqNhGrrk'
    CONSUMER_SECRET = 'FLOrnHNnOQ91WVX27u7NArZlcxPlKIFO5IiwfLSywCbUN6EVhB'
    OAUTH_TOKEN = '251748718-AU8hY5mjrLcdgpFLulXzdGet34ZzRSZEvfiEkinp'
    OAUTH_TOKEN_SECRET = 'IYG8ofZnPJUmJqqD3ZyiQrc3tJ8gE6bReYO6K6iWDbVZo'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Función que realiza las consultas que precisamos
def consultas():
    twitter_api = oauth_login()
    partidos = ("psoe", "PPopular", "ahorapodemos", "CiudadanosCs")
    siguiendo = []
    seguidores = []
    cadiz = [0]*(len(partidos))
    for p in partidos:
        results = twitter_api.statuses.user_timeline(screen_name=p, count=1)
        for status in results:
            siguiendo.append(status["user"]["friends_count"])
            seguidores.append(status["user"]["followers_count"])
    #save_json('siguiendo', siguiendo)
    #save_json('seguidores', seguidores)

    # Geolocalización en la provincia de Cádiz (50 KM alrededor de la capital)
    results = twitter_api.search.tweets(q="Podemos OR Ciudadanos OR CS's OR PP OR PSOE", geocode="36.5270610,-6.2885960,100km", count=100)
    for status in results["statuses"]:
        if ("PSOE" or "psoe" or "socialista" or "Socialista") in status["text"]:
            cadiz[0] += 1
        if ("PP" or "pp" or "Pp" or "partido popular") in status["text"]:
            cadiz[1] += 1
        if ("podemos" or "Podemos") in status["text"]:
            cadiz[2] += 1
        if ("Ciudadanos" or "CS" or "Cs" or "cs" or "ciudadanos") in status["text"]:
            cadiz[3] += 1
    print "Podemos mencionado %d veces.\nCiuadadanos mencionado %d veces.\nPP mencionado %d veces.\nPSOE mencionado %d veces" % (cadiz[2], cadiz[3], cadiz[1], cadiz[0])
    return siguiendo, seguidores, cadiz

def mandar_tweet(cadiz):
    twitter_api = oauth_login()
    status="Estadísticas de interacciones a 100KM de Cádiz. PP: %d, PSOE: %d, Podemos: %d, C's: %d. #UCA @toninoes @ErnestWulff" % (cadiz[1], cadiz[0], cadiz[2], cadiz[3])
    twitter_api.statuses.update(status=status)
