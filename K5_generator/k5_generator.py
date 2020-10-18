# How to use.
# 1. Open up terminal and cd to this file directory.
# To build the associahedron with objects A,B,C,D,E
# enter "python3 pentagon_generator.py A B C D E".
# The file will run, print "meow," and save the .tex in the file directory.


import os 
import argparse
def main(args):
    output_string = "\\begin{{center}}\n" \
    + "     \\begin{{tikzcd}}\n" \
        + "          &[-2cm]\n"\
        + "          &[-2.5cm]\n"\
        + "          &[-1cm]\n"\
        + "          {A} (({B}  {C})  ({D}  {E}))\n"\
        + "          \\arrow[dll, swap, \"1_{{{A}}}\\otimes \\alpha_{{{B} {C},{D},{E}}}\"]\n"\
        + "          \\arrow[drr, \"\\alpha_{{{A},{B} {C},{D} {E}}}\"]\n"\
        + "          &[-1cm]\n"\
        + "          &[-2.5cm]\n"\
        + "          &[-2cm]\n"\
        + "          \\\\[0.2cm] % 1\n"\
        + "          &\n"\
        + "          {A}((( {B}  {C} ) {D})  {E})\n"\
        + "          \\arrow[dddr, \"\\alpha_{{{A}, {B} ({C} {D}), {E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[<-,Black!30!White, dashed,u]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ({A} ({B}  {C}))  ({D}  {E})\n"\
        + "          \\arrow[dr, \"\\alpha_{{{A},{B},{C}}}\\otimes (1_{{{D}}} \\otimes 1_{{{E}}})\"]\n"\
        + "          \\arrow[dddl, swap, \"\\alpha_{{{A} ({B} {C}), {D}, {E}}}\"]\n"\
        + "          &\n"\
        + "          \\\\[0.4cm] % 2\n"\
        + "          {A} (({B}  ({C}  {D})) {E})\n"\
        + "          \\arrow[ur, \"(1_{{{A}}} \\otimes \\alpha_{{{B},{C},{D}}})\\otimes 1_{{{E}}}\"]\n"\
        + "          \\arrow[ddddr, swap, \"\\alpha_{{{A},{B} {C} {D}, {E}}}\"]\n"\
        + "          \\arrow[<-, drr, dashed, Black!30!White]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          (({A} {B})  {C})  ({D}  {E})\n"\
        + "          \\arrow[<-, Black!30!White, dashed, dll]\n"\
        + "          \\arrow[ddddl, \"\\alpha_{{({A} {B}) {C}, {D}, {E}}}\"]\n"\
        + "          \\\\[-0.7cm] %2.5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[<-, Black!30!White, dashed, uur]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[<-, Black!30!White, dashed, uul]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[0.2cm] % 3\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ({A} (({B}  {C})  {D}))  {E}\n"\
        + "          \\arrow[rr, \"\\alpha_{{{A}, {B} {C}, {D}}}\\otimes 1_{{{E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          (({A} ({B}  {C})) {D})  {E}\n"\
        + "          \\arrow[ddr, swap, \"(\\alpha_{{{A},{B},{C}}}\\otimes 1_{{{D}}})\\otimes 1_{{{E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[-0.7cm] %3.5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[<-, Black!30!White, dashed, uur]\n"\
        + "          \\arrow[<-, Black!30!White, dashed, uul]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[0.4cm] % 4\n"\
        + "          &\n"\
        + "          ({A} ({B}  ({C}  {D})))  {E}\n"\
        + "          \\arrow[uur, swap, \"(1_{{{A}}} \\otimes \\alpha_{{{B},{C},{D}}}) \\otimes 1_{{{E}}}\"]\n"\
        + "          \\arrow[drr, swap, \"\\alpha_{{{A}, {B}, {C} {D}}} \\otimes 1_{{{E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ((({A} {B})  {C})  {D})  {E}\n"\
        + "          &\n"\
        + "          \\\\[0.2cm] % 5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          (({A} {B})  ({C}  {D}))  {E}\n"\
        + "          \\arrow[urr, swap, \"\\alpha_{{{A} {B}, {C}, {D}}}\\otimes 1_{{{E}}}\"]\n"\
        + "          \\arrow[<-, uu, dashed, Black!30!White]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "     \\end{{tikzcd}}\n"\
+ "\\end{{center}}\n"\
+ "\\begin{{center}}\n"\
    + "     \\begin{{tikzcd}}\n"\
        + "          &[-2cm]\n"\
        + "          &[-2.5cm]\n"\
        + "          &[-1cm]\n"\
        + "          {A} (({B}  {C})  ({D}  {E}))\n"\
        + "          \\arrow[drr, \"1_{{{A}}}\\otimes \\alpha_{{{B} {C},{D},{E}}}\"]\n"\
        + "          \\arrow[dll, swap, \"\\alpha_{{{A},{B} {C},{D} {E}}}\"]\n"\
        + "          &[-1cm]\n"\
        + "          &[-2.5cm]\n"\
        + "          &[-2cm]\n"\
        + "          \\\\[0.2cm] % 1\n"\
        + "          &\n"\
        + "          ({A} ({B}  {C}))  ({D}  {E})\n"\
        + "          \\arrow[dl, swap, \"\\alpha_{{{A},{B},{C}}}\\otimes (1_{{{D}}} \\otimes 1_{{{E}}})\"]\n"\
        + "          \\arrow[dddr, Black!30!White, dashed]\n"\
        + "          &\n"\
        + "          & \n"\
        + "          {A} ({B} ({C} ({D} {E})))\n"\
        + "          \\arrow[u, \"1_{{{A}}}\\otimes \\alpha_{{{B},{C},{D} {E}}}\"]\n"\
        + "          \\arrow[ddl, swap, \"\\alpha_{{{A},{B}, {C} ({D} {E})}}\"]\n"\
        + "          \\arrow[ddr, \"1_{{{A}}}\\otimes(1_{{{B}}}\\otimes \\alpha_{{{C},{D},{E}}})\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          {A}((( {B}  {C} ) {D})  {E})\n"\
        + "          \\arrow[dddl,dashed, Black!30!White]\n"\
        + "          &\n"\
        + "          \\\\[0.4cm] % 2\n"\
        + "          (({A} {B})  {C})  ({D}  {E})\n"\
        + "          \\arrow[ddddr, swap, \"\\alpha_{{({A} {B}){C}, {D}, {E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          {A} (({B}  ({C}  {D})) {E})\n"\
        + "          \\arrow[swap, ul, \"(1_{{{A}}} \\otimes \\alpha_{{{B},{C},{D}}})\\otimes 1_{{{E}}}\"]\n"\
        + "          \\arrow[swap, ddddl, swap, \"\\alpha_{{{A},{B} {C} {D}, {E}}}\"]\n"\
        + "          \\\\[-0.7cm] %2.5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ({A} {B})({C} ({D} {E}))\n"\
        + "          \\arrow[ull, swap, \"\\alpha_{{{A} {B}, {C}, {D} {E}}}\", \n"\
        + "          start anchor = {{[yshift=-0.25cm]}},\n"\
        + "          end anchor = {{[xshift=-0.5cm]}} ]\n"\
        + "          \\arrow[ddr,swap,\"(1_{{{A}}}\\otimes 1_{{{B}}}) \\otimes \\alpha_{{{C},{D},{E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          {A} ({B} (({C} {D}){E} )\n"\
        + "          \\arrow[urr, swap, \"1_{{{A}}}\\otimes \\alpha_{{{B}, {C} {D}, {E}}}\",\n"\
        + "          start anchor = {{[yshift=-0.25cm]}},\n"\
        + "          end anchor = {{[xshift=1cm]}}]\n"\
        + "          \\arrow[ddl, \"\\alpha_{{{A},{B},({C} {D}) {E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[1cm] % 3\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[Black!30!White, dashed, ddl]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\textcolor{{Black!30!White}}{{\\bullet}}\n"\
        + "          \\arrow[swap, ll, dashed, Black!30!White]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[-0.7cm] %3.5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ({A} {B})(({C} {D}){E})\n"\
        + "          \\arrow[dd, \"\\alpha_{{{A} {B}, {C} {D}, {E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          \\\\[0.4cm] % 4\n"\
        + "          &\n"\
        + "          ((({A} {B})  {C})  {D})  {E}\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          ({A} ({B}  ({C}  {D})))  {E}\n"\
        + "          \\arrow[Black!30!White, dashed, uul]\n"\
        + "          \\arrow[swap, dll, swap, \"\\alpha_{{{A}, {B}, {C} {D}}} \\otimes 1_{{{E}}}\"]\n"\
        + "          &\n"\
        + "          \\\\[0.2cm] % 5\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
        + "          (({A} {B})  ({C}  {D}))  {E}\n"\
        + "          \\arrow[swap, ull, swap, \"\\alpha_{{{A} {B}, {C}, {D}}}\\otimes 1_{{{E}}}\"]\n"\
        + "          &\n"\
        + "          &\n"\
        + "          &\n"\
    + "     \\end{{tikzcd}}\n"\
+ "\\end{{center}}"

    file = open('k5'\
    + '_'+ args.A + '_' + args.B + '_' + args.C + '_' + args.D + '_' + args.E +'.tex', 'w')
    file.write(output_string.format(A=args.A, B=args.B, C=args.C, D=args.D, E =args.E ))
    file.close()
    print("meow")

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("A")
    parser.add_argument("B")
    parser.add_argument("C")
    parser.add_argument("D")
    parser.add_argument("E")

    args = parser.parse_args()
    main(args)



# os.system("latex finite_abelian_factorization.tex")
# os.system("pdflatex finite_abelian_factorization.tex")
# os.system("open finite_abelian_factorization.pdf")
