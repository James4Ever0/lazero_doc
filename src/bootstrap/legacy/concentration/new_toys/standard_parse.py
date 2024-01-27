import subprocess
def getReal(a):
    assert type(a)==str
    x="echo \"{}\" | php no_extra.php".format(a)
#    return subprocess.check_output([x], stderr=subprocess.STDOUT)
    return subprocess.getstatusoutput(x)[1]

def getNormal(a):
    assert type(a)==str
    return subprocess.getstatusoutput(a)

def getEncoding(a):
    return getNormal("chardet {}".format(a))
