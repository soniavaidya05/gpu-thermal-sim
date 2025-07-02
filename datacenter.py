# Imports
from gpu import GPU
from job import Job
from datastructures import PriorityQueue

class DataCenter:
    """
    Attributes:
    - gpus: list of GPU objects in data center
    - job_queue: list of jobs 
    - thermal_reservoir: total thermal energy generated across all GPUs in data center
    - reuse_threshold: how much thermal energy must accumulate in reservoir before it's reusable
    """
    def __init__(self, num_gpus: int):
        self.gpus = [GPU(i) for i in range(num_gpus)]
        self.gpus_in_use = []
        self.job_queue = PriorityQueue()
        self.thermal_reservoir = 0.0     
        self.reuse_threshold = 50.0    
        self.reused_energy = 0.0
    
    def job_queue_from_list(self, job_list):
        self.job_queue.build_heap(job_list)
    
    def add_job_to_queue(self, job):
        self.job_queue.push(job)
    
    def assign_job(self, job: Job, gpu_id):
        gpu = self.gpus[gpu_id]
        if not gpu.in_use:
            gpu.in_use = True
            gpu.current_job = job 
            self.gpus_in_use.append(gpu)

            if self.job_queue.contains(job):
                self.job_queue.remove_by_id(job.id)

            return True 
        
        print("GPU {gpu_id} is already in use! Choose a different GPU.")
        return False 
    
    def reuse_thermal_energy(self):
        if self.thermal_reservoir < self.reuse_threshold:
            return 0.0

        efficiency = 0.15  # 15% ORC conversion efficiency

        reused = self.thermal_reservoir * efficiency
        self.reused_energy += reused

        print(f"Reused {reused:.2f} units of energy using ORC.")
        self.thermal_reservoir = 0.0    # Note: the rest of the energy is wasted (but can be used to power other things)
        return reused
    
    def schedule_jobs(self):
        ...