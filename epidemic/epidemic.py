from events import Clock, Events, Event
import random
import matplotlib.pyplot as plt
import numpy as np

class People:
    def __init__(self, people_num, clock, events, MAX_AGE, CURE_VARIABILITY, BASE_CURE_TIME, HYGENE_VARIABILITY, R):
        self.people_num = people_num
        self.clock = clock
        self.events = events
        self.people = []

        self.MAX_AGE = MAX_AGE
        self.CURE_VARIABILITY = CURE_VARIABILITY
        self.BASE_CURE_TIME = BASE_CURE_TIME
        self.HYGENE_VARIABILITY = HYGENE_VARIABILITY
        self.R = R

        self.infected_num = 0
        self.cured_num = 0

        self.MIN_X = 0
        self.MAX_X = 75

        self.MIN_Y = 0
        self.MAX_Y = 75

    def populate(self):
        for person in range(self.people_num):
            person_pos = Vector(random.uniform(self.MIN_X, self.MAX_X), random.uniform(self.MIN_Y, self.MAX_Y))
            self.people.append(Person(self.clock, self, self.events, person_pos, self.MAX_AGE, self.CURE_VARIABILITY, self.BASE_CURE_TIME, self.HYGENE_VARIABILITY, self.R))

    def add_connections(self):
        for person in self.people:
            for attempt in range(100):
                other = random.choice(self.people)
                if person.get_distance_between(other) < 10:
                    person.add_neighbour(other)
                    other.add_neighbour(person)

    def infect_random_person(self):
        person = random.choice(self.people)
        person.infect()

    def person_is_infected(self, person):
        self.infected_num += 1

    def person_is_cured(self, person):
        self.infected_num -= 1
        self.cured_num += 1

    def person_is_deimunised(self, person):
        self.cured_num -= 1

    def get_infected_num(self):
        return self.infected_num

    def get_cured_num(self):
        return self.cured_num

class Cure(Event):

    def activate(self):
        self.item.cure()

    def __repr__(self):
        return f"Cure {self.item}"


class Infect(Event):
    def activate(self):
        self.item.infect()

    def __repr__(self):
        return f"Infect {self.item}"


class Deimunise(Event):
    def activate(self):
        self.item.deimunise()

    def __repr__(self):
        return f"Deimunise {self.item}"


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Person:
    def __init__(self, clock, people, events, pos, MAX_AGE, CURE_VARIABILITY, BASE_CURE_TIME, HYGENE_VARIABILITY, R):
        self.clock = clock
        self.people = people
        self.events = events
        self.pos = pos

        self.neighbours = []

        self.age = np.abs(np.random.random() * MAX_AGE)
        self.CURE_VARIABILITY = CURE_VARIABILITY
        self.BASE_CURE_TIME = BASE_CURE_TIME
        self.HYGENE_VARIABILITY = random.gauss(HYGENE_VARIABILITY, 3)
        self.R = R

        self.has_virus = False
        self.immune = False

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

    def get_pos(self):
        return self.pos

    def get_distance_between(self, other):
        return abs(self.pos - other.get_pos())

    def get_cure_time(self):
        time = random.gauss(self.BASE_CURE_TIME, self.CURE_VARIABILITY)
        if time < 1:
            time = 1
        if time > 30:
            time = 30
        return int(time)

    def get_people_to_infect(self, cure_time):
        infection_events = []
        number_to_infect = abs(round(random.gauss(self.R, self.HYGENE_VARIABILITY)))
        #print(number_to_infect)

        for _ in range(number_to_infect):
            time = random.randint(1, cure_time)
            target = random.choice(self.neighbours)
            infection_events.append((Infect(target), time))

        return infection_events

    def get_deimunise_time(self):
        time = np.random.randint(2,3)
        return time

    def infect(self):
        if self.immune or self.has_virus:
            return
        else:
            cure_time = self.get_cure_time()

            infection_events_w_time = self.get_people_to_infect(cure_time)

            self.events.schedule(Cure(self), cure_time + self.clock.get_time())

            for event, time in infection_events_w_time:
                self.events.schedule(event, time)

            self.has_virus = True
            self.people.person_is_infected(self)

    def cure(self):
        if not self.has_virus:
            return
        else:
            self.immune = True
            self.has_virus = False

            deimunise_time = self.get_deimunise_time()

            self.events.schedule(Deimunise(self), deimunise_time + self.clock.get_time())

            self.people.person_is_cured(self)

    def deimunise(self):
        self.immune = False
        self.people.person_is_deimunised(self)

    def __repr__(self):
        return f"<Person at {self.pos}>"

def simulate(clock, events, max_time):
    while clock.get_time() < max_time:
        events.activate_current_events()
        yield
        clock.tick()

def main():
    R = 3

    clock = Clock()
    events = Events(clock)
    people = People(500, clock, events, 50, 5, 5, 2, R)
    people.populate()
    people.add_connections()
    for i in range(2):
        people.infect_random_person()

    infected_num = []
    cured_num = []

    for _ in simulate(clock, events, 50):
        infected_num.append(people.get_infected_num())
        cured_num.append(people.get_cured_num())

    plt.plot(infected_num)
    plt.plot(cured_num)
    #plt.ylim(0,people.people_num)
    plt.show()

if __name__ == '__main__':
    main()
