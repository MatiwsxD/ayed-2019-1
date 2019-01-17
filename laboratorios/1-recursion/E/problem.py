import json
def supe(digit):
    digit = str(digit)
    if len(digit)==1:
        return digit
    else:
        cont = 0
        for i in range(len(digit)):
            cont+= int(digit[i])
        return supe(cont)
        
        

# TODO Complete!
def super_digit(n, k):
    digit = str(str(n)*k)
    return int(supe(digit))


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            n = test["n"]
            k = test["k"]
            actual = super_digit(n, k)
            expected = test['result']
            assert actual == expected, f'Test {i} | n: {n} | k: {k} | expected: {expected}, actual: {actual}'
        print('OK!')
