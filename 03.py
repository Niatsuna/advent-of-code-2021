from copy import deepcopy
# >>> Read Input <<<
input = []
with open('inputs/03.txt', 'r') as f:
  f_ = f.readlines()
  for l in f_:
    input.append(l.strip())

# >>> Solution - 1 <<<
gamma_ = ''
epsilon_ = ''

for i in range(0, len(input[0])):
  x = 0
  y = 0

  for j in range(0, len(input)):
    if input[j][i] == '1':
      x += 1
    else:
      y += 1

  gamma_ += f'{1 if x >= y else 0}'
  epsilon_ += f'{1 if x < y else 0}'

# >> Print <<
print(' === PART ONE ===')
print(f'Gamma: {int(gamma_, 2)} ({gamma_})')
print(f'Epsilon: {int(epsilon_, 2)} ({epsilon_})')
print(f' Solution: {int(epsilon_, 2) * int(gamma_, 2)}')

# >> Solution - 2 <<<+
oxygen = ''
oxygen_input = deepcopy(input)
i = 0

while(len(oxygen_input) != 1):
  x = 0
  y = 0

  for j in range(0, len(oxygen_input)):
    if oxygen_input[j][i] == '1':
      x += 1
    else:
      y += 1

  oxygen += f'{1 if x >= y else 0}'
  oxygen_input = list(filter(lambda x: x.startswith(oxygen), oxygen_input))
  i += 1
oxygen = oxygen_input[0]

co2 = ''
co2_input = deepcopy(input)
i = 0

while(len(co2_input) != 1):
  x = 0
  y = 0

  for j in range(0, len(co2_input)):
    if co2_input[j][i] == '1':
      x += 1
    else:
      y += 1

  co2 += f'{0 if x >= y else 1}'
  co2_input = list(filter(lambda x: x.startswith(co2), co2_input))
  i += 1
co2 = co2_input[0]

# >> Print <<
print(' === PART TWO ===')
print(f'Oxygen: {int(oxygen, 2)} ({oxygen})')
print(f'Epsilon: {int(co2, 2)} ({co2})')
print(f' Solution: {int(co2, 2) * int(oxygen, 2)}')