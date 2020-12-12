import sys as _sys
from collections import namedtuple as _nt
from hashlib import md5 as _md5
__all__ = ['raw', 'md5', 'version']
raw = '1.2.1'
md5 = _md5(raw.encode()).hexdigest()
version = _nt('version_info', ('major', 'minor', 'micro',
                                'releaselevel', 'serial'),
              module='relationlist.ver')(1, 2, 1, 'final', 0)
# 'a':   alpha
# 'b':   beta
# 'rc':  candidate
# 'final':    final
