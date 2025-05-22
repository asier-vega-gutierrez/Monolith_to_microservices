from datetime import datetime
import math

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
        
    def f_factor(self):
        """ Method to calculate f factor """
        datetime_shakeout = datetime.strptime(self.time_shake_out, '%Y-%m-%d %H:%M:%S.%f')
        datetime_prod = datetime.strptime(self.time_prod, '%Y-%m-%d %H:%M:%S.%f')        
        minutes = (datetime_shakeout - datetime_prod).total_seconds() / 60.0

        if minutes < 60:
            return 1;
        else:
            value = -0.355 * math.log(minutes) + 2.4713;
            if value > 1:
                return 1;
            else:
                return 0 if value < 0 else value
    
    def q_sand(self):
        """ Method to calculate q_sand """

        if self.pour_status == 0:
            return 0

        return self._sand_weigth() / 7 # Divided by cicle time (simulated in 7 seconds)
    
    def q_metal(self):
        """ Method to calculate q_metal """

        weight = self._metal_weigth()

        if self.pour_status == 0:
            return 0
        
        return weight / 7 # Divided by cicle time (simulated in 7 seconds)
    
    def _metal_weigth(self):
        """ Return the metal weigth """

        # Manusally set due to there is no 
        if self.reference == 3650:
            return 20.4
        elif self.reference == 3793:
            return 23.45
        elif self.reference == 1200:
            return 21.14
        elif self.reference == 6516:
            return 19.89
        elif self.reference == 981:
            return 22.4
        elif self.reference == 2292:
            return 18.90
        elif self.reference == 6552:
            return 24
        elif self.reference == 9692:
            return 22.2
    
    def _sand_weigth(self):
        """ Return the metal weigth """

        # Manusally set due to there is no 
        x = 65
        y = 53
        density = 1.6

        return (x * y * (self.mould_thickness / 10) * density) / 1000; # Getting the value as KG.
        return 0