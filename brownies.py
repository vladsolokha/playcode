'''given array or arrays and an int,
pop out numbers in arrays that are smaller than int
'''

def brownies(n, arr):
  for tray in arr:
    for brownie in tray:
      if brownie < n:
        tray.remove(brownie)
  return arr

print(brownies(3, [[2,1,3],[6,2,7]]))
print(brownies(3, [[1],[2]]))