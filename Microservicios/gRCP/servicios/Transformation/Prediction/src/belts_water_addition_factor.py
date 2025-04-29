import random

def calculate_single_tape_addition(
                                    q_sand_avg : float,
                                    temperature_avg : float
                                ):
    """ Procedure to calclate the single tape addition  """
    random_value = random.uniform(1.5, 4.5)
    return ( random_value * (00.65445 * q_sand_avg)) * (0.15 * temperature_avg)

def calculate_unified_belt_addition(
                                        q_sand_average : float, 
                                        temp_average : float, 
                                        humidity : float
                                ):
    """ Procedure to calculate the unified belt water addition factor """ 
    
    value = 0.0000673 * (q_sand_average ** 2) + 0.0069627 * temp_average + -0.1936083;
    
    # We adjust the value using the humidity
    if humidity < 1.7:
        corrected_value = value
    elif humidity >= 1.7 and humidity < 1.8:
        corrected_value = value - 0.03
    elif humidity >= 1.8 and humidity < 2:
        corrected_value = value - 0.06;
    else:
        corrected_value = value - 0.09;

    # We make some checks before using this information
    corrected_value = 0 if corrected_value < 0 else corrected_value
    corrected_value = 1 if corrected_value > 1 else corrected_value;

    return corrected_value;
    