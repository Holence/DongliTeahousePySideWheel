from DTPySide.DTFunction import *

# MainWindow用的TitleBar Widget
from DTPySide.DTWidget.Ui_DTTitleBar import Ui_DTTitleBar
class DTTitleBar(Ui_DTTitleBar,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)
		self.full=True
		
		# windowIcon是自动继承的，直接设置就好了
		self.title_icon.setIcon(self.windowIcon())

		self.btn_close.clicked.connect(self.window().close)

		self.maximize_icon=QIcon(":/icon/white/white_window-maximize.svg")
		self.restore_icon=QIcon(":/icon/white/white_window-restore.svg")
		
		if self.window().isMaximized():
			#是最大化的
			self.btn_maximize.setIcon(self.restore_icon)
		else:
			self.btn_maximize.setIcon(self.maximize_icon)


		self.setStyleSheet("""

			#TitleBarFrame {	
				background-color: #21252B;
			}
			
			#TitleBarFrame QPushButton {	
				border: none;
				background-color: transparent;
			}

			#TitleBarFrame QPushButton:hover{
				background-color: #30353F;
				border-style: solid; 
				border-radius: 4px;
			}
			#TitleBarFrame QPushButton:pressed {	
				background-color: #49505F;
				border-style: solid;
				border-radius: 4px;
			}

			#TitleBarFrame #title_icon:hover{
				background-color: rgba(0, 0, 0, 0);
			}
			#TitleBarFrame #title_icon:pressed {	
				background-color: rgba(0, 0, 0, 0);
			}
			
			#TitleBarFrame #btn_close:hover{
				background-color: rgb(232, 17, 35);
				border-style: solid;
				border-radius: 4px;
			}
			#TitleBarFrame #btn_close:pressed {	
				background-color: rgb(241, 112, 122);
				border-style: solid;
				border-radius: 4px;
			}
		""")
	
	def setFull(self,full:bool):
		
		if full==False:
			self.btn_maximize.hide()
			self.btn_minimize.hide()
		if full==True:
			self.btn_maximize.clicked.connect(lambda:self.mouseDoubleClickEvent(None,True))
			self.btn_minimize.clicked.connect(self.window().showMinimized)
			self.title_icon.clicked.connect(lambda:show_ContextMenu_Beneath(self.window().MainMenu(),self.title_icon))

	def setWindowTitle(self,title):
		super().setWindowTitle(title)
		self.label_titlebar.setText(title)
	
	def mouseDoubleClickEvent(self, event, ignore_event=False):
		"""最大化最小化切换

		Args:
			event ([type]): [description]
			ignore_event (bool, optional): 没有event的话，想调用这个函数，event设为None，ignore_event设为True就行了. Defaults to False.
		"""		

		if self.full==True:
			if ignore_event==False and event.button() != Qt.LeftButton:
				return
			
			if self.btn_maximize.isHidden():
				self.btn_maximize.show()
			if self.btn_minimize.isHidden():
				self.btn_minimize.show()
			
			if self.window().isMaximized():

				#变成正常
				self.window().showNormal()
				self.btn_maximize.setIcon(self.maximize_icon)
			else:

				#变成最大化
				self.window().showMaximized()
				self.btn_maximize.setIcon(self.restore_icon)

	def mousePressEvent(self, event):
		""" 移动窗口 """
		win32gui.ReleaseCapture()
		win32gui.SendMessage(self.window().winId(), win32con.WM_SYSCOMMAND,
					win32con.SC_MOVE + win32con.HTCAPTION, 0)
		event.ignore()