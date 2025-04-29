from store.base.MySqlStore import MySqlStore
from domain.Alarm import Alarm

class AlarmStore(MySqlStore):
    """ Specific store to manage the Alarm Store """

    def __init__(self):
        """ Default constructor of the Alarm Store """

        super().__init__()
    
    def get_num_alarms(self, num_alarms):
        """ Method to get last alarms """
        
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT   TimeCol, \
                        MSecCol, \
                        LocalCol, \
                        UserCol, \
                        EventCol, \
                        EvNumCol, \
                        EvDescCol, \
                        DescCol, \
                        CommCol, \
                        DurCol, \
                        UniID, \
                        TraID \
                FROM pouring.alarms \
                LIMIT {}".format(num_alarms)


        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        alarm_list = []

        results = cursor.fetchall()
        for row in results:
            current_alarm = Alarm(
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
                row[11]
            )

            alarm_list.append(current_alarm)

        # disconnect from server
        self.disconnect()

        return alarm_list

    def get_alarms(self):
        """ Method to get all alarms """
        # We make the connection
        self.connect()

        # Prepare a cursor object using cursor() method
        cursor = self._conn.cursor()

        # Prepare SQL query to READ a record into the database.
        sql = "SELECT   TimeCol, \
                        MSecCol, \
                        LocalCol, \
                        UserCol, \
                        EventCol, \
                        EvNumCol, \
                        EvDescCol, \
                        DescCol, \
                        CommCol, \
                        DurCol, \
                        UniID, \
                        TraID \
                FROM pouring.alarms"

        # Execute the SQL command
        cursor.execute(sql)

        # Fetch all the rows in a list of lists.
        alarm_list = []

        results = cursor.fetchall()
        for row in results:
            current_alarm = Alarm()

            current_alarm.time = row[0]
            current_alarm.m_sec = row[1]
            current_alarm.local = row[2]
            current_alarm.user = row[3]
            current_alarm.event = row[4]
            current_alarm.ev_num = row[5]
            current_alarm.ev_desc = row[6]
            current_alarm.desc = row[7]
            current_alarm.comm = row[8]
            current_alarm.dur = row[9]
            current_alarm.uni_id = row[10]
            current_alarm.tra_id = row[11]

            alarm_list.append(current_alarm)

        # disconnect from server
        self.disconnect()

        return alarm_list