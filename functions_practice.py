def hello():
    print(" Hello User")

def pack(list1,list2,list3):
    return [list1,list2,list3]
def eat_lunch(my_lunch):
    if my_lunch:
        print(f'first I eat {my_lunch[0]}')
        for item in my_lunch[1:]:
            print(f"Next i eat {item}")
    else:
        print("My lunchbox is empty")

hello()
packed_list = pack('apple','banana', 'cherry')
print(packed_list)
eat_lunch(['sandwich', 'apple', 'cookie'])