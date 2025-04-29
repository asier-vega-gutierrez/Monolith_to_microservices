class PouringDataRecData():
    """ Class to represent the object DataRec from domain  """
   
    def __init__(self,
                    time,
                    m_sec,
                    local,
                    user,
                    reason,
                    aperture_min,
                    nr_pouring_mould,
                    aperture_max,
                    temperature,
                    gr_inoculant,
                    model_code,
                    model_description,
                    level_final,
                    pouring_mode,
                    pouring_fault,
                    model_weight,
                    pouring_duration,
                    gs_inoculant,
                    inoculant_type,
                    ticket_id,
                    weight,
                    elettrodo_level,
                    pression,
                    nr_medaglia,
                    temperatura_manuale,
                    staffa_scarta,
                    inoculant_type_string,
                    archive_model_data) -> None:
        """ Default constructor of the objct DataRec from the domain"""

        self.time = time
        self.m_sec = m_sec
        self.local = local
        self.user = user
        self.reason = reason
        self.aperture_min = aperture_min
        self.nr_pouring_mould = nr_pouring_mould
        self.aperture_max = aperture_max
        self.temperature = temperature
        self.gr_inoculant = gr_inoculant
        self.model_code = model_code
        self.model_description = model_description
        self.level_final = level_final
        self.pouring_mode = pouring_mode
        self.pouring_fault = pouring_fault
        self.model_weight = model_weight
        self.pouring_duration = pouring_duration
        self.gs_inoculant = gs_inoculant
        self.inoculant_type = inoculant_type
        self.ticket_id = ticket_id
        self.weight = weight
        self.elettrodo_level = elettrodo_level
        self.pression = pression
        self.nr_medaglia = nr_medaglia
        self.temperatura_manuale = temperatura_manuale
        self.staffa_scarta = staffa_scarta
        self.inoculant_type_string = inoculant_type_string

        self.archive_model_data = archive_model_data