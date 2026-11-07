# SWIFT – Smart Water Integrated Flow and Turbidity Technology

**An IoT-Based Automatic Water Management System for Real-Time Monitoring, Quality Analysis, and Water Flow Anomaly Detection.**

SWIFT is an Internet of Things (IoT)-based water management system developed for the DTEDI environment at Vocational College, Universitas Gadjah Mada. The project integrates sensors, a microcontroller, network communication, and a web-based dashboard to monitor water conditions and support automatic water quality control.

## Project Overview

Conventional water management often relies on manual monitoring, making it difficult to detect excessive water usage, leakage, and changes in water quality in real time.

SWIFT addresses these challenges by integrating water flow, turbidity, and ultrasonic sensors with an ESP32 microcontroller. The collected data is processed and transmitted to a server through Wi-Fi using MQTT, then displayed on a web dashboard for monitoring and control.

## System Architecture

The system consists of three main layers:

1. **Device Layer**
   - ESP32 microcontroller
   - Water Flow Sensor
   - Turbidity Sensor
   - Ultrasonic Sensor
   - Relay Module, Water Pump, Solenoid Valve, LCD, and Buzzer

2. **Network Layer**
   - Wi-Fi communication
   - MQTT protocol for data transmission

3. **Data Center Layer**
   - Ubuntu Server
   - Kubernetes
   - Mosquitto MQTT Broker
   - SWIFT Web Dashboard

## Key Features

- **Real-Time Monitoring:** Displays water flow rate, turbidity, and water level.
- **Water Quality Classification:** Classifies water conditions into safe, warning, and danger categories based on sensor readings.
- **Automatic Quality Control:** Activates flushing and valve control based on detected water conditions.
- **Anomaly Detection:** Identifies abnormal water flow and potential leakage or blockage conditions.
- **Alert Notification:** Uses a buzzer and dashboard notifications to inform users of abnormal conditions.
- **Historical Data:** Stores monitoring records for further analysis and evaluation.
- **Manual and Automatic Control:** Provides dashboard-based control of pumps and valves.

## Technologies Used

| Category | Technologies |
|---|---|
| Microcontroller | ESP32 |
| Programming | C/C++, HTML, CSS, JavaScript |
| Sensors | Water Flow, Turbidity, Ultrasonic |
| Communication | Wi-Fi, MQTT |
| MQTT Broker | Mosquitto |
| Server | Ubuntu Server, Kubernetes |
| Dashboard | Web-based SWIFT Dashboard |
| Development Tools | Arduino IDE, VirtualBox |

## Testing Results

The final system testing recorded the following monitoring statistics:

| Parameter | Result |
|---|---:|
| Total Data Records | 9,601 |
| Active IoT Devices | 1 |
| Average Flow Rate | 1.485 L/min |
| Average Turbidity | 2.52 NTU |

The testing results indicate that the data pipeline, from sensor readings on the ESP32 to real-time dashboard visualization, operated continuously during the final test.

## My Contribution

- Assisted in the implementation of the IoT system.
- Worked on the integration of the ESP32 with water monitoring sensors.
- Designed the network topology to support communication between IoT devices and the server.
- Contributed to the development of the integrated monitoring system.

## Project Information

- **Project Name:** SWIFT – Smart Water Integrated Flow and Turbidity Technology
- **Project Location:** DTEDI, Vocational College, Universitas Gadjah Mada
- **Project Type:** Academic Collaborative Project
- **Field:** Internet of Things, Networking, and Server Technology

## Documentation

Project documentation, system architecture, prototype implementation, and testing results are included in the uploaded project files.
