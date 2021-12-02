# >>> Read Input <<<
input = []
with open('inputs/02.txt', 'r') as f:
  f_ = f.readlines()
  for l in f_:
    s = l.split(' ')
    input.append([s[0], int(s[1])])

# >>> Solution - 1 <<<
x = 0
y = 0

for inst in input:
  instruction = inst[0]
  if instruction == 'forward':
    x += inst[1]
  elif instruction == 'down':
    y += inst[1]
  elif instruction == 'up':
    y -= inst[1]
  else:
    print(f'Illegal Instruction {inst}')

# >> Print <<
print(' === PART ONE ===')
print(f'Final Horizontal Position: {x}')
print(f'Final Depth: {y}')
print(f'Solution {x} x {y} = {x*y}')

# >> Solution - 2 <<<
x = 0
y = 0
aim = 0

for inst in input:
  instruction = inst[0]
  if instruction == 'forward':
    x += inst[1]
    y += aim * inst[1]
  elif instruction == 'down':
    aim += inst[1]
  elif instruction == 'up':
    aim -= inst[1]
  else:
    print(f'Illegal Instruction {inst}')

# >> Print <<
print(' === PART TWO ===')
print(f'Final Horizontal Position: {x}')
print(f'Final Depth: {y}')
print(f'Solution {x} x {y} = {x*y}')