from DTPySide.DTFunction import *

class DTToolTip(QLabel):
	def __init__(self, parent, tooltip):
		super().__init__(tooltip,parent)
		
		self.setFont(parent.font())
		
		self.setStyleSheet(""" 
			QLabel {
				background-color: #0C0B0B;	
				color: #E6E6E6;
				padding-left: 10px;
				padding-right: 10px;
				border-radius: %spx;
				border: 1px solid #0C0B0B;
				border-left: 3px solid #FF6265;
			}
		"""%(self.font().pointSize()//2))
		
		self.adjustSize()

		# SET OPACITY
		opacity = QGraphicsOpacityEffect(self)
		opacity.setOpacity(0.85)
		self.setGraphicsEffect(opacity)