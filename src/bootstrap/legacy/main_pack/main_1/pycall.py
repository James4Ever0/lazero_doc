from subprocess import call
import subprocess
# this is redirection. but where is stdin?
# making it online is required, but how do you make it online without basic knowledge?
# asking for knowledge is not wise.
# i can pass it to a file object and then just redirect it to the result!
# how to build a spliter in this thing?
# i mean, i can read through the whole shit, but i cannot let you fuck it up.
# with open("sample.log","w+") as f:
s=["echo", "hello", "world"]
# s=["yes"]
c=call(s,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd="/")
# e=c.communicate()
# print(c)
#  not working.
    # well, knowledge is a good thing.
    # I mean, can we do it at some temp location???
    # what does this shit believe? icons? strings? RA9?
    # it does not matter. it is the process.
    # arithmatic. reverse the sequence?