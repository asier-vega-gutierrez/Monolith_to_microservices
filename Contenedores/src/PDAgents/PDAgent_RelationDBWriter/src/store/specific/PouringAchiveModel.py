from store.base.PostgresStore import  PostgresStore
from domain.models import PouringArchiveModelsData

class PouringArchiveModelStore(PostgresStore):
    """ Specific store to manage the Pouring Archive Model Store """

    def __init__(self):
        """ Default constructor """

        super().__init__()
    
    def exists_archive_model(self, archive_model_id):
        """ Method to know if the archive model is stored into database """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ SELECT COUNT(id) as number                         
                    FROM public.pouring_archive_models
                    WHERE id = {} """.format(archive_model_id)    

        # Execute the SQL command
        cursor.execute(sql)
        
        # Fetch just one element
        number = cursor.fetchone()

        # disconnect from server
        self.disconnect()

        return False if float(number[0]) == 0 else True
        
        
    def add_archive_model(self, archive_model_data):
        """ Method to add a archive model to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()    
        
        # Define the SQL for insert data
        sql = """ INSERT INTO public.pouring_archive_models
                    (id, model_code, model_description, model_weight, inoculation_perc, inoculation_gs, material_type, inoculation_start, inoculation_stop, position_axe_x, position_axe_y, aperture_max, aperture_min, during_level, final_level, duration_final_control, pouring_duration, temperature_min, temperature_max)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """    
        
        data = (archive_model_data.id,
                archive_model_data.model_code, 
                archive_model_data.model_description, 
                archive_model_data.model_weight, 
                archive_model_data.inoculation_perc, 
                archive_model_data.inoculation_gs, 
                archive_model_data.material_type, 
                archive_model_data.inoculation_start, 
                archive_model_data.inoculation_stop, 
                archive_model_data.position_axe_x, 
                archive_model_data.position_axe_y, 
                archive_model_data.aperture_max, 
                archive_model_data.aperture_min, 
                archive_model_data.during_level, 
                archive_model_data.final_level, 
                archive_model_data.duration_final_control, 
                archive_model_data.pouring_duration, 
                archive_model_data.temperature_min, 
                archive_model_data.temperature_max)
            
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into pouring archive model table.")

        # Disconnecrt from database
        self.disconnect()   
    