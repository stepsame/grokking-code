def solution(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for p in parts:
        for ch in p:
            if ord(ch) < ord('0') or ord(ch) > ord('9'):
                return False
        num = int(p)
        if num < 0 or num > 255:
            return False
        if p[0] == '0' and len(p) > 1:
            return False
    return True