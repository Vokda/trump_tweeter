import re
import state as state_def

# since generating a tweet is super quick we simply
# retry if it becomes too long
def generate_tweet(states):
    try_again = True
    while try_again: 
        tweet = ''
        next_state = states['BEGIN'].get_next_state()
        tweet += next_state + ' '
        tweet_length = 0
        max_length = 140
        while next_state != 'END':
            next_state = states[next_state].get_next_state()
            tweet += next_state + ' '
            if(len(tweet) >= max_length):
                #print(f'Max length for tweet reached. {len(tweet)} > {max_length} Terminating early')
                try_again = True
                break
            else:
                try_again = False
    return tweet.replace('END', '')

states = {}

def new_state(state_name):
    if(not state_name in states):
        states[state_name] = state_def.State(state_name)

with open('markov_chain') as f:
    print('Building markov chain from file')
    line = f.readline()
    i = 0
    while line:
        line = re.sub('\n', '', line)
        props = line.split(' ')
        if(not props[0] or not props[3]):
            line = f.readline()
            continue
        new_state(props[0])
        states[props[0]].add_state(props[3], float(props[1]), float(props[2]))
        line = f.readline()

while True:
    print('--- TWEET ---')
    print(generate_tweet(states))
    input('Press enter for a new tweet')
