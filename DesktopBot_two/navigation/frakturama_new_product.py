def add_product(self):
        #Typing in a field
        #Click relative to a label
        if not self.find( "Field_Name", matching=0.97, waiting_time=10000):
             self.not_found("Field_Name")
        self.click_relative(x=75, y=15)
        self.paste("Qualidade T2C")


        # Tab to go to another field
        self.tab()
        self.paste("Time foda")