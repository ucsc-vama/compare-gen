from ManualTest import ManualTest 
import sys
import test
sys.path.insert(1, str('./firrtl-operations'))
t = test.runtests()

#write tests below
# ManualTest.test(t, "sint", 3, "pad", 2)
# ManualTest.test(t, "uint", 2341, "+", 1321)
# ManualTest.test(t, "sint", 3, "dshr", 2)
ManualTest.test(t, "sint", 5, "dshl", 4)