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
            current_mould = MouldData(
                row[0], 
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10], 
                row[11], 
                row[12], 
                row[13], 
                row[14], 
                row[15], 
                row[16], 
                row[17], 
                row[18], 
                row[19], 
                row[20], 
                row[21],
                row[22]
            )
            
            mould_list.append(current_mould)

        # disconnect from server
        self.disconnect()

        return mould_list

    