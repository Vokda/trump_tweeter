#  known bugs: &amp; not processed correctly

import state as state_def
import re
import csv

states = {}

def save_states():
    with open('markov_chain', 'w') as f:
        for state in states:
            f.write(str(states[state]))

def new_state(state_name):
    if(not state_name in states):
        states[state_name] = state_def.State(state_name)
    else:
        for state in states:
            states[state].increment_n(state_name)

def generate():
    new_state('BEGIN')
    new_state('END')
    cols = ''
    with open('Donald-Tweets.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')
        tweet = ''
        hash_tags = []
        for i, line in enumerate(csv_reader):
            if(i == 0):
                print(f'Cols: {", ".join(line)}')
            #elif i > 1000:
            #    break
            else:
                tweet = line[2]
                # replace all undesired words with rm
                tweet = re.sub(r'http(s)?://.+', '', tweet) # remove links
                tweet = tweet.replace("\n", ' ')
                tweet = tweet.replace(r'\s{2,}', '')
                prev_w = 'BEGIN'
                for word in tweet.split(' '):
                    if(re.match(r'^\s*', word) or 
                        re.match(r'\s*$', word) or
                        re.match(r'^$', word)
                        ):
                        continue
                    new_state(word)
                    states[prev_w].add_state(word)
                    prev_w = word
                # for last word
                states[prev_w].add_state('END')
            if(i % 100 == 0):
                print(f'tweet #{i}')

# for some debugging
    too_much = 0
    print('calculating probabilities')
    for i, state in enumerate(states):
        too_much += states[state].calc_probs()
    print(f'prob > 1: {too_much}')

    save_states()
