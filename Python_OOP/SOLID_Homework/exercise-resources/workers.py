from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")


class LazyWorker(BaseWorker):
    def work(self):
        print("Uf, I don't want to work...")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f'`worker` must be of type {BaseWorker}')

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
