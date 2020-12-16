# relationlist 1.3.0a0
This is the relationlist module, containing a class that supports relations.  
Example:
```python
>>> import relationlist
>>> lis = relationlist.RelationList([1, 2, 3, 4])
>>> lis.value
[1, 2, 3, 4]
>>> lis.relate(1, 3, assignment='1+3=4')
>>> lis.relations
[(1, 3, 'break', '1+3=4')]
>>> relationlist.ver.raw
'1.3.0a0'
```
See more at [the official documentation](https://relationlist.readthedocs.io/)!
