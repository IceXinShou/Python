# 1. 列出兩數之合
print(int(input("請輸入一個整數: ")) + int(input("請輸入一個整數: ")))  # 列出

# 2. 列出兩數之商與餘數
a = int(input("請輸入一個整數: "))  # 儲存第一個輸入的數
b = int(input("請輸入一個整數: "))  # 儲存第二個輸入的數
print(int(a // b), a % b)  # 列出

# 3. 更改兩數之位置
l1 = input("請輸入兩數值 (eg. 100,60): ").split(",")  # 儲存輸入的字串
print(l1[-1], l1[-2], sep=",")  # 列出

# 4. 判斷輸入數值為偶數還是奇數
print("偶數" if int(input("請輸入一個整數: ")) % 2 == 0 else "奇數")  # 列出


# 5.溫標類型轉換
def tempCalculate(temp):  # 宣告函式
    degree = int(temp[:-1])  # 輸入溫度
    type = temp[-1].upper()  # 原溫標類型
    if type == 'C':  # 如果原類型是攝氏
        return str(round((9 * degree) / 5 + 32, 1)) + " °F"  # 轉換成華氏
    elif type == 'F':  # 如果原類型是華氏
        return str(round((degree - 32) * 5 / 9, 1)) + " ℃"  # 轉換成攝氏
    else:
        return "未知的單位"  # 除錯


print(tempCalculate(input("請輸入需轉換的溫度 (eg. 25C): ")))  # 列出


# 6.平方公尺與坪轉換
def areaCalculate(temp):  # 宣告函式
    if temp[-1] == '坪':  # 判斷單位
        return str(round(int(temp[:-1]) / 0.3025, 1)) + " 平方公尺"  # 單位轉換
    elif len(temp) > 4 and temp[-4:] == "平方公尺":  # 判斷單位
        return str(round(int(temp[:-4]) * 0.3025, 1)) + " 坪"  # 單位轉換
    else:
        return "未知的單位"  # 除錯


print(areaCalculate(input("需轉換的單位面積 (eg. 25平方公尺): ")))  # 列出


# 7. 兩值間閏年的數量
def leapCheck(startYear, endYear, n=0):  # 宣告函式並定義初始值
    for i in range(startYear, endYear, 4):  # 間隔為 4 的迴圈
        if i % 100 == 0 and i % 400 != 0:  # 是否符合閏年條件
            continue  # 不符合則回到迴圈開始點
        n += 1  # 符合加一
    return n


print(leapCheck(int(input("請輸入起始年分: ")), int(input("請輸入結果年分: "))))  # 列出


# QuickSort
def quicksort(array):  # 宣告函式
    if len(array) < 2:  # 判斷是否完成
        return array  # 回傳完成值
    else:  # 未完成
        n = array[0]  # 儲存原數據
        return quicksort([i for i in array if i < n]) + [n] + quicksort(
            [i for i in array if i > n])  # 以"基準值"將大於, 小於的值"遞迴"至最終由小到大排序


def typeChange(array):  # 宣告函式
    for i in range(0, len(array)):  # 將整個 list 一個個放進 i
        array[i] = int(array[i])  # 將轉型過的 i 放入原本的位置
    return array  # 回傳 list


print(quicksort(typeChange(input("請輸入一串數列 (eg. 29, 70, 6, 16, 1): ").split(", "))))  # 列出
