from MMTPy.codecs import codec

codecs = {}

def register(cdec):
    """
    Registers a new codec that can be retrieved later
    """

    # you can only register something that is a codec
    if not isinstance(cdec, codec.Codec):
        raise ValueError("Can only register something that is actually a codec")

    codecname = str(cdec.name)

    # make sure it is not yet registered
    if codecname in codecs:
        raise ValueError("Specified codec already registered")

    # store it in the codecs array
    codecs[codecname] = cdec

    # return the codec
    return cdec

def retrieve(name):
    """
    Retrieves a stored codec. Loads the codec if it is not there yet
    """

    # turn it into a string
    codecname = str(name)

    if codecname in codecs:
        return codecs[codecname]
    else:
        return NotImplementedError

# Import and load all the codecs
from MMTPy.codecs.implementations import register_all
register_all()
del register_all
