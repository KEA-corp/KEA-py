from enum import Enum, IntEnum, auto

class I(IntEnum):
    VARSET = auto()
    COMPARE = auto()
    CALCULATE = auto()
    RANDOM = auto()
    INPUT = auto()
    PRINT = auto()
    
    STOP = auto()