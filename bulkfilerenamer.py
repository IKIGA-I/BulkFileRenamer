import os #letting the program know what os we are using currently

pathinputtemp = input('Input file path: ')
                                                #Taking input of File path can be modified
pathinput = pathinputtemp.replace("\\", "/")
def main():
    i = 0
    path = pathinput +"/"   #Directory of Path where files are located
    for filename in os.listdir(path):
        my_dest = "text" + str(i) + ".text"      #Name of files and their extensions, can be modified
        my_source = path + filename             #Defining the location of source file for rename function
        my_dest = path + my_dest                #Defining the location of destination file for rename function
        os.rename(my_source, my_dest)           
        i += 1

if __name__ == "__main__":
    main()
