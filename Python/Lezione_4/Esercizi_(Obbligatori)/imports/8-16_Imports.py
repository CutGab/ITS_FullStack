# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import city_names_copy

city_names_copy.city_country("Santiago", "Chile")

print("-" * 10)

from city_names_copy import city_country

city_country("Santiago", "Chile")

print("-" * 10)

from city_names_copy import city_country as CC

CC("Santiago", "Chile")

print("-" * 10)

import city_names_copy as CNC

CNC.city_country("Santiago", "Chile")

print("-" * 10)

from city_names_copy import *

city_country("Santiago", "Chile")
