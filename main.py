import gc

class MyClass:
    def __init__(self):
        self.my_object = object()
        self.my_object_name = "my_object"

    def print_object_name(self):
        print(f"The name of my object is '{self.my_object_name}'")

my_object = MyClass()


mydict = gc.get_referrers(my_object)
print(mydict)
print(mydict[0])
dictkeys = mydict[0]
keysList = list(dictkeys.keys())
print(keysList)
print(keysList[11])