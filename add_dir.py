__author__ = 'Keith'
import os
 
print "where would you like the new folder to be located? Press 1 for apdocs , Press 2 for PurchasingDocs," \
      " Press 3 for SalesDocs, Press 4 for Fleet."
choice = raw_input('Please enter choice here:')
 
while choice == '1':
 
    if choice == "1":
        os.chdir('/fileserv/apdocs/')
 
    x = raw_input('Enter Folder Path Here: ')
 
    # This part is to check to see if the directory exists and if it doesn't it will then create the directory.
 
    if os.path.isdir(x) == True:
        print()
 
    else:
        os.mkdir(x, 0755)
 
    dir = os.listdir("/fileserv/apdocs")
    print(dir)
   
    cont = raw_input("Would you like to continue: y/n?")
    if cont in ('N', 'n'):
        break
 
while choice == "2":
    if choice == '2':
        os.chdir('/fileserv/purchasingdocs/')
 
    x = raw_input('Enter Folder Path Here: ')
 
    # This part is to check to see if the directory exists and if it doesn't it will then create the directory.
 
    if os.path.isdir(x) == True:
        print()
 
    else:
        os.mkdir(x, 0755)
    dir = os.listdir("/fileserv/purchasingdocs")
    print(dir)
 
    cont = raw_input("Would you like to continue: y/n?")
    if cont in ('N', 'n'):
        break
   
while choice == '3':
    if choice == "3":
        os.chdir('/fileserv/salesdocs/')
 
    x = raw_input('Enter Folder Path Here: ')
 
    # This part is to check to see if the directory exists and if it doesn't it will then create the directory.
 
    if os.path.isdir(x) == True:
        print()
 
    else:
        os.mkdir(x, 0755)
    dir = os.listdir("/fileserv/salesdocs")
    print(dir)
 
    cont = raw_input("Would you like to continue: y/n?")
    if cont in ('N', 'n'):
        break
   
while choice == '4':
    if choice == "4":
        os.chdir('/fileserv/fleet/')
 
    x = raw_input('Enter Folder Path Here: ')
 
    # This part is to check to see if the directory exists and if it doesn't it will then create the directory.
 
    if os.path.isdir(x) == True:
        print()
 
    else:
        os.mkdir(x, 0755)
    dir = os.listdir("/fileserv/fleet")
    print(dir)
 
    cont = raw_input("Would you like to continue: y/n?")
    if cont in ('N', 'n'):
        break
	quit()
