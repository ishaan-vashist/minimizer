import cv2
import tensorflow as tf
import numpy as np
import pyautogui
import time

# Load the trained model
model = tf.keras.models.load_model('hand_gesture_model.h5') 

# Function to predict gesture
def predict_gesture(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (128, 128))
    image = np.expand_dims(image, axis=0) / 255.0
    predictions = model.predict(image)
    return np.argmax(predictions)

def minimize_all_windows():
    # Ensure the OpenCV window is focused
    cv2.namedWindow("Hand Tracking", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Hand Tracking", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.waitKey(1)
    # Wait a moment to ensure OpenCV window gets focused
    time.sleep(0.1)
    # Send keyboard shortcut to minimize all windows
    pyautogui.hotkey('win', 'm')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gesture = predict_gesture(frame)
    if gesture == 0:  # Class 0 corresponds to "fist"
        print("Fist detected!")
        minimize_all_windows()
    elif gesture == 1:  # Class 1 corresponds to "no_fist"
        print("No fist detected.")

    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
