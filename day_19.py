
num_counter = {}

# {1: 1, 2: 3, 3: 2, ...}

L1 = [1, 2, 2, 3, 2, 3, 4, 5]
for i in L1:
  if i in num_counter:
    num_counter[i] += 1
  else:
    num_counter[i] = 1

num_counter = {1: 1, 2: 3, 3: 2, 4: 1, 5: 1}

temp = 0
final_result = None

for k, v in num_counter.items():
  print(f"k: {k}, v: {v}, temp: {temp}")
  if v > temp:
    temp = v
    final_result = k