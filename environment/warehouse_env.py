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