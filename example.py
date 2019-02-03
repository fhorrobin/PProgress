from pprogress import ProgressBar
from time import sleep
from time import time

N = 100
pb = ProgressBar(N, show_time=True)
for i in range(N):
    pb.update()
    sleep(0.1)
pb.done()

