def deal(interval):
    # python sort
    interval.sort(key = lambda ran: ran[0])
    # python print format
    print(f"Before process: {interval}")
    merged_interval = []
    first = interval[0]
    # len()
    l = len(interval)
    for i in range(1,l):
        second = interval[i]
        if first[1] >= second[0]:
            first = [first[0],second[1]]
        else:
            # list append
            merged_interval.append(first)
            first = second
    merged_interval.append(first)
        
    return merged_interval

if __name__ == '__main__':
    ran_str = input("List with ran_list: ")
    # python eval
    ran_list = eval(ran_str)
    ran_res = deal(ran_list)
    print(f"After process: {ran_res}")
    