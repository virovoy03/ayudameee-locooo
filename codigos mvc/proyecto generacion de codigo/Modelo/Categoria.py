
class Categoria:
    def __init__(self,codigo,denominacion):
        self.codigo = codigo
        self.denominacion = denominacion
    
    def get_cantidad_jugadores_categoria(self,lista):
        return len(self.get_lista_jugadores(lista))

    def get_lista_jugadores(self,lista):
        lista_jugadores_de_categoria = []
        for i in lista:
            if i.categoria.codigo == self.codigo:
                lista_jugadores_de_categoria.append(i)
        return lista_jugadores_de_categoria

    def __str__(self):
        return self.denominacion
    
    def __repr__(self):
        return f"(codigo:{self.codigo} nombre de la categoria: {self.denominacion})"