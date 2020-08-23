import os

class Restart(object):
    def __init__(self,timer=0):
        self.timer = int(timer)

    def __repr__(self):
        os.system(f"shutdown -r -t {self.timer * 60}")
        return str(f"System will restart in {self.timer} minutes!")

if __name__=="__main__":
    try:
        restart_in = int(input("Minutes until restart?: "))
        print(Restart(restart_in))
    except:
        print(Restart())
