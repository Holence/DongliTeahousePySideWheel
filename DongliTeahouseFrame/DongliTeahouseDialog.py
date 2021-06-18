from DongliTeahousePySideWheel.DongliTeahouseFunction import *

# Dialog Module
from DongliTeahousePySideWheel.DongliTeahouseFrame.Ui_DongliTeahouseDialog import Ui_DongliTeahouseDialog
class DongliTeahouseDialog(Ui_DongliTeahouseDialog,QDialog):
	def __init__(self,parent,title):
		if parent==None:
			super().__init__()
		else:
			super().__init__(parent)
		
		self.setupUi(self)
		
		# 无边框
		self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.CustomizeWindowHint)
		
		# 继承字体
		self.setAttribute(Qt.WA_WindowPropagation)
		if 0.7*self.font().pointSize()>=9:
			self.buttonBox.setFont(Font_Resize(self.font(),0.7))
		
		# 缩放角
		self.setSizeGripEnabled(True)

		self.TitleBar.setWindowTitle(title)