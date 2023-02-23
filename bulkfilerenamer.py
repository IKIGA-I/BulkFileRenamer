import os #letting the program know what os we are using currently

pathinput = input('Input file path[After C:/Users/golam/](Please replace backslashes with forward slashes): ')

def main():
    i = 0
    path = "C:/Users/golam/" + pathinput +"/" #Directory of Path where files are located
    for filename in os.listdir(path):
        my_dest = "text" + str(i) + ".txt"
        my_source = path + filename
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()
