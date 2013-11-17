
T = int(raw_input())
for t in range(T):
  N = int(raw_input())
  h = 1
  for t in range(N):
    if t % 2 == 0:
      h *= 2
    else:
      h += 1
  print(h)
