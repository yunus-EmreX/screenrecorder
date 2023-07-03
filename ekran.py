import pyautogui
import cv2
import numpy as np

# Ekran çözünürlüğünü alın
screen_size = (1920, 1080) # Örneğin: 1920x1080

# Video codec ve çıkış dosyası adını belirleyin
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_file = "ekran_kaydi.avi"

# Kaydediciyi başlatın
video_writer = cv2.VideoWriter(output_file, fourcc, 30.0, screen_size)

while True:
    # Ekran görüntüsünü yakalayın ve videoya yazın
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video_writer.write(frame_rgb)

    # 'q' tuşuna basılırsa kaydetmeyi durdurun
    if cv2.waitKey(1) == ord('q'):
        break

# Kaydediciyi kapatın ve pencereleri serbest bırakın
video_writer.release()
cv2.destroyAllWindows()