from case_class import CaseClass


class Position(CaseClass):
    """ Represents the position of a SubObject. """

    def __init__(self, indices):
        """ Creates a new Position() instance.

        :param indices:  List of integers indicating indices
        :type indices: list
        """

        self.__indices = indices  # type: list

    @property
    def indices(self):
        """ Returns the indices of this Position() instance.

        :rtype: list
        """

        return self.__indices

    def __str__(self):
        """ Turns this Position() into a string.

        :rtype: str
        """

        return "_".join(map(str, self.indices))  # type: str

    @staticmethod
    def parse(s):
        """ Parses a string into a position object.

        :param s: _ seperated sting to parse
        :type s: str
        """

        if s == "":
            return Position([])
        else:
            return Position(list(map(int, s.split("_"))))

__all__ = ["Position"]