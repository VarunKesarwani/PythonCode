from abc import ABC,abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    def config(self):
        print('min req: i5 16gb 1tb 1gb')

class laptop(computer):
    def process(self):
        print("running from laptop")

class desktop(computer):
    def process(self):
        print("running from desktop")

class programer:
    def work(self,com):
        print("solve bugs")
        com.process()

#com = computer()
com1 = laptop()
com2 = desktop()

com1.config()

prog1 = programer()
prog1.work(com1)

prog2 = programer()
prog2.work(com2)