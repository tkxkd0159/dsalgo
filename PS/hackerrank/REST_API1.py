


import time
import requests
import threading
# 스레드로 무식하게 푼 방법
cnt_per_page = []
def get_res(addr):
    res = requests.get(addr).json()
    cnt = 0
    for match_ in res['data']:
        if match_['team1goals'] == match_['team2goals']:
            cnt +=1
    cnt_per_page.append(cnt)

def getNumDraws(year):
    res = requests.get(f"https://jsonmock.hackerrank.com/api/football_matches?year={year}").json()
    total_page = res['total_pages']
    threads = []
    for p in range(1, total_page+1):
        addr = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={p}"
        worker = threading.Thread(target=get_res, args=(addr,))
        threads.append(worker)
        worker.start()

    for t in threads:
        t.join()

    total_cnt = sum(cnt_per_page)

    return total_cnt

start = time.time()
print(getNumDraws(2011))
print("Total time : ", time.time() - start)


## 문제 의도대로 푼 방법

def get_res(addr):
    res = requests.get(addr).json()
    cnt = res['total']
    return cnt
def getNumDraws(year):
    total_cnt = 0
    for s in range(0, 11):
        addr = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={s}&team2goals={s}"
        total_cnt += get_res(addr)

    return total_cnt
