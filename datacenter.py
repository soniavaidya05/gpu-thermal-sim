# Imports
from gpu import GPU
from job import Job

class DataCenter:
    """
    Attributes:
    - gpus: list of GPU objects in data center
    - job_queue: list of jobs 
    - thermal_reservoir: total thermal energy generated across all GPUs 
    - reuse_threshold: how much thermal energy must accumulate in reservoir before it's reusable
    """
    def __init__(self, num_gpus: int):
        self.gpus = [GPU(i) for i in range(num_gpus)]
        self.gpus_in_use = []
        self.job_queue = []
        self.thermal_reservoir = 0.0     
        self.reuse_threshold = 100.0    
    
    def assign_job(self, job: Job, gpu_id):
        gpu = self.gpus[gpu_id]
        if not gpu.current_job:
            gpu.current_job = job 
            self.gpus_in_use.append(gpu)
            return True 
        return False 