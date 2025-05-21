
class MouldData():
    """ Domain class for manage the Mould object """

    def __init__(self):
        """ Default construtor of the class """

        self.id_molde = None 
        self.mould_index = None 
        self.mould_counter = None 
        self.setting_index = None 
        self.mould_thickness = None 
        self.compressibility = None 
        self.cycle_time = None 
        self.time_prod = None 
        self.time_pour = None 
        self.time_shake_out = None 
        self.mould_status = None 
        self.core_status = None 
        self.pour_status = None 
        self.id_parametros_molde = None 
        self.indice_calidad_dato = None 
        self.id_molinada = None 
        self.cod_maquina = None 
        self.cod_linea = None 
        self.cod_operario = None 
        self.cod_aplic_captura = None 
        self.fecha_insercion_reg = None 
        self.fecha_actualizacion_reg = None
        self.reference = None
    
#    def __init__(self,
#                id_molde, 
#                mould_index, 
#                mould_counter, 
#                setting_index, 
#                mould_thickness, 
#                compressibility, 
#                cycle_time, 
#                time_prod, 
#                time_pour, 
#                time_shake_out, 
#                mould_status, 
#                core_status, 
#                pour_status, 
#                id_parametros_molde, 
#                indice_calidad_dato, 
#                id_molinada, 
#                cod_maquina, 
#                cod_linea, 
#                cod_operario, 
#                cod_aplic_captura, 
#                fecha_insercion_reg, 
#                fecha_actualizacion_reg,
#                reference):
#        """ Construtor with parameters of the class """
#
#        self.id_molde = id_molde 
#        self.mould_index = mould_index 
#        self.mould_counter = mould_counter 
#        self.setting_index = setting_index 
#        self.mould_thickness = mould_thickness 
#        self.compressibility = compressibility
#        self.cycle_time = cycle_time
#        self.time_prod = time_prod
#        self.time_pour = time_pour
#        self.time_shake_out = time_shake_out 
#        self.mould_status = mould_status
#        self.core_status = core_status
#        self.pour_status = pour_status
#        self.id_parametros_molde = id_parametros_molde 
#        self.indice_calidad_dato = indice_calidad_dato
#        self.id_molinada = id_molinada
#        self.cod_maquina = cod_maquina
#        self.cod_linea = cod_linea
#        self.cod_operario = cod_operario
#        self.cod_aplic_captura = cod_aplic_captura
#        self.fecha_insercion_reg = fecha_insercion_reg
#        self.fecha_actualizacion_reg = fecha_actualizacion_reg
#        self.reference = reference