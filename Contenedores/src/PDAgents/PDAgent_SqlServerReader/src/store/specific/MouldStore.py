from store.base.SqlServerStore import SqlServerStore
from domain.Mould import MouldData

class MouldStore(SqlServerStore):
    """ Specific store to manage the Mould Store """

    def __init__(self, dbname):
        """ Default constructor of the Mould Store """

        super().__init__(dbname)
    
    def get_line_mould(self, line):
        """ Method to get line moulds """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT A.IdMolde,  \
                A.MouldIndex, \
                A.MouldCounter, \
                A.SettingIndex, \
                A.MouldThickness, \
                A.Compressibility, \
                A.CycleTime, \
                A.TimeProd, \
                A.TimePour, \
                A.TimeShakeOut, \
                A.MouldStatus, \
                A.CoreStatus, \
                A.PourStatus, \
                A.IdParametrosMolde, \
                A.IndiceCalidadDato,  \
                A.IdMolinada, \
                A.CodMaquina, \
                A.CodLinea, \
                A.CodOperario, \
                A.CodAplicCaptura, \
                A.FechaInsercionReg, \
                A.FechaActualizacionReg, \
                B.NumeroReferencia  \
                FROM [DB-MOULDING].dbo.MOLDE as A INNER JOIN [DB-MOULDING].dbo.MOTA as B ON A.IdMolde = B.IdMoldePP  \
                WHERE A.CodLinea = {};".format(line)

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        mould_list = []

        results = cursor.fetchall()
        for row in results:
            current_mould = MouldData()

            current_mould.id_molde = row[0] 
            current_mould.mould_index = row[1] 
            current_mould.mould_counter = row[2] 
            current_mould.setting_index = row[3] 
            current_mould.mould_thickness = row[4] 
            current_mould.compressibility = row[5] 
            current_mould.cycle_time = row[6] 
            current_mould.time_prod = row[7] 
            current_mould.time_pour = row[8] 
            current_mould.time_shake_out = row[9] 
            current_mould.mould_status = row[10] 
            current_mould.core_status = row[11] 
            current_mould.pour_status = row[12] 
            current_mould.id_parametros_molde = row[13] 
            current_mould.indice_calidad_dato = row[14] 
            current_mould.id_molinada = row[15] 
            current_mould.cod_maquina = row[16] 
            current_mould.cod_linea = row[17] 
            current_mould.cod_operario = row[18] 
            current_mould.cod_aplic_captura = row[19] 
            current_mould.fecha_insercion_reg = row[20] 
            current_mould.fecha_actualizacion_reg = row[21]
            current_mould.reference = row[22]

            mould_list.append(current_mould)

        # disconnect from server
        self.disconnect()

        return mould_list

    