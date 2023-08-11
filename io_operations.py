
from MyPackage import greet_module_a, greet_module_b
from MyPackage.subpackage.module_b import perform_calculations

with open("output.txt", "w") as file:
    file.write(greet_module_a() + "\n")
    file.write(greet_module_b()+ "\n")

with open("output.txt", "r") as file:
    content = file.read()

    print(content)
one,two = perform_calculations()
print(one)
print(two)


