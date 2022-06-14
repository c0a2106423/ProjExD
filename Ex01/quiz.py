if __name__ == "__main__":
    import random
    Q_list = list()
    Q_num = 0
    def shutudai():
        Q_count = 3
        ans = list() 
        ans.append(("マスオ", "ますお"))
        ans.append(("ワカメ", "わかめ"))
        ans.append(("甥", "おい", "甥っ子", "おいっこ"))

        quiz = list()
        quiz.append("サザエの旦那の名前は？")
        quiz.append("カツオの妹の名前は？")
        quiz.append("タラオはカツオから見てどんな関係？")

        for i in range(Q_count):
            Q_list.append((quiz[i], ans[i]))
        Q_num = random.randint(0,Q_count-1)
        print(Q_list[Q_num][0])
    
    def kaito():
        Usr_ans = input("答えを入力 : ")
        if Usr_ans in Q_list[Q_num][1]:
            print("正解です！")
        else:
            print("違います。")

    shutudai()
    kaito()