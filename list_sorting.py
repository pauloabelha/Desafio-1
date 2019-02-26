input_list = [2, 1, 5, 3, 6, 4, 7]
# Sorting code
def sorter(lista):
  new_list = []
  x = 0
  y = 1
  posx2 = 0
  posy2 = 0
  x = lista[0 + posx2]
  y = lista[1 + posy2]
  print posx2
  print posy2

  for i in range((len(lista))):
    x = lista[0 + posx2]
    y = lista[1 + posy2]
    print "go"
    if x > y:
      inverter(x, y, lista, new_list)
      posx2 = posx2 + 1
      posy2 = posy2 + 1
      continue
    elif x < y:
      posx2 += 1
      posy2 += 1
      continue
  print posx2
  print posy2
  print new_list


def inverter(x, y, lista, new_list):
  posx = lista.index(x)
  posy = lista.index(y)
  new_list.insert(posx, y)
  new_list.insert(posy, x)

sorter(input_list)

# End of sorting code (sorted_list should equal [1, 2, 3, 4, 5, 6, 7]
