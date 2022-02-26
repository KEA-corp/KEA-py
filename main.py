from src.Interpreteur import Interpreteur
from src.Parseur import Parseur

import sys

if len(sys.argv) < 2:
    raise Exception("No file specified")

debug = "-d" in sys.argv

parser = Parseur(sys.argv[1])
parser.generate_instructions()
if debug : print(parser.instructions)
interpreter = Interpreteur(parser.instructions)
interpreter.run()