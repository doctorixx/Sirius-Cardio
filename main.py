import numpy

from core import utils
from core.EdfReader import EdfReader
from core.dataClasses import ECGData, Point
from core.utils import findMagicLine

if __name__ == '__main__':
    reader = EdfReader("records/5.edf")
    data: ECGData = reader.read()

    piks, _ = utils.getPiksAndPlots(data)

    porog = findMagicLine(piks)

    out = []
    # Filter
    for pik in piks:
        if pik.value >= porog: out.append(pik)

    print("Done")

#privet