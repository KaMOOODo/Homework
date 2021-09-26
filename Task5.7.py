"""
The interpreter imports module C (in namespace variable is created with the value 5 ( x = 5 )).
Further module B overwrites variable for 5.
On first call mod_c.x from mod_a we got printing "5"
Next step: Try to change x to a list [1,2,3].
Now we got "5". Why? Because the variable is overwritten by mod_b.
Finally
from mod_c import *
from mod_b import *
In namespace was created variables x = [1, 2, 3] (from mod_c) and mod_c.x = 5 (from mod_b)
"""