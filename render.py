import sys  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWebEngineWidgets import *  
from lxml import html

class Render(QWebEnginePage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebEnginePage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit() 

  def html(self):
  	raw = self.frame.toHtml()
    return html.fromstring(str(raw.toAscii()))