# Hotkey Manager

## Description

The Hotkey Manager is a Python application built using PyQt5 that allows users to create, manage, and delete hotkeys for various actions. The hotkeys and their corresponding actions are stored in an SQLite database.

## Features

- Add new hotkeys with associated actions
- Delete existing hotkeys
- Persistent storage of hotkeys using SQLite
- User-friendly interface built with PyQt5
- Real-time hotkey execution using the `keyboard` module

## Requirements

- Python 3.x
- PyQt5
- `keyboard` module
- SQLite3

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/m-mjd/Hotkey_Manager.git
   cd Hotkey_Manager
   ```

2. **Install the required packages:**

   ```bash
   pip install PyQt5 keyboard
   ```

3. **Run the application:**

   ```bash
   python hotkey_manager.py
   ```

## Usage

1. Launch the application.
2. Use the `Key:` input to define the key combination for the hotkey.
3. Use the `Action:` input to define the action that should be executed when the hotkey is pressed.
4. Click the `Add Hotkey` button to save the hotkey.
5. Existing hotkeys will be listed in the interface with options to delete them.

## Code Overview

- `HotkeyManager` class: Main class for managing the UI and hotkey operations.
  - `__init__`: Initializes the UI and database connection.
  - `create_table`: Creates the SQLite table for storing hotkeys.
  - `init_ui`: Sets up the PyQt5 user interface.
  - `add_hotkey`: Adds a new hotkey to the dictionary, database, and UI.
  - `delete_hotkey`: Deletes a hotkey from the dictionary, database, and UI.
  - `reload_hotkeys`: Reloads hotkeys from the database to update the UI.
  - `execute_action`: Executes the action associated with a hotkey.
  - `save_hotkey_to_db`: Saves a hotkey to the SQLite database.
  - `load_hotkeys_from_db`: Loads hotkeys from the SQLite database.
  - `restart_application`: Restarts the application to apply changes.

## License

This project is licensed under the MIT License.

---

# مدیریت کلیدهای میانبر

## توضیحات

مدیریت کلیدهای میانبر یک برنامه پایتون ساخته شده با استفاده از PyQt5 است که به کاربران اجازه می‌دهد کلیدهای میانبر و عملیات‌های مرتبط با آنها را ایجاد، مدیریت و حذف کنند. کلیدهای میانبر و عملیات‌های مرتبط با آنها در یک پایگاه داده SQLite ذخیره می‌شوند.

## ویژگی‌ها

- اضافه کردن کلیدهای میانبر جدید با عملیات‌های مرتبط
- حذف کلیدهای میانبر موجود
- ذخیره پایدار کلیدهای میانبر با استفاده از SQLite
- رابط کاربری دوستانه ساخته شده با PyQt5
- اجرای بلادرنگ کلیدهای میانبر با استفاده از ماژول `keyboard`

## نیازمندی‌ها

- Python 3.x
- PyQt5
- ماژول `keyboard`
- SQLite3

## نصب

1. **کلون کردن مخزن:**

   ```bash
   git clone https://github.com/m-mjd/Hotkey_Manager.git
   cd Hotkey_Manager
   ```

2. **نصب پکیج‌های مورد نیاز:**

   ```bash
   pip install PyQt5 keyboard
   ```

3. **اجرای برنامه:**

   ```bash
   python hotkey_manager.py
   ```

## استفاده

1. برنامه را راه‌اندازی کنید.
2. از ورودی `Key:` برای تعریف ترکیب کلیدهای میانبر استفاده کنید.
3. از ورودی `Action:` برای تعریف عملیاتی که باید هنگام فشار دادن کلید میانبر اجرا شود استفاده کنید.
4. روی دکمه `Add Hotkey` کلیک کنید تا کلید میانبر ذخیره شود.
5. کلیدهای میانبر موجود در رابط کاربری با گزینه‌هایی برای حذف نمایش داده می‌شوند.

## مرور کد

- کلاس `HotkeyManager`: کلاس اصلی برای مدیریت رابط کاربری و عملیات کلیدهای میانبر.
  - `__init__`: رابط کاربری و اتصال به پایگاه داده را مقداردهی اولیه می‌کند.
  - `create_table`: جدول SQLite را برای ذخیره کلیدهای میانبر ایجاد می‌کند.
  - `init_ui`: رابط کاربری PyQt5 را تنظیم می‌کند.
  - `add_hotkey`: یک کلید میانبر جدید به دیکشنری، پایگاه داده و رابط کاربری اضافه می‌کند.
  - `delete_hotkey`: یک کلید میانبر را از دیکشنری، پایگاه داده و رابط کاربری حذف می‌کند.
  - `reload_hotkeys`: کلیدهای میانبر را از پایگاه داده مجدداً بارگذاری می‌کند تا رابط کاربری به‌روز شود.
  - `execute_action`: عملیاتی را که با یک کلید میانبر مرتبط است اجرا می‌کند.
  - `save_hotkey_to_db`: یک کلید میانبر را در پایگاه داده SQLite ذخیره می‌کند.
  - `load_hotkeys_from_db`: کلیدهای میانبر را از پایگاه داده SQLite بارگذاری می‌کند.
  - `restart_application`: برنامه را برای اعمال تغییرات مجدداً راه‌اندازی می‌کند.

## مجوز

این پروژه تحت مجوز MIT است.
