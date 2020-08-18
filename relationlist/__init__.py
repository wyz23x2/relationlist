__all__ = ['__version__',
           'RelationList',
           '__author__',
           'ver']
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
from .ver import raw as __version__
import warnings as _w
import pickle as _pickle
class RelationList(object):
    '''Relation list class.'''
    __slots__ = ('lis', 'relations', 'elm')
    def __init__(self, iterable:Iterable =(), /):
        if iterable is None:
            iterable = []
        try:
            iterable = list(iterable)
        except Exception:
            raise TypeError("Invaild argument 'iterable'.")
        self.lis = iterable
        self.relations = []
        self.elm = {}
        for i in range(len(iterable)):
            self.elm[iterable[i]] = 0
    def __str__(self) -> str:
        '''Ran when str() is run.'''
        return str(self.__getattribute__('lis', _=False))
    def __repr__(self) -> str:
        '''Ran when repr() is run.'''
        return f"RelationList({str(self.__getattribute__('lis', _=False)).lstrip('[').rstrip(']')})"
    def __iter__(self) -> Iterable:
        '''Ran when iter()/list()/tuple()/set() is run.'''
        return iter(self.value)
    def __len__(self) -> int:
        '''Ran when len() is run.'''
        return len(self.__getattribute__('lis', _=False))           
    def __bool__(self) -> bool:
        '''Ran when bool() is run.'''
        return bool(self.__getattribute__('lis', _=False))
    def __eq__(self, other) -> bool:
        '''The == operator.'''
        if isinstance(other, type(self)):
            return (self.__getattribute__('lis', _=False) == other.lis and self.relations == other.relations)
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
            self.__getattribute__('lis', _=False).extend(other.lis)
            self.relations.extend(other.relations)
            for i in range(len(n:=other.elm)):
                try:
                    self.elm[list(n.keys())[i]] += list(n.values())[i]
                except KeyError:
                    self.elm[list(n.keys())[i]] = list(n.values())[i]
        else:
            return NotImplemented
        return self
    def __or__(self, other):
        if isinstance(other, RelationList):
            return RelationList(self.__getattribute__('lis', _=False)+other.lis)
        elif isinstance(other, list):
            return RelationList(self.__getattribute__('lis', _=False)+other)
        else:
            return NotImplemented
    def __ror__(self, other):
        if isinstance(other, list):
            return RelationList(other+self.__getattribute__('lis', _=False))
        else:
            return NotImplemented
    def __reversed__(self):
        return RelationList(list(reversed(self.__getattribute__('lis', _=False))))
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
                        _w.warn("The %T format code is deprecated and will be removed in v3.0.",
                                PendingDeprecationWarning, stacklevel=2)
                    string += str(dic[fmt[i+1]])
                    flag = True
                else:
                    flag = False
                    string += fmt[i]
            else:
                flag = False
                string += fmt[i]
        return string
    def __getitem__(self, index, /):
        return self.__getattribute__('lis', _=False)[index]
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
            self.delete(self.__getattribute__('lis', _=False)[i])
            self.add(value, index=i)
    def __delitem__(self, index, /):
        if isinstance(index, int):
            index = slice(index, index+1, None)
        if index.step == None:
            step = 1
        if index.stop == None:
            stop = len(self)
        if index.start == None:
            start = 0
        ln = len(self)
        if start > ln or start > ln:
            raise IndexError("index out of range")
        x = self.__getattribute__('lis', _=False)[:]
        for i in range(key.start,key.stop,key.step):
            self.delete(x[i])
    def __contains__(self, item) -> bool:
        return item in self.__getattribute__('lis', _=False)
    def __bytes__(self, encoding='utf-8') -> bytes:
        a = list(map(lambda x: type(x), self.__getattribute__('lis', _=False)))
        if a.count(int) < len(a):
            return bytes(''.join(map(lambda x: str(self.__getattribute__('lis', _=False))), encoding))
        else:
            return bytes(self.__getattribute__('lis', _=False))
    def __enter__(self):
        return self
    def __exit__(self, typ, value, trace):
        self.clear_relations()
    def __getattribute__(self, name, *, _=True):
        if name == 'lis' and _:
            raise AttributeError("'RelationList' object has no attribute 'lis'.")
        return object.__getattribute__(self, name)
    def __delattr__(self, name):
        raise ValueError(f"Cannot delete attribute {name!r}.")
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
        try:
            return copy.deepcopy(self.__getattribute__('lis', _=False))
        except _pickle.PicklingError:
            return copy.copy(self.__getattribute__('lis', _=False))
    def relate(self, val1, val2, /, mode:str ='break', assignment=None):
        '''Creates a relation between two elements.'''
        if val1 not in self.__getattribute__('lis', _=False) and val2 not in self.__getattribute__('lis', _=False):
            raise ValueError(f"Values {val1} and {val2} not found.")
        elif val1 not in self.__getattribute__('lis', _=False):
            raise ValueError(f"Value {val1} not found.")
        elif val2 not in self.__getattribute__('lis', _=False):
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
                self.__getattribute__('lis', _=False).append(val)
            else:
                self.__getattribute__('lis', _=False).insert(index+1, val)
        else:
            self.__getattribute__('lis', _=False).insert(index, val)
        self.elm[val] = 0
    def delete(self, val, /, *, err:str ="raise") -> bool:
        '''Deletes an element in the list.'''
        if err not in ("raise", "ignore"):
            raise ValueError(f"Invaild parameter 'err': {err}")
        elif val not in self.value:
            if err == "raise":
                raise ValueError(f"Value {val} not found.")
            elif err == "ignore":
                return False
        else:
            if self.elm[val] == 0:
                self.__getattribute__('lis', _=False).remove(val)
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
                            self.__getattribute__('lis', _=False).remove(val)
                        else:
                            del r[i]
                            self.__getattribute__('lis', _=False).remove(val)
                            self.__getattribute__('lis', _=False).remove(y)
                            del self.elm[val]
                            del self.elm[y]
                return True
    def remove_relation(self, val1, val2, /, *, err="raise"):
        '''Removes the relation given.'''
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
                    self.__getattribute__('lis', _=False).remove(val1)
                    self.__getattribute__('lis', _=False).remove(val2)
                    del self.elm[val]
                    del self.elm[y]
        if not flag and err == "raise":
            raise ValueError(f"Relation between {val1} and {val2} not found.")
        elif not flag:
            return False
        else:
            return True
    def relate_all(self, mode:str ='break', assignments=None):
        '''Create relations between all elements.'''
        self.clear_relations()
        for i in range(len(li:=self.__getattribute__('lis', _=False))-1):
            for j in range(i+1, len(li)-1):
                if not isinstance(assignments, Iterable):
                    self.relate(li[i], li[j], mode, assignments)
                else:
                    try:
                        self.relate(li[i], li[j], mode, assignments[i])
                    except IndexError:
                        self.relate(li[i], li[j], mode, assignments[-1])
    def clear_relations(self):
        '''Erases all the relations.'''
        self.__init__(self.value)
    erase_relations = clear_relations
    def related(self, val1, val2, /) -> bool:
        '''Returns True if two values are related.'''
        try:
            self.get_relation(val1, val2)
        except ValueError:
            return False
        else:
            return True
    def get_relations(self, key, /) -> list:
        '''Returns all of the relations with the element.'''
        if key not in self.__getattribute__('lis', _=False):
            raise ValueError(f"Key {val} not found.")
        a = []
        for i in range(len(r := self.relations)):
            if key in r[i][:2]:
                a.append(r[i])
        return a
    def get_relates(self, *args, **kwargs):
        '''Deprecated. Use get_relations().'''
        _w.warn('get_relates() is deprecated and will be removed in v1.4. Use get_relations().',
                DeprecationWarning, 2)
        return self.get_relations(*args, **kwargs)
    def get_relation(self, val1, val2, /) -> tuple:
        '''Returns the relation information between two values.'''
        for i in range(len(r := self.relations)):
            if val1 in r[i][:2] and val2 in r[i][:2]:
                return r[i]
        else:
            raise ValueError(f"Relation between {val1} and {val2} not found.")
    def get_relate(self, *args, **kwargs):
        '''Deprecated. Use get_relation().'''
        _w.warn('get_relate() is deprecated and will be removed in v1.4. Use get_relation().',
                DeprecationWarning, 2)
        return self.get_relation(*args, **kwargs)
    def generator(self, *, func:bool =False):
        '''Returns a generator yielding self.value. Returns the function with __call__ if `func` is true.'''
        def gen():
            yield from self.value
        return gen() if not func else gen
    def copy(self, *, deep:bool =True):
        '''Copys self. Uses copy.deepcopy if 'deep' is True, else copy.copy.'''
        import copy as c
        if deep:
            return c.deepcopy(self)
        else:
            return c.copy(self)
