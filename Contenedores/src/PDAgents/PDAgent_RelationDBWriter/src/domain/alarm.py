
class PouringAlarmData():
    """ Domain class for manage the Alarm object """
    
    def __init__(self,
                    time,
                    m_sec,
                    local,
                    user,
                    event,
                    ev_num,
                    ev_desc,
                    desc,
                    comm,
                    dur,
                    uni_id,
                    tra_id):
        """ Constructor with parameters of the lass """
        self.time = time
        self.m_sec = m_sec
        self.local = local
        self.user = user
        self.event = event
        self.ev_num = ev_num
        self.ev_desc = ev_desc
        self.desc = desc
        self.comm = comm
        self.dur = dur
        self.uni_id = uni_id
        self.tra_id = tra_id

