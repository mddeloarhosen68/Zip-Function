names = ['anon','asif','adit','anon']

comps = ['Dell','Apple','Microsoft','Dell']


zipped = list(zip(names,comps))
#zipped = dict(zip(names,comps))
#zipped = set(zip(names,comps))
#print(zipped)

for (a,b) in zipped:
    print(a,b)