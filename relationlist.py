__all__ = ['__version__',
           'RelationList',
           'Iterable',
           'Generator',
           '__author__']
__version__ =  '1.0.0b1'
class str2(str):
    def __str__(self):
        return super().__str__().rstrip('\n')
    def __repr__(self):
        return str(self)
__author__= str2('''Python Bugtracker / Github account: wyz23x2
Email: wyz23x2@163.com
''')
del str2
from typing import Iterable
import warnings as _w
class RelationList(object):
    '''Relation list class.'''
    __slots__ = ('lis', 'relations', 'elm')
    def __init__(self, lis:list =None, /):
        if lis is None:
            lis = []
        if isinstance(lis, str):
            lis = list(lis)
        if not isinstance(lis, list):
            raise TypeError("Invaild argument 'lis'.")
        self.lis = lis
        self.relations = []
        self.elm = {}
        for i in range(len(lis)):
            self.elm[lis[i]] = 0
    def __str__(self) -> str:
        '''Run when str() is run.'''
        return str(self.__getattribute__('lis', a=False))
    def __repr__(self) -> tuple:
        '''Run when repr() is run.'''
        return repr((self.__getattribute__('lis', a=False), self.relations, self.elm))
    def __iter__(self) -> Iterable:
        '''Run when iter()/list()/tuple()/set() is run'''
        a = []
        for i in range(len(self.__getattribute__('lis', a=False))):
            a.append((self.__getattribute__('lis', a=False)[i], self.elm[self.__getattribute__('lis', a=False)[i]]))
        return iter(a)
    def __len__(self) -> int:
        '''Run when len() is run.'''
        return len(self.__getattribute__('lis', a=False))           
    def __bool__(self) -> bool:
        '''Run when bool() is run.'''
        return not self.__getattribute__('lis', a=False) == []
    def __eq__(self, other) -> bool:
        '''The == operator.'''
        if isinstance(other, type(self)):
            return (self.__getattribute__('lis', a=False) == other.lis and self.relations == other.relations)
        else:
            return False
    def __ne__(self, other) -> bool:
        '''The != operator.'''
        return not self.__eq__(other)
    def __add__(self, other):
        '''The + operator.'''
        a = self.copy()
        a += other
        return a
    def __radd__(self, other):
        if isinstance(other, list):
            a = self.copy()
            for i in reversed(other):
                a.add(i,index=0)
            return a
        else:
            return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, list):
            for i in range(len(other)):
                self.add(other[i])
        elif isinstance(other, RelationList):
            self.__getattribute__('lis', a=False).extend(other.lis)
            self.relations.extend(other.relations)
            for i in range(len(n:=other.elm)):
                self.elm[list(n.keys())[i]] = list(n.values())[i]
        else:
            return NotImplemented
        return self
    def __and__(self, other):
        if isinstance(other, RelationList):
            a = []
            for i in set(self.relations+other.relations):
                a.append(i)
            return a
        else:
            return NotImplemented
    def __or__(self, other):
        if isinstance(other, RelationList):
            return RelationList(self.__getattribute__('lis', a=False)+other.lis)
        elif isinstance(other, list):
            return RelationList(self.__getattribute__('lis', a=False)+other)
        else:
            return NotImplemented
    def __ror__(self, other):
        if isinstance(other, list):
            return RelationList(other+self.__getattribute__('lis', a=False))
        else:
            return NotImplemented
    def __reversed__(self):
        return RelationList(list(reversed(self.__getattribute__('lis', a=False))))
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
                    if fmt[i+1] == 'T':
                        raise PendingDeprecationWarning("%T format will be removed in v1.3.0.")
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
        return self.__getattribute__('lis', a=False)[key]
    def __setitem__(self, key, value, /):
        if isinstance(key, int):
            key = slice(key,key+1,None)
        if key.step == None:
            step = 1
        if key.stop == None:
            stop = len(self)
        if key.start == None:
            start = 0
        ln = len(self)
        if start > ln or start > ln:
            raise IndexError("index out of range")
        for i in range(key.start,key.stop,key.step):
            self.delete(self.__getattribute__('lis', a=False)[i])
            self.add(value, index=i)
    def __delitem__(self, key, /):
        if isinstance(key, int):
            key = slice(key,key+1,None)
        if key.step == None:
            step = 1
        if key.stop == None:
            stop = len(self)
        if key.start == None:
            start = 0
        ln = len(self)
        if start > ln or start > ln:
            raise IndexError("index out of range")
        x = self.__getattribute__('lis', a=False)[:]
        for i in range(key.start,key.stop,key.step):
            self.delete(x[i])
    def __contains__(self, item) -> bool:
        return item in self.__getattribute__('lis', a=False)
    def __bytes__(self, encoding='utf-8') -> bytes:
        a = list(map(lambda x: type(x), self.__getattribute__('lis', a=False)))
        if a.count(int) < len(a):
            return bytes(''.join(map(lambda x: str(self.__getattribute__('lis', a=False))), encoding))
        else:
            return bytes(self.__getattribute__('lis', a=False))
    def __enter__(self):
        return self
    def __exit__(self, typ, value, trace):
        self.clear_relations()
    def __getattribute__(self, name, a=True):
        if name == 'lis' and a:
            _w.simplefilter('module')
            _w.warn('Directly using .lis is deprecated and will raise an error in v1.3. Please use .value', DeprecationWarning)
        return object.__getattribute__(self, name)
    def __delattr__(self, name):
        raise PermissionError(f"Cannot delete attribute '{name}'.")
    def __dir__(self):
        x = object.__dir__(self)
        try:
            x.remove('lis')
        except ValueError:
            pass
        return x
    @property
    def value(self) -> list:
        '''Returns the value of the list.'''
        import copy
        return copy.deepcopy(self.__getattribute__('lis', a=False))
    def relate(self, val1, val2, /, mode:str ='break', assignment=None):
        '''Creates a relation between two elements.'''
        if val1 not in self.__getattribute__('lis', a=False) and val2 not in self.__getattribute__('lis', a=False):
            raise ValueError(f"Values {val1} and {val2} not found.")
        elif val1 not in self.__getattribute__('lis', a=False):
            raise ValueError(f"Value {val1} not found.")
        elif val2 not in self.__getattribute__('lis', a=False):
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
                self.__getattribute__('lis', a=False).append(val)
            else:
                self.__getattribute__('lis', a=False).insert(index+1, val)
        else:
            self.__getattribute__('lis', a=False).insert(index, val)
        self.elm[val] = 0
    def delete(self, val, /, *, err:str ="raise"):
        '''Deletes an element in the list.'''
        if err not in ("raise", "ignore"):
            raise ValueError(f"Invaild parameter 'err': {err}")
        elif val not in self.__getattribute__('lis', a=False):
            if err == "raise":
                raise ValueError(f"Value {val} not found.")
            elif err == "ignore":
                return False
        else:
            if self.elm[val] == 0:
                self.__getattribute__('lis', a=False).remove(val)
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
                            self.__getattribute__('lis', a=False).remove(val)
                        else:
                            del r[i]
                            self.__getattribute__('lis', a=False).remove(val)
                            self.__getattribute__('lis', a=False).remove(y)
                            del self.elm[val]
                            del self.elm[y]
    def remove_relation(self, val1, val2, /, *, err="raise"):
        if err not in ("raise", "ignore"):
            raise ValueError(f"Invaild argument '{err}' for parameter err.")
        flag = False
        for i in range(len(r := self.relations)):
            if val1 == r[i][0] and val2 == r[i][1]:
                if r[i][2] == 'break': 
                    del r[i]
                    self.elm[val1] -= 1
                    self.elm[val2] -= 1
                    flag = True
                else:
                    flag = True
                    del r[i]
                    self.__getattribute__('lis', a=False).remove(val1)
                    self.__getattribute__('lis', a=False).remove(val2)
                    del self.elm[val]
                    del self.elm[y]
        if not flag and err == "raise":
            raise ValueError(f"Relation between {val1} and {val2} not found.")
    def relate_all(self, mode:str ='break', assignments=None):
        '''Create relations between all elements.'''
        self.clear_relations()
        for i in range(len(li := self.__getattribute__('lis', a=False))-1):
            for j in range(i+1, len(li)-1):
                if not isinstance(assignments, (list, tuple)):
                    self.relate(li[i], li[j], mode, assignments)
                else:
                    try:
                        self.relate(li[i], li[j], mode, assignments[i])
                    except IndexError:
                        self.relate(li[i], li[j], mode, None)
    def erase_relations(self):
        self.__init__(self.value)
    clear_relations = erase_relations
    def related(self, val1, val2, /) -> bool:
        try:
            self.get_relate(val1, val2)
        except ValueError:
            return False
        else:
            return True
    def get_relates(self, key, /) -> list:
        '''Returns all of the relations with the element.'''
        if val not in self.__getattribute__('lis', a=False):
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
    def generator(self, *, func:bool =False):
        def gen():
            yield from self.value
        return gen() if not func else gen
    def copy(self, *, deep:bool =True):
        if deep:
            import copy as c
            return c.deepcopy(self)
        else:
            return self
