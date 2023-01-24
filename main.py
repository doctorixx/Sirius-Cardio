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
    # PikFilter
    for pik in piks:
        if pik.value >= porog: out.append(pik)
    #TimeFilter
    for i in range (len(out)):
        if out[i].time +0.3 >= out[i+1].time:
            if out[i].value > out[i + 1].value:
                    out.pop(i+1)
            elif out[i].value < out[i + 1].value:
                    out.pop(i)

        elif out[i-1].time +0.3 >= out[i].time:
                if out[i-1].value > out[i].value:
                    out.pop(i)
                elif out[i-1].value < out[i].value:
                    out.pop(i-1)
        if i + 1 == len(out) - 1:
            break












    print("Done")