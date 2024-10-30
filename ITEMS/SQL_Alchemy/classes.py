class Person:
    def __init__(self, name: str, age: int, height: float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def sum(self, x: int, y: int) -> int:
        return x + y

person1: Person = Person("Ryan", 21, 235);

print(person1.sum(4, 3))
