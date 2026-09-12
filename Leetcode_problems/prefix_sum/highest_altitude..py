def highest_altitude(gain):
    prefix=[0]
    count=0
    for gains in gain:
        prefix_sum=prefix[-1]+gains
        if prefix_sum>count:
            count=prefix_sum
        prefix.append(prefix_sum)
    return count
print(highest_altitude([-4,-3,-2,-1,4,3,2]))        