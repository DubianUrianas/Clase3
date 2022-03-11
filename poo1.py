



def main():
    class Persona():
        nombre ="Dubian"
        apellido= "Uriana"
        direccion="km 7"
        telefono ="31039397631"

        def mostrarPersona(self):
     
            print (f"Mi nombre es {self.nombre} {self.apellido}")
    persona1 = Persona()#crear la instancia de la clase
    print (persona1.nombre)
    
    
if __name__ =="__main__":
     main()