import testpackage.hello as h
from testpackage import hello as hl # import specific module
from testpackage.hello import  printSomthing # import specific function

h.show()
hl.show()
printSomthing()