from webbrowser import get
from dataconsumer.consumer import MUCSIConsumer
from dataproducer.producer import notify_data_using_kafka
from config.TwinConfiguration import WaterAdditionConfiguration
from threading import Thread
from subscribers.specific.status import SensorsSubscriber
from subscribers.specific.mould import MouldSubscriber
from domain.Addition import WaterAdditionData
from datetime import datetime, timezone
from statistics import mean 
import requests

from config.TwinConfiguration import WaterAdditionConfiguration

class WaterAdditionDigitalTwin:
    """ Class that represents the digital twin for water addition """

    def __init__(self) -> None:
        """ Constructor of the class """
        
        # We create the elements to generate the digital status of the plant
        self._mould_queue = []
        self._current_line_status = None

        # We create the object to manage data events
        self._data_consumer = MUCSIConsumer()

        # We get the configuration of the digital twin
        self._config = WaterAdditionConfiguration()

    def start_digital_twin_processing(self):
        """ Method to process all events in the plant """
   
        # We configure the subscriptions
        # First for moulds
        if self._config.type.upper() == 'DRUM':
            self._data_consumer .add_subscriber(f"{self._config.kafka_mould_data_topic}_l{self._config.line}", MouldSubscriber(self.add_new_mould))
        else:
            self._data_consumer .add_subscriber(f"{self._config.kafka_mould_for_belts_topic}", MouldSubscriber(self.add_new_mould))
        
        # Then for sensors
        self._data_consumer.add_subscriber(f"{self._config.kafka_sensor_data_topic}_l{self._config.line}", SensorsSubscriber(self.update_current_situation))           
        

        # We launch the reading process
        t1 = Thread(target=self._data_consumer.start_listening_messages)
        t1.start()
        t1.join()

    def update_current_situation(self, sensors_data):
        """ Method to update the value of the sensors (the current status of the plant) """
        
        self._current_line_status = sensors_data
    
    def add_new_mould(self, mould_data):
        """ Method that adds a new mould and starts the calculations and simulation for water addition """

        # We add the mould
        self._mould_queue.append(mould_data)

        # If it is bigger that we need
        if len(self._mould_queue) > self._config.mould_size:
            # We get the output mould and we notificate
            out_mould = self._mould_queue[0]

            t = Thread(target=notify_data_using_kafka, args=(out_mould,))
            t.start()

            # We leve the last n moulds
            self._mould_queue = self._mould_queue[1:]

            # we launch the calculations
            self._calculate_water_addition()
    
    def _calculate_water_addition(self):
        """ Method that calculates the water addition needed """
        
        # For Digital Twin in Cooling Drum
        if self._config.type.upper() == 'DRUM':
            # We get variables, f_avg, q_sand_avg and q_metal_avg
            f_avg = self._calculate_f_average()
            q_sand_avg = self._calculate_qsand_average()
            q_metal_avg = self._calculate_qmetal_average()

            # Then, we call the rest api service 
            api_url = f'{self._config.cooling_drum_predictor_api_url_base}?f_avg={f_avg}&q_sand_avg={q_sand_avg}&q_metal_avg={q_metal_avg}'
            response = requests.get(api_url)
            print("COOLING DRUM Water Addition for Line {}: {}".format(self._config.line, response.text))

            # We distribute the request to be stored or used            
            data_for_prediction = {'mould_size' : self._config.mould_size, 'moulds_to_calculate' : self._config.moulds_to_calculate, 'f_avg' : f_avg, 'q_sand_avg' : q_sand_avg, 'q_metal_avg' : q_metal_avg}
            addition_data = WaterAdditionData(datetime.now(timezone.utc), self._config.line, self._config.type, response.text, data_for_prediction)
            notify_data_using_kafka(addition_data)
        else:
            # we get the variables q_sand_avg, temp_avg and humidity
            q_sand_avg = self._calculate_qmetal_average()
            temp_avg = self._obtain_current_temperature()
            humidity = self._obtain_current_humidity()

            # Then, we call the rest api service 
            api_url = f'{self._config.belts_predictor_api_url_base}?q_sand_average={q_sand_avg}&temp_average={temp_avg}&humidity={humidity}'
            response = requests.get(api_url)
            print("COOLING DRUM Belts Addition: {}".format(self._config.line, response.text))

            # We distribute the request to be stored or used
            data_for_prediction = {'mould_size' : self._config.mould_size, 'moulds_to_calculate' : self._config.moulds_to_calculate, 'q_sand_avg' : q_sand_avg, 'temp_avg' : temp_avg, 'humidity' : humidity}
            addition_data = WaterAdditionData(datetime.now(timezone.utc), self._config.line, self._config.type, response.text, data_for_prediction)
            notify_data_using_kafka(addition_data)

    def _calculate_f_average(self):
        """ Private method to calcuate the f average """

        f_factors = [i.f_factor() for i in self._mould_queue[:self._config.moulds_to_calculate]]
        f_average = mean(f_factors)

        return f_average
            
    def _calculate_qsand_average(self):
        """ Private method used to calculate the q_sand_average """

        q_sand_values = [i.q_sand() for i in self._mould_queue[:self._config.moulds_to_calculate]]
        q_sand_average = mean(q_sand_values)

        return q_sand_average
    
    def _calculate_qmetal_average(self):
        """ Private metod used to calculate the q_metal_average """

        q_metal_values = [i.q_metal() for i in self._mould_queue[:self._config.moulds_to_calculate]]
        q_metal_average = mean(q_metal_values)

        return q_metal_average
    
    def _obtain_current_temperature(self):
        """ Private method to calculate temp average """

        return self._current_line_status.temperature_output

    def _obtain_current_humidity(self):
        """ Private method to get the current humidity """

        return self._current_line_status.humidity
    