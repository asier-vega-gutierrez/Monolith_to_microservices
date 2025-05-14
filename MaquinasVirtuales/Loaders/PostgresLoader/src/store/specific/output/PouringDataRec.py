from store.base.PostgresStore import  PostgresStore
from domain.Pouring import PouringDataRecData

class PouringDataRecStore(PostgresStore):
    """ Specific store to manage the Data Rec Store """

    def __init__(self):
        """ Default constructor of the Data Rec Store """

        super().__init__()
    
    def last_data_rec_id(self):
        """ Method to get las data rec id """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ SELECT id_pouring_data_rec as id
                    FROM public.pouring_data_rec
                    ORDER BY id_pouring_data_rec DESC 
                    LIMIT 1 """    

        # Execute the SQL command
        cursor.execute(sql)
        
        # Fetch just one element
        id = cursor.fetchone()

        # disconnect from server
        self.disconnect()

        return id[0]
        
        
    def add_pouring_data_rec(self, pouring_data_rec_data, model_id):
        """ Method to add a pouring data rec to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ INSERT INTO public.pouring_data_rec
                    ("time", m_sec, "local", "user", reason, aperture_min, nr_pouring_mould, aperture_max, temperature, gr_inoculant, model_id, model_description, level_final, pouring_mode, pouring_fault, model_weight, pouring_duration, gs_inoculant, inoculant_type, ticket_id, weight, elettrodo_level, pression, nr_medaglia, temperatura_manuale, staffa_scarta, inoculant_type_string)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """    
        
        data = (pouring_data_rec_data.time, 
                pouring_data_rec_data.m_sec, 
                pouring_data_rec_data.local, 
                pouring_data_rec_data.user, 
                pouring_data_rec_data.reason, 
                pouring_data_rec_data.aperture_min, 
                pouring_data_rec_data.nr_pouring_mould, 
                pouring_data_rec_data.aperture_max, 
                pouring_data_rec_data.temperature, 
                pouring_data_rec_data.gr_inoculant, 
                model_id, 
                pouring_data_rec_data.model_description, 
                pouring_data_rec_data.level_final, 
                pouring_data_rec_data.pouring_mode, 
                pouring_data_rec_data.pouring_fault, 
                pouring_data_rec_data.model_weight, 
                pouring_data_rec_data.pouring_duration, 
                pouring_data_rec_data.gs_inoculant, 
                pouring_data_rec_data.inoculant_type, 
                pouring_data_rec_data.ticket_id, 
                pouring_data_rec_data.weight, 
                pouring_data_rec_data.elettrodo_level, 
                pouring_data_rec_data.pression, 
                pouring_data_rec_data.nr_medaglia, 
                pouring_data_rec_data.temperatura_manuale, 
                pouring_data_rec_data.staffa_scarta, 
                pouring_data_rec_data.inoculant_type_string)
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into pouring data rec table.")

        # Disconnecrt from database
        self.disconnect()   
    