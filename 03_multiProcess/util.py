#utility
from multiprocessing import Pool
import os
import time
import signal
import subprocess

SLEEP_TIME=500
print("== begin ==")

def init_worker():
    print("_____|--------|_____")
    #signal.signal(signal.SIGINT, signal.SIGINT)
    #signal.signal(signal.SIGINT, signal.SIG_IGN)
def ex_f(fid):
    rc_at_ex_f = "*UNKNOWN"
    try:
        cmd = f'sleep {SLEEP_TIME}'
        proc =subprocess.Popen(cmd, shell=True)
        print(f"     **external worker {fid} [pid:{proc.pid}]")
        output = proc.communicate()[0]
        rc_at_ex_f = "*SUC"
    except KeyboardInterrupt as e:
        print (f'    ** external worker({fid}) got ^C during working process')
        rc_at_ex_f = "*FAIL_INT"
        raise e
    return rc_at_ex_f

def f(fid):
    rc_at_f = "UNKNOWN"
    try:
        print(f"work {fid} [pid:{os.getpid()}]is going to sleep for {SLEEP_TIME} secs")
        ex_f(fid)
        print(f"@f worker#{fid} done ex_f")
        #time.sleep(500)
        rc_at_f = "SUC"
    except KeyboardInterrupt:
        print (f'  ------->worker({fid}) got ^C during working process')
        p.terminate()
        print ('pool is terminated(worker)')
        rc_at_f = "F_FAIL_INT"
    except Exception as e:
        print(f"worker hits Exception: {e}")
        rc_at_f = "F_FAIL_EXP"
    return rc_at_f

ret = None
p = Pool(processes=3, initializer=init_worker)
try:
    print ('starting the pool map')
    ret = p.map(f, range(5))
    p.close()
    print ('pool map complete')
except KeyboardInterrupt:
    print ('got ^C while pool mapping, terminating the pool')
    p.terminate()
    print ('pool is terminated(1)')
except Exception as e:
    print (f'got exception: {e}, terminating the pool')
    p.terminate()
    print ('pool is terminated(2)')
finally:
    print ('joining pool processes')
    p.join()
    print ('join complete')
print(f"{ret}")
print ('the end')
print("== end ==")
