from store.base.PostgresStore import PostgresStore
from domain.Alarm import Alarm

class PouringAlarmStore(PostgresStore):
    """ Specific store to manage the Pouring Alarmn Store """

    def __init__(self):
        """ Default constructor """

        super().__init__()
                
    def add_alarm(self, pouring_alarm_data, pouring_data_rec_id):
        """ Method to add a pouring alarm to the Postgres """
         
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Define the SQL for insert data
        sql = """ INSERT INTO public.pouring_alarm
                    ("time", m_sec, "local", "user", "event", ev_num, ev_desc, "desc", comm, dur, uni_id, tra_id, id_pouring_data_rec)
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """    
        
        data = (pouring_alarm_data.time,
                pouring_alarm_data.m_sec,
                pouring_alarm_data.local,
                pouring_alarm_data.user,
                pouring_alarm_data.event,
                pouring_alarm_data.ev_num,
                pouring_alarm_data.ev_desc,
                pouring_alarm_data.desc,
                pouring_alarm_data.comm,
                pouring_alarm_data.dur,
                pouring_alarm_data.uni_id,
                pouring_alarm_data.tra_id,
                pouring_data_rec_id)
        
        # We execute the query
        cursor.execute(sql, data)

        # Commit trasaction
        self.commit()

        # Get row count 
        count = cursor.rowcount
        print(count, "Record inserted successfully into pouring alarm table.")

        # Disconnecrt from database
        self.disconnect()   

    