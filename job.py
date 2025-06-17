class Job:
    """
    Attributes:
        - id: integer id of job
        - duration: duration of job
        - remaining_time: how much time left for job to complete
        - gpu_usage: how much of the GPU’s capacity a job uses while running, a fraction from 0.0 - 1.0
        - thermal_output: how much heat the job's execution creates
        - priority: priority of the job in the data center's job queue 
    """
    def __init__(self, id, duration, gpu_usage, thermal_output, priority=1):
        self.id = id
        self.duration = duration
        self.remaining_time = duration
        self.gpu_usage = gpu_usage
        self.thermal_output = thermal_output
        self.priority = priority