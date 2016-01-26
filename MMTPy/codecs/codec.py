class Codec(object):
    """
    A Codec is a mapping between MMT Literals and their corresponding python
    values.
    """
    def __init__(self, syntp):
        self.syntp = syntp
    def decode(self, tm):
        """
        Decodes a term using this Codec.
        """
        raise NotImplementedError
    def encode(self, o):
        """
        Encodes an object as an MMT Term using this Codec.
        """
        raise NotImplementedError

class CodecOperator(Codec):
    """
    A CodecOperator represents a function that takes a codec and returns another
    codec.
    """
    def __init__(self, syntp, *args):
        """
        Creates a new instance of this CodecOperator given the repspective codecs
        as arguments.
        """
        super(CodecOperator, self).__init__(syntp)
        self.args = args

class CodingError(Exception): pass
