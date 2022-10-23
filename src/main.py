import cv2
import numpy as np
import mediapipe as mp
from ActuatorInterface import ActuatorInterface
from keras.models import load_model

# initialize mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Load the gesture recognizer model
model = load_model('src/models/mp_hand_gesture')

# Load class names
f = open('src/models/gesture.names', 'r')
classNames = f.read().split('\n')
f.close()

# Initialize the webcam for Hand Gesture Recognition Python project
cap = cv2.VideoCapture(0)
act = ActuatorInterface()

while True:
  # Read each frame from the webcam
  _, frame = cap.read()
  image_height, image_width, _ = frame.shape

  # Flip the frame vertically
  frame = cv2.flip(frame, 1)
  frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

  # Get hand landmark prediction
  result = hands.process(frame_rgb)

  # post process the result
  predicted_gesture_name = ''
  
  if result.multi_hand_landmarks:
    landmarks = []
    for hand_landmarks in result.multi_hand_landmarks:
      for landmark in hand_landmarks.landmark:
        x_pos = int(landmark.x * image_height)
        y_pos = int(landmark.y * image_width)
        landmarks.append([x_pos, y_pos])

      # Drawing landmarks on frames
      mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

      # Predict gesture
      prediction = model.predict([landmarks])
      predicted_gesture_id = np.argmax(prediction)
      predicted_gesture_name = classNames[predicted_gesture_id]

  # show the prediction on the frame
  cv2.putText(frame, predicted_gesture_name, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

  if predicted_gesture_name == 'rock':
    act.move_cursor(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width, 
      hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)

  elif predicted_gesture_name == 'pick':
    # pick: thumb and index meet, other fingers in, right hand pointing left
    # dragging destination determined by index tip location
    act.drag_cursor_to(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width, 
      hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)

  # Show the final output
  cv2.imshow("Output", frame) 

  if cv2.waitKey(1) == ord('q'):
    break

# release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
