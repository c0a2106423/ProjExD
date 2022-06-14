import random
mondai = ["3+4は？","3*3+3は？","6/3は？"]
kotae = [["7","なな","ナナ","七"],["12","じゅうに","十二","ジュウニ"],["2","に","ニ","二"]]
a = 0
def syutudai():
    a = random.randint(0,2)
    print(f"問題:{mondai[a]}")
    n = kotae[a]
    return n

def kaito(x):
    n = input("入力:")
    if n in x:
        print("正解")
    else:
        print("不正解")

def main():
    s = syutudai()
    kaito(s)
