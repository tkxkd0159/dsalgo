def consecutive_sum(start, end):

    if start == end:
        return start
    else:
        return consecutive_sum(start, (start+end)//2) + consecutive_sum((start+end)//2+1, end)



if __name__ == "__main__":
    print(consecutive_sum(1, 100))