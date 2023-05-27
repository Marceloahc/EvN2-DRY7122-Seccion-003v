import urllib.parse
import requests
import datetime

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "8EIKnFNK15ncVheFmhYzKJFotGnkgqDn"

while True:
   print("BIENVENIDO A LA APLICACIÓN DE VIAJE DE MARCELO HIDALGO")
   hora_actual = datetime.datetime.now()
   print("la hora es: ",(hora_actual))
   orig = input("INGRESE EL LUGAR DE ORIGEN : ")
   if orig=="h" or orig=="H":
       print("Ha salido de nuestra aplicación")
       print("hasta luego")
       break
   dest = input("INGRESE EL LUGAR DE DESTINO : ")
   if orig=="h" or orig=="H":
       print("Ha salido de nuestra aplicación")
       print("hasta luego")
       break
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Los datos de viaje desde " + (orig) + " hasta " + (dest) + " son los siguientes: ")
        print("El tiempo estimado de viaje:   " + (json_data["route"]["formattedTime"]))
        print("La distancia en KM es:   " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))