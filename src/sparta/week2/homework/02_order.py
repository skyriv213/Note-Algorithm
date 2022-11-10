shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()
    orders.sort()

    start = 0
    end = len(menus)-1
    mid = (start + end) // 2

    for i in orders:
        while start <= end:
            if i == menus[mid]:
                return True
            elif i < menus[mid]:
                end = mid + 1
            else:
                start = mid + 1
            mid = (start + end) //2
        return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)
