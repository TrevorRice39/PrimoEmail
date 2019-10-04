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
import User as User
import Email as Email
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

        # css for entire application
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
        
        self.user = None

        # initialize all tabs
        self.tabs = QTabWidget()
        self.login_tab = QWidget()
        self.inbox_tab = QWidget()
        self.new_email_tab = QWidget()
        self.spam_tab = QWidget()
        self.chat_tab = QWidget()
        self.tabs.resize(300,200)

        # css for entire TableWidget
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

        # adding the login tab at first
        self.tabs.addTab(self.login_tab, "Welcome!")
        

        #### login tab
        self.login_tab.layout = QVBoxLayout()
        self.login_tab.setLayout(self.login_tab.layout)

        # groupbox for login screen
        self.login_tab.group_box_login = QGroupBox("Login")
        self.login_tab.layout.addWidget(self.login_tab.group_box_login)

        # line edit to enter email address
        self.email_address = QLineEdit(self.login_tab.group_box_login)
        self.email_address.move(140, 50)
        self.email_address.setFixedSize(300, 40)

        # email address label
        self.email_address_label = QLabel(self.login_tab.group_box_login)
        self.email_address_label.setText('Email Address')
        self.email_address_label.move(20, 50)
        self.email_address_label.setFixedSize(120, 40)

        # line edit to enter password
        self.password = QLineEdit(self.login_tab.group_box_login)
        self.password.move(140, 110)
        self.password.setFixedSize(300, 40)
        self.password.setEchoMode(QLineEdit.Password) # hides password

        # password label
        self.password_label = QLabel(self.login_tab.group_box_login)
        self.password_label.setText('Password')
        self.password_label.move(20, 110)
        self.password_label.setFixedSize(120, 40)

        # login button
        self.login_button = QPushButton(self.login_tab.group_box_login)
        self.login_button.setText("Login")
        self.login_button.setFixedSize(100, 50)
        self.login_button.move(200, 200)
        self.login_button.clicked.connect(self.login) # call self.login() when clicked

        ##### inbox tab
        self.inbox_tab.layout = QHBoxLayout()
        self.inbox_tab.setLayout(self.inbox_tab.layout)

        # group box for list of emails
        self.inbox_tab.group_box_emails = QGroupBox("Emails")

        # group box for details
        self.inbox_tab.group_box_email_details = QGroupBox("Details")
        self.inbox_tab.group_box_emails.setFixedWidth(400)

        # adding group boxes to inbox_tab
        self.inbox_tab.layout.addWidget(self.inbox_tab.group_box_emails)
        self.inbox_tab.layout.addWidget(self.inbox_tab.group_box_email_details)

        # layout for email list
        self.emails_layout = QVBoxLayout()

        # list item
        self.email_list = QListWidget()
        self.email_list.insertItem(0, "Sender: Trevor Rice\nSubject: CSC 440\nDate: 05/07/2019")
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
        self.emails_layout.addWidget(self.email_list)
        
        # layout to display email
        self.details_layout = QVBoxLayout()

        # label for sender
        self.sender_label = QLabel(self.inbox_tab.group_box_email_details)
        self.sender_label.setText("Senders: ")
        self.sender_label.setFixedSize(60, 30)
        self.sender_label.move(6, 30)
        self.details_layout.addWidget(self.sender_label)
        
        # read only line edit for sender's address
        self.sender = QLineEdit(self.inbox_tab.group_box_email_details)
        self.sender.move(70, 30)
        self.sender.setFixedSize(700, 30)
        self.sender.setText("Trevor Rice")
        self.sender.setReadOnly(True)

        # label for subject
        self.subject_label = QLabel(self.inbox_tab.group_box_email_details)
        self.subject_label.setText("Subject: ")
        self.subject_label.setFixedSize(60, 30)
        self.subject_label.move(10, 70)
        
        # read only line edit for subject
        self.subject = QLineEdit(self.inbox_tab.group_box_email_details)
        self.subject.move(70, 70)
        self.subject.setFixedSize(700, 30)
        self.subject.setText("CSC 440")
        self.subject.setReadOnly(True)

        # label for date
        self.date_label = QLabel(self.inbox_tab.group_box_email_details)
        self.date_label.setText("Date: ")
        self.date_label.setFixedSize(60, 30)
        self.date_label.move(27, 110)

        # read only line edit for date
        self.date = QLineEdit(self.inbox_tab.group_box_email_details)
        self.date.move(70, 110)
        self.date.setFixedSize(700, 30)
        self.date.setText("05/07/2019")
        self.date.setReadOnly(True)

        # label for body
        self.body_label = QLabel(self.inbox_tab.group_box_email_details)
        self.body_label.setText("Body")
        self.body_label.setFixedSize(60, 30)
        self.body_label.move(10, 145)

        # read only text edit for body
        self.body = QTextEdit(self.inbox_tab.group_box_email_details)
        self.body.move(30, 180)
        self.body.setFixedSize(700, 400)
        self.body.setText("Hello Dr. Chang,\n    Here is my Project Report.\nTrevor Rice")
        self.body.setReadOnly(True)

        # mark as spam button
        self.mark_spam = QPushButton(self.inbox_tab.group_box_email_details)
        self.mark_spam.setText("Mark as spam")
        self.mark_spam.move(30, 585)

        # self.inbox_tab.group_box_email_details.setLayout(details_layout)
        # verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # emails_layout.addItem(verticalSpacer1)
        self.inbox_tab.group_box_emails.setLayout(self.emails_layout)


        ### chat tab
        self.chat_tab.layout = QHBoxLayout()
        self.chat_tab.setLayout(self.chat_tab.layout)

        self.chat_tab.group_box_friends = QGroupBox("Friends List")
        self.chat_tab.group_box_chatrooms = QGroupBox("Chatrooms")
        self.chat_tab.group_box_chat = QGroupBox("Chat")
        
        self.chat_tab.group_box_chatrooms.setFixedWidth(200)
        self.chat_tab.group_box_friends.setFixedWidth(200)
        self.chat_tab.layout.addWidget(self.chat_tab.group_box_friends)
        self.chat_tab.layout.addWidget(self.chat_tab.group_box_chatrooms)
        self.chat_tab.layout.addWidget(self.chat_tab.group_box_chat)

        friends_layout = QVBoxLayout()
        friend_list = QListWidget()
        friend_list.insertItem(0, "Trevor Rice")
        friend_list.insertItem(1, "Allen Roberts")
        friend_list.insertItem(2, "Kuang-nan Chang")
        self.chat_tab.setStyleSheet(
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

            QTextEdit::text {
                text-align: right;
            }

        '''
        )
        friends_layout.addWidget(friend_list)
        self.chat_tab.group_box_friends.setLayout(friends_layout)

        self.chatroom_layout = QVBoxLayout()
        self.chatroom_list = QListWidget()
        self.chatroom_list.insertItem(0, "CSC 440\n10 Users")
        self.chatroom_list.insertItem(1, "CSC 546\n3 Users")
        self.chatroom_list.insertItem(2, "CSC 309\n 7 Users")
        
        self.chatroom_layout.addWidget(self.chatroom_list)
        self.chat_tab.group_box_chatrooms.setLayout(self.chatroom_layout)


        self.chat_text = QLabel(self.chat_tab.group_box_chat)
        self.chat_text.move(26, 30)
        self.chat_text.setText("Trevor Rice")

        self.you_text = QLabel(self.chat_tab.group_box_chat)
        self.you_text.move(380, 30)
        self.you_text.setText("You")

        self.chat_view_left = QTextEdit(self.chat_tab.group_box_chat)
        self.chat_view_left.move(26, 50)
        self.chat_view_left.setFixedSize(350, 400)
        self.chat_view_left.setText("Messages")
        self.chat_view_left.setReadOnly(True)

        self.chat_view_right = QTextEdit(self.chat_tab.group_box_chat)
        self.chat_view_right.move(380, 50)
        self.chat_view_right.setFixedSize(350, 400)
        self.chat_view_right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.chat_view_right.setAlignment(Qt.AlignRight)
        self.chat_view_right.setText("Messages")
        self.chat_view_right.setReadOnly(True)

        self.send_message_text = QTextEdit(self.chat_tab.group_box_chat)
        self.send_message_text.move(26, 480)
        self.send_message_text.setFixedSize(700, 100)
        self.send_message_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.send_message_text.setAlignment(Qt.AlignRight)
        self.send_message_text.setText("")
        self.send_message_text.setReadOnly(False)

        self.send_message_button = QPushButton(self.chat_tab.group_box_chat)
        self.send_message_button.setText("Send Message")
        self.send_message_button.move(620, 585)

        ### new email tab
        self.new_email_tab.layout = QVBoxLayout()
        self.new_email_tab.setLayout(self.new_email_tab.layout)

        self.new_email_tab.group_box = QGroupBox("Compose Email")
        self.new_email_tab.layout.addWidget(self.new_email_tab.group_box)
        
        self.sender_text_new = QLabel(self.new_email_tab.group_box)
        self.sender_text_new.setText("Send to: ")
        self.sender_text_new.setFixedSize(60, 30)
        self.sender_text_new.move(6, 30)
        

        self.send_to = QLineEdit(self.new_email_tab.group_box)
        self.send_to.move(70, 30)
        self.send_to.setFixedSize(1060, 30)

        self.send_to_text = QLabel(self.new_email_tab.group_box)
        self.send_to_text.setText("Subject: ")
        self.send_to_text.setFixedSize(60, 30)
        self.send_to_text.move(10, 70)
        

        self.subject_new = QLineEdit(self.new_email_tab.group_box)
        self.subject_new.move(70, 70)
        self.subject_new.setFixedSize(1060, 30)

        self.date_text_new = QLabel(self.new_email_tab.group_box)
        self.date_text_new.setText("Date: ")
        self.date_text_new.setFixedSize(60, 30)
        self.date_text_new.move(27, 110)

        self.date_new = QLineEdit(self.new_email_tab.group_box)
        self.date_new.move(70, 110)
        self.date_new.setFixedSize(1060, 30)

        self.body_text_new = QLabel(self.new_email_tab.group_box)
        self.body_text_new.setText("Body")
        self.body_text_new.setFixedSize(60, 30)
        self.body_text_new.move(10, 145)

        self.body_new = QTextEdit(self.new_email_tab.group_box)
        self.body_new.move(30, 180)
        self.body_new.setFixedSize(1100, 400)

        self.send = QPushButton(self.new_email_tab.group_box)
        self.send.setText("Send Email")
        self.send.move(30, 585)
        self.send.clicked.connect(self.send_email)

        self.dialog = QErrorMessage()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def login(self, _):
        self.user = User.User(self.email_address.text(), self.password.text())
        valid = self.user.start_server()

        if (valid):
            self.dialog.showMessage('Login Sucessful!')
            self.login_tab.close()
            self.login_tab.deleteLater()
            self.tabs.addTab(self.inbox_tab,"Inbox")
            self.tabs.addTab(self.new_email_tab,"New Email")
            self.tabs.addTab(self.chat_tab,"Chat")
            self.tabs.addTab(self.spam_tab, "Spam")

        else:
            self.dialog.showMessage('Login Unsucessful. Please re-enter credentials.')

        
    def send_email(self, _):
        email = Email.Email(self.user.email_address, self.send_to.text(), self.subject_new.text(), self.body_new.toPlainText(), self.user.server)
        email.send()
        self.send_to.setText("")
        self.subject_new.setText("")
        self.body_new.setText("")
        self.dialog.showMessage("Email sent!")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
