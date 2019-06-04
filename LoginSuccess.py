from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    windowList = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')
        self.showMaximized()

        # 创建菜单栏
        self.createMenus()

    def createMenus(self):
        # 创建动作 注销
        self.printAction1 = QAction(self.tr("注销"), self)
        self.printAction1.triggered.connect(self.on_printAction1_triggered)

        # 创建动作 退出
        self.printAction2 = QAction(self.tr("退出"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

        # 创建菜单，添加动作
        self.printMenu = self.menuBar().addMenu(self.tr("注销和退出"))
        self.printMenu.addAction(self.printAction1)
        self.printMenu.addAction(self.printAction2)

    # 动作一：注销
    def on_printAction1_triggered(self):
        self.close()
        # dialog = logindialog(mode=1)
        # if dialog.exec_() == QDialog.Accepted:
        #     the_window = MainWindow()
        #     self.windowList.append(the_window)  # 这句一定要写，不然无法重新登录
        #     the_window.show()

    # 动作二：退出
    def on_printAction2_triggered(self):
        self.close()

    # 关闭界面触发事件
    def closeEvent(self, event):
        print('Closed')
        pass
