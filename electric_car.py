from car import User

class Privileges(object):
    def __init__(self,privileges = ['can add post','can delete post','can ban user']):
        self.uprivileges = privileges


    def show_privileges(self):
        print ('The privileges include:' + str(self.uprivileges) + '.')

class Admin(User):
    def __init__(self,first_name,last_name):
        super(Admin, self).__init__(first_name,last_name)
        self.admin_privileges = Privileges()
