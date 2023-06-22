# Lista de palabras clave
lista = [
         "como",
         "porque",
         "cuando",
         ""
]
import requests, json, time, pandas as pd

def obtener_sugerencias(consulta, codigo_idioma="en"):
  URL="http://suggestqueries.google.com/complete/search?client=firefox&hl=" + str(codigo_idioma) + "&q=" + consulta
  cabeceras = {'User-agent':'Mozilla/5.0'}
  time.sleep(0.5)  # ¡Sé amable con Google!
  respuesta = requests.get(URL, headers=cabeceras)
  resultado = json.loads(respuesta.content.decode('utf-8'))
  return resultado[1]

def obtener_kws(kws=[]):
  datos = pd.DataFrame()
  if kws:
    for kw in kws:
      # No olvides poner en el código de idioma, en mi caso use "es" para sugerencias en español
      datos[kw] = obtener_sugerencias(kw,"es")
    return datos

resultados = obtener_kws(lista)
resultados.head(10)