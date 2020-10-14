import os   
import subprocess
from binary_word import n_binary_words

def gen_symbol(word):
    word_expr = word.expression
    n = word.len
    output_string =\
    "\\documentclass[border=0.7pt]{standalone}\n"\
    +"\\begin{document}\n"\
    +"$" + word_expr + "$" + "\n"\
    +"\\end{document}"
    file = open('../symbol_imgs/binary_words_len_' + str(n) + "/tex/"+ word_expr + '.tex', 'w')
    file.write(output_string)
    file.close()

def compile_and_convert(word):
    word_expr = esc_pars(word.expression)
    n = word.len
    #we first need to compile the .tex to get a .pdf
    pdf_cmd = "pdflatex "\
    + "-halt-on-error "\
    + "-output-directory=../symbol_imgs/binary_words_len_" + str(n) +"/pdfs "\
    + "../symbol_imgs/binary_words_len_"+ str(n) +"/tex/" + word_expr + ".tex"
    subprocess.run(pdf_cmd, shell = True, check = True)

    # next we need to convert the .pdf to a .jpg 
    jpg_cmd ="convert "\
    +"-verbose "\
    +"-density 5000 " \
    +"../symbol_imgs/binary_words_len_"+ str(n) +"/pdfs/" + word_expr + ".pdf "\
    +"-quality 100 "\
    +"-flatten "\
    +"-sharpen 0x1.0 "\
    +"-resize 50% "\
    + "../symbol_imgs/binary_words_len_"+ str(n) +"/imgs/" + word_expr + ".jpg"
    subprocess.run(jpg_cmd, shell = True, check = True)

def esc_pars(word_expression):
    word_expression = word_expression.replace("(", "\(")
    bash_acceptable = word_expression.replace(")", "\)")
    return bash_acceptable

# To dynamically create the .tex files
for n in range(1,8):
    for word in n_binary_words(n):
        gen_symbol(word)

# To dynamically create the pdfs and convert to pdfs
# Warning: for the larger words, this takes a huge amount of time memory
for n in range(1,8):
    for word in n_binary_words(n):
        compile_and_convert(word)


# pdflatex -halt-on-error -output-directory=../symbol_imgs/binary_words_len_3/pdfs ../symbol_imgs/binary_words_len_3/tex/x(xx).tex
# To convert pdf to jpg 
# convert           \
#    -verbose       \
#    -density 5000   \
#     x.pdf      \
#    -quality 100   \
#    -flatten       \
#    -sharpen 0x1.0 \
#    -resize 50%\
#     x1.jpg


