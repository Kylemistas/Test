shoppingcart = [] #storing of values shoes
print('\t\tTindhan ni Juan')
print('(Sa tindahan  ni juan lahat kompleto, sya lang ang nagkulang!)\n')
print('\t   Welcome to Tindhan ni Juan!')
while True: #whileloop for true
    operation = input('\nEnter Your Choice:\n 1 - Add To Cart \n 2 - Remove To Cart\n 3 - View Your Cart\n 4 - Sort All Your Cart\n 5 - Checkout \n 6 - Clear Cart\n 7 - Exit\n >> ')
    
    if operation == '1':
        print('Add to Cart')
        Item = input('Enter the item you want to add on your cart: ')
        shoppingcart.append(Item) #fuction method that adds an element at the end of the list
        continue
    elif operation == '2':
        print("Remove to Cart")       
        if len(shoppingcart)== 0: #to messure the list of items
            print('You cannot delete any Item. Please try again!')
            continue
        else:
            Item = input('Enter the Item you want to delete: ')
            if Item in shoppingcart:
                shoppingcart.remove(Item) #fuction method that removes the item with the specified value
                print('Your '+ Item + ' item has been deleted.' ) #type casting
                continue
            else:
                print('Invalid Item')
                continue
        continue
    elif operation == '3':
        print('View Your Cart')
        if len(shoppingcart) == 0:
            print('List is Empty! Please Try again.')
            continue
        else:
            for Item in shoppingcart: #for loop
                print(Item)         
        continue
    elif operation == '4':
        if len(shoppingcart)== 0:
            print('You cannot sort any Item. Please try again!')
            continue
        else:
           print('Sorting Your Items')
           shoppingcart.sort() #fuction method that Sorts the list
           print(shoppingcart)
    elif operation == '5':
        print('Checkout')
        if len(shoppingcart)== 0:
            print('You cannot Checkout any Item. Please try again!')
            continue
        else:
            Item = input('Enter the one item you want to checkout: ')
            if Item in shoppingcart:
                print('\n' + Item + ' has been purchase succesfully! Please wait your item for a week1')
                shoppingcart.remove(Item)
                continue
            else:
                print('Invalid Item')
                continue
        continue
    elif operation == '6':
        print("Clear All in Carts\n")
        if len(shoppingcart)== 0:
            print('You cannot Clear the cart. Please try again!')
            continue
        else:
            clear = input('Are You sure you want to Clear all items? (yes/no): ')
            if clear == 'yes':
                shoppingcart.clear() #fuction method that Removes all the elements from the list
                print (shoppingcart)
                print('All the Items are Removed.')
            elif clear == 'no':
                print ('All Items are not completely removed.')
            else:
                 print('Invalid Input')
    elif operation == '7': 
        print('Exiting...') # for exiting the program
        break
    else:
        print('Invalid Input')
        break