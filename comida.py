class PlatilloComedor:
    def __init__(self, nombre, acompanamiento, temperatura, tipo, fecha_preparacion, precio):
        # Este es el método constructor, se ejecuta al crear un objeto de PlatilloComedor
        self.nombre = nombre                       # Guarda el nombre del platillo
        self.acompanamiento = acompanamiento       # Guarda el acompañamiento (arroz, frijoles, etc.)
        self.temperatura = temperatura             # Guarda la temperatura del platillo
        self.tipo = tipo                           # Guarda el tipo de platillo (guisado, sopa, etc.)
        self.fecha_preparacion = fecha_preparacion # Guarda la fecha de preparación
        self.precio = precio

    def recalentar(self):                          # Método para revisar la temperatura
        if self.temperatura <= 0:                  # Si la temperatura es menor o igual a 0
            print("Hay que recalentar la comida. Tempratura actual: ", self.temperatura, "grados.")
            self.temperatura + 50
            print("Tu plato ahora esta a", self.temperatura, "grados.")  # Regresa este mensaje
        elif self.temperatura >= 60:                 # Si la temperatura es mayor o igual a 60
            print("El platillo está muy caliente, ya no lo podemos calentar más. Tempratura actual: ", self.temperatura, "grados.")     # Regresa este mensaje
        else:
            self.temperatura = self.temperatura + 30
            print("Tu plato ahora esta a", self.temperatura, "grados.")

    def tocar(self):
        if self.temperatura <= 15:        
            print("Esta fria mi comida!")
        elif self.temperatura >= 60:
            print("Esta muy caliente mi comida!")
        else:
            print("Mi comida esta bien")

    def comer(self):                               # Método para "comer" el platillo
        print("¡Buen provecho!")
        self.temperatura = self.temperatura - 10
    
    def __str__(self):                             # Método especial para representar el objeto como texto
        descripcion = self.nombre + " con " + self.acompanamiento + " (" + self.tipo + ")" + ", preparado el " + self.fecha_preparacion  # La fecha de preparación
        return descripcion
    
platillo1 = PlatilloComedor("Chilaquiles", "Frijoles", 20, "Desayuno", "Hoy", 65.00)
platillo2 = PlatilloComedor("Sopa Azteca", "Queso con Crema", 10, "Sopa", "13/11/2025", 45)

print("\nHola Bienvenidos al desayuno de la Facultad de Psicología\nEste es el platillo del desayuno: ", platillo1)
salir = 1
contador_mordidas = 0
while salir == 1 or contador_mordidas <= 4:
    print("Que quieres hacer?")
    print("1. Comer")
    print("2. Recalentar")
    print("3. Tocar")
    print("4. Salirte")
    opcion = int(input())

    if opcion == 1:
        platillo1.comer()
        contador_mordidas += 1
    elif opcion == 2:
        platillo1.recalentar()
    elif opcion == 3:
        platillo1.tocar()
    elif opcion == 4:
        salir == 0
    else:
        print("No existe esa opción")
    
print("Gracias por venir a desayunar!")