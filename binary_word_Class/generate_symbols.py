import os   
import subprocess
from binary_word import n_binary_words

def gen_symbol(word):
    word_expr = word.expression
    n = word.len
    output_string =\
    "\\documentclass[border=1pt]{standalone}\n"\
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

'''
The process is as follows:
1. Run create_texs to fill up the tex folders with the LaTeX files which make the binary word images. 
2. Run create_jpg_imgs. This will then find the .texs, compile them, and then convert their pdfs to jpgs and 
store them under imgs/words.
3. Run create K_n images. This will find the K_n.texs, compute them, convert their pdfs to jpgs.
'''
#To create the .tex files for the binary word images.
def create_texs():
    for n in range(8,9):
        for word in n_binary_words(n):
            gen_symbol(word)

# To dynamically compile the .texs for the binary word images and 
# convert the pdfs to jpgs. 
# Warning: for the larger words, this takes a huge amount of time and memory.
def create_jpg_imgs():
    for n in range(8,9):
        for word in n_binary_words(n):
            compile_and_convert(word)

# To compile the K_n.tex files and convert their pdfs to imgs.
def create_K_n_imgs():
    for n in range(1, 11):
        pdf_cmd = "pdflatex "\
        + "-halt-on-error "\
        + "-output-directory=../symbol_imgs/K_n/k_" + str(n)\
        + " ../symbol_imgs/K_n/k_" + str(n) + "/k_" + str(n) + ".tex"
        subprocess.run(pdf_cmd, shell = True, check = True)

        # next we need to convert the .pdf to a .jpg 
        jpg_cmd ="convert "\
        +"-verbose "\
        +"-density 5000 " \
        +"../symbol_imgs/K_n/k_"+ str(n) +"/k_"+ str(n) +".pdf "\
        +"-quality 100 "\
        +"-flatten "\
        +"-sharpen 0x1.0 "\
        +"-resize 50% "\
        +"../associahedra_in_3D/imgs/K_n/k_"+ str(n) +".jpg "
        subprocess.run(jpg_cmd, shell = True, check = True)

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
#     x.jpg


