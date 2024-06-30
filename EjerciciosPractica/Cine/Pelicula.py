class Pelicula:
    def __init__(self, titulo, precio_entrada, pelicula_semana, estado):
        self.titulo = titulo
        self.precio_entrada = precio_entrada
        self.pelicula_semana = pelicula_semana
        self.estado = estado

    def precio_entrada_final(self, cliente):
        precio_final = self.precio_entrada

        if self.pelicula_semana=="0":#0 me indica que es la pelicula de la semana
            precio_final *= 0.6  # descuento del 40% x película de la semana
            return precio_final #para que no me sume otro descuento

        if cliente == "1":
            precio_final /= 2  #  2x1
        if cliente == "2":
            precio_final /= 2  #  Jubilado
        if cliente == "3":
            precio_final = 0  # Discapacidad

        return precio_final

    def isHabilitada(self):
        return self.estado == "0"

    def __str__(self):
        return f"{self.titulo}"