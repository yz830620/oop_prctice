from collections import Container

class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int):
            return False
        return True


class RealOddContainer(Container):
    def __contains__(self, x):
        if not isinstance(x, int):
            return False
        return True

if __name__ == "__main__":
    odd_container = OddContainer()
    real_odd_container = RealOddContainer()

    print("test odd_container which is a duck type")
    print(isinstance(odd_container, Container))
    print(issubclass(OddContainer, Container))
    
    print("test real_odd_container which is an inherent")
    print(isinstance(real_odd_container, Container))
    print(issubclass(RealOddContainer, Container))
