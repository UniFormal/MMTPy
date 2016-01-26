from MMTPy.objects.terms import oma, omid

class RealizedCodec(object):
    """
    A RealizedCodec represents a mapping between an object in the MMT object
    Codecs theory and an actual implementation
    """
    def __init__(self, impl, syntp, pth):
        self.pth = pth
        self.impl = impl
        self.syntp = syntp
    def __call__(self, *args):
        return self.impl(self.syntp, *args)
    def decode(self, tm, *args):
        return self(*args).decode(tm)
    def encode(self, o, *args):
        return self(*args).encode(tm)

class CodecContext(object):
    """
    A CodecContext represents the implementation of a Codec Theory
    """
    def __init__(self, codecs):
        self.codecs = codecs
    def getSingleCodec(self, tm):
        """
        Retrieves a single RealizedCodec (non-composite) from this CodecContext.

        tm - An OMID() pointing to the codec
        """
        for c in self.codecs:
            if c.pth == tm:
                return c
        return None
    def get(self, tm):
        """
        Retrieves a Codec Instance given in the form of an MMT Term from this
        CodecContext
        """

        # if we have an OMID only, we have a single codec to apply
        # so we can simply retrieve the codec and initalise it.
        if isinstance(tm, omid.OMID):
            return self.getSingleCodec(tm)()
        # if we have an OMA, we are applying some realisedCodec operator to an
        # an actual codec
        elif isinstance(tm, oma.OMA):

            # extract the arguments from the term
            (f, args) = tm.uncall(lf=True)

            # we can no go recursively to apply the arguments properly
            return self.getSingleCodec(f)(*[self.get(t) for t in args])
        else:
            # must be either omid or oma
            raise ValueError("given term does not represent a codec")
