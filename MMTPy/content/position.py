from MMTPy.clsutils import caseclass, types
from MMTPy.content.objects import obj

@caseclass.caseclass
@types.argtypes([int])
class Position(object):
    def __init__(self, indices):
        self.indices = indices
        self.indices_str = "_".join(map(str, indices))
    @staticmethod
    def parse(s):
        if s == "":
            return Position([])
        else:
            return Position(list(map(int, s.split("_"))))