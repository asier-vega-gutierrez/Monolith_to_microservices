
class MouldData():
    """ Domain class for manage the Mould object """
        
    def __init__(self,
                id_molde, 
                mould_index, 
                mould_counter, 
                setting_index, 
                mould_thickness, 
                compressibility, 
                cycle_time, 
                time_prod, 
                time_pour, 
                time_shake_out, 
                mould_status, 
                core_status, 
                pour_status, 
                id_parametros_molde, 
                indice_calidad_dato, 
                id_molinada, 
                cod_maquina, 
                cod_linea, 
                cod_operario, 
                cod_aplic_captura, 
                fecha_insercion_reg, 
                fecha_actualizacion_reg,
                reference):
        """ Construtor with parameters of the class """

        self.id_molde = id_molde 
        self.mould_index = mould_index 
        self.mould_counter = mould_counter 
        self.setting_index = setting_index 
        self.mould_thickness = mould_thickness 
        self.compressibility = compressibility
        self.cycle_time = cycle_time
        self.time_prod = time_prod
        self.time_pour = time_pour
        self.time_shake_out = time_shake_out 
        self.mould_status = mould_status
        self.core_status = core_status
        self.pour_status = pour_status
        self.id_parametros_molde = id_parametros_molde 
        self.indice_calidad_dato = indice_calidad_dato
        self.id_molinada = id_molinada
        self.cod_maquina = cod_maquina
        self.cod_linea = cod_linea
        self.cod_operario = cod_operario
        self.cod_aplic_captura = cod_aplic_captura
        self.fecha_insercion_reg = fecha_insercion_reg
        self.fecha_actualizacion_reg = fecha_actualizacion_reg
        self.reference = reference