class VistaAlumno:
    def visualizarAlumno(self, dato):
        print(dato)

    def visualizarAprobadas(self, aprobadas):
        if len(aprobadas) != 0:
            print("Aprobadas")
            for mat in aprobadas:
                print(mat)
