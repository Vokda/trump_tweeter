import math
import random

class State:
    # state structure 
    #{
    #   p : float, // probability of being next state
    #   n : int // number of states)
    #}
    def __init__(self, state_name):
        self.next_states = {}
        self.total_states = 0
        if(not state_name):
            raise Exception(f'no name not allowed: "{state_name}"')
        self.name = state_name

    def add_state(self, new_state): 
        if new_state in self.next_states: # if state exists just add one
            self.next_states[new_state]['n'] += 1
        else:
            self.next_states[new_state] = {
                'p' : 0,
                'n' : 1
            }
        self.total_states += 1

    def add_state(self, new_state, p, n):
        self.next_states[new_state] = {'p': p, 'n' : n}

    def calc_probs(self):
        for state in self.next_states:
            ns = self.next_states[state]
            ns['p'] = min((ns['n'] / self.total_states), 1)

        total = 0
        for state in self.next_states:
            ns = self.next_states[state]
            total += ns['p']
        if total > 1 and math.isclose(total, 1, 0.05):
            print(f'probability for state {self.name} larger than 1: {total}')
            return 1
        else:
            return 0

    # increments n (number of next_states state) 
    def increment_n(self, name):
        if(name in self.next_states):
            self.next_states[name]['n'] += 1
            self.total_states += 1

    def __str__(self):
        out = ''
        for s in self.next_states:
            p = self.next_states[s]['p']
            n = self.next_states[s]['n']
            out += self.name + f' {p} {s} {n}\n'
        return out

    def get_next_state(self):
        x = random.random()
        total_p = 0
        p = 0
        last_state = ''
        for state in self.next_states:
            p = self.next_states[state]['p']
            if(x <= (total_p + p)):
                return state
            else:
                total_p += p
                last_state = state
        #print('Could not access next tweet')
        #print(f'{self.next_states}')
        #print(f'p {p}; total_p {total_p}')
        #print(f'x {x}')
        return state
