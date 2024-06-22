
import os,sys,json

with open('results.json', 'r') as fd:
    j = json.loads(fd.read())
    print(len(j), file=sys.stderr)
    sys.stderr.flush()
    for i,r in enumerate(j):
        dir = 'unpacked/%03d' % (i % 1000)
        if not os.path.exists(dir):
            os.mkdir(dir)
        with open(dir + '/%06d' % i, 'w') as outfd:
            print('<header id=%06d>' % i, file=outfd)
            print(r['header'], file=outfd)
            print('</header>', file=outfd)
            
            print('<body id=%06d>' % i, file=outfd)
            print(r['body'], file=outfd)
            print('</body>', file=outfd)
            

        
