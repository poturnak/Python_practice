#! /library/Frameworks/Python.framework/Versions/3.5/python3.5

class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")

a = Restaurant()
print(a.bankrupt)