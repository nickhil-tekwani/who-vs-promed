#!/usr/bin/env python

import sys,scipy.sparse,argparse,time
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

t0 = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--archive_number_to_ids", default='/work/k.church/Scarpino/WHO/archive_number_to_ids')
parser.add_argument("-M", "--embedding", default='/work/k.church/Scarpino/WHO/done/x.kwc.edges.npy')
parser.add_argument("-m", "--map", default='/work/k.church/Scarpino/WHO/done/x.kwc.nodes.txt')
parser.add_argument("-v", '--verbose', action='store_true')
parser.add_argument("-R", '--random_control', type=int, default=None)
parser.add_argument("-B", '--big', type=float, default=0.999)
args = parser.parse_args()


M = np.load(args.embedding)

archive_number_to_ids = {}

my_map = np.load(args.map + '.old_to_new.npy')

with open(args.archive_number_to_ids, 'r') as fd:
    for line in fd:
        fields = line.rstrip().split()
        archive_number_to_ids[fields[0]] = np.array([my_map[int(f)] for f in fields[1:]], dtype=int)

np.set_printoptions(linewidth=200, precision=3)

if not args.random_control is None:
    keys = [k for k in archive_number_to_ids.keys()]
    nkeys = len(keys)
    for i in range(args.random_control):
        aa,bb = np.random.choice(nkeys, size=2, replace=False)
        a = keys[aa]
        b = keys[bb]
        sim = cosine_similarity(M[archive_number_to_ids[a],:], M[archive_number_to_ids[b],:])
        sim1 = sim.reshape(-1)
        try:
            print(str(np.max(sim1[sim1 < args.big])) + '\t' + str(a) + '\t' + str(b))
        except:
            print('NA\t' + str(a) + '\t' + str(b))
        if args.verbose: print(sim)

else:
    for line in sys.stdin:
        fields = line.rstrip().split()
        if len(fields) >= 2:
            a,b = fields[0:2]
            if a in archive_number_to_ids and b in archive_number_to_ids:
                sim = cosine_similarity(M[archive_number_to_ids[a],:], M[archive_number_to_ids[b],:])
                sim1 = sim.reshape(-1)

                try:
                    print(str(np.max(sim1[sim1 < args.big])) + '\t' + a + '\t' + b)
                except:
                    print('NA\t' + str(a) + '\t' + str(b))

                # print(np.max(sim, axis=0))
                # print(np.max(sim, axis=1))
                if args.verbose: print(sim)

