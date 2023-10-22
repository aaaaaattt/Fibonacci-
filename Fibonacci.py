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
    count=(num+1)*[0]   #리스트의 갯수는 입력값 + 1을 해줘야 함수 매개변수에 대응하는 리스트 요소를 맞출 수 있음
    Fibonacciy(count,num)
    for i in range(len(count)-1,-1,-1): #출력 부분 , 리스트 요소의 갯수보다 -1 작은 수부터 시작해서 0까지 출력
        print(f"Fibo(%d) = %d번"%(i,count[i]))  #문자열 포매팅 주의!
    
printFibo() #함수 실행

