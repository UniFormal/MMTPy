class RealizedType(object):
    def __init__(self, semtp, syntp):
        self.semtp = semtp
        self.syntp = syntp
    def applies(self, tm):
        from MMTPy.objects.terms import omlit
        if isinstance(tm, omlit.UnknownOMLIT):
            return self.syntp == tm.syntp
        return False
    def apply(self, tm):
        if not self.applies(tm):
            raise ValueError("RealizedType does not apply")

        return tm.toOMLIT(self.semtp)
    def tryApply(self, tm):
        if self.applies(tm):
            return self.apply(tm)
        else:
            return tm
    def applyR(self, tm):
        return tm.map(self.tryApply)
    def __call__(self, tm):
        return self.applyR(tm)

class RealizedContext(object):
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
        raise ValueError("something went horribly wrong")
    def tryApply(self, tm):
        if self.applies(tm):
            return self.apply(tm)
        else:
            return tm
    def applyR(self, tm):
        return tm.map(self.tryApply)
    def __call__(self, tm):
        return self.applyR(tm)
