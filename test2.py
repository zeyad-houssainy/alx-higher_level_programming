from test import hello as ok
import sys
ok()

# test.roll(5)



sys.stderr.write("This is a test 1\n")
sys.stdout.write("This is a test 2\n")
sys.stderr.flush()
print(len(sys.argv))
print(sys.argv)