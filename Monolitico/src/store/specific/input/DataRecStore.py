from store.base.MySqlStore import MySqlStore
from domain.DataRec import DataRec

class DataRecStore(MySqlStore):
    """ Specific store to manage the Data Rec Store """

    def __init__(self):
        """ Default constructor to create the specific store for Data Rec """
        super().__init__()
    
    def get_num_data_recs(self, num_data_rec):
        """ Method to get last data recs """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT TimeCol, \
                        MSecCol, \
                        LocalCol, \
                        UserCol, \
                        ReasonCol, \
                        aperture_min, \
                        nr_pouring_mould, \
                        aperture_max, \
                        temperature, \
                        gr_inoculant, \
                        model_code, \
                        model_description, \
                        level_final, \
                        pouring_mode, \
                        pouring_fault, \
                        model_weight, \
                        pouring_duration, \
                        gs_inoculant, \
                        inoculant_type, \
                        ticket_id, \
                        weight, \
                        elettrodo_level, \
                        pression, \
                        nr_medaglia, \
                        temperatura_manuale, \
                        staffa_scarta, \
                        inoculant_type_string \
                FROM pouring.data_rec \
                WHERE model_code IS NOT NULL \
                LIMIT {}".format(num_data_rec)


        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        data_rec_list = []

        results = cursor.fetchall()
        for row in results:
            current_data_rec = DataRec()

            current_data_rec.time = row[0]
            current_data_rec.m_sec = row[1]
            current_data_rec.local = row[2]
            current_data_rec.user = row[3]
            current_data_rec.reason = row[4]
            current_data_rec.aperture_min = row[5]
            current_data_rec.nr_pouring_mould = row[6]
            current_data_rec.aperture_max = row[7]
            current_data_rec.temperature = row[8]
            current_data_rec.gr_inoculant = row[9]
            current_data_rec.model_code = row[10]
            current_data_rec.model_description = row[11]
            current_data_rec.level_final = row[12]
            current_data_rec.pouring_mode = row[13]
            current_data_rec.pouring_fault = row[14]
            current_data_rec.model_weight = row[15]
            current_data_rec.pouring_duration = row[16]
            current_data_rec.gs_inoculant = row[17]
            current_data_rec.inoculant_type = row[18]
            current_data_rec.ticket_id = row[19]
            current_data_rec.weight = row[20]
            current_data_rec.elettrodo_level = row[21]
            current_data_rec.pression = row[22]
            current_data_rec.nr_medaglia = row[23]
            current_data_rec.temperatura_manuale = row[24]
            current_data_rec.staffa_scarta = row[25]
            current_data_rec.inoculant_type_string = row[26]

            data_rec_list.append(current_data_rec)

        # disconnect from server
        self.disconnect()

        return data_rec_list
    
    def get_data_recs(self):
        """ Method to get last data recs """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT TimeCol, \
                        MSecCol, \
                        LocalCol, \
                        UserCol, \
                        ReasonCol, \
                        aperture_min, \
                        nr_pouring_mould, \
                        aperture_max, \
                        temperature, \
                        gr_inoculant, \
                        model_code, \
                        model_description, \
                        level_final, \
                        pouring_mode, \
                        pouring_fault, \
                        model_weight, \
                        pouring_duration, \
                        gs_inoculant, \
                        inoculant_type, \
                        ticket_id, \
                        weight, \
                        elettrodo_level, \
                        pression, \
                        nr_medaglia, \
                        temperatura_manuale, \
                        staffa_scarta, \
                        inoculant_type_string \
                FROM pouring.data_rec \
                WHERE model_code IS NOT NULL "

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        data_rec_list = []

        results = cursor.fetchall()
        for row in results:
            current_data_rec = DataRec()

            current_data_rec.time = row[0]
            current_data_rec.m_sec = row[1]
            current_data_rec.local = row[2]
            current_data_rec.user = row[3]
            current_data_rec.reason = row[4]
            current_data_rec.aperture_min = row[5]
            current_data_rec.nr_pouring_mould = row[6]
            current_data_rec.aperture_max = row[7]
            current_data_rec.temperature = row[8]
            current_data_rec.gr_inoculant = row[9]
            current_data_rec.model_code = row[10]
            current_data_rec.model_description = row[11]
            current_data_rec.level_final = row[12]
            current_data_rec.pouring_mode = row[13]
            current_data_rec.pouring_fault = row[14]
            current_data_rec.model_weight = row[15]
            current_data_rec.pouring_duration = row[16]
            current_data_rec.gs_inoculant = row[17]
            current_data_rec.inoculant_type = row[18]
            current_data_rec.ticket_id = row[19]
            current_data_rec.weight = row[20]
            current_data_rec.elettrodo_level = row[21]
            current_data_rec.pression = row[22]
            current_data_rec.nr_medaglia = row[23]
            current_data_rec.temperatura_manuale = row[24]
            current_data_rec.staffa_scarta = row[25]
            current_data_rec.inoculant_type_string = row[26]

            data_rec_list.append(current_data_rec)

        # disconnect from server
        self.disconnect()

        return data_rec_list