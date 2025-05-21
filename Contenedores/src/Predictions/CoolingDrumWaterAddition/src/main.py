from fastapi import FastAPI

app = FastAPI()

@app.get("/cooling-drum-water-prediction")
def calculate_water_adittion_liters(
                                    f_avg : float,
                                    q_sand_avg : float,
                                    q_metal_avg : float
                                ):

    previous_value_1 = 3.75 * q_sand_avg
    previous_value_2 = (0.41666667 * q_sand_avg) + 6.66666667
    previous_value_3 = (-0.625 * q_sand_avg) + 15
    
    principal_equation = ((11.75847 * q_metal_avg) + (0.1734216 * q_sand_avg) - 6.843978);
            
    if q_sand_avg >= 8 and principal_equation < previous_value_3:
        return f_avg * previous_value_3
    elif q_sand_avg >= 2 and q_sand_avg < 8 and principal_equation < previous_value_2:
        return f_avg * previous_value_2
    elif q_sand_avg < 2 and principal_equation < previous_value_1:
        return f_avg * previous_value_1;
    else:
        return f_avg * principal_equation * 1.05;
