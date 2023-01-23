import numpy
from typing import Tuple, List, Any

import settings.config
from core.dataClasses import Point, ECGData


def getPiksAndPlots(data: ECGData) -> Tuple[List[Point], List[Any]]:
    """
    This function find max values of plot and plots and return this
    :return: tuple(maxInPlots, plots)
    """
    x = list(map(lambda f: f * 10 ** 7, data.values))[0]

    splitted = []
    m_splited = []

    sr = int(1000 / 8 / 5)
    ite = int(22500 / sr)

    # print(f"Каждая цифра - 1/{125 / sr}")

    for i in range(ite):
        srez = x[sr * i:sr * (i + 1)]
        splitted.append(srez)
        maxElem = max(srez)
        maxElemIndex = (numpy.where(srez == maxElem)[0][0])
        timeByIndex = data.times[sr * i + maxElemIndex]
        m_splited.append(Point(maxElem, timeByIndex))

    return m_splited, splitted


def findMagicLine(datas: List[Point]) -> float:
    average: int = settings.config.INT_KOLVO_MAX_AVERAGE
    maxes = [-99999999] * average
    for point in datas:
        mbMax: float = point.value
        for i in range(len(maxes)):
            if maxes[i] < mbMax:
                maxes[i] = mbMax
                break

    result: int = sum(maxes) / average

    result *= (100-settings.config.INT_PROCENT_OTKNONENIYA)/100

    return result
