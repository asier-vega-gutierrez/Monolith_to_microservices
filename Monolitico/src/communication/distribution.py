#El Singelton esta diseñado para que mediante herencia de esta clase no se generen intacias nuevas de las clases hijas
class DataCommunicationManager_meta(type):
    _instances = {}
    #El Singelton hereda este metodo que impide que se creen nuevas clases 
    def __call__(cls, *args, **kwargs): #Aui se llega siempre cuando se instacia uno de estos objetos
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

#Clase hija del meta de Singleton, esto es el Singelton
class DataCommunicationManager(metaclass=DataCommunicationManager_meta):

    def __init__(self):
        self.observers = {} #Aqui se almacenan los los topics y dentro de estos sus observadores

    #Método para agregar un observador a un topic específico
    def add_observer(self, topic, observer):
        if topic not in self.observers:
            #Si el topic no existe en el diccionario, lo creamos como una lista vacía
            self.observers[topic] = []
        #Luego, agregamos el observador a la lista de observadores para ese topic
        self.observers[topic].append(observer)
    
    #Método para eliminar un observador a un topic específico
    def remove_observer(self, topic, observer):
        if topic in self.observers:
            #Si el topic existe en el diccionario
            if observer in self.observers[topic]:
                #Eliminamos el observador de la lista de observadores para ese topic
                self.observers[topic].remove(observer)

    #Método para notificar a los observadores sobre un topic específico
    def data_distribution(self, topic, message):
        if topic in self.observers:
            #Si hay observadores registrados para el topic
            for observer in self.observers[topic]:
                #Llamamos al método "update" de cada observador registrado para ese topic
                observer.notify(message)
        print(self.observers)