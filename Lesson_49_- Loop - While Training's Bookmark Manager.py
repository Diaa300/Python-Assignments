# ----------------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------------

# Empty List To Fill Later
myFavouritWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:

    # Input The New Website
    web = input("Website Name Without https:// ")

    # Add The New Website To The List
    myFavouritWebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allwoed Websites
    maximumWebs -= 1 # maximumWebs = maximumWebs - 1

    # Print The Add Message
    print(f"Website Added, {maximumWebs} Places Left")

    # Print The List
    print(myFavouritWebs)

else :
    print("Bookmark Is Full, you Can't Add More")


# Check If List Not Empty     

if len(myFavouritWebs) > 0:

# Sort The List 
    myFavouritWebs.sort()

    index = 0

    print("Printing The List Of Websites In Your Bookmark")

    while index < len(myFavouritWebs):

        print(myFavouritWebs[index])       

        index += 1
        