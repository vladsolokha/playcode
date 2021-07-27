# For given array of transactoins, group all transactions by item name.
# Return array of strings where each string contains the item name followed by space
# and the number of associated transactions

# Sort the array descending by transaction count, then ascending alphabetically by item name 
# for items with matching transaction counts

def countSortTransactions (transactions):
    #write code here
    pass


#Driver Code
transactions_arr = ['can', 'bin', 'bin', 'can', 'coin', 'bin', 'piggy']
print(countSortTransactions(transactions_arr))