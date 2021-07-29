import random

# 第 1 題

ANS = random.randint(1, 100)


def check(init, ans):
    if init < ans:
        return -1
    if init == ans:
        return 0
    if init > ans:
        return 1


i = 0
for i in range(5):
    outp = check(int(input('請猜數字(1~100),還剩%d次:' % (5 - i))), ANS)
    if (outp < 0):
        print("太小了!")
    elif (outp > 0):
        print("太大了!")
    else:
        break

if i == 4:
    print("遊戲結束, 你失敗了")
else:
    print("恭喜猜對了~~")


# 第 2 題
def calcu(n1, n2):
    try:
        n1 = int(n1)
        n2 = int(n2)
        print("x+y= ", n1 + n2, ", x-y= ", n1 - n2, ", x*y= ", n1 * n2, ", x/y= ", round(n1 / n2, 2, ), sep="")

    except ValueError:
        print("\033[91m[ERROR] 請輸入正確的數字!...\033[0m")

    except ZeroDivisionError:
        print("\033[91m[ERROR] 除數不能為零!...\033[0m")

    except:
        print("\033[91m[ERROR] 錯誤!...\033[0m")


calcu(input("請輸入一個數值: "), input("請輸入一個不為零的數值: "))
