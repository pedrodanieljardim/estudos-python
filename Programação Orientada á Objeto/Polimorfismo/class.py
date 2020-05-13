from ABC import ABC, abstractmethod

# python só suporta o polimorfismo de sobrecarga....

class A:
    @abstractmethod
    def fala(self, msg):
        pass

class B(A):
    def fala(self, msg):
        print('B está falando {}'.format(msg))

class C(A):
    def fala(self, msg):
        print('C está falando {}'.format(msg))


b = B()
c = C()

b.fala('Aaaaa')
c.fala('n.n')