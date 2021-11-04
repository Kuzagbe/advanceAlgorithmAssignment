# num is the number of socks in the pile
# arr[num] is the colors per sock within the array arr

def sockMerchant(num, arr):


    socks_No = {}   # This dictionary will store the number of socks with the same color


    for color_of_socks in range(len(arr)): # Go through the elements of array (arr )
        if arr[color_of_socks] not in socks_No:     # Check if the sock color is not in socks_No
            socks_No[arr[color_of_socks]] = 1   # else, add it to the dictionary as key and its value to one
        else:
            socks_No[arr[color_of_socks]] += 1
            # either than that, increment the respective value of the sock color with one

    sumPairs = 0  # sumPairs will store the final number of pairs with matching colors


    for sock in socks_No:  # Go through the key value pairs in the dictionary with resoect to the number of socks
        sumPairs += socks_No[sock] // 2  #Perform floor division by 2 for each sock color sum
        # Add result to sumPairs
    return sumPairs   #return all paired socks of the same color