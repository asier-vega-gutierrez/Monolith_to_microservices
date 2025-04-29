from transformation.WaterAdditionTwin import WaterAdditionDigitalTwin
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Transformation Script")
    parser.add_argument("--start", action="store_true", help="Start process")

    args = parser.parse_args()

    digital_twin_service = DigitalTwinManagementService()

    if args.start:
        digital_twin_service.start_digital_twin_processing()

class DigitalTwinManagementService():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self):
        """ Constructor of the class """

        # We create the different digital twins
        self._l1_cooling_drum_digital_twin = WaterAdditionDigitalTwin(
            "DRUM",
            1,
            20,
            7
        )

        self._l2_cooling_drum_digital_twin = WaterAdditionDigitalTwin(
            "DRUM",
            2,
            30,
            10
        )

        self._tapes_digital_twin = WaterAdditionDigitalTwin(
            "TAPES",
            1,
            30,
            15
        )

    def start_digital_twin_processing(self):
        """ Method to start all elements of the digital twin ecosystem """

        self._l1_cooling_drum_digital_twin.start_digital_twin_processing()
        self._l2_cooling_drum_digital_twin.start_digital_twin_processing()
        self._tapes_digital_twin.start_digital_twin_processing()

    def stop_digital_twin_processing(self): 
        """ Method to stop all elements of the digital twin ecosystem """

        self._l1_cooling_drum_digital_twin.stop_digital_twin_processing()
        self._l2_cooling_drum_digital_twin.stop_digital_twin_processing()
        self._tapes_digital_twin.stop_digital_twin_processing()

if __name__ == "__main__":
    main()