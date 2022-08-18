import requests
import json
import config

url_controller = "http://127.0.0.1:58000"

#Obtenciòn del ticket
data={config="username",config="password"}
cabecera = {"content-type": "application/json"}
respuesta = requests.post(url_controller+"/api/v1/ticket", json.dumps(data), headers=cabecera)
token = (respuesta.json()["response"]["serviceTicket"])

#Consulta del inventario
cabecera_inventario = {"content-type": "application/json", "X-Auth-Token": token}
inventario = requests.get(url_controller+"/api/v1/topology/physical-topology", headers=cabecera_inventario)
print(inventario.json())