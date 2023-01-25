from app import SiriusCardio

if __name__ == '__main__':
    app: SiriusCardio = SiriusCardio("", "")
    for i in range(5):
        app.output_filename = f"out/{i + 1}.txt"
        app.input_filename = f"records/{i + 1}.edf"
        app.run()
