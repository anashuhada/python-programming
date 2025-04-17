# Approach 1: import and create class object
import a
import b

a_obj = a.Animal()
a_obj.display()

b_obj = b.Bird()
b_obj.display()

# Approach 2
from a import Animal
from b import Bird

a_obj = Animal()
a_obj.display()

b_obj = Bird()
b_obj.display()
