import sys
from PyQt4.QtCore import QSize, Qt
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

html = \
"""


		

<html>
<head>
<meta http-equiv="refresh" content="1">
<title>System CPU usage</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="css/bootstrap.min.css">
<style>
div#saur{
	float: left;
}
</style>
</head>
<body style="background-color:black;">
<center><img src='images/logo-white.png' height="100" width="100">
<br>
<font size=5 face="calibri" color="white">Server-Suite</font>
</center>
<center>
<div class="progress" style="width:850px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:4.65%">
    		4.65% core 0
  		</div>
	</div>
<div id="header" style="width:800px;">
    <div id="saur">
   	<font>core 0</font>
    <div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:3.5%">
    		3.5% core 0
  		</div>
	</div>
	<font>core 1</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:4.5%">
    		4.5% core 1
  		</div>
	</div>
</div>

	<font>core 2</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:3.1%">
    		3.1% core 2
  		</div>
	</div>
	<font>core 3</font>
	<div class="progress" style="width:350px;">
  		<div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar"
  			aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width:7.5%">
    		7.5% core 3
  		</div>
	</div>


</div>

</body>
</html>
"""
class WebWidget(QWidget):

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(Qt.white)
        painter.setPen(Qt.black)
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))
        painter.setBrush(Qt.red)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.width()/4, self.height()/4,
                         self.width()/2, self.height()/2)
        painter.end()

    def sizeHint(self):
        return QSize(100, 100)
class WebPluginFactory(QWebPluginFactory):

    def __init__(self, parent = None):
        QWebPluginFactory.__init__(self, parent)
    
    def create(self, mimeType, url, names, values):
        if mimeType == "x-pyqt/widget":
            return WebWidget()
    
    def plugins(self):
        plugin = QWebPluginFactory.Plugin()
        plugin.name = "PyQt Widget"
        plugin.description = "An example Web plugin written with PyQt."
        mimeType = QWebPluginFactory.MimeType()
        mimeType.name = "x-pyqt/widget"
        mimeType.description = "PyQt widget"
        mimeType.fileExtensions = []
        plugin.mimeTypes = [mimeType]
        print "plugins"
        return [plugin]
if __name__ == "__main__":

    app = QApplication(sys.argv)
    QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
    view = QWebView()
    factory = WebPluginFactory()
    view.page().setPluginFactory(factory)
    view.setHtml(html)
    view.show()
    sys.exit(app.exec_())
