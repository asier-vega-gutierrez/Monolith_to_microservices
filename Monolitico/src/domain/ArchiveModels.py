class ArchiveModels():
    """ Domain class for manage Archive Modesls """

    def __init__(self) -> None:
        """ Deafult constructor of archive models object from domain """
        self.id = None
        self.model_code = None 
        self.model_description = None 
        self.model_weight = None 
        self.inoculation_perc = None 
        self.inoculation_gs = None 
        self.material_type = None 
        self.inoculation_start = None 
        self.inoculation_stop = None 
        self.position_axe_x = None 
        self.position_axe_y = None 
        self.aperture_max = None 
        self.aperture_min = None 
        self.during_level = None 
        self.final_level = None 
        self.duration_final_control = None 
        self.pouring_duration = None 
        self.temperature_min = None 
        self.temperature_max = None 