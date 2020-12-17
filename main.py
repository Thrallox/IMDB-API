import requests

API_KEY = "26e87f71"
#TODO- Arreglar urls para evitar tanta repeticion
url_busqueda = "http://www.omdbapi.com/?apikey={}&s={}"
url_identificador = "http://www.omdbapi.com/?apikey={}&i={}"

def peticion(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos ["Response"] == "False":
            return datos["Error"]
        else:
            return datos
    else:
        return"Error en consulta por id",respuesta.status_code
        


pregunta = input("Titulo de la pelicula")

respuesta = peticion(url_busqueda.format(API_KEY,pregunta))
if isinstance(respuesta, str):
    print(respuesta)
else:
    primera_peli = respuesta["Search"][0]
    clave = primera_peli["imdbID"]

    respuesta = peticion(url_identificador.format(API_KEY, clave))
    if isinstance(respuesta, str):
        print(respuesta)
    else:
        titulo = respuesta["Title"]
        agno = respuesta["Year"]
        director = respuesta["Director"]
        print("La peli {}, estrenada en el año {}, fue dirigida por {}".format(titulo,agno,director))




