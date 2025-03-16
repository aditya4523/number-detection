Hand Sign Number Detection using MediaPipe & OpenCV

Overview

This project implements real-time hand sign number detection using MediaPipe Hands and OpenCV. It tracks hand landmarks and determines the number (1 to 5) based on finger extension patterns.

🚀 Features

🖐 Real-time hand tracking using MediaPipe Hands

🔢 Number detection based on extended fingers

🎥 Live webcam feed for gesture recognition

⚡ Optimized for fast processing (runs on CPU/GPU)

🛠 Technologies Used

Python

OpenCV (for image processing)

MediaPipe Hands (for hand tracking)

NumPy (for efficient calculations)

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/aditya4523/hand-sign-number-detection.git

cdhand-sign-number-detection

2️⃣ Install Dependencies

pip install opencv-python mediapipe numpy




3️⃣ Run the Script

python number_detection.py

🎯 How It Works

The webcam captures real-time hand gestures.
MediaPipe Hands detects 21 hand landmarks.
The script analyzes finger positions to determine which are extended.
Based on finger extension patterns, it assigns a number (1-5).
The detected number is displayed on the screen in real-time.

🖐 Usage

Show different hand gestures to detect numbers.
Press 'q' to exit the program.



🔮 Future Improvements

🔹 Extend detection to more hand gestures & numbers
🔹 Implement gesture-based controls for applications
🔹 Enhance accuracy & robustness

📢 Contributions & Issues

Feel free to fork, improve, and contribute to this project! If you encounter any issues, create a GitHub issue. 🚀# number-detection
