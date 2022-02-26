from src.Instructions import I
 
class Parseur:
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = self.get_content()
        self.instructions = []
    def get_content(self):
        return [x.split("\n")[0] for x in open(self.file_name, "r").readlines()]
    def generate_instructions(self):
        x = 0
        while x < len(self.content):
            match self.content[x].split(" "):
                case "#": # TODO
                    pass
                case "A": # TODO
                    pass
                case "B", output, var1, operator, var2:
                    self.instructions.append((I.COMPARE, output, var1, operator, var2, ))
                case "C", output, var1, operation, var2: 
                    self.instructions.append((I.CALCULATE, output, var1, operation, var2, ))
                case "D":
                    pass # on ne fait pas le débug
                case "E": # TODO
                    pass
                case "F": # TODO
                    pass
                case "H": # TODO
                    pass
                case "I", variable:
                    self.instructions.append((I.INPUT, variable, ))
                case "L": # TODO
                    pass
                case "R", output, maximum:
                    self.instructions.append((I.RANDOM, output, maximum, ))
                case "S", *args:
                    self.instructions.append((I.PRINT, args, ))
                case "T": # TODO
                    pass
                case "V", name, value:
                    self.instructions.append((I.VARSET, name, value, ))
                case "X": # TODO
                    pass
                case "Z": # TODO
                    pass
        
        
            x += 1
        self.instructions.append((I.STOP, ))