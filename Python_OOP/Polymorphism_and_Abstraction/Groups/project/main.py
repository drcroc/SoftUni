class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, person):
        return Person(self.name, person.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, people):
        return Group(f"{self.name} {people.name}", self.people + people.people)

    def __getitem__(self, item):
        return f'Person {item}: {self.people[item]}'

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(str(x) for x in self.people)}"

