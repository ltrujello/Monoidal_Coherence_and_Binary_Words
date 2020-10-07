# This program is for (pure) binary words. A binary word is 
# defined recursively as follows: 
#   The symbol x is a binary word.
#   If u, v are binary words, so is (u)(v).
# Binary words are usually written more informally as x(xx), (xx)x, etc. 
# So, every binary word can be written as (u)(v) for some smaller binary words (except x). 

# A class for binary words. The constructor is recursive.
# An example: word = BinaryWord("x(x(xx))"). It calculates its length, and all of the substructures
# of x(x(xx)), which is harder to think about when we include more and more x's. 

class BinaryWord:
    def __init__(self, form="(x)"): 
            self.form = form # save the binary word expression
            self.formal_form = add_parenthesis(form) # also save the formalized expression
            # This is our base case. 
            if form == "(x)": 
                self.left = None
                self.right = None
                self.length = 1
            # If we're not at out base case, then split the word.
            else:                    
                left, right = split_binary_word(self.formal_form) #we split the binary word
                self.left = BinaryWord(left) 
                self.right = BinaryWord(right)
                self.length = self.left.length + self.right.length

def tensor_words(word1, word2):
    product = BinaryWord( "("+word1.form+")" + "("+word2.form+")")
    return product

class Alpha:
    def __init__(self, source, target): 
        self.source = source
        self.target = target
        # self.source = source
        # if self.target.left.left == source.left and\
        #    self.target.left.right == source.right.left and\
        #    self.target.right.right == source.right.right

# Input: Binary Word. Output: Binary Word with formal parenthesis.
# Ex: x(xx) is rewritten more formally as (x)((x)(x)).
def add_parenthesis(word_expression):  
    # We have three cases.
    new_expression = word_expression.replace("x(", "(x)(")  #...x(... becomes ...(x)(...
    new_expression = new_expression.replace(")x", ")(x)")   #...)x... becomes ...)(x)...
    new_expression = new_expression.replace("xx", "(x)(x)") #...xx... becomes ...(x)(x)...
    return new_expression 

# Input: (formally parenthesized) Binary Word. Output: nonnegtive integer.
# For a binary word w = u \otimes v, we find u, v, and output them.
# Ex: str="(x)((x)(x))" outputs "(x)", "(x)(x)".
def split_binary_word(word_expression):
    num_left_par=0  # number of left parenthesis
    num_right_par=0 # number of right parenthesis
    sep_index=0     # the index for separation
    for letter_index in range(0,len(word_expression)):
        letter = word_expression[letter_index]
        if letter == "(": #if we find a left parenthesis
            num_left_par+=1 
        if letter == ")": #if we find a right parenthesis
            num_right_par +=1
            if num_right_par - num_left_par ==0: 
                sep_index= letter_index
                break
    assert sep_index != 0, "Input had mismatched left and right parenthesis."
    left = word_expression[:sep_index+1]
    right = word_expression[sep_index+1:]
    #we're done, but we just want to remove extra needless paranthesis. e.g. ((x)). 
    #this requires separately checking the left and the right words.
    print("split!")
    if left[:2] == "((" and left[-2:] == "))":
        left = left[1:-1]
    if right[:2] == "((" and right[-2:] == "))":
        right = right[1:-1]
    return left, right

# Input: binary word.
# Output: rank.
# For a binary word w = u \otimes v, we define 
# r(w) = r(u) + r(v) + length(v) - 1.
def rank(word):
    if word.form == "(x)":
        return 0
    else:
        return rank(word.left) + rank(word.right) + word.right.length - 1

# Input: two binary words.
# Outpit: lists of paths. 
def alpha_paths(source):
    target = BinaryWord()
    target.left = source.


    if rank(source) <= rank(target):
        return [], "No alpha-arrows."

    if target.left.left.form == source.left.form and \
    target.left.right.form == source.right.left.form and \
    target.right.form == source.right.right.form:
        return [("alpha", Alpha(source, target))]

    if source.left.form == target.left.form:
        return [("1\otimes \\alpha", Alpha(source, target))] \
        + alpha_paths(source.right, target.right)
    
    if source.right.form == target.right.form:
        return [("\\alpha \otimes 1"), Alpha(source, target)] \
        + alpha_paths(source.left, target.left)



