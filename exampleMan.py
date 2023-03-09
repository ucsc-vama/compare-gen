from ManualTest import ManualTest 
import subprocess
import sys
import test
sys.path.insert(1, str('./firrtl-operations'))
import sint
import uint

t = test.runtests()
# subprocess.call(["mkdir", "testcases/"+str(t.ts)+"/"])

ManualTest.test(t, "uint", 3, "+", 13)
# sint.model_sint(0x6dba, 16).print_bits()