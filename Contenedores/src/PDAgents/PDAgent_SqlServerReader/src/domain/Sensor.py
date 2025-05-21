class SensorData():
    """ Class to represent the object Sensor Data from domain  """

    def __init__(self) -> None:
        """ Default constructor of the objct Sensor Data from the domain"""
        
        self.timestamp = None
        self.line = None
        self.bypass_activated = None 
        self.cooling_drum_running = None
        self.temperature_output = None
        self.mould_temp = None
        self.ambient_temperature = None
        self.humidity = None
 
 #   def __init__(self,
 #               timestamp,
 #               line,
 #               bypass_activated, 
 #               cooling_drum_running,
 #               temperature_output,
 #               mould_temp,
 #               ambient_temperature,
 #               humidity) -> None:
 #       """ Constructor with parameters of the objct Sensor Data from the domain"""
#
 #       self.timestamp = timestamp
 #       self.line = line
 #       self.bypass_activated = bypass_activated
 #       self.cooling_drum_running = cooling_drum_running
 #       self.temperature_output = temperature_output
 #       self.mould_temp = mould_temp
 #       self.ambient_temperature = ambient_temperature
 #       self.humidity = humidity