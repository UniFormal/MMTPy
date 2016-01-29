from MMTPy.content.objects.terms import oma, omid
from MMTPy.paths import path
from MMTPy.library.lf import wrappers

from MMTPy.utils import ustr

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
        self.record = path.Path.parse("http://cds.omdoc.org/urtheories").Records.record
        self.codec = path.Path.parse("http://www.lmfdb.org/").Metadata.codec
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
            sc = self.getSingleCodec(tm)
            if sc != None:
                return sc()
            else:
                from MMTPy.codecs import codec
                return RealizedCodec(codec.IdentityCodec, None, None)
        # if we have an OMA, we are applying some realisedCodec operator to an
        # an actual codec
        elif isinstance(tm, oma.OMA):

            # extract the arguments from the term
            (f, args) = wrappers.lf_unapply(tm)

            # we can no go recursively to apply the arguments properly
            return self.getSingleCodec(f)(*[self.get(t) for t in args])
        else:
            # must be either omid or oma
            raise ValueError("given term does not represent a codec")
    def encodeRecord(self, val, thy):
        """
        Encodes a record into an MMT term
        """
        pass
    def decodeRecord(self, tm, thy):
        """
        Decodes a record into native python object.
        """

        # not a record
        if not isinstance(tm, oma.OMA):
            raise ValueError("not a record (not am OMA)")

        # the output json we want to produce
        out = {}

        # unapply the arguments
        (f, args) = tm.uncall()

        # we need to apply the record to some theory
        # at least, there might be more
        if f != ~self.record or len(args) == 0:
            raise ValueError("not a record (wrong application or not enough arguments)")

        # TODO: Check the theory name

        for d in args[1:]:
            name = d.vd.name
            cd = thy.getConstantDeclaration(name).getMeta(self.codec)
            out[ustr(name)] = self.get(cd.value).decode(d.vd.df)

        return out
