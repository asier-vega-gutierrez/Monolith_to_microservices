import httpx


q_sand_avg = 10.0 
temperature_avg = 25.0 
humidity = 1.8 

url_single_tape = f"http://127.0.0.1:80/calculate_single_tape_addition/?q_sand_avg={q_sand_avg}&temperature_avg={temperature_avg}"
response_single_tape = httpx.get(url_single_tape)


if response_single_tape.status_code == 200:
    result_single_tape = response_single_tape.json()["result"]
    print("Result from calculate_single_tape_addition:", result_single_tape)
else:
    print("Error:", response_single_tape.status_code, response_single_tape.text)


url_unified_belt = f"http://127.0.0.1:80/calculate_unified_belt_addition/?q_sand_average={q_sand_avg}&temp_average={temperature_avg}&humidity={humidity}"
response_unified_belt = httpx.get(url_unified_belt)

if response_unified_belt.status_code == 200:
    result_unified_belt = response_unified_belt.json()["result"]
    print("Result from calculate_unified_belt_addition:", result_unified_belt)
else:
    print("Error:", response_unified_belt.status_code, response_unified_belt.text)

f_avg = 10.0 
q_sand_avg = 25.0 
q_metal_avg = 1.8 

url_unified_belt = f"http://127.0.0.1:80/calculate_water_adittion_liters/?f_avg={f_avg}&q_sand_avg={q_sand_avg}&q_metal_avg={q_metal_avg}"
response_unified_belt = httpx.get(url_unified_belt)

if response_unified_belt.status_code == 200:
    result_unified_belt = response_unified_belt.json()["result"]
    print("Result from calculate_water_adittion_liters:", result_unified_belt)
else:
    print("Error:", response_unified_belt.status_code, response_unified_belt.text)