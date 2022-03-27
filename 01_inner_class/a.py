print('Hello World')

class Tracker:
    jobs__C = {}
    def __init__(self) -> None:
        self.tid = 5
    
    class JobTracker:
        def __init__(self) -> None:
            self.jid =87
            pass
#wrong syntax, inner class must be created by outer.inner
#jtk = JobTracker()

jtk = Tracker.JobTracker()
#wrong sytax, inner class does not have attribute of outer calss
#print(f"job tracker tid:{jtk.tid}")


