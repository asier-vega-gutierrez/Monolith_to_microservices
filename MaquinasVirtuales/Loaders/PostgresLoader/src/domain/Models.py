class PouringArchiveModelsData():
    """ Domain class for manage Archive Modesls """
        
    def __init__(self,
                    id,
                    model_code, 
                    model_description, 
                    model_weight, 
                    inoculation_perc, 
                    inoculation_gs, 
                    material_type, 
                    inoculation_start, 
                    inoculation_stop, 
                    position_axe_x, 
                    position_axe_y, 
                    aperture_max, 
                    aperture_min, 
                    during_level, 
                    final_level, 
                    duration_final_control, 
                    pouring_duration, 
                    temperature_min, 
                    temperature_max) -> None:
        """ Deafult constructor of archive models object from domain """
        self.id = id
        self.model_code = model_code
        self.model_description = model_description 
        self.model_weight = model_weight
        self.inoculation_perc = inoculation_perc
        self.inoculation_gs = inoculation_gs
        self.material_type = material_type
        self.inoculation_start = inoculation_start
        self.inoculation_stop = inoculation_stop
        self.position_axe_x = position_axe_x
        self.position_axe_y = position_axe_y
        self.aperture_max = aperture_max
        self.aperture_min = aperture_min
        self.during_level = during_level
        self.final_level = final_level
        self.duration_final_control = duration_final_control 
        self.pouring_duration = pouring_duration
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max