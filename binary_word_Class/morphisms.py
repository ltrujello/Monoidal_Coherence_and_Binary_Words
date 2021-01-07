from binary_word import *
from associahedron import *
'''
The morphisms in our category can be expressed via alpha arrows, rhos, and lambdas. 
'''
class AlphaArrow:
    '''
    An associator is a natural isomorphism \\alpha_{u,v,w}: u \otimes (v\otimes w) --> (u \otimes v) \otimes w. 
    These morphisms encode a single change of parentheses in monoidal categories. 
    
    This lets us define an ALPHA ARROW recursively as follows. 
        1. \\alpha is an alpha arrow
        2. 1_u \otimes \\beta: u \otimes v --> u \otimes v' and \\beta \otimes 1_v: u \otimes v --> u' \otimes v 
        are both alpha arrows if \\beta is already an alpha arrow.
    ''' 
    def __init__(self, source, target, expression="1"): 
        self.expression = expression
        self.source = source
        self.target = target
        if expression == "1":
            self.left = None
            self.right = None
        elif expression == "\\alpha_{u,v,w}":
            self.left = None
            self.right = None
            self.u = source.left
            self.v = source.right.left
            self.w = source.right.right
        elif expression[:2] == "1(":
            self.left = AlphaArrow(source.left, target.left, "1")
            self.right = AlphaArrow(source.right, target.right, expression[2:-1])
        elif expression[-2:] == ")1":
            self.left = AlphaArrow(source.left, target.left, expression[1:-2])
            self.right = AlphaArrow(source.right, target.right, "1")

class LambdaArrow:
    '''
    The lambda unitor is the natural isomorphism \\lambda: e \otimes u --> u. It removes an instance of the identity 
    from the left.

    This lets us define a LAMBDA ARROW recursively as follows. 
    1. \\lambda is a lambda arrow
    2. 1_u \otimes \\beta: u \otimes v --> u \otimes v' and \\beta \otimes 1_v: u \otimes v --> u' \otimes v 
        are both lambda arrows if \\beta is already an lambda arrow.
    '''
    def __init__(self, source, target, expression="1"): 
        assert source.left.expression == "e", "Invalid application of lambda"
        self.expression = expression
        self.source = source
        self.target = target
        if expression == "1":
            self.left = None
            self.right = None
        elif expression == "\\lambda":
            self.left = None
            self.right = None
        elif expression[:2] == "1(":
            self.left = LambdaArrow(source.left, target.left, "1")
            self.right = LambdaArrow(source.right, target.right, expression[2:-1])
        elif expression[-2:] == ")1":
            self.left = LambdaArrow(source.left, target.left, expression[1:-2])
            self.right = LambdaArrow(source.right, target.right, "1")


class RhoArrow:
    '''
    The Rho unitor is the natural isomorphism \\lambda: u \otimes e --> u. It removes an instance of the identity 
    from the right.

    This lets us define a RHO ARROW recursively as follows. 
    1. \\rho is a rho arrow
    2. 1_u \otimes \\beta: u \otimes v --> u \otimes v' and \\beta \otimes 1_v: u \otimes v --> u' \otimes v 
        are both rho arrows if \\beta is already an rho arrow.
    '''
    def __init__(self, source, target, expression="1"): 
        self.expression = expression
        self.source = source
        self.target = target
        if expression == "1":
            self.left = None
            self.right = None
        elif expression[:2] == "1(":
            self.left = RhoArrow(source.left, target.left, "1")
            self.right = RhoArrow(source.right, target.right, expression[2:-1])
        elif expression[-2:] == ")1":
            self.left = RhoArrow(source.left, target.left, expression[1:-2])
            self.right = RhoArrow(source.right, target.right, "1")