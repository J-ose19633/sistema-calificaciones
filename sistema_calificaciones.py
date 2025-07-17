# sistema_calificaciones.py

from datetime import date
from typing import List, Dict

# Clase Materia
class Materia:
    def __init__(self, nombre: str, clave: str):
        self.nombre = nombre
        self.clave = clave

# Clase Calificacion
class Calificacion:
    def __init__(self, materia: Materia, valor: float, docente):
        if not (0 <= valor <= 10):
            raise ValueError("La calificación debe estar en un rango de 0 a 10.")
        self.materia = materia
        self.valor = valor
        self.fecha = date.today()
        self.docente_evaluador = docente.nombre # Guardamos solo el nombre del docente

# Clase Estudiante
class Estudiante:
    def __init__(self, nombre: str, matricula: str):
        self.nombre = nombre
        self.matricula = matricula
        self.lista_calificaciones: List[Calificacion] = []

    def agregar_calificacion(self, calificacion: Calificacion):
        self.lista_calificaciones.append(calificacion)

    def calcular_promedio_general(self) -> float:
        if not self.lista_calificaciones:
            return 0.0
        total_puntos = sum(c.valor for c in self.lista_calificaciones)
        return total_puntos / len(self.lista_calificaciones)

    def calcular_promedio_por_materia(self, materia_clave: str) -> float:
        calificaciones_materia = [c.valor for c in self.lista_calificaciones if c.materia.clave == materia_clave]
        if not calificaciones_materia:
            return 0.0
        return sum(calificaciones_materia) / len(calificaciones_materia)

    def esta_aprobado(self) -> bool:
        return self.calcular_promedio_general() >= 6.0

    def obtener_materia_promedio_mas_bajo(self) -> Dict[str, float]:
        promedios_por_materia = {}
        for calificacion in self.lista_calificaciones:
            materia_nombre = calificacion.materia.nombre
            if materia_nombre not in promedios_por_materia:
                promedios_por_materia[materia_nombre] = []
            promedios_por_materia[materia_nombre].append(calificacion.valor)

        if not promedios_por_materia:
            return {}

        min_promedio = float('inf')
        materia_mas_baja = ""

        for materia_nombre, calificaciones in promedios_por_materia.items():
            promedio = sum(calificaciones) / len(calificaciones)
            if promedio < min_promedio:
                min_promedio = promedio
                materia_mas_baja = materia_nombre

        return {"materia": materia_mas_baja, "promedio": min_promedio}

# Clase Docente
class Docente:
    def __init__(self, nombre: str, id_empleado: str):
        self.nombre = nombre
        self.id_empleado = id_empleado

    def asignar_calificacion(self, estudiante: Estudiante, materia: Materia, valor: float):
        try:
            calificacion = Calificacion(materia, valor, self)
            estudiante.agregar_calificacion(calificacion)
            print(f"Calificación de {valor} asignada a {estudiante.nombre} en {materia.nombre} por {self.nombre}.")
        except ValueError as e:
            print(f"Error al asignar calificación: {e}")

# Función para generar el reporte final
def generar_reporte_final(estudiantes: List[Estudiante]):
    print("\n--- REPORTE FINAL DE CALIFICACIONES ---")
    print("---------------------------------------")
    for estudiante in estudiantes:
        promedio = estudiante.calcular_promedio_general()
        estatus = "APROBADO" if estudiante.esta_aprobado() else "NO APROBADO"
        print(f"Nombre: {estudiante.nombre}, Matrícula: {estudiante.matricula}, Promedio: {promedio:.2f}, Estatus: {estatus}")
        materia_baja_info = estudiante.obtener_materia_promedio_mas_bajo()
        if materia_baja_info:
            print(f"  Materia con promedio más bajo: {materia_baja_info['materia']} ({materia_baja_info['promedio']:.2f})")
        print("---------------------------------------")

# Función principal para ejecutar el programa
def main():
    # 1. Definir las materias
    materias = {
        "calculo_integral": Materia("Cálculo Integral", "CI001"),
        "programacion_objetos": Materia("Programación Orientada a Objetos", "POO002"),
        "base_datos": Materia("Base de Datos", "BD003"),
        "desarrollo_pensamiento": Materia("Desarrollo del Pensamiento", "DP004"),
        "proyecto_integrador": Materia("Proyecto Integrador", "PI005"),
        "topicos_calidad": Materia("Tópicos de Calidad", "TC006")
    }

    # 2. Crear docentes
    docente1 = Docente("Bruno Luciano", "UTC001")
    docente2 = Docente("Ing. Fidel Arias", "UTC002")
    docente3 = Docente("Gilberto Garcia", "UTC003")
    docente4 = Docente("Alatiel Gomez", "UTC004")
    docente5 = Docente("Sindy Gasca", "UTC005")
    docente5 = Docente("Sindy Gasca", "UTC005")

    # 3. Crear estudiantes
    estudiante1 = Estudiante("Luis Cruz", "UTC24007")
    estudiante2 = Estudiante("Dori Mendez", "UTC240012")
    estudiante3 = Estudiante("Gnesi Gomez", "UTC24005")
    estudiante4 = Estudiante("Gadiel Muños", "UTC24008")
    estudiante5 = Estudiante("Jassiel Perez", "UTC240014")
    estudiante6 = Estudiante("Zuleima Martinez", "UTC240022")
    estudiante7 = Estudiante("Joshua Miss", "UTC240018")
    estudiante8 = Estudiante("Juan Jose Damian", "UTC240017")
    

    # 4. Asignar calificaciones
    # Estudiante 1
    docente1.asignar_calificacion(estudiante1, materias["calculo_integral"], 8.5)
    docente1.asignar_calificacion(estudiante1, materias["programacion_objetos"], 9.0)
    docente2.asignar_calificacion(estudiante1, materias["base_datos"], 7.2)
    docente1.asignar_calificacion(estudiante1, materias["desarrollo_pensamiento"], 6.0)
    docente2.asignar_calificacion(estudiante1, materias["proyecto_integrador"], 9.5)
    docente1.asignar_calificacion(estudiante1, materias["topicos_calidad"], 7.8)

    # Estudiante 2
    docente1.asignar_calificacion(estudiante2, materias["calculo_integral"], 5.0)
    docente2.asignar_calificacion(estudiante2, materias["programacion_objetos"], 8.0)
    docente3.asignar_calificacion(estudiante2, materias["base_datos"], 6.5)
    docente4.asignar_calificacion(estudiante2, materias["desarrollo_pensamiento"], 7.0)
    docente5.asignar_calificacion(estudiante2, materias["proyecto_integrador"], 5.5)
    docente6.asignar_calificacion(estudiante2, materias["topicos_calidad"], 6.0)

    # Estudiante 3 
    docente1.asignar_calificacion(estudiante3, materias["calculo_integral"], 9.0)
    docente2.asignar_calificacion(estudiante3, materias["programacion_objetos"], 10.5) # Esto generará un error de validación
    docente3.asignar_calificacion(estudiante3, materias["base_datos"], 4.0)


    # 5. Generar el reporte final para todos los estudiantes
    generar_reporte_final([estudiante1, estudiante2, estudiante3, estudiante4, estudiante5, eestudiante6, estudiante7, estudiante8])

if __name__ == "__main__":
    main()

