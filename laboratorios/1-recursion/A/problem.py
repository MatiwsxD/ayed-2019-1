import json

def invertir(x,y):
    if len(x)==0:
        return y
    else:
        return invertir(x[:-1],y+x[-1])
# TODO Complete!!
def reverse(text):
    return invertir(text,"")


if __name__ == '__main__':
    with open('./data.json') as f:
        tests = json.load(f)
        for i, test in enumerate(tests):
            text = test["text"]
            actual = reverse(text)
            expected = test['result']
            assert actual == expected, f'Test {i} | expected: {expected}, actual: {actual}'
        print('OK!')
