import json
def orden(lista,izq,der):
    if len(lista)==0:
        return izq+der
    else:
        x = lista[0]
        if x % 2 == 0:
            return orden(lista[1:],izq + [x],der)
        else:
            return orden(lista[1:],izq,der+[x])

# TODO Complete!
def arrange(numbers):
    return orden(numbers,[],[])


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            numbers = test["numbers"]
            actual = arrange(numbers)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
