import numpy as np

class WarehouseEnv:
    def __init__(self, grid_size=5, num_agents=2, num_items=3):
        self.grid_size = grid_size
        self.num_agents = num_agents
        self.num_items = num_items
        self.reset()

    #Create the postion of agents and items randomly
    def reset(self):
        self.agent_pos = [np.random.randint(0, self.grid_size, size=2) for _ in range(self.num_agents)]
        self.item_pos = [np.random.randint(0, self.grid_size, size=2) for _ in range(self.num_items)]

        #True if all items are picked
        self.done = False
        return self._get_obs()

    #Construct observations for each agent, "What they see" there own position and also items position
    def _get_obs_(self):
        obs = []
        for agent in self.agent_pos:
            obs.append(np.concatenate([agent.flatten(), np.array(self.item_pos).flatten()]))
        return obs
    
    #Changes the position of each agent at every step base on actions input
    def step(self, actions):
        rewards = []
        #0: move up, 1: move down, 2: move left, 3: move right, 4:stay
        move_map = {0: (-1,0), 1: (1,0), 2: (0,-1), 3: (0,1), 4: (0,0)}

        for i, action in enumerate(actions):
            #Moves to make for each agent
            move = move_map[action]
            #Update position
            self.agent_pos[i] += np.array(move)
            #Make sure still in grid
            self.agent_pos[i] = np.clip(self.agent_pos[i], 0, self.grid_size-1)
        
        for i, agent in enumerate(self.agent_pos):
            reward = 0