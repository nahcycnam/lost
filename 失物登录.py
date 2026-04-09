import pyautogui, pyperclip
import pygetwindow as gw
import webbrowser
import time, sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QRadioButton, QButtonGroup, QLabel, QMessageBox)
from PyQt6.QtCore import Qt, pyqtSignal, QEventLoop
from PyQt6.QtGui import QFont


class RadioButtonWindow(QWidget):
    selection_made = pyqtSignal(str)
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.selected_value = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('失物类型')
        self.setFixedSize(280, 200)
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.WindowTitleHint |
            Qt.WindowType.WindowCloseButtonHint
        )

        font = QFont("Microsoft YaHei", 10)
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 15, 20, 15)
        layout.setSpacing(8)

        title_label = QLabel("请选择失物类型:")
        title_label.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)
        layout.addSpacing(10)

        self.options = [
            "身份证",
            "普通羊城通",
            "学生羊城通",
            "老年人优待卡",
            "其他"
        ]

        self.button_group = QButtonGroup()
        self.button_group.buttonClicked.connect(self.on_radio_button_clicked)

        for i, option in enumerate(self.options):
            radio_btn = QRadioButton(option)
            radio_btn.setFont(font)
            self.button_group.addButton(radio_btn, i)
            layout.addWidget(radio_btn)

        layout.addStretch()
        self.setLayout(layout)

    def on_radio_button_clicked(self, button):
        self.selected_value = button.text()
        self.selection_made.emit(self.selected_value)
        self.close()

    def closeEvent(self, event):
        if not self.selected_value:
            self.window_closed.emit()
        super().closeEvent(event)


def show_selection_window():
    """显示选择窗口并返回选中的值，如果关闭窗口返回None"""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    window = RadioButtonWindow()
    selected_value = []

    loop = QEventLoop()

    def on_selected(value):
        selected_value.append(value)
        loop.quit()

    def on_window_closed():
        selected_value.append(None)
        loop.quit()

    window.selection_made.connect(on_selected)
    window.window_closed.connect(on_window_closed)
    window.show()

    # 运行事件循环
    loop.exec()

    # 返回结果
    return selected_value[0] if selected_value else None


def LostAndFound():
    webbrowser.register('qaxbrowser', None, webbrowser.BackgroundBrowser(
        r"C:\Program Files\Google\Chrome\Application\1.exe"))
    webbrowser.get('qaxbrowser').open('http://192.168.80.61:8015')

    window_title = "移动互联网时代的企业协作平台 - Google Chrome"

    i = 0
    while True:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            break
        i += 0.1
        time.sleep(0.1)
        if i >= 20:
            sys.exit()

    win = windows[0]
    win.maximize()
    time.sleep(0.2)
    pyautogui.click(x=250, y=100)
    pyautogui.click(x=250, y=130)
    pyautogui.moveTo(x=900, y=610)

    window_title = "失物招领 - Google Chrome"

    i = 0
    while True:
        windows = gw.getWindowsWithTitle(window_title)
        if windows:
            break
        i += 0.1
        time.sleep(0.1)
        if i >= 20:
            sys.exit()

    time.sleep(1.6)
    pyautogui.click(x=1878, y=153)
    time.sleep(0.3)
    pyautogui.click(x=250, y=100)
    pyautogui.click(x=250, y=170)


    # 显示选择窗口并获取选中的值
    selected_card = show_selection_window()

    if selected_card is None:
        print("用户关闭了窗口，取消操作")
        return

    if selected_card == "":
        print("用户选择了空值")
        return

    print(f"选中的失物类型: {selected_card}")

    # 根据选中的值执行不同的操作
    if selected_card == "身份证":
        print("处理身份证相关操作")
        # 这里添加身份证的处理代码
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(0.4)
        pyperclip.copy("""javascript:(function(){const e=document.querySelector('iframe[src*="PickUpDetail"]');const t=()=>{const o=e.contentDocument||e.contentWindow.document;(c=o.getElementById("Content_pickupcategory_5"))&&(c.checked=!0,c.dispatchEvent(new Event("change",{bubbles:!0}))),(a=o.getElementById("Content_pickupitem"))&&(a.value="身份证一张，姓名：XXX，身份号码：XXX",a.dispatchEvent(new Event("input",{bubbles:!0})))};e.onload=t,e.contentDocument?.readyState==="complete"&&t()})()""")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        time.sleep(0.3)
        pyautogui.click(x=1900, y=134)  # 点击 控制台 X
    elif selected_card == "普通羊城通":
        print("处理普通羊城通相关操作")
        # 这里添加身份证的处理代码
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(0.4)
        pyperclip.copy(
            """javascript:(function(){const e=document.querySelector('iframe[src*="PickUpDetail"]');const t=()=>{const o=e.contentDocument||e.contentWindow.document;(c=o.getElementById("Content_pickupcategory_4"))&&(c.checked=!0,c.dispatchEvent(new Event("change",{bubbles:!0}))),(a=o.getElementById("Content_pickupitem"))&&(a.value="普通羊城通一张，ID：XXX，余额：XXX",a.dispatchEvent(new Event("input",{bubbles:!0})))};e.onload=t,e.contentDocument?.readyState==="complete"&&t()})()""")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        time.sleep(0.3)
        pyautogui.click(x=1900, y=134)  # 点击 控制台 X
    elif selected_card == "学生羊城通":
        print("处理学生羊城通相关操作")
        # 这里添加学生羊城通的处理代码
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(0.4)
        pyperclip.copy(
            """javascript:(function(){const e=document.querySelector('iframe[src*="PickUpDetail"]');const t=()=>{const o=e.contentDocument||e.contentWindow.document;(c=o.getElementById("Content_pickupcategory_4"))&&(c.checked=!0,c.dispatchEvent(new Event("change",{bubbles:!0}))),(a=o.getElementById("Content_pickupitem"))&&(a.value="学生羊城通一张，姓名：XXX，ID：XXX，余额：XXX",a.dispatchEvent(new Event("input",{bubbles:!0})))};e.onload=t,e.contentDocument?.readyState==="complete"&&t()})()""")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        time.sleep(0.3)
        pyautogui.click(x=1900, y=134)  # 点击 控制台 X
    elif selected_card == "老年人优待卡":
        print("处理老年人优待卡相关操作")
        # 这里添加老年人优待卡的处理代码
        pyautogui.hotkey('ctrl', 'shift', 'j')
        time.sleep(0.4)
        pyperclip.copy(
            """javascript:(function(){const e=document.querySelector('iframe[src*="PickUpDetail"]');const t=()=>{const o=e.contentDocument||e.contentWindow.document;(c=o.getElementById("Content_pickupcategory_4"))&&(c.checked=!0,c.dispatchEvent(new Event("change",{bubbles:!0}))),(a=o.getElementById("Content_pickupitem"))&&(a.value="老人优待卡一张，姓名：XXX，ID：XXX，余额：XXX",a.dispatchEvent(new Event("input",{bubbles:!0})))};e.onload=t,e.contentDocument?.readyState==="complete"&&t()})()""")
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.hotkey('enter')
        time.sleep(0.3)
        pyautogui.click(x=1900, y=134)  # 点击 控制台 X
    elif selected_card == "其他":
        print("处理其他失物相关操作")
        # 这里添加其他失物的处理代码

    pyautogui.moveTo(x=900, y=610)

if __name__ == '__main__':
    # 创建应用实例
    app = QApplication(sys.argv)

    # 执行主函数
    LostAndFound()

    # 手动退出应用
    app.quit()
    sys.exit()