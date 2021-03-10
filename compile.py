f = open('locate_settings.hxsp')
a = f
f.close()
filename = a + "hbdockread.hxsp"
x = open(filename, 'r')
location = x
x.close()
filename = a + "hbdockread.hxsp"
myfile = open(filename, 'w')
location = myfile
myfile.close()
hxst = open(location + "type.hxs")
typef = hxst
hxst.close()
if typef == "DOC":
  hxsm = open(location + "main_text.hxs")
  text = hxsm
  hxsm.close()
  print(text)
  exit()
if typef == "UNDOC":
  hxsx = open(location + "server_a.hxs")
  blin = hxsx
  hxsx.close()
  if blin == "RUN":
    hxsx = open(location + "server_a_data/server_main.hxs")
    blio = hxsx
    hxsx.close()
  hxsx = open(location + "function_1.hxs")
  blim = hxsx
  hxsx.close()
  if blim == "PrintServerID":
    print(blio) # WEJFERKJBGGJJHERGKGERHJBGERKJHBGRKEF
  if blim == "EXECUTE_PROGRAM":
    # COMPLETE WHEN COMPILER COMPLETE -----------------------------------------------------------------------------------------------------------------------
    hxsx = open(location + "execute_program/folder.hxs")
    ep1 = hxsx
    hxsx.close()
    hxsx = open(location + "execute_program/folder2.hxs")
    ep2 = hxsx
    hxsx.close()
  if blim == "input":
    a = input("")
  if blim == "EXECUTE_PSINPUT":
    hxsx = open(location + "psinput/name.hxs")
    psn = hxsx
    hxsx.close()
    x = input("")
    hxsx = open(location + "server_a_data/vars/" + psn, "w")
    hxsx.write(x)
    hxsx.close()
  if blim == "EXECUTE_IF":
    hxsx = open(location + "if/1.hxs")
    blim1 = hxsx
    hxsx.close()
    hxsx = open(location + "server_a_data/vars/" + blim1)
    blim2 = hxsx
    hxsx.close()
    hxsx = open(location + "if/2.hxs")
    blim3 = hxsx
    hxsx.close()
    if blim1 == blim2:
      hxsx = open(location + "if/result/var/name.hxs")
      hxsx = name
      hxsx.close()
      hxsx = open(location + "if/result/var/data.hxs")
      hxsx = data
      hxsx.close()
      hxsx = open(location + "server_a_data/vars/" + name, "w")
      hxsx.write(data)
      hxsx.close()
