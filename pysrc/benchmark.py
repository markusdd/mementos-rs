import random
import string

def gen_rand_tuples():
    tuples = []
    for _ in range(1000):
        t = (random.randint(0,1000),
             random.randint(0,1000),
             random.randint(0,1000),
             ''.join(random.choice(string.ascii_letters) for i in range(20)),
             ''.join(random.choice(string.ascii_letters) for i in range(20)),
            )
        tuples.append(t)
    return tuples
            
def py_dict_from_tuples(tuples):
    d = {}
    for i, t in enumerate(tuples):
        d[i] = 
