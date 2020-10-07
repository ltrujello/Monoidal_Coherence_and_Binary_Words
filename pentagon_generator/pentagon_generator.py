# How to use.
# 1. Open up terminal and cd to this file directory.
# To build the pentagon with objects A,B,C,D 
#   enter "python3 pentagon_generator.py A B C D".
# The file will run, print "meow," and save the .tex in the file directory.


import os 
import argparse
def main(args):
    output_string = "\\begin{{center}}\n" \
    + "     \\begin{{tikzcd}}[column sep = 1.2cm, row sep = 2cm]\n" \
    + "          {A} \\otimes (  {B}  \\otimes ( {C}  \\otimes  {D} ))\n" \
    + "          \\arrow[r, shift right = -0.5ex, \" \\alpha_{{ {A}, {B} , {C} \\otimes {D} }}\"]\n" \
    + "          \\arrow[d, shift right = 0.5ex,swap, \"1_{{ {A} }} \\otimes \\alpha_{{ {B}  , {C}, {D} }}\"]\n" \
    + "          & \n" \
    + "          (  {A} \\otimes  {B} )\\otimes( {C} \\otimes {D} )\n" \
    + "          \\arrow[r, shift right = -0.5ex, \" \\alpha_{{ {A} \\otimes  {B}, {C}, {D} }}\"]\n" \
    + "          &\n" \
    + "          ((  {A} \\otimes  {B} )\\otimes {C} )\\otimes {D} \n" \
    + "          \\\\ \n" \
    + "          {A} \\otimes((  {B} \\otimes {C} )\\otimes {D} )\n" \
    + "          \\arrow[rr, shift right = 0.5ex, swap, \" \\alpha_{{ {A},  {B} \\otimes {C}, {D} }}\"]\n" \
    + "          && \n" \
    + "          (  {A} \\otimes(  {B}\\otimes {C} ))\\otimes {D} \n" \
    + "          \\arrow[u, shift right = 0.5ex, swap, \"  \\alpha_{{ {A},  {B}, {C} }} \\otimes 1_{{ {D} }} \"]\n" \
    + "     \\end{{tikzcd}}\n" \
    + "\\end{{center}}"
    file = open('/Users/luketrujillo/Desktop/Senior_year/Senior_thesis/thesis_versions/thesis_sept7/pentagon_generator/pengtagon'\
    + '_'+ args.A + '_' + args.B + '_' + args.C + '_' + args.D +'.tex', 'w')
    file.write(output_string.format(A=args.A, B=args.B, C=args.C, D=args.D ))
    file.close()
    print("meow")

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("A")
    parser.add_argument("B")
    parser.add_argument("C")
    parser.add_argument("D")

    args = parser.parse_args()
    main(args)



# os.system("latex finite_abelian_factorization.tex")
# os.system("pdflatex finite_abelian_factorization.tex")
# os.system("open finite_abelian_factorization.pdf")
