input_list = [1, 6, 4, 22, 12, 24, 10, 7]
# Sorting code
def sorter(lista):
  new_list = []
  x = 0
  y = 1
  posx2 = 0
  posy2 = 0
  x = lista[0 + posx2]
  y = lista[1 + posy2]
  counter = 0
  counter2 = 0

  while counter == False:
    print "9: counter2 == %s, posy2 == %s" % (counter2, posy2)
    if posy2 >= (len(lista) - 1):
        print "1: started reseting"
        posx2 = 0
        posy2 = 0
        x = 0
        y = 1
        counter2 += 1
        print "2: %s %s %s %s" % (x, y, posx2, posy2)
        if counter2 == 10:
            counter = True
        else:
            counter = False
    else:
      print "3: standard"
      x = lista[0 + posx2]
      y = lista[1 + posy2]
      print "4: %s, %s" % (x, y)
      if x > y:
        print "5: %s" % (lista)
        inverter(x, y, lista)
        posx2 = posx2 + 1
        posy2 = posy2 + 1
        print "6: x > y == %s" % (lista)
        continue
      elif x < y:
        print "7: x < y"
        posx2 += 1
        posy2 += 1
        print "8: list == %s" % (lista)
        continue
  print lista


def inverter(x, y, lista):
  posx = lista.index(x)
  posy = lista.index(y)
  lista.remove(x)
  lista.insert(posy, x)

sorter(input_list)

# End of sorting code (sorted_list should equal [1, 2, 3, 4, 5, 6, 7]
