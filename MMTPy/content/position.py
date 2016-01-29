from MMTPy.caseclass import caseclass
from MMTPy.content.objects import obj

class Position(caseclass.make([int])):
    def __init__(self, indices):
        super(Position, self).__init__(indices)
        self.indices = indices
        self.indices_str = "_".join(map(str, indices))
    @staticmethod
    def parse(s):
        if s == "":
            return Position([])
        else:
            return Position(list(map(int, s.split("_"))))