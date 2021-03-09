b = input("Enter the setting's, HXSP files usaully, directory that stores data: ")
filename = "locate_settings.hxsp"
myfile = open(filename, 'w')
myfile.write(b)
myfile.close()
