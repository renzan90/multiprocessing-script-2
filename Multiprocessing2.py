import time
import multiprocessing
start=time.perf_counter()
def do_something():
	print('Sleeping 1 second')
	time.sleep(1)
	print('Done sleeping')

processes=[]	
for _ in range(10):
	p=multiprocessing.Process(target=do_something)
	p.start()
	processes.append(p)

for process in processes:
	process.join()

finish=time.perf_counter()
print(f'Finished in {finish-start} second')


