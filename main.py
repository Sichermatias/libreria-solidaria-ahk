# https://requests.readthedocs.io/en/latest/user/quickstart/#
import requests
# https://fastapi.tiangolo.com/
from fastapi import FastAPI

url = "https://httpbin.org/status/404"
mis_params = {"q": 'Cien años de soledad'}
req = requests.get(url, params=mis_params)
print(req.url)

app = FastAPI()
@app.get("/")
def ruta_principal():
    return {"Mensaje": "Bienvenido!"}