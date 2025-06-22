# Green Thumb Core
Green Thumb. Smart gardening for hobbyists.  
Green Thumb consists of a local component running on site in the garden e.g. on a Raspberry Pi (greenthumb-core)
which manages and executes modular tasks and syncs to a cloud component (greenthumb-backend).

This is the core package implementing the local component. 

## Architecture**

1. **Components**  
Components are all (external) elements connected to the core package.
They define multiple actions that can be run on them.

    - **Sensor Components**: e.g., temperature sensor, humidity sensor, light sensor
        - Available as of now:
            - Time Component
    - **Actuator Components**: e.g., water pump, LED, servo motor
        - Available as of now:
            - Serial Port

1. **Tasks**  
Tasks are made up of actions performed on components.
Each task has a trigger that is the result of an Component Action.

    * Available as of now
        - Check Time every N seconds
        - Binary Serial Pin Control for X seconds every N seconds

1. **Task Manager**: Responsible for managing and executing tasks based on their definitions, interacting with components



## Installation

### Prerequisites

You need to have the following setup on your machine:
- pixi

### Requirements

To install the project requirements clone the project and run
```sh
pixi install
```

## Usage

1. Configure the tasks in task_args.json in ./data
2. Run `pixi run start`

## Testing

Run `pixi run tests`

## Project Roadmap

This project is still in it's early stages and will work on the following main areas:

1. **Data Storage**: Responsible for storing data collected from tasks and logging

1. **Queue Client**: This component will connect to a server-based queue (e.g. RabbitMQ) to receive updates to task definitions and send data back to the server.
