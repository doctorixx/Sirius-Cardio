from numpy import ndarray


class Point:
    """
       This class contains data of dot
       @:param time time
       @:param value value

       """

    def __init__(self, value: float, time: float):
        self.time = time
        self.value = int(value)

    def __repr__(self):
        return f"{self.value} [t={self.time}]"


class ECGData:
    """
       This class contains all times and values of record
       (This class used by EdfReader)
       @:param times
       @:param values

       """

    def __init__(self, times: ndarray, values: ndarray):
        self.times = times
        self.values = values
