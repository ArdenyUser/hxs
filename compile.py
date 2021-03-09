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
