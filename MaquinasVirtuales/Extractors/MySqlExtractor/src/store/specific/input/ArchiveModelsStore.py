from store.base.MySqlStore import MySqlStore
from domain.ArchiveModels import ArchiveModels

class ArchiveModelStore(MySqlStore):
    """ Specific store to manage the Archive ModelS tore """

    def __init__(self):
        """ Default constructor to create the specific store for Data Rec """
        super().__init__()

    def get_archive_model_by_code(self, model_code):
        """ Methods to get an specific archiv model """
        pass

    def get_num_archive_models(self, num_archive_models):
        """ Method to get the limited list of arhive models"""
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT id, \
                        model_code, \
                        model_description, \
                        model_weight, \
                        inoculation_perc, \
                        inoculation_gs, \
                        material_type, \
                        inoculation_start, \
                        inoculation_stop, \
                        position_axe_x, \
                        position_axe_y, \
                        aperture_max, \
                        aperture_min, \
                        during_level, \
                        final_level, \
                        duration_final_control, \
                        pouring_duration, \
                        temperature_min, \
                        temperature_max \
                FROM pouring.archive_models; \
                LIMIT {}".format( num_archive_models)

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        alarm_list = []

        results = cursor.fetchall()
        for row in results:
            current_archive_model = ArchiveModels()

            current_archive_model.id = row[0]
            current_archive_model.model_code = row[1]
            current_archive_model.model_description = row[2]
            current_archive_model.model_weight = row[3]
            current_archive_model.inoculation_perc = row[4]
            current_archive_model.inoculation_gs = row[5]
            current_archive_model.material_type = row[6]
            current_archive_model.inoculation_start = row[7]
            current_archive_model.inoculation_stop = row[8]
            current_archive_model.position_axe_x = row[9]
            current_archive_model.position_axe_y = row[10]
            current_archive_model.aperture_max = row[11]
            current_archive_model.aperture_min = row[12]
            current_archive_model.during_level = row[13]
            current_archive_model.final_level = row[14]
            current_archive_model.duration_final_control = row[15]
            current_archive_model.pouring_duration = row[16]
            current_archive_model.temperature_min = row[17]
            current_archive_model.temperature_max = row[18]

            alarm_list.append(current_archive_model)

        # disconnect from server
        self.disconnect()

        return alarm_list
    
    def get_archive_models(self):
        """ Method to get the full list of arhive models"""
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT id, \
                        model_code, \
                        model_description, \
                        model_weight, \
                        inoculation_perc, \
                        inoculation_gs, \
                        material_type, \
                        inoculation_start, \
                        inoculation_stop, \
                        position_axe_x, \
                        position_axe_y, \
                        aperture_max, \
                        aperture_min, \
                        during_level, \
                        final_level, \
                        duration_final_control, \
                        pouring_duration, \
                        temperature_min, \
                        temperature_max \
                FROM pouring.archive_models; "

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        alarm_list = []

        results = cursor.fetchall()
        for row in results:
            current_archive_model = ArchiveModels()

            current_archive_model.id = row[0]
            current_archive_model.model_code = row[1]
            current_archive_model.model_description = row[2]
            current_archive_model.model_weight = row[3]
            current_archive_model.inoculation_perc = row[4]
            current_archive_model.inoculation_gs = row[5]
            current_archive_model.material_type = row[6]
            current_archive_model.inoculation_start = row[7]
            current_archive_model.inoculation_stop = row[8]
            current_archive_model.position_axe_x = row[9]
            current_archive_model.position_axe_y = row[10]
            current_archive_model.aperture_max = row[11]
            current_archive_model.aperture_min = row[12]
            current_archive_model.during_level = row[13]
            current_archive_model.final_level = row[14]
            current_archive_model.duration_final_control = row[15]
            current_archive_model.pouring_duration = row[16]
            current_archive_model.temperature_min = row[17]
            current_archive_model.temperature_max = row[18]

            alarm_list.append(current_archive_model)

        # disconnect from server
        self.disconnect()

        return alarm_list
    
    def get_archive_model_by_code(self, model_code):
        """ Method to get an arhive model by code """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT id, \
                        model_code, \
                        model_description, \
                        model_weight, \
                        inoculation_perc, \
                        inoculation_gs, \
                        material_type, \
                        inoculation_start, \
                        inoculation_stop, \
                        position_axe_x, \
                        position_axe_y, \
                        aperture_max, \
                        aperture_min, \
                        during_level, \
                        final_level, \
                        duration_final_control, \
                        pouring_duration, \
                        temperature_min, \
                        temperature_max \
                FROM pouring.archive_models \
                WHERE model_code = {}; ".format(str(model_code))

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        

        results = cursor.fetchall()
        row = results[0]
        current_archive_model = ArchiveModels()

        current_archive_model.id = row[0]
        current_archive_model.model_code = row[1]
        current_archive_model.model_description = row[2]
        current_archive_model.model_weight = row[3]
        current_archive_model.inoculation_perc = row[4]
        current_archive_model.inoculation_gs = row[5]
        current_archive_model.material_type = row[6]
        current_archive_model.inoculation_start = row[7]
        current_archive_model.inoculation_stop = row[8]
        current_archive_model.position_axe_x = row[9]
        current_archive_model.position_axe_y = row[10]
        current_archive_model.aperture_max = row[11]
        current_archive_model.aperture_min = row[12]
        current_archive_model.during_level = row[13]
        current_archive_model.final_level = row[14]
        current_archive_model.duration_final_control = row[15]
        current_archive_model.pouring_duration = row[16]
        current_archive_model.temperature_min = row[17]
        current_archive_model.temperature_max = row[18]

        # disconnect from server
        self.disconnect()

        return current_archive_model


   