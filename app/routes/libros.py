from fastapi import APIRouter
from app.services.openlibrary_service import OpenLibraryService

router = APIRouter(prefix="/api/libros", tags=["libros"])
svc = OpenLibraryService()

# 1) Buscar por título / autor / género
@router.get("/")
def buscar_libros(titulo=None, autor=None, genero=None):
    #TODO: Realizar modificaciones para obtener 
    try:
        if titulo:
            data = svc.buscar_libros(titulo)
            return {"success": True, "filtro": "titulo", "data": data}
        if autor:
            data = svc.buscar_libros_por_autor(autor)
            return {"success": True, "filtro": "autor", "data": data}
        if genero:
            data = svc.buscar_libros_por_genero(genero)
            return {"success": True, "filtro": "genero", "data": data}
        return {"success": False, "mensaje": "Enviá ?titulo=... o ?autor=... o ?genero=..."}
    except Exception as e:
        return {"success": False, "error": f"Error al buscar libros: {e}"}
