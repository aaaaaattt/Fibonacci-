# num = int(input("몇번째 피보나치?"))
# count=(num+1)*[0]
# print(count)
# print(range(len(count),-1,-1))


#피보나치 수열 구현 함수
def Fibonacciy(count, n):   #첫번째 매개변수로 매개변수별 호출을 위한 list를 받아야함        
    count[n] = count[n] +1  #피보나치 함수가 호출이 되면 각 함수의 매개변수(n)에 대응하는 리스트요소에 +1 ex. Fibonaciy(10) => count[10]++
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return Fibonacciy(count,n-2)+Fibonacciy(count,n-1)
    
#매개변수별 호출 빈도 계산 + 출력함수
def printFibo():
    num = int(input("몇번째 피보나치?"))
    count=(num+1)*[0]
    Fibonacciy(count,num)
    for i in range(len(count)-1,-1,-1):
        print(f"Fibo(%d) = %d번"%(i,count[i]))
    
printFibo()

