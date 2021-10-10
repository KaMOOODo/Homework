"""
Implement the [dining philosophers problem](https://en.wikipedia.org/wiki/Dining_philosophers_problem).
"""

from threading import Thread, Lock
from time import sleep
from random import choice, randint



class Philosopher(Thread):

    def __init__(self, number, own_fork, not_own_fork):
        Thread.__init__(self)
        self.number = number
        self.hungry = False
        self.own_fork = own_fork
        self.not_own_fork = not_own_fork

    def run(self):
        while True:
            sleep(randint(10, 15))
            self.hungry = choice((True, False))
            if self.hungry:
                print(f"The philosopher {self.number} will start dining")
                self.dining()

    def dining(self):
        while True:
            with self.own_fork:
                print(f"The philosopher {self.number} take own fork")
                with self.not_own_fork:
                    print(f"The philosopher {self.number} dining")
                    sleep(6)
                print(f"The philosopher {self.number} finished dining")
            break



forks = [Lock() for i in range(5)]


philosophers = [Philosopher(i, forks[i % 5], forks[(i + 1) % 5]) for i in range(5)]


for philosopher in philosophers:
    philosopher.start()

