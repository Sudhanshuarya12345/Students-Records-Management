from functools import reduce
 
def EditContent():
    # Opening file as read mode
    fileR = open('tutpy51Student_Data.txt','r')
    
    data = input("Enter the new data: ")
    thing = int(input("Above data is for which info (usn-0, name-1, Mob-2, Address-3): "))
    line = int(input("For which Line(i.e; line = USN+1): "))-1
    print(f"We are Editing for line{line+1} and thing{thing} to {data}")
    
    # reading complete content as List 
    contents = fileR.readlines()
    
    # seperation of each line of content
    contents[line] = contents[line].split('$')
    
    # Get the value you want to change
    olddata = contents[line][thing]

    if thing==0:
        data = data.center(15)
    elif thing==1:
        data = data.center(30)
    elif thing==2:
        data = data.center(17)
    elif thing==3:
        data = data.center(50)
        
    # replace that value
    contents[line][thing] = contents[line][thing].replace(olddata, data)
    
    # join all the list value
    # contents[line] = contents[line][0]+'$'+contents[line][1]+'$'+contents[line][2]+'$'+contents[line][3]
    NewLine = reduce(lambda x,y: x+'$'+y, contents[line])    # add all line and form a single string
    
    contents[line] = NewLine
        
    # NewData = ''.join(contents)
    NewLines = reduce(lambda x,y: x+y, contents)                     # add all element of a line
    
    fileR.close()

    fileW = open('tutpy51Student_Data.txt','w')
    fileW.write(NewLines)
    # NewData is collection of every old line of file in which we change content using list and string method, string concatination
    print("Editing Completed....\n","Congratulation.......")
    fileW.close()


def AddNewContent():
    with open('tutpy51Student_Data.txt','r') as fileR:
        content = fileR.readlines()
        line = len(content)
        print(f"Your data will store in {line+1}")    

    fileA = open('tutpy51Student_Data.txt','a')
    usn = input('Enter the USN: ')
    name = input('Enter you name: ')
    mob = input('Enter your Mob. No: ')
    Address = input('Enter your Address: ')
    fileA.write(f"\n{usn.center(15)}${name.center(30)}${mob.center(17)}${Address.center(50)}$")
    fileA.close()

def searchContent():
    with open('tutpy51Student_Data.txt','r') as FileR:
        Contents = FileR.readlines()
        
        data = input("Enter the data(like usn, name, mob. no. or address) which you want to find: ")
        LineNumber = 0
        FindOrNot = 0
        specify = int(input('Do you want to check in any specific (yes - 1 or No - 0)'))
        if specify:
            index = int(input('Specify 0-usn, 1-name, 2-mob, 3-Address'))
            for content in Contents:
                LineNumber +=1
                Data = content.split('$')
                if Data[index].find(f'{data}') != -1:
                    FindOrNot = 1
                    print('\nYour data may be following')
                    print(f'Line    - {LineNumber}')
                    print(f'USN     - [{Data[0].center(50)}]')
                    print(f'Name    - [{Data[1].center(50)}]')
                    print(f'Mob. No - [{Data[2].center(50)}]')
                    print(f'Address - [{Data[3]}]')
        else:
            for ContentInLine in Contents:
                LineNumber +=1
                if ContentInLine.find(f'{data}') != -1:
                    FindOrNot = 1
                    Data = ContentInLine.split('$')
                    print('\nYour data may be following')
                    print(f'Line    - {LineNumber}')
                    print(f'USN     - [{Data[0].center(50)}]')
                    print(f'Name    - [{Data[1].center(50)}]')
                    print(f'Mob. No - [{Data[2].center(50)}]')
                    print(f'Address - [{Data[3]}]')
    if FindOrNot==0:
        print("No Data Matching.......")
    
    
if __name__ == '__main__':
    loop = True
    while loop:
        opt = int(input('What do you want to do\nPress\n1 for Add new Detail\n2 for Change previous detail\n3 for search any data\n4 for exit\n'))
        match opt:
            case 1:
                AddNewContent()
            case 2:
                EditContent()
            case 3:
                searchContent()
            case 4:
                loop = False
        print() 