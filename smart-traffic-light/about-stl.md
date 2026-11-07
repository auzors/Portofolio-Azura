# Smart Traffic Light System

An adaptive traffic management system prototype that utilizes computer vision to automatically adjust green light durations based on real-time vehicle density[cite: 16]. This project replaces traditional fixed-time traffic signals with an intelligent, computer-vision-driven approach to minimize intersection congestion.

## Tech Stack
* **Language & Vision:** Python, OpenCV
* **AI Model:** YOLOv13 (Object Detection)
* **Microcontroller:** ESP32
* **Actuators:** LED Traffic Light Simulators

## Key Features
* **Real-Time Vehicle Detection:** Deploys a computer vision pipeline utilizing YOLOv13 and OpenCV via a camera feed to detect and track vehicles on the road in real-time.
* **Dynamic Density Classification:** Automatically categorizes traffic density levels into three distinct tiers (sparse, moderate, and crowded) based on the exact vehicle count detected per lane.
* **Adaptive Signal Timing:** Automatically adjusts the green light timing proportionally to traffic loads (e.g., default 20s for sparse, up to 40s for crowded conditions) to optimize traffic flow and eliminate unnecessary wait times.
* **IoT Hardware Integration:** Establishes communication between the computer vision processing unit (Python) and an ESP32 microcontroller to switch physical LED traffic signals dynamically based on calculated timing.
