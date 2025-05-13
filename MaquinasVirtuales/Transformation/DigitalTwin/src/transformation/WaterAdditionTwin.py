from config.configuration import ApplicationConfiguration
from domain.Addition import WaterAdditionData

from communication.publisher import data_distribution
from communication.base.subscriber_base import SubscriberBase
from communication.consumer import Consumer


from message_processors.sensors import SensorMessageProcessor
from message_processors.mould import MouldMessageProcessor

from threading import Thread
from datetime import datetime, timezone
from statistics import mean 

from json import dumps 
import json
import httpx
import logging



class WaterAdditionDigitalTwin(SubscriberBase):
    """ Class that represents the digital twin for water addition """

    def __init__(self,
                 type: str,
                 line: int,
                 mould_size: int,
                 moulds_to_calculate: int) -> None:
        """ Constructor of the class """
        
        # We create the elements to generate the digital status of the plant
        self._mould_queue = []
        self._current_line_status = None

        # We configure the type of working
        self._type = type
        self._line = line
        self._mould_size = mould_size
        self._moulds_to_calculate = moulds_to_calculate

        # We create the communication element
        '''self._data_communication_manager = DataCommunicationManager()'''
        self._data_communication_manager = Consumer()

        # We get the configuration of the application
        self._config = ApplicationConfiguration()

        # We create the messages processors
        self._sensor_message_processor = SensorMessageProcessor(self.update_current_situation)
        self._mould_message_processor = MouldMessageProcessor(self.add_new_mould)

    def start_digital_twin_processing(self):
        """ Method to process all events in the plant """
   
        # We configure the subscriptions
        # First for moulds
        if self._type.upper() == 'DRUM':
            self._data_communication_manager.add_subscriber(f"{self._config.mould_data_topic}_l{self._line}", self._mould_message_processor)
        else:
            self._data_communication_manager.add_subscriber(f"{self._config.mould_for_belts_topic}", self._mould_message_processor)
        
        # Then for sensors
        self._data_communication_manager.add_subscriber(f"{self._config.sensor_data_topic}_l{self._line}", self._sensor_message_processor)           

    def stop_digital_twin_processing(self): 
        """ Method to stop processing all events in the plant  """

        # We remove the subscriptions
        # First for moulds
        if self._type.upper() == 'DRUM':
            self._data_communication_manager.remove_subscriber(f"{self._config.mould_data_topic}_l{self._line}", self._mould_message_processor)
        else:
            self._data_communication_manager.remove_subscriber(f"{self._config.mould_for_belts_topic}", self._mould_message_processor)
        
        # Then for sensors
        self._data_communication_manager.remove_subscriber(f"{self._config.sensor_data_topic}_l{self._line}", self._sensor_message_processor)


    def update_current_situation(self, sensors_data):
        """ Method to update the value of the sensors (the current status of the plant) """
        
        self._current_line_status = sensors_data
    
    def add_new_mould(self, mould_data):
        """ Method that adds a new mould and starts the calculations and simulation for water addition """

        # We add the mould
        self._mould_queue.append(mould_data)

        # If it is bigger that we need
        if len(self._mould_queue) > self._mould_size:
            # We get the output mould and we notificate
            out_mould = self._mould_queue[0]

            if(self._type.upper() == "DRUM"):
                out_mould_json = json.dumps(out_mould.__dict__, indent=3, sort_keys=True, default=str)
                '''self._data_communication_manager.data_distribution(self._config.mould_for_belts_topic, out_mould_json)'''
                data_distribution(self._config.mould_for_belts_topic, out_mould_json)
                self.log_info(f"Distribution new mould: {self._config.mould_for_belts_topic} {out_mould_json}")
            
            # We leve the last n moulds
            self._mould_queue = self._mould_queue[1:]

            # we launch the calculations
            self._calculate_water_addition()

    def log_info(self, message):
        # Configure the logging system (you can customize this based on your needs)
        logging.basicConfig(filename='logs/DigitalTwin.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the provided message at the INFO level
        logging.info(message)

    def _calculate_water_addition(self):

        """ Method that calculates the water addition needed """
        
        # For Digital Twin in Cooling Drum
        if self._type.upper() == 'DRUM':
            # We get variables, f_avg, q_sand_avg and q_metal_avg
            f_avg = self._calculate_f_average()
            q_sand_avg = self._calculate_qsand_average()
            q_metal_avg = self._calculate_qmetal_average()

            # Then, we call the rest api service
            '''response_liters = calculate_water_adittion_liters(f_avg, q_sand_avg, q_metal_avg)'''
            water_aditton_liters = f"http://10.0.6.5:80/calculate_water_adittion_liters/?f_avg={f_avg}&q_sand_avg={q_sand_avg}&q_metal_avg={q_metal_avg}"
            response_water_aditton_liters = httpx.get(water_aditton_liters)
            if response_water_aditton_liters.status_code == 200:
                result_water_aditton_liters = response_water_aditton_liters.json()["result"]
                print("Result from calculate_water_adittion_liters:", result_water_aditton_liters)
                self.log_info(f"Result from calculate_water_adittion_liters: {result_water_aditton_liters}")
            else:
                print("Error:",  response_water_aditton_liters.status_code,  response_water_aditton_liters.text)
                self.log_info("Error:",  response_water_aditton_liters.status_code,  response_water_aditton_liters.text)
            print(f"COOLING DRUM Water Addition for Line {self._line}: {result_water_aditton_liters}")
            self.log_info(f"COOLING DRUM Water Addition for Line {self._line}: {result_water_aditton_liters}")

            # We distribute the request to be stored or used            
            data_for_prediction = {'mould_size' : self._mould_size, 'moulds_to_calculate' : self._moulds_to_calculate, 'f_avg' : f_avg, 'q_sand_avg' : q_sand_avg, 'q_metal_avg' : q_metal_avg}
            addition_data = WaterAdditionData(datetime.now(timezone.utc), self._line, self._type, result_water_aditton_liters, data_for_prediction)
            
            water_addition_data_json = json.dumps(addition_data.__dict__, indent=3, sort_keys=True, default=str)
            '''self._data_communication_manager.data_distribution(f"{self._config.water_prediction_drum_topic}_l{self._line}", water_addition_data_json)'''
            data_distribution(f"{self._config.water_prediction_drum_topic}_l{self._line}", water_addition_data_json)
            self.log_info(f"Distribution water prediction drum: {self._config.water_prediction_drum_topic}_l{self._line}")
            
        else:
            # we get the variables q_sand_avg, temp_avg and humidity
            q_sand_avg = self._calculate_qmetal_average()
            temp_avg = self._obtain_current_temperature()
            humidity = self._obtain_current_humidity()

            # Then, we call the rest api service
            '''response_factor = calculate_unified_belt_addition(q_sand_avg, temp_avg, humidity)'''
            url_unified_belt = f"http://10.0.6.5:80/calculate_unified_belt_addition/?q_sand_average={q_sand_avg}&temp_average={temp_avg}&humidity={humidity}"
            response_unified_belt = httpx.get(url_unified_belt)
            if response_unified_belt.status_code == 200:
                result_unified_belt = response_unified_belt.json()["result"]
                print("Result from calculate_unified_belt_addition:", result_unified_belt)
                self.log_info(f"Result from calculate_unified_belt_addition: {result_unified_belt}")
            else:
                print("Error:", response_unified_belt.status_code, response_unified_belt.text)
                self.log_info("Error:", response_unified_belt.status_code, response_unified_belt.text)
            print("COOLING DRUM Belts Addition: {}".format(self._line, result_unified_belt))
            self.log_info("COOLING DRUM Belts Addition: {}".format(self._line, result_unified_belt))

            # We distribute the request to be stored or used
            data_for_prediction = {'mould_size' : self._mould_size, 'moulds_to_calculate' : self._moulds_to_calculate, 'q_sand_avg' : q_sand_avg, 'temp_avg' : temp_avg, 'humidity' : humidity}
            addition_data = WaterAdditionData(datetime.now(timezone.utc), self._line, self._type, result_unified_belt, data_for_prediction)
            
            water_addition_data_json = json.dumps(addition_data.__dict__, indent=3, sort_keys=True, default=str)
            '''self._data_communication_manager.data_distribution(self._config.water_prediction_unified_belts_topic, water_addition_data_json)'''
            data_distribution(self._config.water_prediction_unified_belts_topic, water_addition_data_json)
            self.log_info(f"Distribution water prediction belts: {self._config.water_prediction_unified_belts_topic} {water_addition_data_json}")
            
    def _calculate_f_average(self):
        """ Private method to calcuate the f average """

        f_factors = [i.f_factor() for i in self._mould_queue[:self._moulds_to_calculate]]
        f_average = mean(f_factors)

        return f_average
            
    def _calculate_qsand_average(self):
        """ Private method used to calculate the q_sand_average """

        q_sand_values = [i.q_sand() for i in self._mould_queue[:self._moulds_to_calculate]]
        q_sand_average = mean(q_sand_values)

        return q_sand_average
    
    def _calculate_qmetal_average(self):
        """ Private metod used to calculate the q_metal_average """

        q_metal_values = [i.q_metal() for i in self._mould_queue[:self._moulds_to_calculate]]
        q_metal_average = mean(q_metal_values)

        return q_metal_average
    
    def _obtain_current_temperature(self):
        """ Private method to calculate temp average """

        return self._current_line_status.temperature_output

    def _obtain_current_humidity(self):
        """ Private method to get the current humidity """

        return self._current_line_status.humidity
    