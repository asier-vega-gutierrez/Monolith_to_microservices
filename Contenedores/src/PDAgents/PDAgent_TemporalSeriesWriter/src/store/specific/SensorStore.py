from domain.sensor import SensorData
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

from config.configuration import PDAgentTemporlSeriesWriterConfiguration

class SensorStore():
    """ Specific store to manage the Data Rec Store """
       
    def add_sensor(self, sensor_data):
        """ Method to add a Sensor Data to the Postgres """
 
        # Define data to insert
        sensor_json = [
            {
                "measurement": "foundry_sensors",
                "tags": {
                    "line": int(sensor_data.line)
                },
                "time": sensor_data.timestamp,
                "fields": {
                    "bypass_activated" : int(sensor_data.bypass_activated),
                    "cooling_drum_running" : int(sensor_data.cooling_drum_running),
                    "temperature_output" : float(sensor_data.temperature_output),
                    "mould_temp" : float(sensor_data.mould_temp),
                    "ambient_temperature" : float(sensor_data.ambient_temperature),
                    "humidity" : float(sensor_data.humidity)                     
                }
            }
        ]

        # We get the configuration
        config = PDAgentTemporlSeriesWriterConfiguration()

        token = config.influx_token
        inf_org = config.influx_org
        url = config.influx_url

        client = influxdb_client.InfluxDBClient(url=url, token=token, org=inf_org, timeout=60000)

        bucket=config.influx_bucket

        write_api = client.write_api(write_options=SYNCHRONOUS)

        print("SENSOR POINT to write: {0}".format(sensor_json))
        write_api.write(bucket=bucket, org=inf_org, record=sensor_json)
        write_api.flush()
        
        # Disconnecrt from database
        write_api.close()
        client.close()

        return sensor_json
    
    