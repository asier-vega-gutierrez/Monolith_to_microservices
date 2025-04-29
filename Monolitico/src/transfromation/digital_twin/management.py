from transfromation.digital_twin.WaterAdditionTwin import WaterAdditionDigitalTwin

class DigitalTwinManagement():
    """ Class to manage all diferente digital twin working together  """

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
