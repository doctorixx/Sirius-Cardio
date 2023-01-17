import mne
import mne.channels
from mne import Info
from mne.io.edf.edf import RawEDF
from numpy import ndarray

from core.dataClasses import ECGData


class EdfReader:
    """
    This class is reading and parsing data from disk and return class ECGData with values and times

    @:param path of file
    """
    def __init__(self, path: str):
        self.path = path

    def read(self) -> ECGData:
        data: RawEDF = mne.io.read_raw_edf(self.path)

        info: Info = data.info
        channels = data.ch_names

        values: ndarray = data.get_data()
        times: ndarray = data.times

        return ECGData(values, times)
