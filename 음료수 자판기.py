from bdb import Breakpoint
import numbers
from tokenize import Number
from tracemalloc import stop


while 1:
    money:input("금액을 넣어주세요")

drink=( "[이화네 음류수]", "1. 콜라 - 500원", "2. 커피 - 400원", "3. 사이다 - 300원", "4. 율무차 - 200원")
print(drink)
number=input("음료를 선택해주세요")
temp=money

if number==1:
    #콜라 500원
    print ("잔액은 ",money-500,"원 입니다")
    money=temp-500

elif number==2:
    #커피 400원
    print ("잔액은 ",money-400,"원 입니다")
    money=temp-400

elif number==3:
    #사이다 300원
    print ("잔액은 ",money-300,"원 입니다")
    money=temp-300

else number==4: 
    #율무차 200원
    print ("잔액은 ",money-200,"원 입니다")
    money=temp-200

print("추가로 구매하시겠습니다?(Y/N)")

if "N" == break