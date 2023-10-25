from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    you='I Love You Anvil!'
    alert(' You Said '  + you)
    

    # Any code you write here will run before the form opens.
    
    

 

  

  
  
  
  def button_1_click(self, **event_args):
    name = self.text_box_1.text
    mobile= self.text_box_2.text
    model = self.text_box_3.text
    address = self.text_box_4.text
    anvil.server.call('add_submit',name,mobile,model,address)

    Notification("Your request Successfully Submitted!").show()
      
    #def clear_all(self):
      #self.name.text=''
      #self.mobile.text=''
      #self.model.text=''
      #self.address.text=''

  
  


  
    
    
  
  


  

    






    

    


  
  
    

    

