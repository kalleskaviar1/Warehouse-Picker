# Warehouse-Picker

## 1. Project Overview
#### Objective: 
Develop a multi-agent reinforcement learning (RL) system to optimize warehouse picking operations, minimizing opeatins, minimizing total picking time, avoid congestion, and improving energy effiency.

#### Key Features:
- Multi-agent coordination for simultaneous picking
- Congestion modeling to avoid collisions and optimize traffic flow.
- Energy efficiency reward to promote minimal and smooth movement.

#### Tools & Libraries:
- Pytorch (RL model training)
- Gymnasium (custom multi-agent warehouse enviroment)
- Numpy (State representation)
- Matplotlib / Pygame (visualization)

## 2. Problem definition
- Warehouse Grid: Rows = aisles, columns = shelves
- Agents: Multiple pickers
- Orders: Sets of items randomly distributed on shelves.
- Goal: Pick all items quickly, without collisions, and with minimal energy expenditure.

## 3. Environment Design
#### - Grid Representation
- Empty cell, item, or occupied by agent.
- Agents move in 4 directions (up, down, left, right).

#### - Congestion modeling: 
- Collision penalty: -5 per collision.
- Near-agent penalty: -0.1 per step when agents are in close proximity.

#### - Energy Efficiency:
- Movement penalty: -0.05 per step.

## 4. RL Setup
#### State represenation
- Agent positions
- Remaining items
- Position of other agents

#### Action Space
- Move: up, down, left, right, stay

#### Reward Fucntion
reward = +10*items_picked  -1 per step - 5 collision_penalty - 0.05 * steps_for_energy_efficiency -0.1 congestion_penalty