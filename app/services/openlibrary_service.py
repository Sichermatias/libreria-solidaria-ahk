# openlibrary_service.py
# Requisitos: python -m pip install requests
# Uso sugerido con FastAPI:
#   from openlibrary_service import OpenLibraryService, NotFoundError, InternalServerError
#   svc = OpenLibraryService()

import requests

class OpenLibraryService:
    
    base_url = "https://openlibrary.org"
    covers_url = "https://covers.openlibrary.org"

    # 1) Búsqueda general de libros
    def buscar_libros(self, query):
        try:
            resp = requests.get(
                f"{self.base_url}/search.json",
                params={"q": query}
            )
            
            data = resp.json()
            return data
            
        except:
            print("Ha ocurrido un error")

    # 2) Búsqueda por autor
    def buscar_por_autor(self, author_name):
        try:
            resp = requests.get(
                f"{self.base_url}/search.json",
                params={"author": author_name}
            )
            data = resp.json()
            return data

        except:
            print("Ha ocurrido un error")

    # 3) Búsqueda por género/tema (subjects)
    def buscar_por_genero(self, subject):
        try:
            resp = requests.get(
                f"{self.base_url}/subjects/{subject}.json"
            )
            data = resp.json()
            return data

        except:
            print("Ha ocurrido un error" + resp.url)

    # 4) Obtener datos de un libro por OLID
    def buscar_libro_por_olid(self, olid):
        try:
            resp = requests.get(
                f"{self.base_url}/books/{olid}.json"
            )

            data = resp.json()
            return data

        except:
            print("Ha ocurrido un error")

    # 5) Obtener datos de un libro por ISBN
    def buscar_libro_por_isbn(self, isbn):
        try:
            resp = requests.get(
                f"{self.base_url}/isbn/{isbn}.json",
                timeout=self.timeout
            )
            data = resp.json()
            return data

        except:
            print("Ha ocurrido un error")

    # 6) Generar URL de la portada (covers API)
    def buscar_portada(self, isbn, size="M"):
        try:

            cover_url = f"{self.covers_url}/b/isbn/{isbn}-{size}.jpg"
            
            resp = requests.get(
                cover_url
            )
            data = resp.text
            return data

        except:
            print("Ha ocurrido un error")
