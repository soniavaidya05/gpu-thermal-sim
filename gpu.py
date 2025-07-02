class GPU:
    """
    Attributes:
        - id: integer representing the GPU
        - in_use: whether the GPU is currently running a job (bool)
        - current_job: the job the GPU is running
        - heat: accumulated thermal energy in the GPU
        - cooling_rate: cooling rate of GPU
        - max_temp: maximum safe operating temperature for a GPU
    """
    def __init__(self, id):
        self.id = id
        self.in_use = False
        self.current_job = None 
        self.heat = 0.0 # accumulated thermal energy in gpu
        self.cooling_rate = 0.1 # TODO: Find a realistic value
        self.max_temp = 100

    def step(self):
        if self.in_use:
            heat_generated = self.current_job.thermal_output 
            self.heat += heat_generated
            self.current_job.remaining_time -= 1

            if self.current_job.remaining_time <= 0:
                print(f"Job {self.current_job.id} completed on GPU {self.id}")
                self.in_use = False 
                self.current_job = None
                return -1

            return heat_generated
        
        else:
            self.heat -= self.cooling_rate
            self.heat = max(self.heat, 0.0) # amount of thermal energy can't be <0
            return 0 