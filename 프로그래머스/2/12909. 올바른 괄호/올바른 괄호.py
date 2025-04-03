def solution(s):
    ll = []
    for word in s:
        if word == '(':
            ll.append(1)
        else:
            if len(ll) == 0:
                return False
            else:
                ll.pop()
    if len(ll) == 0 :
        return True
    else:
        return False
