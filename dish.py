a = 0.02
r = 50
D2_ARRAY = []
D2_ARRAY_EXACT = []
D3_ARRAY = []
def compute(ang,radius):
  for i in range(0 - radius, radius + 1):
    D2_ARRAY.append(round(ang * i * i))
    D2_ARRAY_EXACT.append(ang * i * i)
  for i in range(0 - radius, radius + 1):
    D3_ARRAY_LINE = []
    for x in range(0, radius * 2 + 1):
      D3_ARRAY_LINE.append(round(D2_ARRAY_EXACT[i] + D2_ARRAY_EXACT[x]))
    D3_ARRAY.append(D3_ARRAY_LINE)
  D2_MAX = max(D2_ARRAY)
  count = 0
  for i in D3_ARRAY:
    count2 = 0
    for x in i:
      if D3_ARRAY[count][count2] > D2_MAX:
        D3_ARRAY[count][count2] = D2_MAX
      count2 += 1
    count += 1
  print(D3_ARRAY)
compute(a,r)
