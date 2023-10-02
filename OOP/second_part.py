class MyClass:
    def __init__(self):
        self.public_attribute = "Public attribute"
        self.__private_attribute = "Private attribute"
        self._protected_attribute = "Protected attribute"

    def public_method(self):
        print("This is public method")

    
    def __private_method(self):
        print("This is protected method")
    
    def _protected_method(self):
        print("This is protectedd method")


