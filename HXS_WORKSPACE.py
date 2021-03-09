print("Welcome to HXS WORKSPACE!")
print("1: Execute 2: Python Executer Maker")
x = input("To answer, enter number: ")
if x == "1":
  hbdock = input("Program directory: ")
  f = open('locate_settings.hxsp')
  a = f
  f.close()
  filename = a + "hbdockread.hxsp"
  myfile = open(filename, 'w')
  myfile.write(hbdock)
  myfile.close()
  inport compile
