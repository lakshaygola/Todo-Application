# Main application file for the todo list application

from PyQt5.QtWidgets import *
from Todo_Application import Ui_MainWindow
from DialogWindow import Ui_Dialog
import sqlite3

# Opening the database and connect it to the store the list from the application list
tododb = sqlite3.connect('todoDB.db')
c = tododb.cursor()

# Crete the table todotask to save the task in the database
c.execute(""" CREATE TABLE if not exists todoTask(
            taskList text)
            """)

# Commiting changes to the database
tododb.commit()

tododb.close()

# Dialog class (control the dialog box)
class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


# Main window which we will see in the application
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.remainingTasksList = []
        self.finishTasksList = []

        # Click here button - used to open the dialog
        self.clickHereButton.clicked.connect(self.openDialog)

        # Finished button - Move the certain task from the remaining list to finished list
        self.finishButton.clicked.connect(self.finishwork)

        # Delete button - delete the particular row from the remaining list
        self.deleteButton.clicked.connect(self.deleteParticular)

        # Clear All button - clear all the output from the final list
        self.cleraAllButton.clicked.connect(self.clearFinalList)

        # notDone - button used the move back the task from the finish list to the remaining list
        self.notDoneButton.clicked.connect(self.notDoneTask)

        # EditButton - to edit the particular task
        self.editButton.clicked.connect(self.editTask)

        # saveButton - save all the current tasks in the database
        self.saveButton.clicked.connect(self.saveTaskToDB)

        # perviousTaskLoad - function to load all the task from the database
        self.perviousTaskLoad()

    # Function to grab all the perivous data and display it on the screen
    def perviousTaskLoad(self):
        tododb = sqlite3.connect('todoDB.db')

        c = tododb.cursor()

        c.execute(" SELECT * from todoTask ")

        records = c.fetchall()

        tododb.commit()
        tododb.close()

        for record in records:
            self.RemainingList.addItem(str(record[0]))

    # Function to save the todo list in the database
    def saveTaskToDB(self):
        todoTask = []
        finishTask = []

        tododb = sqlite3.connect('todoDB.db')

        c = tododb.cursor()

        # Deleting the task items from the database so that we can save the new one
        c.execute("DELETE FROM todoTask;",)

        for idx in range(self.RemainingList.count()):
            todoTask.append(self.RemainingList.item(idx).text())

        for idx in range(self.finishedList.count()):
            finishTask.append(self.finishedList.item(idx).text())

        for item in todoTask:
            c.execute('INSERT INTO todoTask VALUES (:item)',
                      {
                          'item' : item,
                      })

        tododb.commit()
        tododb.close()

        # Creating the message box - pop up after the task are saved to the database
        msgbox = QMessageBox()
        msgbox.setWindowTitle('TODO Task Application')
        msgbox.setText('Your tasks are saved sucessfully.')
        msgbox.setIcon(QMessageBox.Information)
        msgbox.exec_()

    # Function to edit the particular task in the todo list
    def editTask(self):
        old = self.RemainingList.currentItem().text()
        self.RemainingList.takeItem(self.RemainingList.currentRow())
        if (old):
            self.openDialog(old)

    # Function to clear all the row from the final list
    def clearFinalList(self):
        self.finishedList.clear()
        self.finishTasksList.clear()

    # Function to delete the particular element from the list
    def deleteParticular(self):
        self.RemainingList.takeItem(self.RemainingList.currentRow())

    # Function to move the work from the remaining list to the finish list
    def finishwork(self):
        task = self.RemainingList.takeItem(self.RemainingList.currentRow())
        if (task):
            self.finishedList.addItem(task)

    # Function to move the task from the finish list to the remaining list
    def notDoneTask(self):
        task = self.finishedList.takeItem(self.finishedList.currentRow())
        if (task):
            self.addTask(task)

    # Function to add the task written in the line edit
    def addTask(self, task):
        if bool(task):
            self.RemainingList.addItem(task)
            self.remainingTasksList.append(task)

    # Function to open the dialog from click here button
    def openDialog(self, task):
        dialog = Dialog()

        if (task):
            dialog.ui.newTaskLine.setText(task)
            dialog.ui.addButton.pressed.connect(dialog.close)

        # To Add the task in the remaining list
        dialog.ui.addButton.pressed.connect(lambda : self.addTask(dialog.ui.newTaskLine.text()))
        dialog.ui.addButton.pressed.connect(lambda: self.addTask(dialog.ui.newTaskLine.setText('')))

        # Cancel button - close the dialog window
        dialog.ui.cancelButton.pressed.connect(dialog.close)
        dialog.exec()


if __name__ == '__main__':
    application = QApplication([])
    window = MainWindow()
    window.show()
    application.exec()
