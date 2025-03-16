import cv2
import numpy as np
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open the webcam
cap = cv2.VideoCapture(0)

# Function to detect if a finger is extended
def is_finger_extended(tip, dip):
    """
    Determines if a finger is extended by comparing the y-coordinates of the tip and the dip.
    """
    return tip.y < dip.y  # Extended if the tip is above the dip (normalized coordinates)

# Function to interpret hand signs
def detect_number(hand_landmarks):
    """
    Maps hand landmarks to numbers based on finger extension.
    """
    # Retrieve landmark positions
    thumb_tip = hand_landmarks.landmark[4]
    thumb_ip = hand_landmarks.landmark[2]
    index_tip = hand_landmarks.landmark[8]
    index_dip = hand_landmarks.landmark[7]
    middle_tip = hand_landmarks.landmark[12]
    middle_dip = hand_landmarks.landmark[11]
    ring_tip = hand_landmarks.landmark[16]
    ring_dip = hand_landmarks.landmark[15]
    pinky_tip = hand_landmarks.landmark[20]
    pinky_dip = hand_landmarks.landmark[19]

 # Determine if fingers are extended
    thumb_extended = thumb_tip.x > thumb_ip.x  # Thumb extends outward
    index_extended = is_finger_extended(index_tip, index_dip)
    middle_extended = is_finger_extended(middle_tip, middle_dip)
    ring_extended = is_finger_extended(ring_tip, ring_dip)
    pinky_extended = is_finger_extended(pinky_tip, pinky_dip)

    # Combine the states of fingers
    extended_fingers = [thumb_extended, index_extended, middle_extended, ring_extended, pinky_extended]

    # Map finger states to numbers
    if extended_fingers == [False, True, False, False, False]:
        return 1
    elif extended_fingers == [False, True, True, False, False]:
        return 2
    elif extended_fingers == [False, True, True, True, False]:
        return 3
    elif extended_fingers == [False, True, True, True, True]:
        return 4
    elif extended_fingers == [True, True, True, True, True]:
        return 5
    else:
        return None  # Not a recognizable number

# Main loop for webcam processing
while True:
    # Capture the current frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break
  # Flip the frame horizontally for a mirror-like effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB (required by MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(rgb_frame)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Detect the number
            number = detect_number(hand_landmarks)

            # Draw landmarks on the frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Display the detected number
            if number is not None:
                cv2.putText(frame, f"Number: {number}", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Show the frame
    cv2.imshow("Hand Sign Number Recognition", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
