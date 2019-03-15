def hangman(word):
    wrong = 0
    stages = ["",
              "_______     ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /|＼   ",
              "|    / ＼   ",
              "|           "
                ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンにようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字予想してください。"
        char = input(msg)
        
        #文字が含まれている時#
        if char in rletters:
            cind = rletters.index(char)     #文字の位置#
            board[cind] = char              #所定の位置の文字を置き換え#
            rletters[cind] = "$"            #当てられた文字を変換#

        #文字が含まれていないとき#
        else:
            wrong += 1

        #結果を表示#
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        #勝利判定#
        if "_" not in board:
            print("あなたの勝ちです！")
            print(" ".join(board))
            win = True
            break

        #敗北判定#
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負けです。正解は{}".format(word))
            
hangman("cat")
