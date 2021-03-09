print("Welcome to HXS WORKSPACE!")
print("1: Execute 2: Python Executer Maker")
x = input("To answer, enter number: ")
if x == "1":
  hbdock = input("Program directory: ")
  f = open('locate_settings.hxsp')
  filename = f + "hbdockread.hxsp"
  myfile = open(filename, 'w')
  myfile.write(hbdock)
  myfile.close()
