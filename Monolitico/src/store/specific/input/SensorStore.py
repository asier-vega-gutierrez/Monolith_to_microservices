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
            sensor_l1 = SensorData(
                row[0],
                1,
                row[1], 
                row[2],
                row[3],
                row[4],
                row[9],
                row[10]
            )
            sensor_l2 = SensorData(
                row[0],
                2,
                row[5], 
                row[6],
                row[7],
                row[8],
                row[9],
                row[10]
            )
                       
            sensor_list.append([sensor_l1, sensor_l2])

        # disconnect from server
        self.disconnect()

        return sensor_list
   