uthor__ = 'Keith'
import os

print "where would you like the new folder to be located? Press 1 for apdocs , Press 2 for PurchasingDocs," \
      " Press 3 for SalesDocs, Press 4 for Fleet."

i = raw_input('Please enter choice here:')

# This first part is to change director based on selection from above.

if i == "1":
    os.chdir("/fileserv/apdocs/")

    x = raw_input('Enter Folder Path Here: ')


# This part is to check to see if the directory exists and if it doesn't it will then create the directory.

    if os.path.isdir(x) == True:
        print"Directory already EXISTS"

    else:
        os.mkdir(x, 0755)
    dir = os.listdir("/fileserv/apdocs")
    print(dir)


if i == "2":
    os.chdir("/fileserv/purchasingdocs/")

    x = raw_input('Enter Folder Path Here: ')


# This part is to check to see if the directory exists and if it doesn't it will then create the directory.

    if os.path.isdir(x) == True:
        print"Directory already EXISTS"

    else:
        os.mkdir(x, 0755)
    dir1 = os.listdir("/fileserv/purchasingdocs")
    print(dir1)
