from persona import persona as per

class pacientecovid(per):
    """Esta clase hereda de la clase persona que he llamado per."""
    
    def __init__(self, dni, nombre, estado):
        super().__init__(dni, nombre)
        self.__estado = estado # esta entre 0 y 3 si no salta error
        self.__contactos = []
        
    @property
    def estado(self):
        return self.__estado
        
    @estado.setter
    def estado(self, estado1):
        if 0<=estado1<=3:
            self.estado = estado1
        else:
            raise ValueError("Esto esta mal")
            
    def add_contacto(self, newcontacto):
        self.__contactos.append(newcontacto)
    
    def __eq__(self, other):
        """Comparamos que son iguales."""
        if type(other) == pacientecovid:
            return self.dni == other.dni
        else:
            return False
    
    def __iter__(self):
        for i in self.__contactos:
            yield i
paciente1 = pacientecovid("332458123A", "Jose Carlos", 2)
paciente2 = pacientecovid("231232331B", "Pablo", 3)
print(paciente1.__eq__(paciente1))
print(paciente1.estado)
paciente1.add_contacto(per("123456789", "Ayose"))
paciente1.add_contacto(per("123423789", "Ismael"))

for person in paciente1:
    print(person)