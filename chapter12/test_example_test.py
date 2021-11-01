def setup_module(module):
    print(f"setting up MODULE {module.__name__}")

def teardown_module(module):
    print(f"tearing down MODULE {module.__name__}")

def test_a_function():
    print("Running Test Function")

class BaseTest:
    def setup_class(cls):
        print(f"setting up CLASS {cls.__name__}")
    
    def teardown_class(cls):
        print(f"tearing down CLASS {cls.__name__}")

    def setup_method(self, method):
        print(f"setting up Method {method.__name__}")

    def teardown_method(self, method):
        print(f"tearing down METHOD {method.__name__}")

class TestClass1(BaseTest):
    def test_method_1(self):
        print("Running method 1-1")

    def test_method_2(self):
        print("Running method 1-2")

class TestClass2(BaseTest):
    def test_method_1(self):
        print("Running method 2-1")
    
    def test_method_2(self):
        print("Running method 2-2")

        
