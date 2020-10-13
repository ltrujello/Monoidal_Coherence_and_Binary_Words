import os   
import argparse
import binary_word_Class

def gen_symbol(word_expression):
    n = len(args.expression)
    output_string =\
    "\\documentclass[border=5pt, convert={ density=300 -alpha deactivate, size=1080x800, outext=.png}]{standalone}\n"
    "\\begin{document}\n"
    "$" + word.expression + "$" + "\n"
    "\\end{document}"
    file = open('binary_words_len_' + str(n) + "/tex/"+ word.expression + '.tex', 'w')
    file.write(output_string)
    file.close()

for n in range(1, 11):
    for word in n_binary_words(n):
        gen_symbol(word.expression)
