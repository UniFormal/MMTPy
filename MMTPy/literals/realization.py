from MMTPy.objects.terms import omlit

class RealizedType(object):
    """
    A RealizedType represents a mapping between a single semantic type (an
    arbitrary MMT Term) and a semantic type (a native python type).
    """
    def __init__(self, semtp, syntp):
        self.semtp = semtp
        self.syntp = syntp
    def applies(self, tm):
        if isinstance(tm, omlit.UnknownOMLIT):
            return self.syntp == tm.syntp
        return False
    def apply(self, tm):
        if not self.applies(tm):
            raise ValueError("RealizedType does not apply")

        return tm.toOMLIT(self.semtp)
    def realizes(self, o):
        return self.semtp.valid(o)
    def realize(self, o):
        if not self.realizes(o):
            raise ValueError("RealizedType does not apply")

        return omlit.OMLIT(self.semtp, self.syntp, o)
    def tryApply(self, tm):
        if self.applies(tm):
            return self.apply(tm)
        else:
            return tm
    def applyR(self, tm):
        return tm.map(self.tryApply)
    def __call__(self, tm):
        return self.applyR(tm)

class LiteralContext(object):
    def __init__(self, lrts):
        self.lrts = lrts
    def applies(self, tm):
        for rt in self.lrts:
            if rt.applies(tm):
                return True
        return False
    def apply(self, tm):
        if not self.applies(tm):
            raise ValueError("RealizedType does not apply")
        for rt in self.lrts:
            if rt.applies(tm):
                return rt.apply(tm)
    def tryApply(self, tm):
        if self.applies(tm):
            return self.apply(tm)
        else:
            return tm
    def applyR(self, tm):
        return tm.map(self.tryApply)
    def realizes(self, o):
        for rt in self.lrts:
            if rt.realizes(o):
                return True
        return False
    def realize(self, o):
        if not self.realizes(o):
            raise ValueError("RealizedType does not apply")

        for rt in self.lrts:
            if rt.realizes(o):
                return rt.realize(o)
    def __call__(self, tm):
        return self.applyR(tm)
