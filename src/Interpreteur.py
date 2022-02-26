from src.Instructions import I
import random

class Interpreteur:
    def __init__(self, instructions):
        self.instructions = instructions
        self.variables = {}
    def run(self):
        x = 0
        while self.instructions[x] != (I.STOP,):
            match self.instructions[x]:
                case I.VARSET, name, value, :
                    self.variables[name] = value
                case I.COMPARE, output, var1, operator, var2, :
                    self.variables[output] = eval(f"{self.variables[var1]} {operator} {self.variables[var2]}")
                case I.CALCULATE, output, var1, operation, var2, :
                    self.variables[output] = eval(f"{self.variables[var1]} {operation} {self.variables[var2]}")
                case I.RANDOM, output, maximum, :
                    self.variables[output] = random.randint(0, int(maximum))
                case I.INPUT, variable, :
                    entree = input(f"{variable} : ")
                    if entree.isnumeric():
                        self.variables[variable] = int(entree)
                    else:
                        self.variables[variable] = entree
                case I.PRINT, *args, :
                    print(f"{' '.join(args[0])}")
            print(self.variables)
            x += 1