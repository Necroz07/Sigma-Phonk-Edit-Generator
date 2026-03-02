# Sigma Phonk Edit Generator

Sigma Phonk Edit Generator is a real-time webcam-based visual and audio effect application that overlays dynamic sigma-style edits on your face using facial landmark detection and synchronized phonk audio.

The project combines computer vision, real-time video processing, and audio triggering to create an interactive “sigma edit” experience directly from your camera feed.

---
## How It Works

### Face Detection & Landmark Tracking

- Uses MediaPipe Face Landmarker to detect facial landmarks in real time
- Extracts key facial coordinates for eyes, lips and facial structure
- Calculates trigger condition (smile more than threshold)
- Applies transformations based on facial geometry

### Visual Overlay System

- Converts webcam frames to grayscale
- Dynamically places emoji overlays at specific coordinates
- Maintains proper alignment and scaling relative to face position
- Supports layered rendering without breaking frame structure

## Audio Trigger System

- Plays phonk audio clips based on detected facial triggers (smile)
- Syncs visual overlays with sound effects
- Prevents overlapping audio glitches

## User Interaction

- Launch the app → Webcam feed opens automatically
- Smile detected → Effects activate
- Specific expressions trigger sigma overlay + phonk sound
- Press ``Q`` to exit

## Features

- Real-time webcam processing
- MediaPipe face landmark detection
- Expression-based triggering logic
- Emoji overlay rendering
- Grayscale + stylized visual filters
- Phonk sound integration
- Modular structure (core functions separated from main app)
  
---

## Tech Stack

- Python
- OpenCV
- MediaPipe (Face Landmarker Task API)
- NumPy
- OS / Pathlib for file handling

---

## Purpose

The purpose of this project was to learn a new library and see how I can implement real-time video libraries creatively and have them react to human input.

- Real-time computer vision pipelines
- Expression-based interactive systems
- Audio-visual synchronization
- Building chaotic but technically structured meme tools

---

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/Necroz07/sigma-phonk-edit-generator
   ```

2. Navigate to the project directory
   ```
   cd sigma-phonk-edit-generator
   ```

3. Install Dependencies
   ```
   python -m pip install -r requirements.txt
   ```

5. Run the application
   ```
   python "main.py"
   ```
   
Make sure:

- Your webcam index is correct in the script
- face_landmarker.task is in the project directory
- Emoji and phonk asset folders are present
---

## Project Structure

```
sigma-phonk-edit-generator/
├── core_funcs.py
├── main.py
├── face_landmarker.task
├── emojis/
│   └── (overlay images)
├── phonk/
│   └── (audio clips)
├── requirements.txt
└── README.md
```

---

## What I Learned

- Using MediaPipe Task API for structured landmark detection
- Working with normalized landmark coordinates
- Converting between BGR ↔ RGB in OpenCV pipelines
- Real-time audio triggering without blocking the main loop
- Managing modular project structure
- Handling webcam failures and edge cases
