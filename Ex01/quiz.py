if __name__ == "__main__":
    import random
    Q_COUNT = 3
    q_list = list()
    q_num = random.randint(0,Q_COUNT-1)
    
    def shutudai():
        ans = list() 
        ans.append(("マスオ", "ますお"))
        ans.append(("ワカメ", "わかめ"))
        ans.append(("甥", "おい", "甥っ子", "おいっこ"))

        quiz = list()
        quiz.append("サザエの旦那の名前は？")
        quiz.append("カツオの妹の名前は？")
        quiz.append("タラオはカツオから見てどんな関係？")

        for i in range(Q_COUNT):
            q_list.append((quiz[i], ans[i]))
        print(q_list[q_num][0])
    
    def kaito():
        Usr_ans = input("答えを入力 : ")
        if Usr_ans in q_list[q_num][1]:
            print("正解です！")
        else:
            print("違います。")

    shutudai()
    kaito()