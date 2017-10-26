class User(object):
    def __init__(self,first_name,last_name):
        self.FN = first_name
        self.LN= last_name

    def describe(self):
        print ('The username is: ' + str(self.FN) + str(self.LN))

