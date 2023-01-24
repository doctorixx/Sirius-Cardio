from app import SiriusCardio


if __name__ == '__main__':
    app: SiriusCardio = SiriusCardio("records/1.edf", "out/1.txt")
    app.run()
