from ManualTest import ManualTest 
import sys
import test
sys.path.insert(1, str('./firrtl-operations'))
t = test.runtests()

#write tests below
ManualTest.test(t, "sint", 1, "+", 0)
# ManualTest.test(t, "sint", 2341, "+", 1321)