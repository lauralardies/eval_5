import pickle

class Personaje():
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa 
        self.alcance = alcance

class Gestor():
    def __init__(self, personaje):
        self.personaje = personaje
    
    def agregar(self):
        pass

    def eliminar(self):
        pass

    def modificar(self):
        pass

nombres = ['Caballero', 'Guerrero', 'Arquero']
vidas = ['4', '2', '2']
ataques = ['2', '4', '4']
defensas = ['4', '2', '1']
alcance = ['2', '4', '8']

personajes = []

for i in range(len(nombres)):
    p = Personaje(nombres[i], vidas[i], ataques[i], defensas[i], alcance[i])
    personajes.append(p)

