import sys
import cv2
from ultralytics import YOLO,solutions
from sort import *
import time
import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLineEdit,QLabel,QComboBox,QToolTip,QRadioButton,QPushButton
from PyQt5.QtGui import QIcon,QImage,QPixmap,QFont,QIntValidator,QKeyEvent
from PyQt5.QtCore import QTimer,Qt
app=QApplication(sys.argv)
model = YOLO("yolov8l.pt")
total_count=[]
total_count2=[]
total_count3=[]
total_count4=[]
total_count5=[]
total_count6=[]
total_count7=[]
total_count8=[]
total_count9=[]
total_count10=[]
total_count11=[]
total_count12=[]
total_count13=[]
total_count14=[]
total_count15=[]
total_count16=[]
class Window(QWidget): #Window adında bir class oluşturulur.Nesne üretildiğinde(window1) QWidget'in pencere özelliklerine sahip olur,pencere özelliklerini başlatır ve ayarlamalar yapılır
    def __init__(self):
        super().__init__()
        self.setGeometry(0,40,1400,920)
        self.setWindowTitle("Bilgisayarlı Görü ile Mağazalara Giren Çıkış Yapan İnsanların Sayılandırılması")
        self.setWindowIcon(QIcon("speed/sda.jpg"))
        self.setStyleSheet("background:gray")
        self.kamera_etiketi = QLabel(self)
        self.kamera_etiketi2 = QLabel(self)
        self.kamera_etiketi3=QLabel(self)
        self.kamera_etiketi3.setGeometry(200,30,360,40)
        self.kamera_etiketi3.setStyleSheet("border: 4px solid black;border-radius:14px")
        self.kamera_etiketi2.setGeometry(260,30,340,40)
        self.kamera_etiketi3.setText("Kavşak Görüntü Akatarımı")
        self.kamera_etiketi2.setGeometry(900, 30, 340, 40)
        self.kamera_etiketi2.setText("Sayılandırma Sistemi")
        self.kamera_etiketi2.setFont(QFont("Times New Roman", 18))
        self.kamera_etiketi3.setFont(QFont("Times New Roman", 18))
        self.kamera_etiketi2.setStyleSheet("border: 4px solid black;border-radius:14px")
        self.kamera_etiketi.setStyleSheet("border: 13px solid black;border-radius:36px")
        self.kamera_etiketi.setStyleSheet("border: 4px solid black;border-radius:14px")
        self.kamera_etiketi.setStyleSheet("border: 13px solid black;border-radius:36px")
        self.kamera_etiketi.move(40, 80)
        self.kamera_etiketi.resize(800, 800)
        self.cap = cv2.VideoCapture("intersection.mp4")
        self.label = QLabel(self)
        self.label.setFont(QFont("Times New Roman", 16))
        self.label.setGeometry(900, 80, 500, 30)
        self.label.setText("Batıdan Güneye Geçen Araç Sayısı:")
        self.label4 = QLabel(self)
        self.label4.setFont(QFont("Times New Roman", 16))
        self.label4.setGeometry(900, 130, 500, 30)
        self.label4.setText("Batıdan Doğuya Geçen Araç Sayısı:")
        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Times New Roman", 16))
        self.label2.setGeometry(900, 180, 500, 30)
        self.label2.setText("Batıdan Kuzeye Geçen Araç Sayısı:")
        self.label5 = QLabel(self)
        self.label5.setFont(QFont("Times New Roman", 16))
        self.label5.setGeometry(900, 230, 500, 30)
        self.label5.setText("Doğudan Güneye Geçen Araç Sayısı:")
        self.label6 = QLabel(self)
        self.label6.setFont(QFont("Times New Roman", 16))
        self.label6.setGeometry(900, 280, 500, 30)
        self.label6.setText("Doğudan Batıya Geçen Araç Sayısı:")
        self.label7 = QLabel(self)
        self.label7.setFont(QFont("Times New Roman", 16))
        self.label7.setGeometry(900, 330, 500, 30)
        self.label7.setText("Doğudan Kuzeye Geçen Araç Sayısı:")
        self.label8 = QLabel(self)
        self.label8.setFont(QFont("Times New Roman", 16))
        self.label8.setGeometry(900, 380, 500, 30)
        self.label8.setText("Kuzeyden Güneye Geçen Araç Sayısı:")
        self.label9 = QLabel(self)
        self.label9.setFont(QFont("Times New Roman", 16))
        self.label9.setGeometry(900, 430, 500, 30)
        self.label9.setText("Kuzeyden Batıya Geçen Araç Sayısı:")
        self.label10 = QLabel(self)
        self.label10.setFont(QFont("Times New Roman", 16))
        self.label10.setGeometry(900, 480, 500, 30)
        self.label10.setText("Kuzeyden Doğuya Geçen Araç Sayısı:")
        self.label11 = QLabel(self)
        self.label11.setFont(QFont("Times New Roman", 16))
        self.label11.setGeometry(900, 530, 500, 30)
        self.label11.setText("Güneyden Kuzeye Geçen Araç Sayısı:")
        self.label12 = QLabel(self)
        self.label12.setFont(QFont("Times New Roman", 16))
        self.label12.setGeometry(900, 580, 500, 30)
        self.label12.setText("Güneyden Batıya Geçen Araç Sayısı:")
        self.label13 = QLabel(self)
        self.label13.setFont(QFont("Times New Roman", 16))
        self.label13.setGeometry(900, 630, 500, 30)
        self.label13.setText("Güneyden Doğuya Geçen Araç Sayısı:")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.secim_degisti)
        self.timer.start(30)
    def secim_degisti(self):
        ret, self.im0 = self.cap.read()
        zaman=time.time()
        self.im0 = cv2.resize(self.im0, (600, 600))
        cv2.line(self.im0, (114, 359), (148, 489), (0, 255, 0), 2)
        cv2.line(self.im0, (144, 334), (344, 309), (0, 255, 0), 2)
        cv2.line(self.im0, (412, 325), (509, 416), (0, 255, 0), 2)
        cv2.line(self.im0, (506, 448), (215, 520), (0, 255, 0), 2)
        zaman1 = time.time()
        tracks = model.track(self.im0, persist=True, show=False,verbose=False, classes=[2, 3, 5, 7], tracker="bytetrack.yaml")
        a = 0
        for track in tracks:
            for box in track.boxes:
                a += 1
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                id = box.id.tolist()
                id = id[0]
                id = int(id)
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(self.im0, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(self.im0, ((x1 + x2) // 2, (y1 + y2) // 2), 5, (0, 255, 0), -1)
                cv2.putText(self.im0, f"ID:{id}", (x1, y1 - 10), 1, 1, (0, 0, 255), 2)
                if 0 < (x1 + x2) / 2 < 150 and 340< (y1 + y2) / 2 < 490:
                    if total_count.count(id) == 0:
                        total_count.append(id)
                if id in total_count and 200 < (x1 + x2) / 2 < 510 and 440 < (y1 + y2) / 2 < 530:
                    if total_count2.count(id) == 0:
                        total_count2.append(id)
                if id in total_count and 400 < (x1 + x2) / 2 < 510 and 320 < (y1 + y2) / 2 < 420:
                    if total_count3.count(id) == 0:
                        total_count3.append(id)
                if id in total_count and 130 < (x1 + x2) / 2 < 360 and 300 < (y1 + y2) / 2 < 340:
                    if total_count4.count(id) == 0:
                        total_count4.append(id)
                #####################
                if 400 < (x1 + x2) / 2 < 510 and 320< (y1 + y2) / 2 < 420:
                    if total_count5.count(id) == 0:
                        total_count5.append(id)
                if id in total_count5 and 200 < (x1 + x2) / 2 < 510 and 440 < (y1 + y2) / 2 < 530:
                    if total_count6.count(id) == 0:
                        total_count6.append(id)
                if id in total_count5 and 100 < (x1 + x2) / 2 < 150 and 340 < (y1 + y2) / 2 < 490:
                    if total_count7.count(id) == 0:
                        total_count7.append(id)
                if id in total_count5 and 130 < (x1 + x2) / 2 < 360 and 300 < (y1 + y2) / 2 < 340:
                    if total_count8.count(id) == 0:
                        total_count8.append(id)
                #####################
                if 140 < (x1 + x2) / 2 < 350 and 305< (y1 + y2) / 2 < 335:
                    if total_count9.count(id) == 0:
                        total_count9.append(id)
                if id in total_count9 and 200 < (x1 + x2) / 2 < 510 and 440 < (y1 + y2) / 2 < 530:
                    if total_count10.count(id) == 0:
                        total_count10.append(id)
                if id in total_count9 and 100 < (x1 + x2) / 2 < 150 and 340 < (y1 + y2) / 2 < 490:
                    if total_count11.count(id) == 0:
                        total_count11.append(id)
                if id in total_count9 and 400 < (x1 + x2) / 2 < 510 and 320 < (y1 + y2) / 2 < 420:
                    if total_count12.count(id) == 0:
                        total_count12.append(id)
                #####################
                if 200 < (x1 + x2) / 2 < 510 and 440< (y1 + y2) / 2 < 530:
                    if total_count13.count(id) == 0:
                        total_count13.append(id)
                if id in total_count13 and 130 < (x1 + x2) / 2 < 360 and 300 < (y1 + y2) / 2 < 340:
                    if total_count14.count(id) == 0:
                        total_count14.append(id)
                if id in total_count13 and 100 < (x1 + x2) / 2 < 150 and 340 < (y1 + y2) / 2 < 490:
                    if total_count15.count(id) == 0:
                        total_count15.append(id)
                if id in total_count13 and 400 < (x1 + x2) / 2 < 510 and 320 < (y1 + y2) / 2 < 420:
                    if total_count16.count(id) == 0:
                        total_count16.append(id)
        self.label.setText(f"Batıdan Güneye Geçen Araç Sayısı:{len(total_count2)}")
        self.label2.setText(f"Batıdan Kuzeye Geçen Araç Sayısı:{len(total_count4)}")
        self.label4.setText(f"Batıdan Doğuya Geçen Araç Sayısı:{len(total_count3)}")
        self.label5.setText(f"Doğudan Güneye Geçen Araç Sayısı:{len(total_count6)}")
        self.label6.setText(f"Doğudan Batıya Geçen Araç Sayısı:{len(total_count7)}")
        self.label7.setText(f"Doğudan Kuzeye Geçen Araç Sayısı:{len(total_count8)}")
        self.label8.setText(f"Kuzeyden Güneye Geçen Araç Sayısı:{len(total_count10)}")
        self.label9.setText(f"Kuzeyden Batıya Geçen Araç Sayısı:{len(total_count11)}")
        self.label10.setText(f"Kuzeyden Doğuya Geçen Araç Sayısı:{len(total_count12)}")
        self.label11.setText(f"Güneyden Kuzeye Geçen Araç Sayısı:{len(total_count14)}")
        self.label12.setText(f"Güneyden Batıya Geçen Araç Sayısı:{len(total_count15)}")
        self.label13.setText(f"Güneyden Doğuya Geçen Araç Sayısı:{len(total_count16)}")
        image = QImage(self.im0.data, self.im0.shape[1], self.im0.shape[0],
                       QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        self.kamera_etiketi.setPixmap(pixmap.scaled(self.kamera_etiketi.size(), Qt.IgnoreAspectRatio))
        zaman2=time.time()
        fps=1/(zaman2-zaman1)
        print(fps)
window1 = Window()
window1.show()
sys.exit(app.exec_())
