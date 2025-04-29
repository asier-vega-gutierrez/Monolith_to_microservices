class WaterAdditionData:
    """ Domain class for manage the Water Addition Prediction object """

    def __init__(self,
                datetime,
                line,
                type,
                prediction,
                data_for_prediction):
        """ Consturctor with parameters """

        self.datetime = datetime
        self.line = line
        self.type = type
        self.prediction = prediction
        self.data_for_prediction = data_for_prediction