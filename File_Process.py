import os

def main():

    # prompt the user for the directory they would like to save the file
    directory = input("Please, enter the directory that you want to save the file : ")

    filename = input("Now enter the filename : ")

    user_name = input("Next, enter your name : ")

    address = input("Please enter your address : ")

    phone_number = input("Lastly, enter your phone number : ")

    # validate that a directory exists before creating a file 
    # in that directory
    if os.path.isdir(directory):

        # create and open the file to write

        writeFile = open(os.path.join(directory,filename),'w')

        # writing the data and seperate entries with a comma

        writeFile.write(user_name+','+address+','+phone_number+'\n')

        # close the file after writing is done

        writeFile.close()

        print("File contents:")

        # read the file for proof of storage

        readFile = open(os.path.join(directory,filename),'r')

        for line in readFile:

            print(line)

        readFile.close()

    else:

        print("Sorry, that directory does not exist,\nPlease, enter another.")

# Call the main function
if __name__ == '__main__':
    main()