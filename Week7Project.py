#Kris Candy Cane Factory
#Tuesday December 16th 2014
#benet morando bis 323

from tkinter import *

class Application(Frame):
    """GUI application that works for the inventory of Kris Candy Cane Factory"""
    def _init_(self, master):
        """initialize Frame"""
        super(Application, self)._init_(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets to get and display information """
        #create the input for the documenting the number of candy canes.
        Label(self,
              text = "Welcome to the Kris Candy Cane Inventory and Production Report."
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #create a label and text entry for the number of candy canes
        Label(self,
              text = "Candy Cane Production: "
              ).grid(rox = 1, column = 0, sticky = W)
        self.ccprod_ent = Entry(self)
        self.ccprod_ent.grid(row = 1, column = 1, sticky = W)

        #createa label and text entry for the number of candy canes per box
        Label(self,
              text = "Candy Canes per Box: "
              ).grid(row = 2, column = 0, sticky = W)
        self.ccperbox_ent = Entry(self)
        self.ccperbox_ent.grid(row = 2, column = 1, sticky = W)

        #create a label and text entry for price per box
        Label(self,
              text = "Price per box: "
              ).grid(row = 3, column = 0, sticky = W)
        self.boxprice_ent = Entry(self)
        self.boxprice_ent.grid(row = 3, column = 1, sticky = W)

        #create a calculate button
        Button(self,
               text = "Calculate",
               command = self.calculate
               ).grid(row = 4, column = 0, sticky = W)

        self.calculate_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.calculate_txt.grid(row = 5, column = 0, columnspan = 4)

    def calculate(self):
        """Fill text box with summary based upon user input. """
        #get values from the GUI
        Candy_Cane_Production = self.ccprod_ent.get()
        Per_Box = self.ccperbox_ent.get()
        Price_per_box = self.boxprice_ent.get()
        Final_Price = Per_Box * Price_per_box

        #create the summary
        summary = "Here is the summary for the Kris Candy Cane report. Here is the total production "
        summary += Candy_Cane_Production + ". "
        summary += "The amount of candy canes per box is "
        summary += Per_Box + ". "
        summary += "The price per box is "
        summary += Price_per_box + ". "
        summary += "The retail price for the finished packaging is "
        summary += Final_Price + ". "
        summary += "Thank you for your information. Have a nice day!"

        #display summary
        self.summary_txt.delete(0.0, END)
        self.summary_txt.insert(0.0, summary)
        
root = Tk()
root.title("Kris's Candy Cane Inventory and Production Report")
app = Application(root)
root.mainloop()
    
              
