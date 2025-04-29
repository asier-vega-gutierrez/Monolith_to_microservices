from load.loaders.relational.mould import MouldDataWriter
from load.loaders.relational.chemical_composition import ChemicalCompositionDataWriter
from load.loaders.relational.pouring_alarm import PouringAlarmDataWriter
from load.loaders.relational.pouring import PouringDataRecWriter
from load.loaders.relational.sensor_data import SensorDataWriter
from load.loaders.relational.water_belts_prediction import WaterBeltsDataPredictionWriter
from load.loaders.relational.water_drum_prediction import WaterDrumDataPredictionWriter
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Load Script")
    parser.add_argument("--start", action="store_true", help="Start process")

    args = parser.parse_args()

    chemical_composition_service = ChemicalCompositionService()
    mould_service_1 = MouldLoaderService(1)
    mould_service_2 = MouldLoaderService(2)
    pouring_alarm_service = PouringAlarmService()
    pouring_data_service = PouringDataService()
    sensor_data_service_1 = SensorDataService(1)
    sensor_data_service_2 = SensorDataService(2)
    water_belts_service = WaterBeltsService()
    water_drum_service_1= WaterDrumService(1)
    water_drum_service_2 = WaterDrumService(2)

    if args.start:
        chemical_composition_service.start_load_process()
        mould_service_1.start_load_process()
        mould_service_2.start_load_process()
        pouring_alarm_service.start_load_process()
        pouring_data_service.start_load_process()
        sensor_data_service_1.start_load_process()
        sensor_data_service_2.start_load_process()
        water_belts_service.start_load_process()
        water_drum_service_1.start_load_process()
        water_drum_service_2.start_load_process()


class ChemicalCompositionService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._chemical_composition_loader = ChemicalCompositionDataWriter()

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._chemical_composition_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._chemical_composition_loader.stop_observe_and_load_data()

class MouldLoaderService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self._mould_loader = MouldDataWriter(id)

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._mould_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._mould_loader.stop_observe_and_load_data()

class PouringAlarmService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._pouring_alarm_loader = PouringAlarmDataWriter()

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._pouring_alarm_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._pouring_alarm_loader.stop_observe_and_load_data()

class PouringDataService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._pouring_dataRec_loader = PouringDataRecWriter()

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._pouring_dataRec_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._pouring_dataRec_loader.stop_observe_and_load_data()

class SensorDataService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self._sensor_loader = SensorDataWriter(id)

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._sensor_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._sensor_loader.stop_observe_and_load_data()

class WaterBeltsService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._water_belts_loader = WaterBeltsDataPredictionWriter()

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._water_belts_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._water_belts_loader.stop_observe_and_load_data()
    
class WaterDrumService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self._water_drum_loader = WaterDrumDataPredictionWriter(id)

    def start_load_process(self) -> None:
        """ Method to star the extraction process """
        
        self._water_drum_loader.start_observe_and_load_data()

    def stop_load_process(self) -> None:
        """ Method to stop the extraction process """

        self._water_drum_loader.stop_observe_and_load_data()


if __name__ == "__main__":
    main()