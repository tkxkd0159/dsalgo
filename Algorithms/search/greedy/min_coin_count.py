def min_coin_count(value, coin_list):
    count = 0
    for coin in sorted(coin_list, reverse=True):
        count += (value // coin)
        value %= coin

    return count

if __name__ == "__main__":
    default_coin_list = [500, 100, 50, 10]
    print(min_coin_count(1440, default_coin_list))
    print(min_coin_count(1700, default_coin_list))
    print(min_coin_count(23520, default_coin_list))
    print(min_coin_count(32590, default_coin_list))

