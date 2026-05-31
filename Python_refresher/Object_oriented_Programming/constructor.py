class MyClass:
    # parametarise constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # non-parametarise constructor
    def __init__(self):
        pass

    def print(self):
        print(f"Name: {self.name} \nEmail: {self.email}")


if __name__ == "__main__":
    my_class_obj = MyClass()
   # my_class_obj.print()
