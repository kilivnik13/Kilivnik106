import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QHBoxLayout
)
from PyQt5.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class LivePlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)
        self.setParent(parent)

        self.x_data = []
        self.y_data = []
        self.line, = self.ax.plot([], [], 'r-')

        self.ax.set_title("Живой график")
        self.ax.set_xlabel("Время")
        self.ax.set_ylabel("Значение")

    def add_point(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)
        self.line.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.draw()

    def reset(self):
        self.x_data = []
        self.y_data = []
        self.line.set_data([], [])
        self.ax.relim()
        self.ax.autoscale_view()
        self.draw()


class LiveGraphApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Живой график с обновлением")
        self.setGeometry(100, 100, 800, 600)

        self.counter = 0
        self.timer = QTimer()
        self.timer.setInterval(1000) 
        self.timer.timeout.connect(self.update_plot)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.canvas = LivePlotCanvas(self)
        layout.addWidget(self.canvas)

        button_layout = QHBoxLayout()
        self.start_btn = QPushButton("Старт")
        self.stop_btn = QPushButton("Стоп")

        self.start_btn.clicked.connect(self.start_plotting)
        self.stop_btn.clicked.connect(self.stop_plotting)

        button_layout.addWidget(self.start_btn)
        button_layout.addWidget(self.stop_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def start_plotting(self):
        self.counter = 0
        self.canvas.reset()
        self.timer.start()

    def stop_plotting(self):
        self.timer.stop()

    def update_plot(self):
        self.counter += 1
        y = random.uniform(0, 10)
        self.canvas.add_point(self.counter, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LiveGraphApp()
    window.show()
    sys.exit(app.exec_())
