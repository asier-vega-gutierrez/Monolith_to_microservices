from store.base.PostgresStore import  PostgresStore
from domain.Addition import WaterAdditionData

class PredictionStore(PostgresStore):
    """ Specific store to manage the Prediction Store """

    def __init__(self):
        """ Default constructor """

        super().__init__()
    
    def add_prediction(self, water_addition_data):
        """ Method to add a Prediction to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ INSERT INTO public.water_addition
                    (datetime, line, "type", prediction, data_for_prediction)
                    VALUES(%s, %s, %s, %s, %s); """    
        
        data = (water_addition_data.datetime, 
                water_addition_data.line if water_addition_data.type.upper() == "DRUM" else 999, 
                water_addition_data.type, 
                water_addition_data.prediction, 
                str(water_addition_data.data_for_prediction))
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into chemical composition table.")

        # Disconnecrt from database
        self.disconnect()   
    