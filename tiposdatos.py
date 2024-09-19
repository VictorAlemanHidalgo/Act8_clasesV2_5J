print("Clases V2 Victor Aleman")
# Zona de clase
class Datos:
    # El constructor funcion
    def __init__(self, estatura, peso):
        self.estatura = estatura
        self.peso = peso
    
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} kg")
    
    def mi_lista(self):
        Videojuegos = ["Super Mario Galaxy", "Mario y Luigi: Bowser Inside Story's", "Mario y Luigi: Dream Team", "Luigi's Mansion 3", "Super Mario Wonder"]
        print(Videojuegos)
        for juego in Videojuegos:
            print(juego)

    def mi_tupla(self):
        MateriasEscolares = ("Español", "Matematicas", "Quimica", "Ingles", "Historia")
        print(MateriasEscolares)
        for materia in MateriasEscolares:
            print(materia)

    def mi_conjunto(self):
        AnimalesExoticos = {"Delfin Rosado", "Rana Toro", "Gecko", "Tortuga galápo", "Mejillón cebra"}
        print(AnimalesExoticos)
        for animal in AnimalesExoticos:
            print(animal)
        
    def mi_diccionario(self):
        MisHermanos = {
            "Rodrigo": 14,
            "Carlos": 12,
            "Elyzabeth": 8
        }
        print(MisHermanos)
        for nombre, edad in MisHermanos.items():
            print(f"Nombre: {nombre}, edad: {edad} años")

# Creacion de objetos
Info = Datos(1.70, 77.9)

# Utilizando el objeto --> Info
Info.mostrar_datos()
print(" Lista de Videojuegos Victor Aleman")
Info.mi_lista()

print(" Tupla de Materias Escolares Victor Aleman")
Info.mi_tupla()

print(" Conjunto de Animales Exoticos Victor Aleman")
Info.mi_conjunto()

print(" Diccionario de Mis hermanos Victor Aleman")
Info.mi_diccionario()