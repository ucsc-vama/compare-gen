from ManualTest import ManualTest 
import sys
import test
sys.path.insert(1, str('./firrtl-operations'))
t = test.runtests()

#write tests below
ManualTest.test(t, "sint", 3, "pad", 0)
ManualTest.test(t, "uint", 2341, "+", 1321)