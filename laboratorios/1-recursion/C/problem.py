import json
def palab(pal,voc,con):
    if len(pal)==0:
        if voc>con:
            return True
        else:
            return False
    else:
        vocal=["a","e","i","o","u","A","E","I","O","U"]
        if pal[0] in vocal:
            voc+=1
            return palab(pal[1:],voc,con)
        else:
            con+=1
            return palab(pal[1:],voc,con)


# TODO Complete!
def has_more_vowels(s):
    return palab(s,0,0)


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            s = test["s"]
            actual = has_more_vowels(s)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
