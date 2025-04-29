from extraction.pouring_alarm import PouringAlarmExtractor
from extraction.pouring_data import PouringDataExtractor
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Extraction Script")
    parser.add_argument("--start", action="store_true", help="Start the extraction process")

    args = parser.parse_args()

    pouring_alarm_extractor = PouringAlarmExtractorService()
    pouring_data_extractor = PouringDataExtractorService()

    if args.start:
        pouring_alarm_extractor.start_extraction_process()
        pouring_data_extractor.start_extraction_process()

class PouringAlarmExtractorService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self.pouring_alarm_extractor = PouringAlarmExtractor()

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """
        
        self.pouring_alarm_extractor.start_extract_and_inject_data()

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self.pouring_alarm_extractor.stop_extract_and_inject_data()

class PouringDataExtractorService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self.pouring_data_extractor = PouringDataExtractor()

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """
        
        self.pouring_data_extractor.start_extract_and_inject_data()

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self.pouring_data_extractor.stop_extract_and_inject_data()

if __name__ == "__main__":
    main()