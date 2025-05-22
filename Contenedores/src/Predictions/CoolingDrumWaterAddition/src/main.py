from fastapi import FastAPI
import uvicorn
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
@app.get("/calculate_water_adittion_liters/")
def api_calculate_single_tape_addition(f_avg: float, q_sand_avg: float, q_metal_avg: float):
    result = calculate_water_adittion_liters(f_avg, q_sand_avg, q_metal_avg)
    return {"result": result}


if __name__ == "__main__":
    main()

'''
#Para realizar llamadas desde la url
http://localhost:8080/calculate_water_adittion_liters/?f_avg=1.5&q_sand_avg=2.0&q_metal_avg=3.0
'''