import os                                       #letting the program know what os we are using currently

pathinputtemp = input('Input file path: ')      #Taking input of File path and storing in a temporary variable
pathinput = pathinputtemp.replace("\\", "/")    #Making modifications, i.e correcting file path for use in the python function

thefilename = input('Name of new Files: ')      #Taking input of File Name
thefiletype = input("Please input what type of files they are(i.e extension): ")    #Taking input of File extension

def main():
    i = 0
    path = pathinput +"/"                       #Directory of Path where files are located
    for filename in os.listdir(path):
        my_dest = thefilename + str(i) + "." + thefiletype     #Name of files and their extensions concatenated
        my_source = path + filename             #Defining the location of source file for rename function
        my_dest = path + my_dest                #Defining the location of destination file for rename function
        os.rename(my_source, my_dest)           
        i += 1

if __name__ == "__main__":
    main()
