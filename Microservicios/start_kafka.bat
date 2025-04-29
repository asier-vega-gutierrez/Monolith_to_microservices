@echo off

echo Activating Conda environment
call C:/Users/asier/miniconda3/Scripts/activate cloud
REM call C:/ProgramData/Anaconda3/Scripts/activate cloudproyecto
if %errorlevel% neq 0 (
    echo Failed to activate Conda environment.
    exit /b %errorlevel%
) else (
    echo Conda environment activated successfully.
)

echo Changing directory to Microservicios
cd "C:\ASIER\00-Cloud\Arquitecturas\Microservicios"

echo ---

echo Starting ChemicalCompositionExtractor
start /B "ChemicalCompositionExtractor" python "kafka\servicios\Extractors\ChemicalCompositionExtractor\src\main.py" --start > logs/launch/launch_ChemicalCompositionExtractor.txt 2>&1
echo ChemicalCompositionExtractor executed successfully

echo Starting SqlServerExtractor
start /B "SqlServerExtractor" python "kafka\servicios\Extractors\SqlServerExtractor\src\main.py" --start > logs/launch/launch_SqlServerExtractor.txt 2>&1
echo SqlServerExtractor executed successfully

echo Starting MySqlExtractor
start /B "MySqlExtractor" python "kafka\servicios\Extractors\MySqlExtractor\src\main.py" --start > logs/launch/launch_MySqlExtractor.txt 2>&1
echo MySqlExtractor executed successfully

echo ---

echo Starting InfluxDBLoader
start /B "InfluxDBLoader" python "kafka\servicios\Loaders\InfluxDBLoader\src\main.py" --start > logs/launch/launch_InfluxDBLoader.txt 2>&1
echo InfluxDBLoader executed successfully

echo Starting PostgresLoader
start /B "PostgresLoader" python "kafka\servicios\Loaders\PostgresLoader\src\main.py" --start > logs/launch/launch_PostgresLoader.txt 2>&1
echo PostgresLoader executed successfully

echo ---

echo Starting DigitalTwin
start /B "DigitalTwin" python "kafka\servicios\Transformation\DigitalTwin\src\main.py" --start > logs/launch/launch_DigitalTwin.txt 2>&1
echo DigitalTwin executed successfully
echo All scripts launched.

echo Starting Prediction
start /B "Prediction" python "kafka\servicios\Transformation\Prediction\src\main.py" --start > logs/launch/launch_Prediction.txt 2>&1
echo Prediction executed successfully

echo ---