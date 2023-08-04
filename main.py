import sys
import datetime
import time


def time_every_second(seconds):
    for second in range(seconds):
        result = datetime.datetime.now()
        print(result)
        time.sleep(1)


print(sys.argv)
argv_second = int(sys.argv[-1])
res = time_every_second(argv_second)
