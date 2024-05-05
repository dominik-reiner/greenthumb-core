# Green Thumb
Green Thumb. Smart gardening for hobbyists.  
Green Thumb consists of a local component running on site in the garden. (E.g. on a Raspberry Pi) which manages and executes modular tasks and syncs to a cloud component.

This is the core package implementing the local component. 

**Architecture**

1. **Components**  
Components are all external elements connected to the core package.
* **Sensor Components**: e.g., temperature sensor, humidity sensor, light sensor
* **Actuator Components**: e.g., water pump, LED, servo motor
	+ YAML file: `water_pump.yaml`
		- name: Water Pump
		- resulting_data: pump_status (bool)
		- python_modules: `water_pump_controller.py`, `water_pump_monitor.py`
2. **Tasks**  
Tasks are  actions performed on components.
* Defined in YAML files, referencing one or more components
* Example: `task_watering.yaml`
	+ name: Watering Task
	+ components: `water_pump`, `soil_moisture_sensor`
	+ python_module: `watering_task_executor.py`
3. **Data Storage**: Responsible for storing data collected from tasks and logging
4. **Task Manager**: Responsible for managing and executing tasks based on their definitions, interacting with components
5. **Queue Client**: This component will connect to a server-based queue (e.g. RabbitMQ) to receive updates to task definitions and send data back to the server.
