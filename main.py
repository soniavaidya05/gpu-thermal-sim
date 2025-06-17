# Imports
from job import Job
from gpu import GPU
from datacenter import DataCenter

num_gpus = 3

# Make data center 
data_center = DataCenter(num_gpus)

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
# Assume a GPU can do only ONE job at a time
data_center.assign_job(samplejob1, 0)
data_center.assign_job(samplejob2, 1)

# Simulate 15 timesteps
for t in range(15):
    print(f"\n--- Time Step {t} ---")
    for gpu in data_center.gpus_in_use:
        heat = gpu.step()
        data_center.thermal_reservoir += heat
        if gpu.current_job != None:
            print(f"GPU {gpu.id} | Heat: {gpu.heat:.2f} | Job: {gpu.current_job.id if gpu.current_job else 'None'}")
    
    if len(data_center.gpus_in_use) != 0:
        print(f"Thermal Reservoir: {data_center.thermal_reservoir:.2f}")

    if data_center.reuse_thermal_energy() > 0:
        print(f"\nTotal reusable energy recovered: {data_center.reused_energy:.2f}")
    
    # Update the list of GPUs in use in case some jobs are finished
    data_center.gpus_in_use = [gpu for gpu in data_center.gpus_in_use if gpu.current_job]
