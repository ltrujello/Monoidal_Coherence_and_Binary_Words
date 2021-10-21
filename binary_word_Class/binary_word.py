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
        assert is_matched(expression), "Parentheses are mismatched"
        self.expression = expression  # save the binary word expression
        self.x_expression = swap_letters_for_x(expression)
        # This is our base case. 
        if self.x_expression == "x":
            self.left = None
            self.right = None
            self.form = "(x)"
            self.len = 1
            self.idlen = 0
            self.rank = 0
        elif self.x_expression == "e":
            self.left = None
            self.right = None
            self.form = "(e)"
            self.len = 0
            self.idlen = 1
            self.rank = 0
        # If we're not at out base case, then split the word.
        else:
            left, right = swap_x_for_letters(self.x_expression, self.expression,
                                             True)  # we split the binary word, then add the letters back
            self.left = BinaryWord(left)
            self.right = BinaryWord(right)
            self.len = self.left.len + self.right.len
            self.idlen = self.left.idlen + self.right.idlen
            self.rank = self.left.rank + self.right.rank + self.right.len + self.right.idlen - 1
            self.full_rank = self.rank + self.idlen
        self.form = self.add_formal_pars()  # also save the formalized expression. Note this needs to execute at the end, not earlier.

    def tensor(self, right_word):
        '''Compute the tensor product of two binary words.
        '''
        left = self.x_expression
        right = right_word.x_expression

        # If there are redundant parentheses, remove them, because we may add parentheses later 
        if is_surrounded(left):
            left = remove_outer_pars(left)
        if is_surrounded(right):
            right = remove_outer_pars(right)

        ''' of concern is the case when we are tensoring x. Because we want the expression 
        of the binary word to be informal, i.e., natural for the reader, we need to make sure we don't put redundant 
        parentheses on individual x's.
        '''
        if left == "x" and right == "x":
            prod_expression = left + right  # no parentheses

        elif left == "e" and right == "e":
            prod_expression = left + right  # no parentheses

        # If this is true, then the right is not "x" 
        elif left == "x":
            prod_expression = left + "(" + right + ")"  # just parentheses for the right

        # If this is true, then the left is not "x"
        elif right == "x":
            prod_expression = "(" + left + ")" + right  # just parentheses for the left

        # If this is true, then the right is not "e" 
        elif left == "e":
            prod_expression = left + "(" + right + ")"  # just parentheses for the right

        # If this is true, then the left is not "e"
        elif right == "e":
            prod_expression = "(" + left + ")" + right  # just parentheses for the left

        # in all other cases, we do want to produce an expression of the form (...)(---).
        else:
            prod_expression = "(" + left + ")" + "(" + right + ")"  # parentheses for left and right

        final_expression = swap_x_for_letters(prod_expression, self.expression + right_word.expression)
        product = BinaryWord(final_expression)
        return product


    def add_formal_pars(self):
        '''adds the formal parentheses to a binary word expression. E.g., x(xx) => (x)((x)(x))
        '''
        # Our base case is x or xx, since we expect the user to write x(xx), (x(xx))x, etc.
        if self.x_expression == "x":
            return "(x)"
        elif self.x_expression == "xx":
            return "(x)(x)"
        elif self.x_expression == "e":
            return "(e)"
        elif self.x_expression == "ee":
            return "(e)(e)"
        elif self.x_expression == "xe":
            return "(x)(e)"
        elif self.x_expression == "ex":
            return "(e)(x)"
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


def swap_letters_for_x(letter_expression):
    '''Replaces every letter in an expression with 'x'. This allows the user  
    the convenience to write whatever they want, e.g. A(BC), while behind the scenes, we work with x, e.g. x(xx).  

    Note: I will be interpreted as an identity.
    '''
    word_list = list(letter_expression)
    for ind in range(0, len(word_list)):
        if word_list[ind] != "(" and word_list[ind] != ")":
            if word_list[ind] == 'I':
                word_list[ind] = 'e'
            else:
                word_list[ind] = 'x'
    swapped_word = "".join(word_list)
    return swapped_word

def swap_x_for_letters(x_expression, letter_expression, left_right=False):
    print(x_expression, letter_expression)
    if left_right == True:
        left, right = split_binary_word(x_expression)
        num_left_xs = left.count("x")
        j = 0
        pos = 0
        for ind in range(0, len(x_expression)):
            if x_expression[j] == "x":
                j += 1
            elif j == num_left_xs:
                pos = ind
                break
        return swap_x_for_letters(left, letter_expression), swap_x_for_letters(right, letter_expression[pos:])
    letters = letter_expression.replace("(", "").replace(")", "")  # removes parentheses
    ith_letter = 0
    word_list = list(x_expression)
    for ind in range(0, len(word_list)):
        if word_list[ind] != "(" and word_list[ind] != ")":
            word_list[ind] = letters[ith_letter]
            ith_letter += 1
    swapped_word = "".join(word_list)
    return swapped_word


def parenthesis_tracker(word_expression, index=None):
    """ Counts parenthesis-matches up to index. By default, index = length of the word. """
    if index is None:  # work-around of defining default param in terms of other param
        index = len(word_expression)

    assert index <= len(word_expression), "index tracker too large"
    num_left_par = 0  # number of left parenthesis
    num_right_par = 0  # number of right parenthesis
    for ind in range(0, index):
        letter = word_expression[ind]
        if letter == "(":  # if we find a left parenthesis
            num_left_par += 1
        if letter == ")":  # if we find a right parenthesis
            num_right_par += 1
    par_count = num_left_par - num_right_par
    return par_count


def is_matched(word_expression, index=None):
    """ Helper for is_surround. This is a tool to figure out if the word has a correctly matched parenthesis up to desired index.
       By default, the index is the length of the word.
       A user has input and incorrect word if this is false when index = len(word_expression). 
    """
    if index is None:  # work-around of defining default param in terms of other param
        index = len(word_expression)
    assert index > 0, "Checking matched parenthesis at index = 0 is not logical."
    par_count = parenthesis_tracker(word_expression, index)
    if par_count != 0:
        return False
    else:
        return True


def is_surrounded(word_expression):
    """Helper for split_binary_word. Detects if the expression is already surrounded, or enclosed, in backets.
    Some surrounded words: (x), (xx), (x(xx)), ... """
    if word_expression == "x" or word_expression == "e":
        return False
    assert is_matched(
        word_expression), "Mismatched parentheses in " + word_expression  # at the very least, the whole word should be matched
    for ind in range(1, len(word_expression)):
        if is_matched(word_expression, ind):  # if we find a set of closed brackets
            return False  # then the expression is not closed
    return True


def remove_outer_pars(word_expression):
    """Helper for split_binary_word."""
    # print(word_expression + " has redundant parenthesis, removing the outer ones.")
    assert is_surrounded(word_expression), "Asked to remove outer parentheses on word which is not surrounded."
    stripped_expression = word_expression[1:-1]
    return stripped_expression


def split_binary_word(word_expression):
    """ Finds and returns the left and right components. """
    # Base cases
    if word_expression == "":
        return None, None
    elif word_expression == "x":
        return "x", None
    elif word_expression == "xx":
        return "x", "x"
    elif word_expression == "e":
        return "e", None
    elif word_expression == "ee":
        return "e", "e"
    elif word_expression == "ex":
        return "e", "x"
    elif word_expression == "xe":
        return "x", "e"
    # At this point, the word has parentheses. So we check that they're matched before moving on.
    assert is_matched(word_expression), "Mismatched parentheses in " + word_expression

    # Cases for when we have x(...) of (...)x
    if word_expression[:2] == "x(":
        return "x", remove_outer_pars(word_expression[1:])  # returns x and ...
    if word_expression[-2:] == ")x":  #
        return remove_outer_pars(word_expression[:-1]), "x"  # returns ... and x

    # Cases for when we have e(...) of (...)e
    if word_expression[:2] == "e(":
        return "e", remove_outer_pars(word_expression[1:])  # returns e and ...
    if word_expression[-2:] == ")e":  #
        return remove_outer_pars(word_expression[:-1]), "e"  # returns ... and e

    # This is just to catch an unlikely error in which the user put in a word redundantly surrounded by parentheses.
    if is_surrounded(word_expression):
        return split_binary_word(remove_outer_pars(word_expression))

    # In all other cases, we have something of the form (...)(---). So, we need to find the index marking the
    # end of the left (...)
    else:
        for ind in range(1, len(word_expression)):
            if is_matched(word_expression, ind):  # if we find a closed expression
                # print("match", ind)
                left, right = word_expression[:ind], word_expression[ind:]  # returns (...) and (---)
                clean_left = remove_outer_pars(left)
                clean_right = remove_outer_pars(right)
                return clean_left, clean_right
