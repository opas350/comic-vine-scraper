'''
This module contains the CVForm class.

Created on Mar 10, 2010
@author: cbanack
'''
#corylow: comment and cleanup this file
import clr
from persistentform import PersistentForm

clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import FormBorderStyle

#==============================================================================
class CVForm(PersistentForm):
   '''
   This class is the direct superclass of all Comic Vine Scraper Forms.
   It contains functionality and default configuration that is common to
   all forms in this application.
   '''

   #===========================================================================
   def __init__(self, owner, persist_loc_key = "", persist_size_key = "" ):
      ''' 
      Constructs a new CVForm.
      Requires an owner parameter, which is the Form that will own this form.
      The other two parameters are passed up to the PersistentForm superclass.
      '''
      PersistentForm.__init__( self, persist_loc_key, persist_size_key )
      
      self.Owner = owner 
      self.Modal = False
      self.MaximizeBox = False                                                
      self.MinimizeBox = False                                                
      self.ShowIcon = False                                                   
      self.ShowInTaskbar = False    
      self.FormBorderStyle = FormBorderStyle.FixedToolWindow
      

   #===========================================================================
   def __enter__(self):
      ''' Called automatically when you using this form in a "with" block. '''
      return self
   
   
   #===========================================================================
   def __exit__(self, type, value, traceback):
      ''' Called automatically when you using this form in a "with" block. '''
      self.Close()
      self.Dispose()

