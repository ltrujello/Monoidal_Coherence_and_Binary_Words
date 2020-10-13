import json
# This program is for (pure) binary words. 
# satan was here XD
'''
A class for binary words. The constructor is recursive.
An example: word = BinaryWord("x(x(xx))"). It calculates its length and all of the substructures
of x(x(xx)), which is harder to think about when we include more and more x's. 
'''
class BinaryWord:
    '''
    A BINARY WORD is defined recursively as follows: 
        1. The symbol x is a binary word.
        2. If u, v are binary words, so is (u)(v).
    Therefore, every binary word has a "left" component, which is a  binary word, and a right component.
    
    Moreover, every binary word has a FORM, which is the formal expression of the word into its (x)'s. 
    The formal expression is what will make a computer's life easier, but in practice they're clunky. E.g., 
    (x)((x)(x)) is a binary word, but in practice, we'd like to actually just write x(xx). Therefore we define 
    such a ''reduced'' form as the EXPRESSION. 

    Every binary word has LENGTH. It is the number of letters in the word. 
    Rigorously, length of a binary word is defined recursively as follows:
        1. The word x has length 1.
        2. The word (u)(v) has length len(u) + len(v).

    Binary words also have a RANK. The rank of a binary word is defined recursively as follows. 
        1. The rank of x is 0.
        2. The rank of (u)(v) is rank(u) + rank(v) + len(v) - 1.
    '''
    def __init__(self, expression="x"): 
        self.expression = expression # save the binary word expression
        # This is our base case. 
        if expression == "x": 
            self.left = None
            self.right = None
            self.form = "(x)"
            self.len = 1
            self.rank = 0
        # If we're not at out base case, then split the word.
        else:                    
            left, right = split_binary_word(self.expression) #we split the binary word
            self.left = BinaryWord(left) 
            self.right = BinaryWord(right)
            self.len = self.left.len + self.right.len
            self.rank = self.left.rank + self.right.rank + self.right.len - 1
        self.form = self.add_formal_pars() # also save the formalized expression
    '''
    Parameters
    ----------
    word1 : BinaryWord
    word2 : BinaryWord    

    Returns
    ----------
    product: BinaryWord
    '''
    def tensor(self, right):
        '''Compute the tensor product of two binary words.
        '''
        left= self.expression 
        right = right.expression 

        # If there are redundant parentheses, remove them, because we may add parentheses later 
        if is_surrounded(left):
            left = remove_outer_pars(left)
        if is_surrounded(right):
            right = remove_outer_pars(right)

        ''' of concern is the case when we are tensoring x. Because we want the expression 
        of the binary word to be informal, i.e., natural for the reader, we need to make sure we don't put redundant 
        parentheses on individual x's.
        '''
        if left == "x" and right ==  "x":
            product = BinaryWord( left + right ) #no parentheses
        
        # If this is true, then the right is not "x" 
        elif left == "x":
            product = BinaryWord( left + "("+ right +")") #just parentheses for the right
        # If this is true, then the left is not "x"
        elif right == "x":
            product = BinaryWord("("+ left +")" + right)  #just parentheses for the left

        # in all other cases, we do want to produce an expression of the form (...)(---).
        else:
            product = BinaryWord( "("+ left + ")" + "("+ right +")") #parentheses for left and right
        return product

    '''
    Parameters
    ----------
    word : BinaryWord

    Returns
    ----------
    string
    '''
    def add_formal_pars(self):
        '''adds the formal parentheses to a binary word expression. E.g., x(xx) => (x)((x)(x))
        '''
        # Our base case is x or xx, since we expect the user to write x(xx), (x(xx))x, etc.
        if self.expression == "x": 
            return "(x)"
        if self.expression == "xx":
            return "(x)(x)"
        # If we are not at our base case, we split the binary word into its left and right components and recurse.
        else:
            left = self.left.add_formal_pars()
            right = self.right.add_formal_pars()
            
            # Next two ifs guarantee we don't have redundant parentheses in our final expression    
            if is_surrounded(left):
                left = remove_outer_pars(left)
            if is_surrounded(right):
                right = remove_outer_pars(right)
            return "(" + left + ")" + "(" + right + ")"


'''
Parameters
----------
word : string

Returns
----------
swapped_word : string
'''
def swap_letters_for_x(word_expression):
    '''Replaces every letter in an expression with 'x'. This allows the user  
    the convenience to write whatever they want, e.g. A(BC), while behind the scenes, we work with x, e.g. x(xx).  
    '''
    word_list = list(word_expression)
    for ind in range(0, len(word_list)):
        if word_list[ind] != "(" and word_list[ind] !=  ")" and word_list[ind] != 'x':
            word_list[ind] = 'x'
    new_expression = "".join(word_list)
    return new_expression
            
'''         
Parameters
----------
word_expression : string

Returns
----------
par_count : int
'''
def parenthesis_tracker(word_expression, index=None):
    ''' counts parenthesis-matches up to index. By default, index = length of the word.
    '''
    if index is None: # work-around of defining default param in terms of other param
        index = len(word_expression)

    assert index <= len(word_expression), "index tracker too large"
    num_left_par=0  # number of left parenthesis
    num_right_par=0 # number of right parenthesis
    for ind in range(0, index):
        letter = word_expression[ind]
        if letter == "(": #if we find a left parenthesis
            num_left_par+=1 
        if letter == ")": #if we find a right parenthesis
            num_right_par +=1
    par_count = num_left_par - num_right_par
    return par_count

'''
Parameters
----------
word_expression : string

Returns
----------
Bool 
'''
def is_matched(word_expression, index=None):
    '''Helper for is_surrounded.'''
    '''A tool to figure out if the word has a correctly matched parenthesis up to desired index.
       By default, the index is the length of the word.
       A user has input and incorrect word if this is false when index = len(word_expression). 
    '''
    if index is None: # work-around of defining default param in terms of other param
        index = len(word_expression)
    assert index>0, "Checking matched parenthesis at index = 0 is not logical."
    par_count = parenthesis_tracker(word_expression, index)
    if par_count != 0:
        return False
    else:
        return True


'''
Parameters
----------
word_expression : string

Returns
----------
Bool
'''
def is_surrounded(word_expression):
    '''Helper for split_binary_word.'''
    ''' Detects if the expression is already surrounded, or enclosed, in backets.
    Some surrounded words: (x), (xx), (x(xx)), ...
    '''
    if word_expression == "x":
        return False
    assert is_matched(word_expression), "Mismatched parentheses in " + word_expression #at the very least, the whole word should be matched
    for ind in range(1, len(word_expression)):
        if is_matched(word_expression, ind): #if we find a set of closed brackets 
            return False #then the expression is not closed
    return True

'''
Parameters
----------
word_expression : string
                  A word_expression which has redundant outer parentheses on it.
Returns
----------
stripped_expression : Returns string
                      The same expression, with the outer parentheses removed.
'''
def remove_outer_pars(word_expression):
    ''' Helper for split_binary_word.'''
    # print(word_expression + " has redundant parenthesis, removing the outer ones.")
    assert is_surrounded(word_expression), "Asked to remove outer parentheses on word which is not surrounded."
    stripped_expression = word_expression[1:-1]
    return stripped_expression

'''
Parameters
----------
word_expression : string

Returns
----------
left, right : string
              The informal expression of a binary word.
Ex: str="x(xx)" outputs "x", "xx".
'''
def split_binary_word(word_expression):
    ''' Finds and returns the left and right components. 
    '''
    # ----------- base cases ----------
    if word_expression == "":
        return None, None
    if word_expression == "x": 
        return "x", None       
    if word_expression == "xx":
        return "x", "x"
    # ---------------------------------

    # at this point, the word has parentheses. So we check that they're matched before moving on.
    assert is_matched(word_expression), "Mismatched parentheses in " + word_expression

    # cases for when we have x(...) of (...)x
    if word_expression[:2] == "x(": 
        return "x", remove_outer_pars(word_expression[1:])   # returns x and ... 
    if word_expression[-2:] == ")x": #
        return remove_outer_pars(word_expression[:-1]), "x"  # returns ... and x
    
    # this is just to catch an unlikely error in which the user put in a word redundantly surrounded by parentheses.
    if is_surrounded(word_expression): 
        return split_binary_word(remove_outer_pars(word_expression))
    
    # in all other cases, we have something of the form (...)(---). So, we need to find the index marking the 
    # end of the left (...)
    else: 
        for ind in range(1, len(word_expression)):
            if is_matched(word_expression, ind): #if we find a closed expression
                # print("match", ind)
                left, right = word_expression[:ind], word_expression[ind:] #returns (...) and (---)
                clean_left = remove_outer_pars(left)
                clean_right = remove_outer_pars(right)
                return clean_left, clean_right
'''
Parameters
----------
word_expression : string

Returns
----------
words_of_len_n : list
'''
def n_binary_words(n):
    ''' (Recrusively) returns a list containing all binary words of length n.
    '''
    words_of_len_n = []
    if n == 1: # Base case
        return [BinaryWord("x")] 
    else:
        # Each binary word w of length n can be written as w = uv where u has length i and v has length n - i.
        # Therefore, we find all such binary words of length n by iterating through i. 
        for i in range(1,n):
            for left_word in n_binary_words(i): # this is u, len i
                for right_word in n_binary_words(n-i): # this is v, len n-i
                    words_of_len_n.append(left_word.tensor(right_word)) # we tensor uv, add it to the list
        return words_of_len_n
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
            self.u = None
            self.v = None
            self.w = None
            self.left = None
            self.right = None
        if expression == "\\alpha_{u,v,w}":
            self.u = source.left
            self.v = source.right.left
            self.w = source.right.right
            self.left = None
            self.right = None
        elif expression[:2] == "1(":
            self.u = None
            self.v = None
            self.w = None
            self.left = AlphaArrow(source.left, source.left)
            self.right = AlphaArrow(source.right, target.right, expression[2:])
        elif expression[-2:] == ")1":
            self.u = None
            self.v = None
            self.w = None
            self.left = AlphaArrow(source.left, target.left, expression[:-2])
            self.right = AlphaArrow(source.right, source.right)

'''
Parameters
----------
source : BinaryWord

Returns
----------
path : List
'''
def alpha_expressions(source):
    ''' Given a binary word source, it returns all the possible alpha-arrow expressions
        with domain source. 
    '''
    paths = []
    if source.len <= 3: # Simple base case. 
        if source.expression == "x(xx)":
            paths+=["\\Alpha"]
        else:
            return []
    else:  
        lefts = source.left.len  
        rights = source.right.len
        if rights > 1: # then we can apply an \alpha, so add it to the list
            paths += ["\\Alpha"]
        if rights == 1: # if the right component is trivial, look at the left component.
            paths += ["(" + expr + ")1" for expr in alpha_expressions(source.left)]
        if lefts == 1: # if the left component is trivial, look at the right. 
            paths += ["1(" + expr + ")"for expr in alpha_expressions(source.right)]
        if lefts > 1 and rights > 1: # neither are trivial, separately look at both the left and right.
            paths += [lefts*"1(" + expr + ")"*lefts for expr in alpha_expressions(source.right) ]
            paths += [rights*"(" + expr + ")1"*rights for expr in alpha_expressions(source.left)]
    return paths # once we're done collecting the paths, return them

# def count_left_ones(alpha_expr):
#     num_left_ones = 0
#     i = 0
#     while i < len(alpha_expr):
#         if alpha_expr[i:2+i] == "1(":
#             num_left_ones +=1 
#             i+=2
#         else:
#             break
#     return num_left_ones

# def count_right_ones(alpha_expr):
#     num_right_ones = 0
#     i = len(alpha_expr)
#     while i <= len(alpha_expr):
#         if alpha_expr[(i-2):i] == ")1":
#             num_right_ones += 1
#             i-=2
#         else:
#             break
#     return num_right_ones

# def remove_single_xs(word, nested_ind, side):
#     assert nested_ind >= 0, "Asked to remove a nonnegative number of elements."
#     # --------- base cases ------------
#     if nested_ind == 0:
#         return word
#     # if word.length == ""
#     # ---------------------------------

#     if side ==  "right":
#         r_len = word.right.len
#         if r_len == nested_ind:
#             return codomain_of_alpha_exp(word.left).tensor(word.right)
#         elif r_len > nested_ind:
#             right = remove_single_xs(word.right, nested_ind, side)
#             return word.left.tensor(right)
#         elif r_len < nested_ind:
#             return remove_single_xs(word.left, nested_ind-r_len, side).tensor(word.right)
#     if side == "left":
#         l_len = word.left.len
#         if l_len == nested_ind:
#             return word.left.tensor(codomain_of_alpha_exp(word.right))
#         elif l_len > nested_ind:
#             left = remove_single_xs(word.left, nested_ind, side)
#             return left.tensor(word.right)
#         elif l_len < nested_ind:
#             return word.left.tensor(remove_single_xs(word.right, nested_ind-l_len, side))

'''
Parameters
----------
source : BinaryWord

Returns
----------
target: BinaryWord
'''
def pure_alpha_arrow(source):
    ''' Helper for target_of_alpha. 
    If the source.expression is of the form u(vw), it returns the binary word (uv)w. 
    '''
    assert source.len >= 3 and source.right.len >= 2, "Cannot apply an \\alpha to " + source.expression
    target_left = source.left.tensor(source.right.left)
    target_right = source.right.right
    target = target_left.tensor(target_right)                
    return target 

'''
Parameters
----------
source : BinaryWord
alpha_expr: string

Returns
----------
target : BinaryWord
'''
def target_of_alpha(source, alpha_expr):
    ''' Given a binary word source and an alpha arrow with domain source, 
        target_of_alpha returns the codomain (a binary word) of the alpha arrow.
    '''
    if alpha_expr == "\\Alpha":
        return pure_alpha_arrow(source)
    elif alpha_expr[:2] == "1(":
        l_len = source.left.len
        return source.left.tensor(target_of_alpha(source.right, alpha_expr[2*l_len:-1*l_len]))
    elif alpha_expr[-2:] == ")1":
        r_len = source.right.len 
        return target_of_alpha(source.left, alpha_expr[1*r_len:-2*r_len]).tensor(source.right)


'''
Parameters
----------
source : BinaryWord

Returns
----------
all_alpha_paths : list
'''
def alpha_paths(source):
    ''' Returns a list consisting of all alpha arrows 
        with domain source. The list consists of tuples of the form 
        (alpha expression, domain, codomain).
    '''
    all_alpha_paths = []
    for path_expr in alpha_expressions(source): # we access 
        path_target = target_of_alpha(source, path_expr)
        path = (path_expr, source, path_target)
        all_alpha_paths.append(path)
    return all_alpha_paths

'''
Parameters
----------
n : int

Returns
----------
paths_dict : list
'''
def alpha_paths_on_n(n):
    ''' Returns a dictionary of the following form. 
        dict = {
            "word_1_of_length_n" = {
                "expression_of_alpha_arrow_with_domain_word_1" = alpha_arrow
                ...
            }
            ...
        }
    '''
    paths_dict = {}
    for word_len_n in n_binary_words(n):
        paths_dict[word_len_n.expression] = {}  
        for path in alpha_paths(word_len_n):
            arrow = path[0]
            paths_dict[word_len_n.expression][arrow.expression] = arrow
    return paths_dict

'''
Parameters
----------
n : int

Returns
----------
int, int 
'''
def nth_associahedron(n):   
    ''' Given an integer n, computes the nth associahedron. This is done by creating a .json file in the local directory of the following form.
        {
            "nodes":[
                {"id" : "word_1_of_length_n_expression"
                 "name": "word_1_of_length_n_expression"
                },
                {"id" : "word_2_of_length_n_expression"
                 "name": "word_2_of_length_n_expression"
                },
                ...
            ]
            "links":[
                {"source":word_1_of_length_n, "target": codomain_of_alpha_arrow_with_domain_word_1},
                ...
            ]
        }  
        The integer output of the function tells us the number of vertices and edges of the associahedron.
    '''
    dict = {} 
    words = []
    paths = []
    for word in n_binary_words(n):
        print(word.expression)
        word_dict = {}
        word_dict["id"] = word.expression
        word_dict["name"] = word.expression
        word_dict["img"] = word.expression + ".jpg"
        words.append(word_dict)
        for path in alpha_paths(word):
            # print(path[0].expression)
            path_dict = {}
            path_dict["source"] = path[1].expression
            path_dict["target"] = path[2].expression
            paths.append(path_dict)
    dict["nodes"] = words
    dict["links"] = paths
    with open("binary_words_of_" + str(n) + ".json", "w") as outfile:
        json.dump(dict, outfile, indent = 4)
    return len(dict["nodes"]), len(dict["links"])