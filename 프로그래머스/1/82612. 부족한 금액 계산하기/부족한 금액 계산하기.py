def solution(price, money, count):
    answer = 0
    first_price = price
    
    for i in range(count):   
        money -= price
        price += first_price
    
    if money < 0:
        answer = abs(money)
    else:
        answer = 0

    return answer