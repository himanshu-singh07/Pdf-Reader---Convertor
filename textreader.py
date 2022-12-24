menu = {}
menu['1']="1" 
menu['2']="2"
menu['3']="3"
while True: 
  options=menu.keys()
  options.sort()
  for entry in options: 
      print (entry, menu[entry])

    selection = input(a)
    file = open("{}.txt".format(selection))  