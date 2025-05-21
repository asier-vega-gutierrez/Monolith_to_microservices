from store.base.PostgresStore import  PostgresStore
from domain.sensor import SensorData

class SensorStore(PostgresStore):
    """ Specific store to manage the Data Rec Store """

    def __init__(self):
        """ Default constructor of the Data Rec Store """

        super().__init__()
    
    def add_sensor(self, sensor_data):
        """ Method to add a Sensor Data to the Postgres """
 
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ INSERT INTO public.sensor
                        (datetime, cod_line, bypass_activated, cooling_drum_running, temperature_output, mould_temp, ambient_temperature, humidity)
                  VALUES(%s, %s, CAST(%s as bit), CAST(%s as bit), %s, %s, %s, %s); """    
        data = (sensor_data.timestamp, sensor_data.line, 1 if sensor_data.bypass_activated else 0, 1 if sensor_data.cooling_drum_running else 0, sensor_data.temperature_output, sensor_data.mould_temp, sensor_data.ambient_temperature, sensor_data.humidity)
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into sensor table.")

        # Disconnecrt from database
        self.disconnect()
    
    def get_last_sensor(self, line):
        """ Method to get the last sensor id for a given line. Double return, Sensor Data and ID """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT 	id_sensor, \
		                datetime, \
		                cod_line, \
                        bypass_activated, \
                        cooling_drum_running, \
                        temperature_output, \
                        mould_temp, \
                        ambient_temperature, \
                        humidity \
                FROM public.sensor \
                WHERE cod_line = {} \
                ORDER BY datetime DESC \
                LIMIT 1".format(line)

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch just one element
        id_sensor, datetime, cod_line, bypass_activated, cooling_drum_running, temperature_output, mould_temp, ambient_temperature, humidity = cursor.fetchone()
        
        # create the object
        sensor_data = SensorData(datetime,
                cod_line,
                bypass_activated, 
                cooling_drum_running,
                temperature_output,
                mould_temp,
                ambient_temperature,
                humidity)

        # disconnect from server
        self.disconnect()
        
        return sensor_data, id_sensor