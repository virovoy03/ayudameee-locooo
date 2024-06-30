
class Partido:
    def __init__(self,equipo_local,equipo_visitante,goles_local,goles_visitante):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.goles_local = goles_local
        self.goles_visitante = goles_visitante

    def get_(self):
        return self.equipo_local    
    def get_(self):
        return self. equipo_visitante   
    def get_(self):
        return self.goles_local        
    def get_(self):
        return self.goles_visitante
    
    def __str__(self):
        return {f"el partido entre:,{self.equipo_local}, y el: {self.equipo_visitante} termino\n {self.goles_local} a {self.goles_visitante}"}