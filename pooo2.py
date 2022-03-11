


def main():
    class Persona():
        def __init__(self):
            self.nombre =input ("ingrese el nombre:    ")
            self.apellido =input ("ingrese el apellido ")
            self.direccion =input ("ingrese la direccion ")
            self.telefono =input ("ingrse el telefono")

            def mostrarPersona(self):
     
             print (f"Mi nombre es {self.nombre} {self.apellido}")

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.sueldo = float (input("ingrese el sueldo:   "))
            if self.__<2000000:
                self.alimentacion = 80000
                self.transporte= 60000
            else:
                self.alimentacion=0
                self.transporte=0

            self.pension= self.__sueldo *0.04
                
            self.salud= self.__sueldo *0.0375

            
            self.dev=self.alimentacion+self.transporte

            
            self.ded=self.pension+self.salud        
          

        def mostrarEmpleado(self):
            super().mostrarPersona()
            print (f"sueldo:{self.__sueldo}")
            print (f"transporte:{self.transporte}")
            print(f"alimentacion:{self.alimentacion}")
            print (f"pension:{self.pension}")

     

    empleado1= Empleado()
    #empleado1=__sueldo =4000000
    empleado1.mostrarEmpleado()



if __name__ =="__main__":
     main()