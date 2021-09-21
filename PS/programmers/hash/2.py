def solution1(phoneBook):   # 효율성 테스트 시간초과 뜨는 풀이, for문 2개 돌리지말고 더미 배열 하나 더 만들어서 비교하는게 빠름
    phoneBook.sort(key=str.lower)

    for i in range(len(phoneBook)-1):
        for j in range(i+1, len(phoneBook)):
            if phoneBook[i] == phoneBook[j][:len(phoneBook[i])]:
                return False
    return True

def solution2(phoneBook):  # 더미 배열 만들어서 계산한거
    phoneBook.sort(key=str.lower)
    iter_ = len(phoneBook)-1
    p = phoneBook[0:iter_]
    dummy_p = phoneBook[1:]

    for i in range(iter_):
        if p[i] == dummy_p[i][:len(p[i])]:
            return False
    return True


def solution3(phoneBook):  # 사이트 답안 1
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution5(phone_book):  # 사이트 답안2, 해쉬이용, 역시 이중 for문을 쓰지만 전화번호 길이는 max가 20이므로 phone_book (1000000)을 이중으로 돌리는거에 비해 훨씬 시간복잡도 적음.
    answer = True
    hash_map = {}
    for phone_number in phone_book:   # Counter(phone_book)로도 가능
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return answer
