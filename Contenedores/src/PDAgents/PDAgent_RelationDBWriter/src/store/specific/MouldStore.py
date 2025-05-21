from store.base.PostgresStore import  PostgresStore
from domain.addition import WaterAdditionData

class MouldStore(PostgresStore):
    """ Specific store to manage the Mould Store """

    def __init__(self):
        """ Default constructor """

        super().__init__()
    
    def add_mould_data(self, mould_data, chemical_composition_id, pouring_id):
        """ Method to add a Prediction to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ INSERT INTO public.mould
                    (mould_index, mould_counter, setting_index, mould_thickness, compressibility, cycle_time, time_prod, time_pour, time_shake_out, mould_status, core_status, pour_status, id_parametros_molde, indice_calidad_dato, id_molinada, cod_maquina, cod_linea, cod_operario, cod_aplic_captura, fecha_insercion_reg, fecha_actualizacion_reg, reference, id_chemical_composition, id_pouring_data_rec)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """    
        
        data = (mould_data.mould_index, 
                mould_data.mould_counter, 
                mould_data.setting_index, 
                mould_data.mould_thickness, 
                mould_data.compressibility, 
                mould_data.cycle_time, 
                mould_data.time_prod, 
                mould_data.time_pour, 
                mould_data.time_shake_out, 
                mould_data.mould_status, 
                mould_data.core_status, 
                mould_data.pour_status, 
                mould_data.id_parametros_molde, 
                mould_data.indice_calidad_dato, 
                mould_data.id_molinada, 
                mould_data.cod_maquina, 
                mould_data.cod_linea, 
                mould_data.cod_operario, 
                mould_data.cod_aplic_captura, 
                mould_data.fecha_insercion_reg, 
                mould_data.fecha_actualizacion_reg,
                mould_data.reference,
                chemical_composition_id,
                pouring_id)
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into mould table.")

        # Disconnecrt from database
        self.disconnect()   
    