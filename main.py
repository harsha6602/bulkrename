import os

#input of the filepath 
folder_path = input("Enter the file path:")
file_names = os.listdir(folder_path)

def Number_of_items():
    print(f"\nThere are {len(file_names)} items with file starting from {file_names[0]} to {file_names[-1]}")
    while True:
        choice = input("\ncheck the above data and confirm if yes or no? (y,n) : ")
        if choice == "y" or choice == "Y":
            return "yes" 
        elif choice == "n" or choice == "N":
            return "no"

#changes filepath's \ to /
def changing_path():
    global folder_changed 
    folder_changed = ""
    for i in range(0,len(folder_path)):
        if folder_path[i] == "\\" :
            folder_changed = folder_changed + "/"
        else:
            folder_changed = folder_changed + folder_path[i]

#changing file path
def changing_names(choice):
    if choice == "yes":
        name = input("\nEnter the name to be changed to:")
        print(("\nEnter the number from where the index should start :"))
        while True:
            try:
                count = int(input())
            except ValueError:
                count = print("\nReEnter the number from where the index should start :")        
            else:
                break
        for i in file_names:
            type = i.split('.')[-1]
            os.rename(folder_changed + "/" + i,folder_changed + "/" + name +"_"+ str(count) + "." + type)
            count = count + 1 
        print("Successfully changed")
    else:
        print("Filenames not changed")


if __name__ == "__main__":
    changing_path()
    choice = Number_of_items()
    changing_names(choice)
    