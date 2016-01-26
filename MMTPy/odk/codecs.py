from MMTPy.codecs import codec, realization
from MMTPy.objects.terms import omlit, oma
from MMTPy.odk import literals, paths

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
        return ~paths.Logic.true if o else ~paths.Logic.false
    def decode(self, tm):
        if tm == ~paths.Logic.true:
            return True
        if tm == ~paths.Logic.false:
            return False
        raise codec.CodingError()

class BoolAsInt(codec.Codec):
    def encode(self, o):
        return ~paths.Logic.true if o==1 else ~paths.Logic.false
    def decode(self, tm):
        if tm == ~paths.Logic.true:
            return 1
        if tm == ~paths.Logic.false:
            return 0
        raise codec.CodingError()

class StandardList(codec.CodecOperator):
    def __init__(self, syntp, tc):
        super(StandardList, self).__init__(syntp, tc)

        self.nil = ~paths.Lists.nil
        self.cons = ~paths.Lists.cons

        self.tc = tc
    def encode(self, o):
        sofar = self.nil(self.tc.syntp, lf=True)
        for e in reversed(o):
            sofar = self.cons(self.tc.syntp, self.tc.encode(e), sofar, lf=True)

        return sofar
    def decode(self, tm):

        # it needs to be an oma
        if not isinstance(tm, oma.OMA):
            raise codec.CodingError()

        # we unapply and need to take care of two different case
        (f, args) = tm.uncall(lf=True)

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
    realization.RealizedCodec(StandardInt, ~paths.Int.int, ~paths.Codecs.standardInt),
    realization.RealizedCodec(StandardString, ~paths.Strings.string, ~paths.Codecs.standardString),
    realization.RealizedCodec(StandardBool, ~paths.Logic.bool, ~paths.Codecs.standardBool),
    realization.RealizedCodec(BoolAsInt, ~paths.Logic.bool, ~paths.Codecs.boolAsInt),
    realization.RealizedCodec(StandardList, ~paths.Lists.list, ~paths.Codecs.standardList)
])
