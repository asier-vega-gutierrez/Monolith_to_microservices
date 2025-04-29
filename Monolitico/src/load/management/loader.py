from load.loaders.temporal_series.water_belts_prediction_ts import WaterBeltsPredictionTemporalSeriesWriter
from load.loaders.temporal_series.water_drum_prediction_ts import WaterDrumPredictionTemporalSeriesWriter
from load.loaders.temporal_series.sensor_data_ts import SensorDataTemporalSeriesWriter

from load.loaders.relational.chemical_composition import ChemicalCompositionDataWriter
from load.loaders.relational.mould import MouldDataWriter
from load.loaders.relational.pouring_alarm import PouringAlarmDataWriter
from load.loaders.relational.pouring import PouringDataRecWriter
from load.loaders.relational.sensor_data import SensorDataWriter
from load.loaders.relational.water_belts_prediction import WaterBeltsDataPredictionWriter
from load.loaders.relational.water_drum_prediction import WaterDrumDataPredictionWriter

class DataLoaderManager():
    """ Class focused on management of data extractor for the whole system """

    def __init__(self) -> None:
        """ Default contsructor creating all needed elements """

        # Loaders for Temporal Series
        self._water_belts_prediction_ts = WaterBeltsPredictionTemporalSeriesWriter()
        self._water_drum_prediction_ts_loader_line_1 = WaterDrumPredictionTemporalSeriesWriter(1)
        self._water_drum_prediction_ts_loader_line_2 = WaterDrumPredictionTemporalSeriesWriter(2)
        self._sensor_data_ts_loader_line_1 = SensorDataTemporalSeriesWriter(1)
        self._sensor_data_ts_loader_line_2 = SensorDataTemporalSeriesWriter(2)

        # Loader for relational database
        self._chemical_composition_loader = ChemicalCompositionDataWriter()
        self._mould_loader_line_1 = MouldDataWriter(1)
        self._mould_loader_line_2 = MouldDataWriter(2)
        self._pouring_alarm_loader = PouringAlarmDataWriter()
        self._pouring_data_loader = PouringDataRecWriter()
        self._sensor_data_loader_line_1 = SensorDataWriter(1)
        self._sensor_data_loader_line_2 = SensorDataWriter(2)
        self._water_belts_prediction = WaterBeltsDataPredictionWriter()
        self._water_drum_prediction_loader_line_1 = WaterDrumDataPredictionWriter(1)
        self._water_drum_prediction_loader_line_2 = WaterDrumDataPredictionWriter(2)

    def start_loading_process(self) -> None:
        """ Method to star the loading process """

        # Starting Loaders for Temporal Series
        self._water_belts_prediction_ts.start_observe_and_load_data()
        self._water_drum_prediction_ts_loader_line_1.start_observe_and_load_data()
        self._water_drum_prediction_ts_loader_line_2.start_observe_and_load_data()
        self._sensor_data_ts_loader_line_1.start_observe_and_load_data()
        self._sensor_data_ts_loader_line_2.start_observe_and_load_data()

        # Starting Loader for relational database
        self._chemical_composition_loader.start_observe_and_load_data()
        self._mould_loader_line_1.start_observe_and_load_data()
        self._mould_loader_line_2.start_observe_and_load_data()
        self._pouring_alarm_loader.start_observe_and_load_data()
        self._pouring_data_loader.start_observe_and_load_data()
        self._sensor_data_loader_line_1.start_observe_and_load_data()
        self._sensor_data_loader_line_2.start_observe_and_load_data()
        self._water_belts_prediction.start_observe_and_load_data()
        self._water_drum_prediction_loader_line_1.start_observe_and_load_data()
        self._water_drum_prediction_loader_line_2.start_observe_and_load_data()

    def stop_loading_process(self) -> None:
        """ Method to stop the loading process """

        # Stopping Loaders for Temporal Series
        self._water_belts_prediction_ts.stop_observe_and_load_data()
        self._water_drum_prediction_ts_loader_line_1.stop_observe_and_load_data()
        self._water_drum_prediction_ts_loader_line_2.stop_observe_and_load_data()
        self._sensor_data_ts_loader_line_1.stop_observe_and_load_data()
        self._sensor_data_ts_loader_line_2.stop_observe_and_load_data()

        # Stopping Loader for relational database
        self._chemical_composition_loader.stop_observe_and_load_data()
        self._mould_loader_line_1.stop_observe_and_load_data()
        self._mould_loader_line_2.stop_observe_and_load_data()
        self._pouring_alarm_loader.stop_observe_and_load_data()
        self._pouring_data_loader.stop_observe_and_load_data()
        self._sensor_data_loader_line_1.stop_observe_and_load_data()
        self._sensor_data_loader_line_2.stop_observe_and_load_data()
        self._water_belts_prediction.stop_observe_and_load_data()
        self._water_drum_prediction_loader_line_1.stop_observe_and_load_data()
        self._water_drum_prediction_loader_line_2.stop_observe_and_load_data()