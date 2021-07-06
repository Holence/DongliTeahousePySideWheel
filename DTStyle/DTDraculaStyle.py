DTDraculaNormalStyle="""

#TitleBarFrame * {	
	background-color: #21252B;
}
#TitleBarFrame {	
	background-color: #21252B;
}
#TitleBarFrame #label_titlebar {
	color: #EBEBEB;
}

#DTMainWindow #centralWidget {	
	background-color: #282C34;
}

#DTMainWindow #statusBar{
	background-color: #30353F;
}


QDialog {
	border: 2px solid #21252B;
	border-radius: 1px;
}

QPushButton {
	font-family: "Hack";
}


"""

###############################################################################################

DTDraculaEffectStyle="""

* {
	background-color: transparent;
}

#TitleBarFrame * {	
	background-color: #21252B;
}
#TitleBarFrame {	
	background-color: #21252B;
}
#TitleBarFrame #label_titlebar {
	color: #EBEBEB;
}


#DTMainWindow #statusBar{
	background-color: #30353F;
}



/* 设置Window Effect后有些Palette会失效，得用stylesheet补足 */

QMenu {
	background-color: #282C34;
	color: #EBEBEB;
}
QMenu::item:selected {
	background-color: #BD93F9;
}

QLineEdit {
	background-color: #21252B;
}

QDialog {
	background-color: #282C34;
	border: 2px solid #21252B;
	border-radius: 1px;
}

QPushButton {
	font-family: "Hack";
	background-color: #282C34;
}


"""