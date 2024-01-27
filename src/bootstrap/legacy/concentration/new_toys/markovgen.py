import markovtextgen as mt
import random
def generate(filepath,wordnum):
    m=mt.get_word_list(filepath)
#    print(m)
    if len(m)>100:
        m=random.sample(m,100)
    y=mt.get_ngram_counts(m)
    v=mt.generate_text(y,wordnum)
    return v

if __name__ =="__main__":
    #demo
    g=generate("pypi_indexer.py",4)
    print(g)
