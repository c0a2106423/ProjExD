import string
import random
import datetime
#from this import s

def main():
    global string_len, missing_len, retry_count
    retry_count = 2
    show_text, droped_text ,droped_pos= list(), list(), list()
    string_len = int(set_int("対象文字数を入力 : "))
    missing_len = int(set_int("欠損文字数を入力 : "))
    origin_text = random.choices(string.ascii_uppercase, k=string_len)
    #for i in range(missing_len):
        #droped_text.add(random.sample(origin_text, k=missing_len))
    droped_text = random.sample(origin_text, k=missing_len)
    for i in range(len(origin_text)):
        show_text.append(origin_text[i])
    #for i,j in zip(droped_text, droped_pos):

    print("対象文字 : \n"+"".join(origin_text))
    print("欠損文字 : \n"+"".join(droped_text))
    for i in range(missing_len):
        show_text.remove(droped_text[i])
    print("表示文字 : \n"+"".join(show_text))
    
    #droped_text = set(droped_text)
    #print("".join(origin_text))
    #print("".join(droped_text))
    #print("".join(show_text))
    ans=set_int("欠損文字はいくつあるでしょうか:")
    if ans == missing_len:
        print("正解です。それでは、具体的に欠損文字を1つずつ入力してください")
        for i in range(missing_len):
            ans = set_str(str(i+1)+"つ目の文字を入力してください : ")
            if ans != droped_text:
                print("不正解です。またチャレンジしてください")
                break
            #else:
            #    droped_text.remove(ans)
        else:
            print("全問正解です。おめでとうございます！")
    else:
        print("不正解です。")

def set_arg(text):
    try:
        argument
    except:
        argument = input(text)
    return argument

def set_str(text):
    argument = set_arg(text)
    try:
        argument=str(argument)
    except:
        argument = input(text+" 文字を入力してください！")
    if len(argument)!=1:
        argument = input(text+" 一文字だけ入力してください！")
    return argument

def set_int(text):
    argument = set_arg(text)
    try:
        argument=int(argument)
    except:
        argument = input(text+" 整数を入力してください！")
    return argument



if __name__ == "__main__":

    main()