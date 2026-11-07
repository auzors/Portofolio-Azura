# Smart Traffic Light System

An IoT-based smart traffic light prototype that uses computer vision and YOLOv13 to detect vehicle density and dynamically adjust green light duration at road intersections.

This project was developed as a Project-Based Learning assignment to explore how Artificial Intelligence and IoT can be integrated to create a more adaptive traffic management system.

## Project Overview

Conventional traffic lights generally use fixed-time settings, which cannot always adapt to changing traffic conditions. This project addresses that limitation by detecting the number of vehicles in each lane and adjusting the green light duration according to the detected traffic density.

## Tech Stack

- **Programming Language:** Python
- **Computer Vision:** OpenCV
- **Object Detection:** YOLOv13
- **Microcontroller:** ESP32
- **Hardware:** Camera and LED traffic light simulators
- **Communication:** Wi-Fi

## Key Features

- **Real-Time Vehicle Detection:** Uses a camera feed and YOLOv13 to detect and count vehicles.
- **Traffic Density Classification:** Categorizes traffic conditions based on the number of detected vehicles.
- **Adaptive Green Light Duration:** Adjusts green light duration according to traffic density.
- **IoT Integration:** Connects the Python-based detection system with an ESP32 to control LED traffic light indicators.

## System Workflow

1. A camera captures traffic conditions.
2. Python and OpenCV process the camera feed.
3. YOLOv13 detects and counts vehicles.
4. The system determines the traffic density and calculates the green light duration.
5. Commands are sent to the ESP32 through Wi-Fi.
6. The ESP32 controls the traffic light LEDs according to the received commands.

## Testing Results

The system was tested under several traffic conditions:

## Testing Results

<table>
  <thead>
    <tr>
      <th>Detected Vehicles</th>
      <th>Traffic Condition</th>
      <th>Green Light Duration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2</td>
      <td>Sparse</td>
      <td>20 seconds</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Moderate</td>
      <td>30 seconds</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Crowded</td>
      <td>40 seconds</td>
    </tr>
  </tbody>
</table>

These tests demonstrate that the prototype can adjust green light duration based on the number of detected vehicles.

## Project Type

Academic Project – Project-Based Learning  
Internet Technology Engineering, Universitas Gadjah Mada
