from domain.Addition import WaterAdditionData
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

from config.configuration import ApplicationConfiguration

class PredictionStoreTS():
    """ Specific store to manage the Prediction Store """

        
    def add_prediction(self, water_addition_data):
        """ Method to add a Prediction to the Postgres """

        # Define data to insert
        if water_addition_data.type.upper() == 'DRUM':
            prediction_json = [
                {
                    "measurement": "water_addition",
                    "tags": {
                        "line": int(water_addition_data.line if water_addition_data.type.upper() == "DRUM" else 999),
                        "type": str(water_addition_data.type.upper())
                    },
                    "time": water_addition_data.datetime,
                    "fields": {
                        "prediction" : float(water_addition_data.prediction),    
                        "f_avg" : float(water_addition_data.data_for_prediction['f_avg']),
                        "mould_size" : int(water_addition_data.data_for_prediction['mould_size']),
                        "moulds_to_calculate" : int(water_addition_data.data_for_prediction['moulds_to_calculate']),
                        "q_metal_avg" : float(water_addition_data.data_for_prediction['q_metal_avg']),
                        "q_sand_avg" : float(water_addition_data.data_for_prediction['q_sand_avg'])
                    }
                }
            ]
        else:
            prediction_json = [
                {
                    "measurement": "water_addition",
                    "tags": {
                        "line": int(water_addition_data.line if water_addition_data.type.upper() == "DRUM" else 999),
                        "type": str(water_addition_data.type.upper())
                    },
                    "time": water_addition_data.datetime,
                    "fields": {
                        "prediction" : float(water_addition_data.prediction),    
                        "temp_avg" : float(water_addition_data.data_for_prediction['temp_avg']),
                        "q_sand_avg" : float(water_addition_data.data_for_prediction['q_sand_avg']),
                        "mould_size" : int(water_addition_data.data_for_prediction['mould_size']),
                        "moulds_to_calculate" : int(water_addition_data.data_for_prediction['moulds_to_calculate']),                        
                        "humidity" : float(water_addition_data.data_for_prediction['humidity'])
                    }
                }
            ]

        # We get the configuration
        config = ApplicationConfiguration()

        token = config.influx_token
        inf_org = config.influx_org
        url = config.influx_url

        client = influxdb_client.InfluxDBClient(url=url, token=token, org=inf_org, timeout=60000)
        print("Connected to the database.(InfluxDB)")
        bucket=config.influx_bucket

        write_api = client.write_api(write_options=SYNCHRONOUS)

        # We write data
        print("PREDICTION POINT to write: {0}".format(prediction_json))
        write_api.write(bucket=bucket, org=inf_org, record=prediction_json)
        write_api.flush()
        
        # Disconnecrt from database
        write_api.close()
        client.close()
        print("Disconnected from the database.(InfluxDB)")

        return prediction_json
        
    