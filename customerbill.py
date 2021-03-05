#customerbill.py
#Muhammad Ahmed Cheema and Samit Basnet
#prints out the bill for the user and keeps track of items for the store

import sys

def main():

    #list of barcodes of the items available in the store
    barcodes=['551141570', '12548965', '287281', '9856547']
    
    #list of dictionaries that relates the unique barcode to the name of the product, price and the quantity in the store
    lists=[{'551141570':['Womens Tee', 21.00, 500]},{'12548965':['Border Bed', 540, 200]},{'287281':['Forty Guns',5.00, 1000]},{'9856547':['Mob Case', 24.00, 25]}]

    #a list of dictionaries which contains empty lists for values to store the name, price and quantity of items bought by the user
    bill=[{'names':[]}, {'prices':[]}, {'quantities':[]}, {'totals':[]}]

    
    #while loop operates when the value for ans is "y"
    ans='y'
    while ans=='y':

        #takes the barcode of the product scanned by using the barcode scanner        
        barcode=input("Scan the barcode:")

        #allows the customer to enter the quantity they want to buy
        quantity=input("Enter the quantity you want to buy:")
            
        #gets the index of that barcode in the list of barcodes
        index=barcodes.index(str(barcode))

        #gets the name corresponding to the barcode using the index from above and appends the name in the list bill
        name=lists[index][str(barcode)][0]
        bill[0]['names'].append(name)
        
        #gets the price corresponding to the barcode using the index above and appends the price in the list bill
        price=lists[index][str(barcode)][1]
        bill[1]['prices'].append(price)
        
        #keeps track of the quantity of the items for the shop
        quantityforshop=lists[index][str(barcode)][2]       
        quantityforshop=int(quantityforshop)-int(quantity) #subtracts the quantity entered by the user from the quantity available in the store
        lists[index][str(barcode)][2]=quantityforshop #updates the new value to the list in the dictionary

        #displays a warning message when the quantity for the shop runs falls below 10
        if quantityforshop<=10:
            print("Warning! Running Out of Stock. You only have",quantityforshop,"items left.")

        
        #appends the quantity entered by the user in the bill
        bill[2]['quantities'].append(quantity)

        #calculates the total for an item and appends it in the bill
        total= float(price)*int(quantity)
        bill[3]['totals'].append(total)
        
        #asks the customer if they want to continue buying 
        ans=input("Do you want to continue buying?(y/n):")

        while ans != "y" and ans != "n" : #keeps on asking until the customer gives a valid answer

            print ("Please type y or n")
            ans=input("Do you want to continue buying?(y/n):")
    
    #prints the first row of the bill which is the titles
    print("| Product Name | Price | Quantity | Total Price |")
    print("-------------------------------------------------")

    Grandtotal=0 #accumulator that gives the grand total of the bill

    for i in range(len(bill[0]['names'])): #runs the loop as many times as there are items in the list for the values part of the dictionary inside the bill list

        #gets the name, price, quantity and total for the purchase
        name= bill[0]['names'][i]
        price= bill[1]['prices'][i]
        quantity= bill[2]['quantities'][i]
        total= bill[3]['totals'][i]

        #prints the name, price, quantity and total in table format such that the display is organized column wise with equal spaces between each columns
        print("|", name, " "* (11-len(name)),"|", price, " "* (4-len(str(price))),"|",quantity, " "*(7-len(str(quantity))),"|",total, " "* (10-len(str(total))),"|")
        Grandtotal=Grandtotal+total #accumulator adds total to itself after every loop

    print("-------------------------------------------------")
    print("Grand Total:",Grandtotal) #prints the grand total at the end 

    #asks the amount paid by user
    paid=input("Enter the amount the user paid:")

    #gives the amount to be returned
    change=int(paid)-Grandtotal
    print("Change to be returned:",change)
    
                                                                                                       
main()    
