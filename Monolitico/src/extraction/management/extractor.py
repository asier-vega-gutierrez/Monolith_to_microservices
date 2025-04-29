from extraction.extractors.chemical_composition import ChemicalCompositionExtractor
from extraction.extractors.mould_data import MouldDataExtractor
from extraction.extractors.pouring_data import PouringDataExtractor
from extraction.extractors.pouring_alarm import PouringAlarmExtractor
from extraction.extractors.sensor_data import SensorDataExtractor

class DataExtractorManager():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._chemical_composition_extractor = ChemicalCompositionExtractor()
        self._mould_data_extractor_line_1 = MouldDataExtractor(1)
        self._mould_data_extractor_line_2 = MouldDataExtractor(2)
        self._pouring_alarm_extractor = PouringAlarmExtractor()
        self._pouring_data_extrator = PouringDataExtractor()
        self._sensor_data_extractor = SensorDataExtractor()

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """

        self._chemical_composition_extractor.start_extract_and_inject_data() #Hecho
        self._mould_data_extractor_line_1.start_extract_and_inject_data() #Hecho
        self._mould_data_extractor_line_2.start_extract_and_inject_data() #Hecho
        self._pouring_alarm_extractor.start_extract_and_inject_data() #Hecho
        self._pouring_data_extrator.start_extract_and_inject_data() #Hecho
        self._sensor_data_extractor.start_extract_and_inject_data() #Hecho

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self._chemical_composition_extractor.stop_extract_and_inject_data()
        self._mould_data_extractor_line_1.stop_extract_and_inject_data()
        self._mould_data_extractor_line_2.stop_extract_and_inject_data()
        self._pouring_alarm_extractor.stop_extract_and_inject_data()
        self._pouring_data_extrator.stop_extract_and_inject_data()
        self._sensor_data_extractor.stop_extract_and_inject_data()