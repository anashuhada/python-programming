# Approach 1
import sys # predefined module
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/pack1")

import module1
import module2

module1.display()
module2.show()

# Approach 2
import sys # predefined module
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/pack1")

from module1 import *
from module2 import *

display()
show()