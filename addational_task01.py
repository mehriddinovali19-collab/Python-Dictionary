products = [
    {
        "id": 1,
        "name": "s22",
        "price": 450,
        "quantity": 3,
    },
    {
        "id": 2,
        "name": "s23",
        "price": 550,
        "quantity": 2,
    },
    {
        "id": 3,
        "name": "s24",
        "price": 650,
        "quantity": 8,
    }
]

def total_price(products):
    total = 0
    for product in products:
        total += product["price"] * product["quantity"]
    return total
print(total_price(products))


def get_max_product(products):
    max_product = products[0]
    # bu yearda men product [0] ni ishlatgan sababim shu list ichida 1 ta element bor va shu elementni max deb olganman, agar list ichida 0 ta element bolganida bu kod xatolik beradi, shuning uchun men bu kodni ishlatishdan oldin list ichida element bor yoki yo'qligini tekshirishim kerak, agar element bo'lmasa, max_product ni None qilib olaman va keyin tekshiraman 
    for product in products:
        if product["price"] > max_product["price"]:
            max_product = product 
    return max_product
print(get_max_product(products))



def get_average_price(products):
    total  = 0 
    for product in products:
        total += product["price"]
        average = total / len(products )
    return average 


print(get_average_price(products))