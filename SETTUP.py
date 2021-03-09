b = input("Enter the setting's, HXSP files usaully, directory that stores data: ")
filename = b
myfile = open(filename, 'w')
myfile.write('Written with Python\n')
myfile.close()
