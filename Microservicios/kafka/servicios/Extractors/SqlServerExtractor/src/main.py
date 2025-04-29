from extraction.extractors.mould_data import MouldDataExtractor
from extraction.extractors.sensor_data import SensorDataExtractor
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Extraction Script")
    parser.add_argument("--start", action="store_true", help="Start the extraction process")

    args = parser.parse_args()

    mould_data_extractor_1 = MouldDataExtractorService(1)
    mould_data_extractor_2 = MouldDataExtractorService(2)
    sensor_data_extractor = SensorDataExtractorService()

    if args.start:
        mould_data_extractor_1.start_extraction_process()
        mould_data_extractor_2.start_extraction_process()
        sensor_data_extractor.start_extraction_process()

class MouldDataExtractorService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self, id) -> None:
        """ Default contsructor creating all needed elements """

        self.mould_data_extractor = MouldDataExtractor(id)

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """
        
        self.mould_data_extractor.start_extract_and_inject_data()

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self.mould_data_extractor.stop_extract_and_inject_data()

class SensorDataExtractorService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self.pouring_data_extractor = SensorDataExtractor()

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """
        
        self.pouring_data_extractor.start_extract_and_inject_data()

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self.pouring_data_extractor.stop_extract_and_inject_data()


if __name__ == "__main__":
    main()