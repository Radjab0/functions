def find_ticket(ticket):
    num = str(ticket)
    numbers1 = int(num[:1]) + int(num[1:2])
    numbers2 = int(num[-1]) + int(num[-2])
    if numbers1 == numbers2:
        return True
    else:
        return False
 
ticket = 323123
print(find_ticket(ticket))