'''
    === BEGIN of procedure ===
    an example to demstrate shared library mechanism
    step 1 ...
    BeatHeart 0
    get TASK
    BeatHeart 1
    get [1, 2, 3, 4, 5, 6]
    BeatHeart 2
    get {'a': 'A', 'b': 'BV', 'c': 123}
    BeatHeart 3
    step 2 ...
    get TERM
    === END of procedure ===
'''

from multiprocessing import Process, Queue
import debugpy
import time

def f(q : Queue, k: bool = False):
    i = 0 
    while True:        
        time.sleep(1)
        print(f"BeatHeart {i}")
        q_code = q.get()
        print(f"get {q_code}")
        if q_code == "TERM":
            break
        i+=1

print("=== BEGIN of procedure ===")
# debugpy.listen(("10.185.15.107", 9641))
# debugpy.wait_for_client()
# breakpoint()
print("an example to demstrate shared library mechanism")

queue = Queue()
p = Process(target=f, name="binning_worker", args=(queue,))

p.start()

print("step 1 ...")
queue.put("TASK")
queue.put([1,2,3,4,5,6])
queue.put({
    "a" : "A",
    "b" : "BV",
    "c" : 123,
})
print("step 2 ...")
queue.put("TERM")
#p.terminate()
p.join()

print("=== END of procedure ===")