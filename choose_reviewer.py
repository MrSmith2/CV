import hashlib

name = 'Denis Malinovskiy'

reviewers = [
    'Serggorsar',
    'Rozemarin',
    'yu432'
]

print(reviewers[int(hashlib.md5(name.encode('utf-8')).hexdigest(), 16) % len(reviewers)])