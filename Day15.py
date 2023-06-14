start = [9,6,0,10,18,2,1]
dist = {9:[0], 6:[1], 0:[2], 10:[3], 18:[4], 2:[5]}

def find_nth(n):
    for i in range(len(start)-1, n-1):
        if start[i] not in dist:
            dist[start[i]] = [i]
            start.append(0)
        else:
            start.append(i-dist[start[i]][-1])
            dist[start[i]].append(i)
    return start[n-1]

print(find_nth(2020))
print(find_nth(30000000))