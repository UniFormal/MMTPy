from MMTPy.objects.terms import term, omlit
from MMTPy.codecs import codec
from MMTPy.codecs import storage

class standardInt(codec.Codec):
    def __init__(self):
        self.name = "standardInt" # TODO: Full name
    def encode(tm):
        if isinstance(tm, term.OMLIT) and tm.type == omlit.OMLIT.type_bigint:
            return int(tm.value)
        else:
            raise ValueError("Codec not applicable")
    def decode(o):
        return term.OMLIT(term.OMLIT.type_bigint, str(o))

# register the codec
storage.register(standardInt())
