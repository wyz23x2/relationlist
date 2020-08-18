import sys as _sys
from collections import namedtuple as _nt
from hashlib import md5 as _md5
class ver(object):
    @property
    def __all__(self):
        return ['raw',
                'md5',
                'version']
    @property
    def raw(self):
        raw = '1.2.0rc1'
    @property
    def md5(self):
        md5 = _md5(raw.encode()).hexdigest()
    @property
    def version(self):
        version = _nt('version_info', ('major', 'minor', 'micro',
                                       'releaselevel', 'serial'),
                  module='relationlist.ver')(1, 2, 0, 'candidate', 1)
# 'a':   alpha
# 'b':   beta
# 'rc':  candidate
# '':    final
_sys.modules[__name__] = ver()
