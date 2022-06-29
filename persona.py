class persona:
    """Inicializo la clase persona."""
    
    def __init__(self, dni, nombre):
        """Inicialización de los parámetros de la clase."""
        self.dni = dni
        self.nombre = nombre
    
    def getdni(self):
        return self.dni
    def getnombre(self):
        return self.nombre
    def __repr__(self):
        """Representación formal."""
        return "dni: {}, nombre: {}".format(self.dni, self.nombre)
