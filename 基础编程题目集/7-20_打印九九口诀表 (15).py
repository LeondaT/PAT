n = int(raw_input())
s = []
for i in xrange(1, n+1):
    line = ''
    for j in xrange(1, i+1):
        line += '%d*%d=%s' % (j, i, '{:<{}}'.format(j*i, 4))
    s.append(line)
print '\n'.join(s)
