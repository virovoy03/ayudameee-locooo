
class Club:
    def __init__(self,codigo,denominacion):
        self.codigo = codigo
        self.denominacion = denominacion
    
    def get_lista_jugadores(self,lista):
        lista_jugadores_del_club = []
        for i in lista:
            if i.club.codigo == self.codigo:
                lista_jugadores_del_club.append(i)
        return lista_jugadores_del_club

    def __str__(self):
        return self.denominacion
    
    def __repr__(self):
        return f"(codigo:{self.codigo} nombre del club: {self.denominacion})"