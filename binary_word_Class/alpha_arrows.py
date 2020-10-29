import binary_word
'''
The morphisms in our category are of the form 
of alpha arrows.
'''
class AlphaArrow:
    '''
    An alpha arrow is a morphism u \otimes (v\otimes w) --> (u \otimes v) \otimes w. These encode 
    a single change of parentheses in monoidal categories.  w = u v = u (y z) --> (u y) z 
    '''
    def __init__(self, source, target, expression="1"): 
        self.expression = expression
        self.source = source
        self.target = target
        if expression == "1":
            self.left = None
            self.right = None
        if expression == "\\alpha_{u,v,w}":
            self.u = source.left
            self.v = source.right.left
            self.w = source.right.right
            self.left = None
            self.right = None
        elif expression[:2] == "1(":
            self.left = AlphaArrow(source.left, target.left, "1")
            self.right = AlphaArrow(source.right, target.right, expression[2:])
        elif expression[-2:] == ")1":
            self.left = AlphaArrow(source.left, target.left, expression[:-2])
            self.right = AlphaArrow(source.right, target.right, "1")
