import hashlib

algs = ['md4', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
      'whirlpool', 'ripemd160']

def hash(s, alg):
    if alg.lower() == 'md4':
        hasher = hashlib.new('md4')
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'md5':
        hasher = hashlib.md5()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'sha1':
        hasher = hashlib.sha1()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'sha224':
        hasher = hashlib.sha224()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'sha256':
        hasher = hashlib.sha256()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'sha384':
        hasher = hashlib.sha384()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'sha512':
        hasher = hashlib.sha512()
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'whirlpool':
        hasher = hashlib.new('whirlpool')
        hasher.update(s)
        return hasher.hexdigest()
    elif alg.lower() == 'ripemd160':
        hasher = hashlib.new('ripemd160')
        hasher.update(s)
        return hasher.hexdigest()


    else: print("ERROR")


def calcAll(s):
    for alg in algs:
        h = hash(s, alg)
        print(alg +': '+h)
