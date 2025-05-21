from store.base.SqlServerStore import SqlServerStore
from domain.Sensor import SensorData

class SensorStore(SqlServerStore):
    """ Specific store to manage the Sensor tore """

    def __init__(self, dbname):
        """ Default constructor to create the specific store for Sensor Data """
        super().__init__(dbname)
            
    def get_sensors_data(self):
        """ Method to get the full list of sensor data"""
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT [Timestamp], \
                    Item14, \
                    Item19,  \
                    TemperaturaArenaI34, \
                    CopaMoldeL1, \
                    Item214, \
                    Item219, \
                    TemperaturaArenaI230, \
                    CopaMoldeL2, \
                    TemperaturaAmbienteAre, \
                    Humedad \
                    FROM [DB-SENSORS].dbo.Sensores;"

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        sensor_list = []

        results = cursor.fetchall()
        for row in results:
            sensor_l1 = SensorData()
            sensor_l2 = SensorData()

            sensor_l1.timestamp = row[0]
            sensor_l1.line = 1
            sensor_l1.bypass_activated = row[1] 
            sensor_l1.cooling_drum_running = row[2]
            sensor_l1.temperature_output = row[3]
            sensor_l1.mould_temp = row[4]
            sensor_l1.ambient_temperature = row[9]
            sensor_l1.humidity = row[10]

            sensor_l2.timestamp = row[0]
            sensor_l2.line = 2
            sensor_l2.bypass_activated = row[5] 
            sensor_l2.cooling_drum_running = row[6]
            sensor_l2.temperature_output = row[7]
            sensor_l2.mould_temp = row[8]
            sensor_l2.ambient_temperature = row[9]
            sensor_l2.humidity = row[10]
                       
            sensor_list.append([sensor_l1, sensor_l2])

        # disconnect from server
        self.disconnect()

        return sensor_list
   