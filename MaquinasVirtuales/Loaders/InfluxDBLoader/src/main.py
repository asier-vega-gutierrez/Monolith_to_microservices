from load.loaders.temporal_series.water_belts_prediction_ts import WaterBeltsPredictionTemporalSeriesWriter
from load.loaders.temporal_series.water_drum_prediction_ts import WaterDrumPredictionTemporalSeriesWriter
from load.loaders.temporal_series.sensor_data_ts import SensorDataTemporalSeriesWriter

from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Load Script")
    parser.add_argument("--start", action="store_true", help="Start process")

    args = parser.parse_args()

    water_belts_service_ts = WaterBeltsService_ts()
    water_drum_service_1_ts = WaterDrumService_ts(1)
    water_drum_service_2_ts = WaterDrumService_ts(2)
    sensor_data_service_1_ts = SensorDataService_ts(1)
    sensor_data_service_2_ts = SensorDataService_ts(2)

    if args.start:
        water_belts_service_ts.start_load_process()
        water_drum_service_1_ts.start_load_process()
        water_drum_service_2_ts.start_load_process()
        sensor_data_service_1_ts.start_load_process()
        sensor_data_service_2_ts.start_load_process()



class WaterBeltsService_ts():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._water_belts_loader_ts = WaterBeltsPredictionTemporalSeriesWriter()

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._water_belts_loader_ts.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._water_belts_loader_ts.stop_observe_and_load_data()


class WaterDrumService_ts():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self._water_drum_loader_ts = WaterDrumPredictionTemporalSeriesWriter(id)

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._water_drum_loader_ts.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._water_drum_loader_ts.stop_observe_and_load_data()

class SensorDataService_ts():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self._sensor_data_loader_ts = SensorDataTemporalSeriesWriter(id)

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._sensor_data_loader_ts.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._sensor_data_loader_ts.stop_observe_and_load_data()

if __name__ == "__main__":
    main()