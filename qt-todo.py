from PyQt6.QtWidgets import (QPushButton, QApplication, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QHBoxLayout, QMainWindow, QInputDialog, QMessageBox)
from PyQt6.QtCore import Qt
import sys

class ToDoList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.setFixedSize(700, 700)

        self.setStyleSheet("""
        QMainWindow {
            background-color: #333;
        }
        
        QListWidget {
            background-color: #444;
            color: white;
            font-size: 24px;
        }
        
        QInputDialog {
            background-color: #333;
            color: white;
        }

        QLabel {
            color: white;
        }

        QPushButton {
            background-color: #555;
            color: white;
            border: 1px solid #666;
            padding: 5px
        }

        QPushButton:hover {
            border: 3px solid #666;
        }
        """)

        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self.createDisplay()
        self.createButtons()


    def createDisplay(self):
        self.display = QListWidget()
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setFixedHeight(600)

    def createButtons(self):
        mainLayout = QVBoxLayout()
        buttonsLayout = QHBoxLayout()

        createToDoBtn = QPushButton('+')
        removeToDoBtn = QPushButton('-')
        
        buttonsLayout.addWidget(createToDoBtn)
        buttonsLayout.addWidget(removeToDoBtn)
        buttonsLayout.setSpacing(20)
        mainLayout.addLayout(buttonsLayout)
        mainLayout.addStretch()
        buttonsLayout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.generalLayout.addLayout(mainLayout)
        
        additLayout = QVBoxLayout()
        additButtonsLayout = QHBoxLayout()
        
        self.changeThemeBtn = QPushButton('☀')
        self.changeThemeBtn.setFixedWidth(25)
        removeToDoBtn.setFixedWidth(25)

        additButtonsLayout.addWidget(self.changeThemeBtn)
        additLayout.addLayout(additButtonsLayout)
        additLayout.addStretch()
        additButtonsLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.generalLayout.addLayout(additLayout)

        self.generalLayout.addWidget(self.display)
        createToDoBtn.clicked.connect(self.addToDo)
        removeToDoBtn.clicked.connect(self.removeToDo)
        self.changeThemeBtn.clicked.connect(self.changeTheme)

    def addToDo(self):
        text, ok = QInputDialog.getText(self, 'Adding new To-Do in List', 'Enter the new To-Do: ')
        if ok and text:
            item = QListWidgetItem("• " + text + "\n")
            self.display.addItem(item)

    def removeToDo(self):
        selected = self.display.currentRow()
        if selected != -1:
            self.display.takeItem(selected)
            QMessageBox.information(
                    self,
                    "Done!",
                    "To Do has been removed",
            )
        else:
            QMessageBox.critical(
                    self,
                    "Error",
                    "Please choise a To Do to remove",
                    QMessageBox.StandardButton.Ok
            )

    def changeTheme(self):
        if self.changeThemeBtn.text() == "☀":
            self.setStyleSheet("""
                QMainWindow {
                    background-color: white;
                }

                QListWidget {
                    background-color: white;
                    color: black;
                    font-size: 24px;
                }
                
                QInputDialog {
                    background-color: white;
                    color: black;
                }

                QLabel {
                    color: black;
                }

                QPushButton {
                    background-color: #f0f0f0;
                    border: 1px solid #ccc;
                    padding: 5px;
                }

                QPushButton:hover {
                    border: 3px solid #ccc;
                }
                """)
            self.changeThemeBtn.setText("☾")
        else:
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #333;
                }

                QListWidget {
                    background-color: #444;
                    color: white;
                    font-size: 24px;
                }

                QInputDialog {
                    background-color: #333;
                    color: white;
                }

                QLabel {
                    color: white;
                }

                QPushButton {
                    background-color: #555;
                    color: white;
                    border: 1px solid #666;
                    padding: 5px;
                }

                QPushButton:hover {
                    border: 3px solid #666;
                }
                """)
            self.changeThemeBtn.setText("☀")


def main():
    app = QApplication(sys.argv)
    todo = ToDoList()
    todo.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
