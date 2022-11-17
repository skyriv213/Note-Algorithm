shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    shop_prices.sort(reverse = True)  # 가격대를 비싼 순서로 정렬
    user_coupons.sort(reverse = True)
    cnt = 0
    sum = 0
    for i in range(len(coupons)):
        sum += (prices[i] * (100 - coupons[i]) / 100)
        cnt += 1
    for i in range(cnt, len(prices)):
        sum += prices[i]
    return int(sum)


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
