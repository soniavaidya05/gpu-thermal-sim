class GPU:
    def __init__(self, id):
        self.id = id
        self.current_job = None 
        self.heat = 0.0 # accumulated thermal energy in gpu
        self.cooling_rate = 0.1 # TODO: Find a realistic value
        self.max_temp = 100

    def step(self):
        if self.current_job:
            self.heat += self.current_job.thermal_output 
            return self.current_job.thermal_output 
        else:
            self.heat -= self.cooling_rate
            self.heat = max(self.heat, 0.0) # amount of thermal energy can't be <0
            return 0 