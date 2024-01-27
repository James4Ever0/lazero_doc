# schema: position in word. position in the overall paragraph.
def acquire(a):
    with open(a, "r") as f:
        return f.read()

def charDecompose(a):
    # it is a sparse matrix?
    # yes fuck it.
    word_pos=0
    line_pos=0
    sent_pos=0
    fk=[]
    prev_char=""
    # these are shits.
    for x in a:
        # print(a)
        if x == " ":
            if prev_char==" ":
                word_pos+=1
                # fk.append((x,word_pos,line_pos,sent_pos))
            else:
                word_pos=0
                sent_pos+=1
                prev_char=" "
            # fk.append((x,word_pos,line_pos,sent_pos))
            # fk.append((x,word_pos,sent_pos,line_pos))
        elif x == "\n":
            if prev_char=="\n":
                word_pos+=1
                # fk.append((x,word_pos,line_pos,sent_pos))
            else:
                word_pos=0
                sent_pos+=1
                prev_char="\n"
            line_pos+=1
            sent_pos=0
            # fk.append((x,word_pos,sent_pos,line_pos))
        else:
            if prev_char!=x:
                word_pos+=1
                # fk.append((x,word_pos,line_pos,sent_pos))
            else:
                word_pos=0
                sent_pos+=1
                # prev_char="\n"
            # line_pos+=1
            # fk.append((x,word_pos,sent_pos,))
        fk.append((x,word_pos,sent_pos,line_pos))
    return fk,list(set(a))

def img(a,k):
    # use charhot.
    return [(k[x[0]]+1j*x[1],x[2]+1j*x[3]) for x in a]

def oneHot(a):
    return {a[x]:x for x in range(len(a))}
# start your slow reading. just by posing them. select your target. the most valuable one. think you can solve it?
if __name__ == "__main__":
    a=acquire("decompose_0.py")
    b,k=charDecompose(a)
    c=img(b,oneHot(k))
    for x in c:
        print(x)