class Delivery(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame __init__(self,parent)
        self.controller= controller
        deliverylabel=tk.Label(self,text='confirm your address:')
        deliverylabel.pack(side="top",fill="x",pady=10)
        deliveryentry=tk.Entry(self)
        deliverylabel.pack(pady=10)
        submitbutton=tk.Button(self,text="submit",command=lambda:print("m"))
        submitbutton.pack()
class Insurance(tk.Frame):
    def __init__(self,parent,controller):
        tk.frame __init__(self,parent)
        self.controller= controller
        insurancelabel=tk.Label(self,text='is product damage during return?')
        checkbutton=tk.button(self,text='yes')
        insurancelabel.pack(side="top",fill='x',pady=10)
        insuranceentry=tk.Entry(self)
        insurancelabel.pack(pady=10)
        createbutton=tk.button(self,text='claim insurance',command=lambda:print("x"))
class Invoice(tk.frame):
    def __init__(self,parent,controller):
        tk.frame __init__(self,parent)
        self.controller= controller
        descriptionlabel=tk.Label(self,text='description')
        invoicelabel.pack(side="top",fill='x',pady=10)
        quantitylabel=tk.Label(self,text='quantity')
        invoicelabel.pack(pady=10)
        pricelabel=tk.label(self,text='price')
        pricelabel.pack(pady=10)
        





