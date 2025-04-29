from extraction.chemical_composition import ChemicalCompositionExtractor
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Extraction Script")
    parser.add_argument("--start", action="store_true", help="Start the extraction process")

    args = parser.parse_args()

    chemical_composition_service = ChemicalCompositionExtractorService()

    if args.start:
        chemical_composition_service.start_extraction_process()


class ChemicalCompositionExtractorService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        self._chemical_composition_extractor = ChemicalCompositionExtractor()

    def start_extraction_process(self) -> None:
        """ Method to star the extraction process """
        
        self._chemical_composition_extractor.start_extract_and_inject_data()

    def stop_extraction_process(self) -> None:
        """ Method to stop the extraction process """

        self._chemical_composition_extractor.stop_extract_and_inject_data()


if __name__ == "__main__":
    main()