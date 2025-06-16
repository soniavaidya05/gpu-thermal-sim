# Imports
from job import Job
from gpu import GPU
from datacenter import DataCenter

num_gpus = 3

# Make data center 
data_center = DataCenter(num_gpus)

# Add GPUs to data center
for i in range(num_gpus):
    new_gpu = GPU(i)
    data_center.gpus.append(new_gpu)

# Create jobs
# TODO: Make this user input
samplejob1 = Job(
    id=1,
    duration=10,             # ~10 time steps (longer run)
    gpu_usage=1.0,           # full GPU utilization
    thermal_output=8.0       # high thermal output per step
)
samplejob2 = Job(
    id=2,
    duration=5,              # shorter job
    gpu_usage=0.6,           # partial GPU usage
    thermal_output=3.0       # lower heat output
)

# Add jobs to queue
data_center.job_queue.append(samplejob1)
data_center.job_queue.append(samplejob2)

# Assign jobs to arbitrary GPUs
data_center.assign_job(samplejob1, 0)
data_center.assign_job(samplejob2, 1)

# Step through each job for each GPU in use
for gpu in data_center.gpus_in_use:
    thermal_output = gpu.step()
    while thermal_output > 0:
        data_center.thermal_reservoir += thermal_output
        thermal_output = gpu.step()