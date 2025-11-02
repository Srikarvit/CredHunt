import hashlib


def hash_string(data):
    return hashlib.sha256(data.encode()).hexdigest()