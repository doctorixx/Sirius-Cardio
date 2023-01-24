import numpy
from core import utils
from core.EdfReader import EdfReader
from core.dataClasses import ECGData, Point
from core.utils import findMagicLine

if __name__ == '__main__':
    reader = EdfReader("records/1.edf")
    data: ECGData = reader.read()

    piks, _ = utils.getPiksAndPlots(data)

    porog = findMagicLine(piks)
    numOfMinutes = 3
    pulse = [0]*numOfMinutes

    out = []
    # PikFilter
    for pik in piks:
        if pik.value >= porog: out.append(pik)
    # TimeFilter
    for i in range(len(out)):
        if out[i].time + 0.3 >= out[i + 1].time:
            if out[i].value > out[i + 1].value:
                out.pop(i + 1)
            elif out[i].value < out[i + 1].value:
                out.pop(i)

        elif out[i - 1].time + 0.3 >= out[i].time:
            if out[i - 1].value > out[i].value:
                out.pop(i)
            elif out[i - 1].value < out[i].value:
                out.pop(i - 1)
        if i + 1 == len(out) - 1:
            break

    #Pulsecounter
    for pik in out:
        time = int(pik.time)
        pulse[time//60]+=1

    #TxTwriter
    try:
        with open("out1.txt", "w") as file:
            file.write(f"ЧСС первой минуты: {pulse[0]} уд./мин\n")
            file.write(f"ЧСС второй минуты: {pulse[1]} уд./мин\n")
            file.write(f"ЧСС третий минуты: {pulse[2]} уд./мин\n")
            file.write('\n')
            file.write('Интервалы (мс):')
            file.write('\n')
            for j in range(len(out) - 1):
                file.write(str(int((out[j + 1].time - out[j].time) * 1000)))
                file.write('\n')
            file.close()
    except Exception as e:
        print("Ошибка при записи в файл")

print("Done")

