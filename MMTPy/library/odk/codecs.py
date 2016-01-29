from MMTPy.codecs import codec, realization
from MMTPy.content.objects.terms import omlit, oma
from MMTPy.library.odk import literals, ODK
from MMTPy.library.lf import wrappers

class LiteralCodec(codec.Codec):
    """
    Encodes an object as a direct wrapper of an OMLIT
    """
    def encode(self, o):
        return literals.ctx.realize(o)
    def decode(self, tm):
        if isinstance(tm, omlit.OMLIT):
            return tm.o
        raise codec.CodingError()

class StandardInt(LiteralCodec): pass

class StandardString(LiteralCodec): pass

class StandardBool(codec.Codec):
    def encode(self, o):
        return ~ODK.Logic.true if o else ~ODK.Logic.false
    def decode(self, tm):
        if tm == ~ODK.Logic.true:
            return True
        if tm == ~ODK.Logic.false:
            return False
        raise codec.CodingError()

class BoolAsInt(codec.Codec):
    def encode(self, o):
        return ~ODK.Logic.true if o==1 else ~ODK.Logic.false
    def decode(self, tm):
        if tm == ~ODK.Logic.true:
            return 1
        if tm == ~ODK.Logic.false:
            return 0
        raise codec.CodingError()

class StandardList(codec.CodecOperator):
    def __init__(self, syntp, st, tc):
        super(StandardList, self).__init__(syntp, tc)

        self.st = st
        self.nil = ~ODK.Lists.nil
        self.cons = ~ODK.Lists.cons

        self.tc = tc
    def encode(self, o):
        sofar = wrappers.lf_apply(self.nil, self.tc.syntp)
        for e in reversed(o):
            sofar = wrapper.lf_apply(self.cons, self.tc.syntp, self.tc.encode(e), sofar)

        return sofar
    def decode(self, tm):

        # it needs to be an oma
        if not isinstance(tm, oma.OMA):
            raise codec.CodingError()

        # we unapply and need to take care of two different case
        (f, args) = wrappers.lf_unapply(tm)

        # we need to be of the right type
        if args[0] != self.tc.syntp:
            raise codec.CodingError()

        # in case we are nill
        if f == self.nil:
            return []
        # in case we are cons
        elif f == self.cons:
            l = self.tc.decode(args[1])

            return [l] + self.decode(args[2])
        # we need nill or cons
        else:
            raise codec.CodingError()

ctx = realization.CodecContext([
    realization.RealizedCodec(StandardInt, ~ODK.Int.int, ~ODK.Codecs.standardInt),
    realization.RealizedCodec(StandardString, ~ODK.Strings.string, ~ODK.Codecs.standardString),
    realization.RealizedCodec(StandardBool, ~ODK.Logic.bool, ~ODK.Codecs.standardBool),
    realization.RealizedCodec(BoolAsInt, ~ODK.Logic.bool, ~ODK.Codecs.boolAsInt),
    realization.RealizedCodec(StandardList, ~ODK.Lists.list, ~ODK.Codecs.standardList)
])
