from DTPySide.DTFunction import *

# Login 
from DTPySide.DTModule.Ui_DTLogin import Ui_DTLogin
class DTLogin(Ui_DTLogin,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)