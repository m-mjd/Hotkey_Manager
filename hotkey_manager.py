import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QKeySequenceEdit, QGridLayout
import keyboard
import os


class HotkeyManager(QWidget):
    def __init__(self):
        super().__init__()

        self.hotkey_dict = {}
        self.db_connection = sqlite3.connect('hotkeys.db')
        self.create_table()

        self.init_ui()

    def create_table(self):
        cursor = self.db_connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS hotkeys
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           key_combination TEXT,
                           action TEXT)''')
        self.db_connection.commit()

    def init_ui(self):
        layout = QVBoxLayout()

        self.key_label = QLabel('Key:')
        self.key_edit = QKeySequenceEdit(self)
        self.action_label = QLabel('Action:')
        self.action_edit = QLineEdit(self)
        self.add_button = QPushButton('Add Hotkey', self)
        self.add_button.clicked.connect(self.add_hotkey)

        self.hotkey_layout = QGridLayout()

        # Set some style options for better appearance
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
            }
    
            QLineEdit, QKeySequenceEdit {
                font-size: 14px;
                padding: 5px;
            }
    
            QPushButton {
                font-size: 14px;
                padding: 5px;
            }
        """)

        # Add some spacing between widgets
        layout.setSpacing(10)

        layout.addWidget(self.key_label)
        layout.addWidget(self.key_edit)
        layout.addWidget(self.action_label)
        layout.addWidget(self.action_edit)
        layout.addWidget(self.add_button)
        layout.addLayout(self.hotkey_layout)

        self.load_hotkeys_from_db()

        self.setLayout(layout)

    def add_hotkey(self):
        key_sequence = self.key_edit.keySequence()
        action = self.action_edit.text()

        if not key_sequence.isEmpty() and action:
            key_combination = key_sequence.toString()
            self.hotkey_dict[key_combination] = action

            hotkey_label = QLabel(f"{key_combination}: {action}")
            delete_button = QPushButton('Delete', self)
            delete_button.clicked.connect(
                lambda _, key=key_combination: self.delete_hotkey(key))
            row_position = self.hotkey_layout.rowCount()
            self.hotkey_layout.addWidget(hotkey_label, row_position, 0)
            self.hotkey_layout.addWidget(delete_button, row_position, 1)

            self.save_hotkey_to_db(key_combination, action)

            keyboard.add_hotkey(
                key_combination, self.execute_action, args=(action,))

            self.key_edit.clear()
            self.action_edit.clear()

    def delete_hotkey(self, key_combination):
        # Remove hotkey from dictionary
        if key_combination in self.hotkey_dict:
            del self.hotkey_dict[key_combination]

        # Remove hotkey from the database
        cursor = self.db_connection.cursor()
        cursor.execute(
            'DELETE FROM hotkeys WHERE key_combination = ?', (key_combination,))
        self.db_connection.commit()

        # Reload hotkeys to update the UI
        self.reload_hotkeys()

        # Restart the application
        self.restart_application()

    def reload_hotkeys(self):
        # Clear existing UI
        for i in reversed(range(self.hotkey_layout.count())):
            item = self.hotkey_layout.itemAt(i)
            if isinstance(item, QLabel) or isinstance(item, QPushButton):
                item.widget().setParent(None)

        # Load and display hotkeys from the database
        self.load_hotkeys_from_db()

    def execute_action(self, action):
        keyboard.write(action)

    def save_hotkey_to_db(self, key_combination, action):
        cursor = self.db_connection.cursor()
        cursor.execute(
            'INSERT INTO hotkeys (key_combination, action) VALUES (?, ?)', (key_combination, action))
        self.db_connection.commit()

    def load_hotkeys_from_db(self):
        cursor = self.db_connection.cursor()
        cursor.execute('SELECT * FROM hotkeys')
        hotkeys = cursor.fetchall()

        for hotkey in hotkeys:
            key_combination, action = hotkey[1], hotkey[2]

            self.hotkey_dict[key_combination] = action

            hotkey_label = QLabel(f"{key_combination}: {action}")
            delete_button = QPushButton('Delete', self)
            delete_button.clicked.connect(
                lambda _, key=key_combination: self.delete_hotkey(key))
            row_position = self.hotkey_layout.rowCount()
            self.hotkey_layout.addWidget(hotkey_label, row_position, 0)
            self.hotkey_layout.addWidget(delete_button, row_position, 1)

            keyboard.add_hotkey(
                key_combination, self.execute_action, args=(action,))

    def restart_application(self):
        QApplication.quit()
        python = sys.executable
        os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hotkey_manager = HotkeyManager()
    hotkey_manager.show()
    sys.exit(app.exec_())
