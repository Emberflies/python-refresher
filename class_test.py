class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

    def goodbyefunc(self, user_message):
        user_age = str(self.age)
        if self.age > 40:
            print("Goodbye you are ancient! And " + user_age + " years old.")
        elif self.age < 40:
            print(
                "Goodbye you are young! And "
                + user_age
                + " years old. "
                + "Wdym by: "
                + user_message
            )


p1 = Person("John", 36)
p2 = Person("Bob", 42)
p1.myfunc()
p2.goodbyefunc("Bye computer")
