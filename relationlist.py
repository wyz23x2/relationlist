__all__ = ['__version__',
           'RelationList',
           'Iterable',
           'Generator',
           '__author__',
           'str2']
__version__ =  '1.0.0a1' # 0.15.0
class str2(str):
    def __str__(self):
        return super().__str__().rstrip('\n')
    def __repr__(self):
        return str(self)
__author__= str2('''Python Bugtracker account: wyz23x2
Email: wyz23x2@163.com
Be free to contact during:
Monday~Thursday  18:50~21:35
Friday                      18:15~22:00
Saturday~Sunday    10:25~22:00
''')
del str2
from typing import Iterable, Generator
__all__.remove('str2')
class RelationList(object):
    '''Relation list class.'''
    __slots__ = ('lis', 'relations', 'elm')
    def __init__(self, lis:list =[], /):
        if not isinstance(lis, list):
            raise TypeError("Invaild argument 'lis'.")
        self.lis = lis
        self.relations = []
        self.elm = {}
        for i in range(len(lis)):
            self.elm[lis[i]] = 0
    def __str__(self) -> str:
        return str(self.lis)
    def __repr__(self) -> tuple:
        return repr((self.lis, self.relations, self.elm))
    def __iter__(self) -> Iterable:
        a = []
        for i in range(len(self.lis)):
            a.append((self.lis[i], self.elm[self.lis[i]]))
        return iter(a)
    def __len__(self) -> int:
        return len(self.lis)           
    def __bool__(self) -> bool:
        return not self.lis == []
    def __eq__(self, other) -> bool:
        return (self.lis == other.lis and self.relations == other.relations)
    def __ne__(self, other) -> bool:
        return not self.__eq__(self, other)
    def __add__(self, other):
        a = self
        a += other
        return a
    def __radd__(self, other):
        if isinstance(other, list):
            return RelationList(other+self.lis)
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, list):
            for i in range(len(other)):
                self.add(other[i])
        elif isinstance(other, RelationList):
            self.lis.extend(other.lis)
            self.relations.extend(other.relations)
            for i in range(len(n:=other.elm)):
                self.elm[list(n.keys())[i]] = list(n.values())[i]
        else:
            return NotImplemented
        return self
    def __reversed__(self):
        return RelationList(self.lis.reverse())
    def __format__(self, fmt:str ='%L') -> str:
        dic = {'L': self.value, 'R': self.relations, 'E': self.elm, 'T': tuple(self)}
        string = ''
        flag = False
        for i in range(len(fmt)):
            if flag:
                flag = False
                continue
            if fmt[i] == '%' and i != len(fmt):
                if fmt[i+1] in list(dic.keys()):
                    string += str(dic[fmt[i+1]])
                    flag = True
                else:
                    flag = False
                    string += fmt[i]
            else:
                flag = False
                string += fmt[i]
        return string
    def __getitem__(self, key, /):
        return self.lis[key]
    def __setitem__(self, key, value, /):
        self.delete(value)
        self.add(value, index=key)
    def __delitem__(self, key, /):
        self.delete(self.lis[key])
    def __contains__(self, item) -> bool:
        return item in self.lis
    def __bytes__(self, encoding='utf-8') -> bytes:
        a = list(map(lambda x: type(x), self.lis))
        if a.count(int) < len(a):
            return bytes(''.join(self.lis), encoding)
        else:
            return bytes(self.lis)
    @property
    def value(self) -> list:
        '''Returns the value of the list.'''
        return self.lis
    def relate(self, val1, val2, /, mode:str ='break', assignment=None):
        '''Creates a relation between two elements.'''
        if val1 not in self.lis and val2 not in self.lis:
            raise ValueError(f"Values {val1} and {val2} not found.")
        elif val1 not in self.lis:
            raise ValueError(f"Value {val1} not found.")
        elif val2 not in self.lis:
            raise ValueError(f"Value {val2} not found.")
        if mode not in ('break', 'delete'):
            raise ValueError("Invaild mode.")
        if (val1, val2, mode, assignment) in self.relations:
            self.remove_relation(val1, val2)
        self.relations.append((val1, val2, mode, assignment))
        self.elm[val1] += 1
        self.elm[val2] += 1
    def add(self, val, /, index:int =-1):
        '''Appends a new element to the assigned index in the list.'''
        if index < 0:
            if index == -1:
                self.lis.append(val)
            else:
                self.lis.insert(index+1, val)
        else:
            self.lis.insert(index, val)
        self.elm[val] = 0
    def delete(self, val, /, *, err:str ="raise"):
        '''Deletes an element in the list.'''
        if err not in ("raise", "ignore", "append"):
            raise ValueError(f"Invaild parameter 'err': {err}")
        elif val not in self.lis:
            if err == "raise":
                raise ValueError(f"Value {val} not found.")
            elif err == "ignore":
                return False
            elif err == "append":
                self.lis.add(val)
        else:
            if self.elm[val] == 0:
                self.lis.remove(val)
                del self.elm[val]
            else:
                for i in range(len(r := self.relations)):
                    if val in (r[i][0], r[i][1]):
                        y = r[i][1] if val == r[i][0] else r[i][0]
                        if r[i][2] == 'break': 
                            print(r[i])
                            print(val)
                            del r[i]
                            self.elm[y] -= 1
                            del self.elm[val]
                            self.lis.remove(val)
                        else:
                            del r[i]
                            self.lis.remove(val)
                            self.lis.remove(y)
                            del self.elm[val]
                            del self.elm[y]
    def remove_relation(self, val1, val2, /):
        for i in range(len(r := self.relations)):
            if val1 == r[i][0] and var2 == r[i][1]:
                if r[i][2] == 'break': 
                    del r[i]
                    self.elm[val1] -= 1
                    self.elm[val2] -= 1
                else:
                    del r[i]
                    self.lis.remove(val1)
                    self.lis.remove(val2)
                    del self.elm[val]
                    del self.elm[y]
    def relate_all(self, mode:str ='break', assignments=None):
        '''Create relations between all elements.'''
        self.clear_relations()
        for i in range(len(li := self.lis)-1):
            for j in range(i+1, len(li)-1):
                if not isinstance(assignments, (list, tuple)):
                    self.relate(li[i], li[j], mode, assignments)
                else:
                    try:
                        self.relate(li[i], li[j], mode, assignments[i])
                    except IndexError:
                        self.relate(li[i], li[j], mode, None)
    def clear_relations(self):
        self = RelationList(self.lis)
    def related(self, val1, val2, /) -> bool:
        try:
            self.get_relate(val1, val2)
        except ValueError:
            return False
        else:
            return True
    def get_relates(self, key, /) -> list:
        '''Returns all of the relations with the element.'''
        if val not in self.lis:
            raise KeyError(f"Key {val} not found.")
        a = []
        for i in range(len(r := self.relations)):
            if val in r[i][:2]:
                a.append(r[i])
        return a
    def get_relate(self, val1, val2, /) -> tuple:
        '''Returns the relation information between two values.'''
        for i in range(len(r := self.relations)):
            if val1 in r[i][:2] and val2 in r[i][:2]:
                return r[i]
        else:
            raise ValueError(f"Relation between {val1} and {val2} not found.")
    def generator(self, *, func:bool =False) -> (Generator, callable):
        a = list(self)
        def gen():
            for i in a:
                yield i
        return gen() if not func else gen
    def copy(self, *, deep:bool =True):
        if bool(deep) is not deep:
            import warnings as w
            w.simplefilter(action="default")
            w.warn("copy() 'deep' parameter should be bool.", Warning)
            deep = bool(deep)
            del w
        if deep:
            import copy as c
            return c.deepcopy(self)
        else:
            return self
