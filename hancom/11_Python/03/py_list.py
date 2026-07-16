# 리스트는 순서가 있고 수정 가능하며 중복을 허용하는 자료입니다. 

colors = ["red", "green", "blue"] # 순서 있음 ,  수정 가능 , 중복 허용

#print(colors[0])   # red 첫번째 -- 0이 컴퓨터에서는 첫번쨰를 의미 순서 있어 [] 사용
#print(colors[-1])  # 순서에서 -1의 의미는 리스트에서의 마지막을 의미함 
#print(colors[0:2]) # :   가 ~부터 ~까지를 의미함 -  red  green  출력됨


#  리스트 수정법 

#colors[-1] = "black" # 마지막을 black  으로 할당 하겠다. 
#print(colors[-1])    #위의 선언으로 blaxk 으로 나옴

#colors.append("pink")
#print(colors)

# colors.insert(0, "white")
# print(colors)

#colors.remove('red')
#print(colors)   #red   사라짐

numbers =[8, 5, 3, 2, 7]
#numbers.sort()  # 오름차순 정렬 오름차순 자은거에서 큰거로 오르는 오름차순 
#numbers.sort(reverse=True)  # 내림차순 정렬
#print(numbers)

#print(9 in numbers) # N 이 숫자안에 들어 있냐 물어 보는 것 