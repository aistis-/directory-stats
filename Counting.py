import sys
from os import listdir
from os.path import isfile, join
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import FileStats


def main():
    app = QApplication(sys.argv)
    w = App()
    w.setWindowTitle('Symbols counting')
    w.showMaximized()
    sys.exit(app.exec_())


class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)

        self.editor = QTextEdit()

        layout = QVBoxLayout(self)
        layout.addWidget(self.editor)

        directory = sys.argv[1]

        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        files_stats = [FileStats.FileStats(directory + '/' + f) for f in files]

        output_string = ''

        for file in files_stats:
            output_string += file.get_counted_content() + '\n\n'

        output_string = FileStats.FileStats.get_all_counted_content() + \
            '\n\n' + output_string

        with open(sys.argv[2], 'w+') as output:
            output.write(output_string)

        self.editor.setText(output_string)


if __name__ == "__main__":
    main()
