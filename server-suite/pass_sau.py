import os
def set_enc_pass(user,s):
    f=open("user","w")
    f.write(user)
    f.close()
    f=open("passwd","w")
    pass_=""
    for i in s:
        pass_=pass_+str(ord(i))+"\n"
    f.write(pass_)
    f.close()
def check_enc_pass(user,s):
    f=open("user","r")
    user_name=f.read()
    f.close()
    f=open("passwd","r")
    #print f.read()
    pass_=""
    for i in f:
        pass_=pass_+chr(int(i))
    f.close()
    if s==pass_ and user==user_name:
        return True
    else:
        return False
