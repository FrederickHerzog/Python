import hashlib

algs = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
      'whirlpool']

def hash(s, alg):
    if alg.lower() == 'md5':
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


    else: print("ERROR")
