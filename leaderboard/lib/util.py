def simplify(s):
    s = s.lower()
    return ''.join(c for c in s if c >= 'a' and c <= 'z')
