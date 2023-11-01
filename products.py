pro_num = int(input ("Enter number of products you want to purchase: "))



#start the loop
total = 0

num_001=0
num_002=0
num_003=0


pro_001 =0
pro_002 =0
pro_003 =0
for product in range (1, pro_num+1):

    #ask for product
    print("\n 001 for product 1, 002 for product 2, 003 for product 3")
    pro_id=input("Enter product id:")

    num= int(input ("How many items of product" + pro_id+ "do you want to buy:"))

    #evaluate

    if pro_id =="001":
        pro_001= num * 8.7

        total += pro_001

        num_001=num

    elif pro_id =="002":
        pro_002 = num * 10.58

        total = total + pro_002
        num_001=num

    else:
        pro_003 = num * 4
        

        total = total + pro_003
        num_003=num

#print information

print (f'{"Product ID":<10} {"Units Sold":<10} {"Total Sales"}')

print (f'{"-"*32}')

print(f'{"001":<10} {num_001:<10} {pro_001}')
print(f'{"002":<10} {num_002:<10} {pro_002}')
print(f'{"003":<10} {num_003:<10} {pro_003}')

print (f'{"-"*32}')

print(f'{"Total Sales:" :<22} ${total}')

