import sys
from PyQt4.QtGui import *

def main():
	app= QApplication(sys.argv)
	widget= QWidget()
	widget.move(300,350)
	widget.setWindowTitle("SimpleWidget")
	widget.show()

	sys.exit(app.exec_())

if __name__=='__main__':
	main()