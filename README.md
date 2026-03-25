#  Multi-Sensor IoT Dashboard (Socket → MQTT → Grafana)

##  Project Overview

This project implements a **real-time multi-sensor monitoring system** that collects environmental data
(temperature, humidity, and light intensity), transmits it across devices, and visualizes it on a dashboard.

The system architecture includes:

* **Laptop 1 (Sensor Node)**
  Simulates sensor readings and sends data via TCP socket.

* **Laptop 2 (Edge Device)**
  Receives socket data and publishes it to an MQTT broker.

* **MQTT Broker**
  Manages message distribution between devices.

* **Dashboard (Grafana)**
  Displays sensor data in real-time using visual panels.

---

#  System Architecture

```
Laptop 1 (Sensor)
   │
   │ TCP Socket
   ▼
Laptop 2 (Edge Device)
   │
   │ MQTT Publish
   ▼
MQTT Broker
   │
   │ MQTT Subscribe
   ▼
Grafana Dashboard
```

---

#  Sensors Used

This system simulates three environmental sensors:

###  Temperature Sensor

* Measures ambient temperature
* Unit: °C
* Range: 20 – 35

###  Humidity Sensor

* Measures air moisture level
* Unit: %
* Range: 40 – 80

###  Light Sensor

* Measures light intensity
* Unit: lux
* Range: 100 – 1000

---

#  MQTT Topics Used

Each sensor is published to a **separate MQTT topic**:

```text
savonia/Yetunde/temperature
savonia/Yetunde/humidity
savonia/Yetunde/light
```

---

#  MQTT Broker

* Broker: **EMQX Broker**
* Address:

```text
broker.emqx.io
```

* Port: `1883`

#  Dashboard Explanation

The dashboard is designed to provide **clear and real-time monitoring**:

###  Temperature Graph

* Displays temperature changes over time
* Helps identify trends and fluctuations

###  Humidity Gauge

* Shows current humidity level
* Easy to read in percentage

###  Light Gauge

* Displays current light intensity
* Useful for environment brightness monitoring

###  Status Panels

* Show system condition (e.g., Normal / High / Low)
* Provide quick alerts without reading graphs


# Reflection Question

##  Why do we separate each sensor into a different MQTT topic?

Separating each sensor into its own MQTT topic improves **flexibility, scalability, and efficiency**.

###  Key Reasons:

### 1. Selective Subscription

Subscribers can choose only the data they need:

* Temperature-only apps subscribe to:

```text
Yetunde/IoT/Light
```

### 2. Better Organization

Each topic represents a specific data stream, making the system easier to manage and debug.

### 3. Scalability

New sensors can be added without affecting existing ones:

```text
Yetunde/IoT/Light
```

### 4. Efficient Processing

Applications process only relevant data instead of filtering large combined messages.


### Conclusion

Using separate topics allows:

* Modular system design
* Easier scaling
* Cleaner data handling


