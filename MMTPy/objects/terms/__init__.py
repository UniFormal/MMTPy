"""
    This module defines terms for MMT

    Abstractly speaking a term is represented as:

    Term = OMV (name : LocalName)
         | OMID (path : ContentPath)
         | OMA (fun : Term, args : List[Term])
         | OMATTR (arg : Term, key : OMID, value : Term)
         | OMBINDC (binder : Term, context: Context, scopes : List[Term])
         | OMLIT (type: Term, value : string)
"""
