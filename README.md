# DCIT-403_PRROJECT_SHEM
# Smart Home Energy Manager (SHEM)

**DCIT 403 – Designing Intelligent Agents Semester Project**

## 1. Project Overview

The Smart Home Energy Manager (SHEM) is an intelligent agent system designed to optimize energy usage in a household environment. The system monitors environmental conditions such as room occupancy, electricity prices, and temperature, and autonomously decides how to control appliances in order to reduce energy costs while maintaining user comfort.

The project follows the **Prometheus methodology** for agent-oriented software development. It demonstrates the design, reasoning, and implementation of an intelligent agent capable of perceiving environmental events, making decisions based on stored knowledge, and performing appropriate actions.

The system simulates a smart home environment where the agent reacts to sensor inputs and executes energy-saving strategies such as turning off lights in empty rooms or adjusting HVAC settings during periods of high electricity prices.



## 2. Project Objectives

The main objectives of the project are:

* Design an intelligent agent capable of managing household energy consumption.
* Demonstrate the use of agent-oriented analysis and design concepts.
* Implement the **perceive–decide–act agent loop**.
* Apply the **Prometheus methodology** for system design.
* Simulate decision-making behavior in a smart home environment.



## 3. System Functionality

The Smart Home Energy Manager performs the following functions:

* Monitors room occupancy using simulated sensor data.
* Tracks real-time electricity price levels.
* Maintains beliefs about environmental conditions.
* Executes energy-saving strategies when certain conditions are met.
* Sends action commands to simulated actuators.

Example automated behaviors include:

* Turning off lights when rooms are empty.
* Dimming lights when electricity prices are high.
* Adjusting HVAC settings to reduce energy consumption.



## 4. System Architecture

The prototype is implemented as a **single-agent system** responsible for managing energy usage within one household.

### Main Components

* **Sensors** – Provide environmental data such as occupancy, temperature, and electricity price.
* **Energy Manager Agent** – Processes sensor inputs and decides appropriate actions.
* **Actuators** – Execute commands such as switching lights off or adjusting temperature.

The system operates using a continuous loop where the agent perceives environmental data, decides the best course of action, and performs the required operation.



## 5. Agent Design

The agent is structured using three key internal components:

### Beliefs

Information stored by the agent about the environment:

* Current electricity price
* Room occupancy status
* User comfort preferences

### Capabilities

Groups of related behaviors:

* Lighting Efficiency Management
* Climate Control Management

### Plans

Predefined strategies executed when certain conditions occur.

Example:

* **ConservePlan:** If electricity price exceeds a threshold, the system reduces energy consumption by dimming lights or adjusting HVAC temperature.



## 6. Implementation

The prototype implementation is written in **Python**.
The program simulates sensor input and demonstrates how the agent reacts to environmental changes.

The agent follows the classic intelligent agent loop:

1. **Perceive** – Receive environmental input from sensors.
2. **Decide** – Evaluate current beliefs and select a plan.
3. **Act** – Execute an action through actuators.



## 7. Installation Requirements

To run the simulation, ensure the following are installed:

* Python **3.8 or later**

No additional libraries are required.



## 8. How to Run the Project

1. Download or clone the project folder.
2. Navigate to the project directory in the terminal.
3. Run the simulation using:

```
python smart_energy_agent.py
```

The program will simulate sensor input and display the agent's decisions in the terminal.



## 9. Example Output

```
Sensor Input: Room1 Occupancy = False
Action: Turning off lights in Room1

Sensor Input: Electricity Price = High
Action: Dimming lights to 50% to conserve energy
```


## 10. Limitations

The current implementation is a simplified simulation and does not directly connect to real smart home devices. Additionally, decision-making relies on predefined rules rather than machine learning techniques.

Future improvements may include:

* Integration with IoT smart home devices
* Learning user behavior patterns
* Predictive energy optimization
* Multi-agent coordination



## 11. Author

Student Name: *Denis Bagresolzu Bayor*

Course: **DCIT 403 – Designing Intelligent Agents**

Institution: **University of Ghana**



## 12. License

This project is developed for academic purposes as part of the DCIT 403 coursework.
