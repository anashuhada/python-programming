# Approach 1
import sys # predefined module
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/package1")
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/package1/package2")

import module1
import module2

module1.display()
module2.show()

# Approach 2
import sys
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/package1")
sys.path.append("/Users/anashuhada/PycharmProjects/PythonProgramming/day9/package1/package2")

from module1 import *
from module2 import *

display()
show()