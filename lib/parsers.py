def number(equation: str, start: int = 0) -> tuple[float, int] | None:
  buffer = ""
  percentage = False

  for i in range(start, len(equation)):
    char = equation[i]
    if(char == "%"):
      percentage = True
      break

    if(char not in "0123456789."):
      break

    buffer += char

  if(buffer == ""):
    return None

  length = len(buffer)
  numb = float(buffer)
  if(percentage):
    numb /= 100
    length += 1

  return (numb, length)