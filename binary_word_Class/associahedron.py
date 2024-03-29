import json
from binary_word import BinaryWord


def n_binary_words(n):
    """ Returns a list containing all binary words of length n.
        Each binary word w of length n can be written as w = uv where u has length i and v has length n - i.
        Therefore, we find all such binary words of length n by iterating through i.
    """
    words_of_len_n = []
    if n == 1:  # Base case
        return [BinaryWord("x")]
    else:
        for i in range(1, n):
            for left_word in n_binary_words(i):  # This is u, with length i
                for right_word in n_binary_words(n - i):  # This is v, length n - i
                    words_of_len_n.append(left_word.tensor(right_word))  # We tensor uv, add it to the list
        return words_of_len_n


def alpha_expressions(source):
    """ Given a binary word source, it returns all the possible alpha-arrow expressions with domain source."""
    paths = []
    if source.len <= 3:  # Simple base case
        if source.expression == "x(xx)":
            paths += ["\\Alpha"]
        else:
            return []
    else:
        lefts = source.left.len
        rights = source.right.len
        if rights > 1:  # Then we can apply an \alpha, so add it to the list
            paths += ["\\Alpha"]
        if rights == 1:  # If the right component is trivial, look at the left component.
            paths += ["(" + expr + ")1" for expr in alpha_expressions(source.left)]
        if lefts == 1:  # If the left component is trivial, look at the right.
            paths += ["1(" + expr + ")" for expr in alpha_expressions(source.right)]
        if lefts > 1 and rights > 1:  # Neither are trivial, separately look at both the left and right.
            paths += [lefts * "1(" + expr + ")" * lefts for expr in alpha_expressions(source.right)]
            paths += [rights * "(" + expr + ")1" * rights for expr in alpha_expressions(source.left)]
    return paths


def pure_alpha_arrow(source):
    """ If the source.expression is of the form u(vw), it returns the binary word (uv)w."""
    assert source.len >= 3 and source.right.len >= 2, "Cannot apply an \\alpha to " + source.expression
    target_left = source.left.tensor(source.right.left)
    target_right = source.right.right
    target = target_left.tensor(target_right)
    return target


def target_of_alpha(source, alpha_expr):
    """ Given a binary word source and an alpha arrow with domain source,
    target_of_alpha returns the codomain (a binary word) of the alpha arrow."""
    if alpha_expr == "\\Alpha":
        return pure_alpha_arrow(source)
    elif alpha_expr[:2] == "1(":
        l_len = source.left.len
        return source.left.tensor(target_of_alpha(source.right, alpha_expr[2 * l_len:-1 * l_len]))
    elif alpha_expr[-2:] == ")1":
        r_len = source.right.len
        return target_of_alpha(source.left, alpha_expr[1 * r_len:-2 * r_len]).tensor(source.right)


def alpha_paths(source):
    """ Returns a list consisting of all alpha arrows
    with domain source. The list consists of tuples of the form
    (alpha expression, domain, codomain). """
    all_alpha_paths = []
    for path_expr in alpha_expressions(source):
        path_target = target_of_alpha(source, path_expr)
        path = (path_expr, source, path_target)
        all_alpha_paths.append(path)
    return all_alpha_paths

def nth_associahedron(n):
    """ Given an integer n, computes the nth associahedron. This is done by creating a .json file in the
    local directory of the following form.
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
    """
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
            path_dict = {}
            path_dict["source"] = path[1].expression
            path_dict["target"] = path[2].expression
            paths.append(path_dict)
    dict["nodes"] = words
    dict["links"] = paths
    with open("binary_words_of_" + str(n) + ".json", "w") as outfile:
        json.dump(dict, outfile, indent=4)
    return len(dict["nodes"]), len(dict["links"])
