class State:
    def __init__(self, q, pa, a):
        self.q = q
        self.pa = pa
        self.a = a
        self.mc = None
        self.v = 0
        self.rollouts = []
        self.rollout_was_visited = [] # bool

    def __repr__(self):
        return f"[State] Q:{self.q} || PA:{self.pa} || MC:{self.mc} ||"
    #[State] Q:{问题} || PA:{部分答案} || MC:{蒙特卡洛估计值} ||

    
    def add_rollout(self, result):
        self.rollouts.append(result)
        self.rollout_was_visited.append(False)
    
    def add_visit(self):
        self.v += 1

    def get_rollouts(self):
        return self.rollouts