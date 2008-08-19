"General math/geometry functionality"


from info import __doc__

from combinatorial import *
from parity import *
from graph import *
from volume import *
from circumcenter import *
from kd_tree import *

__all__ = filter(lambda s:not s.startswith('_'),dir())

from pydec.testing import Tester
test = Tester().test

