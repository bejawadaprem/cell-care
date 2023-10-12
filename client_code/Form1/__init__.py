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
    

    # Any code you write here will run before the form opens.
    
    

 # def text_box_1_pressed_enter(self, **event_args):
    #name=self.text_box_1.text
    #alert(name)

  #def button_1_click(self, **event_args):
    #name=self.text_box_1.text
    #alert('Thank for your Feedback')
    #This method is called when the button is clicked"

  def text_box_2_pressed_enter(self, **event_args):
    #mobile=self.text_box_2.text
    #alert(mobile)
    """This method is called when the user presses Enter in this text box"""

  def text_box_3_pressed_enter(self, **event_args):
    #model=self.text_box_3.text
    #alert(model)
    """This method is called when the user presses Enter in this text box"""

  def text_box_4_pressed_enter(self, **event_args):
    #address=self.text_box_4.text
    #alert(address)
    """This method is called when the user presses Enter in this text box"""

  def button_1_click(self, **event_args):
    name = self.text_box_1
    mobile= self.text_box_2
    model = self.text_box_3
    address = self.text_box_4
  
    
    #button=self.text_box_4.text
    #alert('Thanks for contacting us!')
    anvil.server.call('add_cellcare','name','mobile','model','address')
    Notification("Thank you for contacting us!").show()
    self.clear_inputs()
    """This method is called when the button is clicked"""
  def clear_inputs(self):
    self.text_box_1=''
    self.self.text_box_2=''
    self.self.text_box_3=''
    self.text_box_4=''
  def name_box_pressed_enter(self,**event_args):
    pass

  


  

    






    

    


  
  
    

    

