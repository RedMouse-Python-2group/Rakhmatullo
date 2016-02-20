__author__ = 'alimovtillo'


# class Par1(object):
#     def name1(self): return 'part1'
#
#
# class Par2(object):
#     def name2(self): return 'part2'
#
#
# class Child(Par1, Par2):
#     pass
#
#
# x = Child()
# print(x.name1())
# print(x.name2())

from abc import ABCMeta, abstractmethod, abstractproperty


class Abstr():
    __metaclass__ = ABCMeta

    @abstractmethod
    def method1(self):
        pass


class Chl(Abstr):
    p = 1


c = Chl()