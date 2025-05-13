from fastapi import FastAPI
import uvicorn
from belts_water_addition_factor import calculate_single_tape_addition, calculate_unified_belt_addition
from cooling_drum_water_addition import calculate_water_adittion_liters
import logging
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Api Script")
    parser.add_argument("--start", action="store_true", help="Start process")

    args = parser.parse_args()

    if args.start:
        #Ejecuta uvicor al iniciar 
        uvicorn.run("main:app", host="0.0.0.0", port=80, reload=False)

app = FastAPI()

#Metodo get para cada una de las tres unidades de calculo
@app.get("/calculate_single_tape_addition/")
def api_calculate_single_tape_addition(q_sand_avg: float, temperature_avg: float):
    result = calculate_single_tape_addition(q_sand_avg, temperature_avg)
    return {"result": result}

#Metodo get para cada una de las tres unidades de calculo
@app.get("/calculate_unified_belt_addition/")
def api_calculate_unified_belt_addition(q_sand_average: float, temp_average: float, humidity: float):
    result = calculate_unified_belt_addition(q_sand_average, temp_average, humidity)
    return {"result": result}

#Metodo get para cada una de las tres unidades de calculo
@app.get("/calculate_water_adittion_liters/")
def api_calculate_single_tape_addition(f_avg: float, q_sand_avg: float, q_metal_avg: float):
    result = calculate_water_adittion_liters(f_avg, q_sand_avg, q_metal_avg)
    return {"result": result}


if __name__ == "__main__":
    main()

'''
#Para realizar llamadas desde la url
http://127.0.0.1:80/calculate_single_tape_addition/?q_sand_avg=VALOR1&temperature_avg=VALOR2
http://127.0.0.1:80/calculate_unified_belt_addition/?q_sand_average=VALOR1&temp_average=VALOR2&humidity=VALOR3
http://localhost:80/calculate_water_adittion_liters/?f_avg=VALOR1&q_sand_avg=VALOR2&q_metal_avg=VALOR3

http://127.0.0.1:80/calculate_single_tape_addition/?q_sand_avg=10&temperature_avg=10
http://127.0.0.1:80/calculate_unified_belt_addition/?q_sand_average=10&temp_average=10&humidity=10
http://localhost:80/calculate_water_adittion_liters/?f_avg=1.5&q_sand_avg=2.0&q_metal_avg=3.0
'''