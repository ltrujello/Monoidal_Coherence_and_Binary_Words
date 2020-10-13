import os 
import argparse
def main(args):
    output_string =\
    "\\documentclass[border=5pt, convert={ density=300 -alpha deactivate, size=1080x800, outext=.png}]{standalone}\n"
    "\\begin{document}\n"
    "$" + args.expression + "$" + "\n"
    "\\end{document}"
    n = len(args.expression)
    file = open('binary_words_len_' + str(n) + "/tex/"+ args.expression + '.tex', 'w')
    file.write(output_string)
    file.close()
    print("meow")

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("expression")

    args = parser.parse_args()
    main(args)