
from tkinter import *
import urllib3
import urllib.request
import json

class window(Frame):  # frame acts as a container for all the other widgets 

    def __init__(self,master):

        Frame.__init__(self,master) 

        self.grid() # makes sure all the widgets are put into their specific grids

        self.create() # calls the create function

            

    def create (self):

        photo = PhotoImage (file = "lol.gif")# photoimage can read a gif and ppm image and here it reads the image file lol
        self.intro = Label (self, image = photo) # the label widget displays the image onto the screen 
        self.intro.photo = photo # sets the image that was already read onto photo 
        self.intro.grid (row = 0, column = 0) # puts the image into the specific location / grid on the screen
        

        self.info = Label(self, text = "Plese Enter Your Barcode", font = (16)) # this label widget displays text on to the screen 
        self.info.grid(row = 1, column = 0,  sticky = EW) # sets the image below the widget above it  ( sticky aligns it in the center as we write east west )
        self.barcode = Entry(self) # creats an emtry widget which returns anything entered in it 
        self.barcode.grid(row = 2, column = 0,  sticky = EW) # it again sets it below the upper one 

        self.demand = Label(self, text = "What Information Do You Want For The Product", font = (14)) # label widget, prints the text 
        self.demand.grid(row = 4, column = 0,  sticky = EW) # sets it below the the upper widget

           
        self.name = BooleanVar() # creats a variable with only true or false 
        Checkbutton (self, text = " Product Name",font = (14), variable = self.name, command = self.updatetext).grid(row = 5, column = 0, sticky = EW) # creates a check button and sets it on the screen         

        self.textname = Text(self, width = 50, height = 1, wrap = WORD) # creates a text widget in which the information can be shown 
        self.textname.grid ( row = 6 , column = 0, sticky = EW) # sticky again sets it in the center and puts it on the screen 
        

        self.price = BooleanVar()
        Checkbutton (self, text = "Price",font = (14), variable = self.price, command = self.updateprice).grid(row = 7, column = 0, sticky = EW)

        self.pricetext = Text(self, width = 50, height = 1, wrap = WORD)
        self.pricetext.grid ( row = 8 , column = 0, sticky = EW)

        self.desc = BooleanVar()
        Checkbutton (self, text = "Brief Description", font = (14),variable = self.desc, command = self.updatedesc).grid(row = 9, column = 0, sticky = EW)

        self.desctext = Text(self, width = 50, height = 1, wrap = WORD)
        self.desctext.grid ( row = 10 , column = 0, sticky = EW)

        self.avail = BooleanVar()
        Checkbutton (self, text = "Availability", font = (14),variable = self.avail, command = self.updateavail).grid(row = 11, column = 0, sticky = EW)

        self.availtext = Text(self, width = 50, height = 1, wrap = WORD)
        self.availtext.grid ( row = 12 , column = 0, columnspan = 2, sticky = EW)

        self.pic = BooleanVar()
        Checkbutton (self, text = "Display Picture", font = (14),variable = self.pic, command = self.updatepic).grid(row = 13, column = 0, sticky = EW)

        
        self.enter = Button (self, text = "Submit", command = self.updatefill) # creates a button and links it with the command function which contains sub functions
        self.enter.grid ( row = 14 , column = 0, sticky = EW) # sets it in the center of the screen at the end 

    def updatefill (self):

        self.textname.delete(0.0, END) 
        self.pricetext.delete(0.0, END)  # this deletes everything in text widgets, everytime submit is pressed 
        self.desctext.delete(0.0, END)
        self.availtext.delete(0.0, END)            
                  
        self.updatetext()  # calls the functions everytime the submit button is pressed 
        self.updateprice()
        self.updatedesc()
        self.updateavail()
        self.updatepic()


    def updatetext (self):

        content = self.barcode.get()  # gets the barcode entered into the entry widget (self.barcode)
        url = "http://api.walmartlabs.com/v1/items/" + content + "?format=json&apiKey=sx3wvy7ak5379dexwf385t39" # puts the barcode into the url
        http = urllib3.PoolManager() # pool manager defines http and makes sure to call the url 
        dat = http.request("GET", url) # it gets the data from the api server in json strings 
        forma = json.loads(dat.data.decode()) # this converts json strings into python objects

        
        
        if self.name.get() == False: # if the check box is unchecked it deleted all the text in it 

            self.textname.delete(0.0, END)            
            
        elif self.name.get() == True: # else if it is checked it prints the required data on it 

            textname = forma["name"] # reads the value from the dictionary with key enterd in 
            self.textname.insert(0.0, "  " + textname) # inserts the information retrieved by the previous in the text box 

    def updateprice (self):

        content = self.barcode.get()  # gets the barcode entered into the entry widget (self.barcode)
        url = "http://api.walmartlabs.com/v1/items/" + content + "?format=json&apiKey=sx3wvy7ak5379dexwf385t39" # puts the barcode into the url
        http = urllib3.PoolManager() # pool manager defines http and makes sure to call the url 
        dat = http.request("GET", url) # it gets the data from the api server in json strings 
        forma = json.loads(dat.data.decode()) # this converts json strings into python objects

        if self.price.get() == False:

             self.pricetext.delete(0.0, END)            

        elif self.price.get() == True:

            pricetext = str(forma["salePrice"])
            self.pricetext.insert(0.0, "  $ " + pricetext)


    def updatedesc (self):

        content = self.barcode.get()  # gets the barcode entered into the entry widget (self.barcode)
        url = "http://api.walmartlabs.com/v1/items/" + content + "?format=json&apiKey=sx3wvy7ak5379dexwf385t39" # puts the barcode into the url
        http = urllib3.PoolManager() # pool manager defines http and makes sure to call the url 
        dat = http.request("GET", url) # it gets the data from the api server in json strings 
        forma = json.loads(dat.data.decode()) # this converts json strings into python objects

        

        if self.desc.get() == False:

            self.desctext.delete(0.0, END)            

        elif self.desc.get():

            desctext = forma["shortDescription"]
            self.desctext.insert(0.0, "  " + desctext)


    def updateavail (self):

        content = self.barcode.get()  # gets the barcode entered into the entry widget (self.barcode)
        url = "http://api.walmartlabs.com/v1/items/" + content + "?format=json&apiKey=sx3wvy7ak5379dexwf385t39" # puts the barcode into the url
        http = urllib3.PoolManager() # pool manager defines http and makes sure to call the url 
        dat = http.request("GET", url) # it gets the data from the api server in json strings 
        forma = json.loads(dat.data.decode()) # this converts json strings into python objects



        if self.avail.get() == False:

            self.availtext.delete(0.0, END)            
           

        elif self.avail.get() == True:

            availtext = forma["stock"]
            self.availtext.insert(0.0, "  " + availtext)

    def updatepic(self):

        content = self.barcode.get()  # gets the barcode entered into the entry widget (self.barcode)
        url = "http://api.walmartlabs.com/v1/items/" + content + "?format=json&apiKey=sx3wvy7ak5379dexwf385t39" # puts the barcode into the url
        http = urllib3.PoolManager() # pool manager defines http and makes sure to call the url 
        dat = http.request("GET", url) # it gets the data from the api server in json strings 
        forma = json.loads(dat.data.decode()) # this converts json strings into python objects

        picurl = forma["largeImage"]  # returns the url for the lare size of that picture from the api 

        urllib.request.urlretrieve(picurl, "pici.gif") # saves the picture from the url with the same name so everytime a different barcode is called it updates the image 

              

        
def main():
    
    win = Tk () 

    win.title ("Product Information Viewer By Muhammad & Samit") # prints the title on the top of the screen 

    app = window(win)

    win.geometry ("1000x650") # makes a window with pixles 1000 and 650

    win.mainloop() # calls the tkinter window 

main()



        

        

        

        

        
