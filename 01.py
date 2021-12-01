# >>> Read Input <<<
input = []
with open('inputs/01.txt', 'r') as f:
  f_ = f.readlines()
  for l in f_:
    input.append(int(l))

# >>> Solution - 1 <<<
last = input[0]

increased = 0
decreased = 0
same = 0

for m in input[1:] :
  if last == m:
    same += 1
  elif last > m:
    decreased += 1
  else:
    increased += 1

  last = m

# >>> Print <<<
print(' === PART ONE ===')
print(f'Increased {increased} times.')
print(f'Decreased {decreased} times.')
print(f'Stayed the same {same} times.')

# >>> Solution - 2 <<<
input_length = len(input)
size = 3

x = 1

increased = 0
decreased = 0
same = 0

while( x + size <= input_length) :
  last = sum(input[(x-1):(x-1+size)])
  current = sum(input[x:(x+size)])

  if last == current:
    same += 1
  elif last > current:
    decreased += 1
  else:
    increased += 1

  x += 1

# >>> Print <<<
print(' === PART TWO ===')
print(f'Increased {increased} times.')
print(f'Decreased {decreased} times.')
print(f'Stayed the same {same} times.')