from store.base.PostgresStore import  PostgresStore
from domain.Chemical import ChemicalComposition

class ChemicalCompositionStore(PostgresStore):
    """ Specific store to manage the Chemical Composition Store """

    def __init__(self):
        """ Default constructor """

        super().__init__()
    
    def add_chemical_composition(self, chemical_composition_data):
        """ Method to add a a chemical composition to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor() 

        # Define the SQL for insert data
        sql = """ INSERT INTO public.chemical_composition
                        (datetime, p, s, c, si, cu, cr, mg, mn, al, ce, sn, zn, mo, sb, w, ni, co, v, nb, ti, pb, bi, b, fe, zr)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """    
        
        data = (chemical_composition_data.date, 
                chemical_composition_data.p, 
                chemical_composition_data.s, 
                chemical_composition_data.c, 
                chemical_composition_data.si, 
                chemical_composition_data.cu, 
                chemical_composition_data.cr, 
                chemical_composition_data.mg, 
                chemical_composition_data.mn, 
                chemical_composition_data.al, 
                chemical_composition_data.ce, 
                chemical_composition_data.sn, 
                chemical_composition_data.zn, 
                chemical_composition_data.mo, 
                chemical_composition_data.sb, 
                chemical_composition_data.w, 
                chemical_composition_data.ni, 
                chemical_composition_data.co, 
                chemical_composition_data.v, 
                chemical_composition_data.nb, 
                chemical_composition_data.ti, 
                chemical_composition_data.pb, 
                chemical_composition_data.bi, 
                chemical_composition_data.b, 
                chemical_composition_data.fe, 
                chemical_composition_data.zr)
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into chemical composition table.")

        # Disconnecrt from database
        self.disconnect()
    
    def get_last_chemical_composition(self):
        """ Method to get the last chemical composition. Double return, Chemical Composition Data and ID """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = """SELECT 	id_chemical_composition, 
                            datetime, 
                            p, 
                            s, 
                            c, 
                            si, 
                            cu, 
                            cr, 
                            mg, 
                            mn, 
                            al, 
                            ce, 
                            sn, 
                            zn, 
                            mo, 
                            sb, 
                            w, 
                            ni, 
                            co, 
                            v, 
                            nb, 
                            ti, 
                            pb, 
                            bi, 
                            b, 
                            fe, 
                            zr
                    FROM public.chemical_composition
                    ORDER by datetime DESC;"""

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch just one element
        id_chemical_composition, datetime, p, s, c, si, cu, cr, mg, mn, al, ce, sn, zn, mo, sb, w, ni, co, v, nb, ti, pb, bi, b, fe, zr = cursor.fetchone()
        
        # create the object
        chemical_compositon_data = ChemicalComposition(
                id_chemical_composition, 
                datetime, 
                p, 
                s, 
                c, 
                si, 
                cu, 
                cr, 
                mg, 
                mn, 
                al, 
                ce, 
                sn, 
                zn, 
                mo, 
                sb, 
                w, 
                ni, 
                co, 
                v, 
                nb, 
                ti, 
                pb, 
                bi, 
                b, 
                fe, 
                zr)

        # disconnect from server
        self.disconnect()
        
        return chemical_compositon_data, id_chemical_composition