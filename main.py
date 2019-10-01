import os
directoryPath = os.path.dirname(os.path.realpath(__file__))
directoryPath = directoryPath[ :directoryPath.rfind('/')]
import sys
import subprocess
sys.path.insert(1, directoryPath + '/Code')
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import PyQt5.QtCore as QtCore


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Primo Email'
        self.left = 0
        self.top = 0
        self.width = 1200
        self.height = 700
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("""
            QMainWindow {
                background: #4C151E;
            }
        """)
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class TableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.loaded_test_data = None
        self.sample_test_data = None
        ############################################
        #                                          #
        #            Initialize Tabs               #
        #                                          #
        ############################################
        self.tabs = QTabWidget()
        self.inbox_tab = QWidget()
        self.new_email_tab = QWidget()
        self.spam_tab = QWidget()
        self.chat_tab = QWidget()
        self.tabs.resize(300,200)
        #e8ad9f
        self.setStyleSheet("""
            QWidget {
                background:#e18478;
            }
            QLineEdit {
                background: white;
            }
            QLineEdit:disabled {
                background: #CDCDCD;
            }
            QLabel {
                color: black;
            }
            QPushButton {
                background-color: #992c3e;
                color: black;
            }
            QPushButton:disabled {
                background-color: white;
            }
            QPushButton:hover {
                color:#4C151E;
            }
            QTextEdit {
                background: #e8ad9f;
                color: black;
            }
        """)
        ########################################################################

        ############################################
        #                                          #
        #                Add Tabs                  #
        #                                          #
        ############################################
        self.tabs.addTab(self.inbox_tab,"Inbox")
        self.tabs.addTab(self.new_email_tab,"New Email")
        self.tabs.addTab(self.chat_tab,"Chat")
        self.tabs.addTab(self.spam_tab, "Spam")
        ########################################################################


        ##### inbox tab
        self.inbox_tab.layout = QHBoxLayout()
        self.inbox_tab.setLayout(self.inbox_tab.layout)

        self.inbox_tab.group_box_emails = QGroupBox("Emails")
        self.inbox_tab.group_box_email_details = QGroupBox("Details")
        self.inbox_tab.group_box_emails.setFixedWidth(400)
        self.inbox_tab.layout.addWidget(self.inbox_tab.group_box_emails)
        self.inbox_tab.layout.addWidget(self.inbox_tab.group_box_email_details)

        emails_layout = QVBoxLayout()
        email_list = QListWidget()
        email_list.insertItem(0, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(1, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(2, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(3, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(4, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(5, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(6, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(7, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(8, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(9, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(10, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(11, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(12, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(13, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(14, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(15, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(16, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        email_list.insertItem(17, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
        self.inbox_tab.setStyleSheet(
        '''
            QListWidget::item {
                border: 1px solid black;
                background: gray;
                margin-bottom: 5px;
            }

            QLabel {
            
            }

            QLineEdit {
                
            }

        '''
        )
        emails_layout.addWidget(email_list)
        
        details_layout = QVBoxLayout()
        sender_text = QLabel(self.inbox_tab.group_box_email_details)
        sender_text.setText("Senders: ")
        sender_text.setFixedSize(60, 30)
        sender_text.move(6, 30)
        details_layout.addWidget(sender_text)
        

        sender = QLineEdit(self.inbox_tab.group_box_email_details)
        sender.move(70, 30)
        sender.setFixedSize(700, 30)
        sender.setText("Trevor Rice")
        sender.setReadOnly(True)


        subject_text = QLabel(self.inbox_tab.group_box_email_details)
        subject_text.setText("Subject: ")
        subject_text.setFixedSize(60, 30)
        subject_text.move(10, 70)
        details_layout.addWidget(sender_text)
        

        subject = QLineEdit(self.inbox_tab.group_box_email_details)
        subject.move(70, 70)
        subject.setFixedSize(700, 30)
        subject.setText("CSC 440")
        subject.setReadOnly(True)

        date_text = QLabel(self.inbox_tab.group_box_email_details)
        date_text.setText("Date: ")
        date_text.setFixedSize(60, 30)
        date_text.move(27, 110)
        details_layout.addWidget(sender_text)
        

        date = QLineEdit(self.inbox_tab.group_box_email_details)
        date.move(70, 110)
        date.setFixedSize(700, 30)
        date.setText("05/07/2019")
        date.setReadOnly(True)



        body_text = QLabel(self.inbox_tab.group_box_email_details)
        body_text.setText("Body")
        body_text.setFixedSize(60, 30)
        body_text.move(10, 145)
        details_layout.addWidget(sender_text)
        

        body = QTextEdit(self.inbox_tab.group_box_email_details)
        body.move(30, 180)
        body.setFixedSize(700, 400)
        body.setText("Hello Dr. Chang,\n    Here is my Project Report.\nTrevor Rice")
        body.setReadOnly(True)

        mark_spam = QPushButton(self.inbox_tab.group_box_email_details)
        mark_spam.setText("Mark as spam")
        mark_spam.move(30, 585)

        details_layout.addWidget(sender)

        # self.inbox_tab.group_box_email_details.setLayout(details_layout)
        # verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # emails_layout.addItem(verticalSpacer1)
        self.inbox_tab.group_box_emails.setLayout(emails_layout)


        ### new email tab
        self.new_email_tab.layout = QVBoxLayout()
        self.new_email_tab.setLayout(self.new_email_tab.layout)

        self.new_email_tab.group_box = QGroupBox("Compose Email")
        self.new_email_tab.layout.addWidget(self.new_email_tab.group_box)
        
        sender_text_new = QLabel(self.new_email_tab.group_box)
        sender_text_new.setText("Senders: ")
        sender_text_new.setFixedSize(60, 30)
        sender_text_new.move(6, 30)
        details_layout.addWidget(sender_text)
        

        sender_new = QLineEdit(self.new_email_tab.group_box)
        sender_new.move(70, 30)
        sender_new.setFixedSize(1060, 30)

        subject_text_new = QLabel(self.new_email_tab.group_box)
        subject_text_new.setText("Subject: ")
        subject_text_new.setFixedSize(60, 30)
        subject_text_new.move(10, 70)
        details_layout.addWidget(sender_text)
        

        subject_new = QLineEdit(self.new_email_tab.group_box)
        subject_new.move(70, 70)
        subject_new.setFixedSize(1060, 30)

        date_text_new = QLabel(self.new_email_tab.group_box)
        date_text_new.setText("Date: ")
        date_text_new.setFixedSize(60, 30)
        date_text_new.move(27, 110)
        details_layout.addWidget(sender_text)
        

        date_new = QLineEdit(self.new_email_tab.group_box)
        date_new.move(70, 110)
        date_new.setFixedSize(1060, 30)

        body_text_new = QLabel(self.new_email_tab.group_box)
        body_text_new.setText("Body")
        body_text_new.setFixedSize(60, 30)
        body_text_new.move(10, 145)
        details_layout.addWidget(sender_text)
        

        body_new = QTextEdit(self.new_email_tab.group_box)
        body_new.move(30, 180)
        body_new.setFixedSize(1100, 400)

        send = QPushButton(self.new_email_tab.group_box)
        send.setText("Send Email")
        send.move(30, 585)



        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
