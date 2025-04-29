@echo off

echo ---

echo Finding the Process ID (PID) of ChemicalCompositionExtractor:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%ChemicalCompositionExtractor%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping ChemicalCompositionExtractor (PID: %PID%):
taskkill /F /PID %PID%
echo ChemicalCompositionExtractor stopped successfully.


echo Finding the Process ID (PID) of SqlServerExtractor:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%SqlServerExtractor%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping SqlServerExtractor (PID: %PID%):
taskkill /F /PID %PID%
echo SqlServerExtractor stopped successfully.


echo Finding the Process ID (PID) of MySqlExtractor:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%MySqlExtractor%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping MySqlExtractor (PID: %PID%):
taskkill /F /PID %PID%
echo MySqlExtractor stopped successfully.

echo ---

echo Finding the Process ID (PID) of InfluxDBLoader:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%InfluxDBLoader%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping InfluxDBLoader (PID: %PID%):
taskkill /F /PID %PID%
echo InfluxDBLoader stopped successfully.


echo Finding the Process ID (PID) of PostgresLoader:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%PostgresLoader%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping PostgresLoader (PID: %PID%):
taskkill /F /PID %PID%
echo PostgresLoader stopped successfully.

echo ---

echo Finding the Process ID (PID) of DigitalTwin:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%DigitalTwin%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping DigitalTwin (PID: %PID%):
taskkill /F /PID %PID%
echo DigitalTwin stopped successfully.

echo Finding the Process ID (PID) of Prediction:
for /f "tokens=2 delims=," %%a in ('wmic process where "CommandLine like '%%Prediction%%' and Name='python.exe'" get ProcessId /format:csv') do set "PID=%%~a"

if not defined PID (
    echo Process not found.
    exit /b
)

echo Found PID: %PID%

echo Stopping Prediction (PID: %PID%):
taskkill /F /PID %PID%
echo Prediction stopped successfully.

echo ---


