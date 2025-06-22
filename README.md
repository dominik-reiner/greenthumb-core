# Green Thumb
Green Thumb. Smart gardening for hobbyists.  
Green Thumb consists of a local component running on site in the garden. (E.g. on a Raspberry Pi) which manages and executes modular tasks and syncs to a cloud component.

This is the core package implementing the local component. 

**Architecture**

1. **Components**  
Components are all external elements connected to the core package.
* **Sensor Components**: e.g., temperature sensor, humidity sensor, light sensor
* **Actuator Components**: e.g., water pump, LED, servo motor
They define multiple actions that can be run on them.
2. **Tasks**  
Tasks are made up of actions performed on components.
Each task has a trigger that is the result of an Component Action.
3. **Data Storage**: Responsible for storing data collected from tasks and logging
4. **Task Manager**: Responsible for managing and executing tasks based on their definitions, interacting with components
5. **Queue Client**: This component will connect to a server-based queue (e.g. RabbitMQ) to receive updates to task definitions and send data back to the server.
6. **Components Manager**: This service will manage all components.