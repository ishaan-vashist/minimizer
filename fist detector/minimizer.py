import cv2
import mediapipe as mp
import pyautogui

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def detect_fist(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process hand landmarks
    results = hands.process(image)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = hand_landmarks.landmark
            
            # Get y-coordinates of thumb, index, middle, ring, and pinky fingertips
            thumb_y = landmarks[4].y
            index_y = landmarks[8].y
            middle_y = landmarks[12].y
            ring_y = landmarks[16].y
            pinky_y = landmarks[20].y
            
            # Check if fingertips are in a fist-like configuration
            if (thumb_y > index_y > middle_y > ring_y > pinky_y):
                return True
            
    return False

def minimize_all_windows():
    pyautogui.hotkey('win', 'm')  # Shortcut to minimize all windows on Windows

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect fist gesture
    if detect_fist(frame):
        print("Fist detected!")
        minimize_all_windows()

    # Display hand tracking visualization
    cv2.imshow('Hand Tracking', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
