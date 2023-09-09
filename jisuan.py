# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:22:14 2023

@author: 15950
"""

"""
输入两派数字，取最小值
分别计算常量的到结果
结果混合相加，结果存在数组中
求余按原数归类
归类后求平均数
"""

def inputNum():
    #用于获取输入的数字，以逗号做分割
    num1 = input("请输入第一组数字，请用,作为间隔(注意中英文): \n")
    num1 = num1.split(",")
    num2 = input("请输入第二组数字，请用,作为间隔(注意中英文):\n")
    num2 = num2.split(",")
    return num1 , num2

def minNum(num1 , num2):
    #取两组数的最小值
    #num1=[100,99,200]
    num1 = list(map(float,num1))
    num2 = list(map(float,num2))
    minNum1 = min(num1)
    minNum2 = min(num2)
    print("获得第一组最小值：" + str(minNum1))
    print("获得第二组最小值：" + str(minNum2))

    return minNum1, minNum2
    
def multiplicationNum(minNum1 , minNum2):
    #计算最小值乘法后的数值
    num1List = []
    num2List = []
    for i in count:
        num1List.append(minNum1 * i)
        num2List.append(minNum2 * i)
    print("\n第一组数据乘固定常量的结果" )
    print(num1List)
    print("\n第二组数据乘固定常量的结果：")
    print( num2List)
    return num1List,num2List

def addNum(num1List, num2List):
    #相乘后的数需要相加
    addnum = []
    for n in num1List:
        for m in num2List:
            #print(str(n)+"+"+str(m))
            result = n + m
            addnum.append(result)
    print("\n相加后的结果：" )
    print(addnum)
    return addnum
            

def divisionSum(sumList):
    #算出循环的数
    result = []
    for i in sumList:
        a = format(round((i / 3),7),".7f")
        result.append(a)
    return result

def groupNum(result,addnum):
    #分类
    a = 0
    result0 = []
    result3 = []
    result6 = []
    for i in result:
        if int(i[-3:]) == 000:
            result0.append(addnum[a])
        if int(i[-3:]) == 333:
            result3.append(addnum[a])
        if int(i[-3:]) == 667:
            result6.append(addnum[a])
        a += 1
    print("\n归类结果数据：")
    print(result0)
    print(result3)
    print(result6)
    return result0,result3,result6
            
        
def average(arr):
    #求平均数
    total = 0
    for num in arr:
        total += num
    avg = total / len(arr)
    return avg



if __name__ == '__main__': 
    count = [2, 2.25, 2.5, 2.75]
    num1,num2 = inputNum()
    #num2 = [100,99,200]
    #num1 = [1,3,2]
    minNum1, minNum2 = minNum(num1, num2)
    num1List,num2List = multiplicationNum(minNum1 , minNum2)
    addnum = addNum(num1List, num2List)
    divisionsum = divisionSum(addnum)
    groupnum1, groupnum2, groupnum3 = groupNum(divisionsum,addnum)
    print("\n算出的平均值：" )
    print(average(groupnum1))
    print(average(groupnum2))
    print(average(groupnum3))
    