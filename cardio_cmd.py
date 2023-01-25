import sys
from app import SiriusCardio

USAGE_GUIDE = '''
Use with arguments: [input_file] [output_file]
Example: [filename] records/1.edf out/1.txt
Where filename - exe file name
'''

if __name__ == '__main__':
    if len(sys.argv) != 2 + 1:
        print(USAGE_GUIDE)
        exit()

    app: SiriusCardio = SiriusCardio(input_filename=sys.argv[1], output_filename=sys.argv[2])
    app.run()
