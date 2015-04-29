def abc(s1, s2):
    return s1 in s2

def abc2(s1, s2):
    for i in range(0, len(s2)):
        if s2[i:i+len(s1)] == s1:
            return True
    else:
        return False

def abc3(s1, s2):
    for i in range(0, len(s2)):
        for j in range(0, len(s1)):
            if s2[i + j] != s1[j]:
                break
        else:
            return True
    else:
        return False

print abc2("ello1", "Hello World!")