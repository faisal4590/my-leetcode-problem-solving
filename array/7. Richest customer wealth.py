def richest_customer_wealth(accounts):
    all_sums = []
    for i in range(len(accounts)):
        sum = 0
        for j in range(len(accounts[i])):
            sum += accounts[i][j]
        all_sums.append(sum)
    return max(all_sums)


richest_customer_wealth([[1, 5], [7, 3], [3, 5]])
