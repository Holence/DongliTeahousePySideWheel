from DTPySide.DTFunction import *

class DTCapsuleButton(QLabel):
	clicked=Signal()
	def __init__(self,parent,text,color):
		super().__init__(parent)
		self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Fixed)
		
		# setStyleSheet会自动清空font，这里还得手动set一下
		self.setText(text)
		self.setFont(parent.font())
		self.adjustSize()
		
		self.setStyleSheet(""" 
			QLabel {
				color: white;
				background-color: %s;
				border-radius: %spx;
				border: 1px solid %s;
			}
		"""%(color,int(self.height()/2),color))

		# SET DROP SHADOW
		shadow = QGraphicsDropShadowEffect(self)
		shadow.setBlurRadius(0.8)
		shadow.setXOffset(4)
		shadow.setYOffset(4)
		shadow.setColor(QColor("#252525"))
		self.setGraphicsEffect(shadow)
	
	def mouseReleaseEvent(self,event):
		super().mouseReleaseEvent(event)
		if event.button()==Qt.LeftButton:
			self.clicked.emit()
	
	# Clear_Layout时调用deleteLater删除DTCapsuleButton，但shadow消不干净，那就setGraphicsEffect为空
	def deleteLater(self):
		super().deleteLater()
		self.setGraphicsEffect(None)