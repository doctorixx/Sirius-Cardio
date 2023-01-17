from core.EdfReader import EdfReader
from core.dataClasses import ECGData, Point

if __name__ == '__main__':
    reader = EdfReader("records/test.edf")
    data: ECGData = reader.read()
    print()
