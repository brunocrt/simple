def test(str):
  # a - true
  # abc - false
  # aba - true
  # abba - true
  if len(str) == 1:
    return True

  if len(str) == 3:
    if str[0] == str[len(str)-1]:
      return True
    else:
      return False

  middle = len(str)/2
  x = 0
  stack = []
  while x < middle:
    #print(f"append({str[x]})")
    stack.append(str[x])
    x = x + 1

  y = middle
  while y < len(str):
    ch = stack.pop()
    #print(f"ch: {ch}")
    if ch != str[int(y)]:
      #print(f"ch: {ch} != {str[int(y)]}")
      return False
    y = y + 1

  return True
  
print(f"a: {test('a')}")
print(f"abc: {test('abc')}")
print(f"aba: {test('aba')}")
print(f"abba: {test('abba')}")
print(f"abca: {test('abca')}")
print(f"abamomaba: {test('abamomaba')}")
print(f"abamolaba: {test('abamolaba')}")