# Para instalar las dependencias necesarias:
# python -m pip install fastapi uvicorn requests

# Para iniciar nuestro servidor: 
# python -m uvicorn app.main:app --reload

# https://requests.readthedocs.io/en/latest/user/quickstart/#
# https://fastapi.tiangolo.com/
from fastapi import FastAPI
from app.routes.libros import router as libros_router

app = FastAPI(title="Librería")

@app.get("/")
def raiz():
    return {"ok": True, "mensaje": "API funcionando 🚀"}

# Montamos el router de libros
app.include_router(libros_router)