from io import open
import pickle

class Personaje():
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa 
        self.alcance = alcance
        print('Se ha creado el personaje {}.'.format(self.nombre))
    
    def __str__(self) -> str:
        return '{}: Vida {}, Ataque {}, Defensa {}, Alcance {}.'.format(self.nombre, self.vida, self.ataque, self.defensa, self.alcance)

class Gestor():

    personajes = []

    def __init__(self):
        self.cargar()
    
    def agregar(self, p):
        self.personajes.append(p)
        self.guardar()

    def eliminar(self, p):
        for personaje in self.personajes:
            if p.nombre == personaje.nombre:
                indice = self.personajes.index(p)
                del self.personajes[indice]
                self.guardar()
                print('El personaje {} ha sido eliminado.'.format(p.nombre))
                return
        else:
            print('El personaje seleccionado a borrar no está en nuestra lista.')
            return

    def mostrar(self):
        if len(self.personajes) == 0:
            print("No hay personajes.")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('ejercicios/ejercicio3/personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print("El fichero está vacío.")
        finally:
            fichero.close()

    def guardar(self):
        fichero = open('ejercicios/ejercicio3/personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()

g = Gestor()

cab = Personaje('Caballero', '4', '2', '4', '2')
gue = Personaje('Guerrero', '2', '4', '2', '4')
arq = Personaje('Arquero', '2', '4', '1', '8')

# Creamos los personajes.
g.agregar(cab)
g.agregar(gue)
g.agregar(arq)

# Muestro los personajes.
g.mostrar()

# Elimino personaje Arquero.
g.eliminar(arq)

# Muestro de nuevo los personajes.
g.mostrar()

# Borramos el gestor de la memoria ram
del(g)