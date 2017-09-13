#--coding:utf-8--

#original dictionary
userinfo = {}

#login Flag
islog = False

#Register Function
def register():
    uname = raw_input("Please input username:")
    upass = raw_input("Please input password:")
    userinfo[str(uname)] = upass
    print "Register Successful!"

#login Function
def login():
    global islog
    for count in range(3):
        if (islog):
            break
        uname = raw_input("Please input your username:")
        upass = raw_input("Please input your password:")
        sumcount = 2 - count
        for Name in userinfo.keys():
            if (Name == uname and userinfo[Name] == upass):
                print ("Welcome %s login system!" %uname)
                islog = True
            else:
                if (sumcount != 0):   #
                    print ("Login Faild!You have %d chances left!" %sumcount)
        if (sumcount == 0):
            print ("Sorry,login times reached upper limit.Please login after 30 minutes.")

register()
login()
