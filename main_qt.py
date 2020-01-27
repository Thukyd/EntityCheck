import sys
from qtpy import QtWidgets

from ui_entity.mainwindow import Ui_MainWindow

# imports for entity check
import os,glob
import csv

app = QtWidgets.QApplication(sys.argv)

class mainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setWindowTitle("Currywurst") # set Window Witle
        
        self.ui_entity = Ui_MainWindow() # intiate Main Window
        self.ui_entity.setupUi(self) # setuo window

        #self.ui_entity.jp_task_button.clicked.connect(self.ui_entity.checkBox_3.toggle) # button click triggers checkbSSox (sender => ) signal


        ### BUTTON ACTIONS
        #self.ui_entity.myButton.clicked.connect(self.on_button_click)
        self.ui_entity.checkEntityButton.clicked.connect(self.on_button_click_entity_check)
            # "checkEntityButton" = Butten name in QT

        
        ### for entity_check
        self.folder = "csv_entities/"
        self.foundValues = set()

    def on_button_click(self):
        text = self.ui_entity.myInput.setText()
        print("on_button_click: Text =  \"" + text + "\"")

    def on_button_click_entity_check(self):
        self.ui_entity.label.setText("Der Button wurde geklickt")
        #print("Event:  \"" + str(text) + "\"")
            # "resultCheck" = Label name for text element in QT
        self.entity_check()
        self.ui_entity.label.setText("Entity Check erfolgreich ausgeführt")

    def entity_check(self):
        for filepath in glob.glob(os.path.join(self.folder, "*.csv")):
            # set filename
            filepathSplit = filepath.split("\\")
            filename = filepathSplit[1]
            newFilename = "output_files/new" + filename

            with open(filepath) as fileInput, open(self.folder + newFilename, "w", encoding="utf-8", newline="") as fileOutput: 
                reader = csv.reader(fileInput, delimiter=";")
                writer = csv.writer (fileOutput, delimiter=";")


                 ############TODO
                # 1. check for double
                # 2. save doubles in a list
                # 3. write a new function 
                    # for doubles the user has to be asked
                    # for empty elements and rows it should be deleted immediately

                for row in reader:
                    # delete empty list elements & filter out already seen elements
                    # new_row = [x for x in row if x and x not in found_values]
                    allData = []
                    for x in row:
                        if not x: # empty element
                            # do not add to list!!!
                            print("empyt element")
                           
                        elif x not in self.found_values: # unique element
                            print("new " + x)
                            allData.append(x)
                        else: # found element again
                            print("shit, I found " + str(x) + " again")
                            
                    if not row:
                        print("empty row")

                    print(allData)
                    writer.writerow(allData)




window = mainWindow()

window.show()

sys.exit(app.exec_())
