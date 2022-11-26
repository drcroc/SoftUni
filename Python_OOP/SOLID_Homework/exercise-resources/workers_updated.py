from abc import ABC, abstractmethod
import time


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class AbleToEat(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, AbleToEat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, AbleToEat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")


class BaseManager(ABC):
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        self.worker = worker


class WorkManager(BaseManager):
    def set_worker(self, worker):
        if not isinstance(worker, Workable):
            raise AssertionError(f'`worker` must be of type {Workable}')

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        if not isinstance(worker, AbleToEat):
            raise AssertionError(f'`worker` must be of type {AbleToEat}')

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass