from localbooks_service import LocalBookService
from openlibrary_service import OpenLibraryService

class CombinedBooksService:
    
    localbooks_service = LocalBookService
    openlibrary_service = OpenLibraryService
    
    def obtener_libros(self):
        #TODO
        return None
