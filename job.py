class Job:
    def __init__(self, id, duration, gpu_usage, thermal_output, priority=1):
        self.id = id
        self.duration = duration
        self.remaining_time = duration
        self.gpu_usage = gpu_usage
        self.thermal_output = thermal_output
        self.priority = priority