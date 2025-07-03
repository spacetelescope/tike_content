# this script assumes that the python version has been set correctly and all packages versions have been appropriately downlaoded!
from platform import python_version
import time

import astropy.units as u
import dask
import dask.array as da
# import dask.dataframe as dd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy 
from tqdm import tqdm

from astroquery.mast import Observations, Catalogs
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord
from dask import delayed, compute
from dask.dataframe.utils import make_meta
from dask.diagnostics import ProgressBar  # Import the ProgressBar
from dask_gateway import Gateway, GatewayCluster
from distributed.diagnostics.plugin import PipInstall

# Import necessary libraries
import numpy as np
import os
import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from IPython.display import display, HTML

# Import Dask components
import dask
from dask.distributed import Client, performance_report, wait

from dask.distributed import performance_report

import time
import matplotlib.pyplot as plt
import numpy as np
from functools import partial
import psutil
import os
from dask_gateway import Gateway, GatewayCluster

import numpy as np
import pandas as pd
import os
import psutil
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
from IPython.display import display, HTML

# Import Dask components
import dask
from dask.distributed import Client, performance_report, wait

def cpu_intensive_task(task_id, matrix_size=1000, iterations=20):
    """A CPU-intensive task that performs matrix operations repeatedly."""
    start_time = time.time()
    
    # Create random matrices
    matrix_a = np.random.random((matrix_size, matrix_size))
    matrix_b = np.random.random((matrix_size, matrix_size))
    
    # Perform multiple matrix operations to simulate CPU-intensive work
    result = np.identity(matrix_size)
    for i in range(iterations):
        # Mix of operations to stress different CPU aspects
        if i % 3 == 0:
            result = np.matmul(result, matrix_a)
        elif i % 3 == 1:
            result = np.matmul(result, matrix_b)
        else:
            # Element-wise operations
            temp = np.sin(matrix_a) + np.cos(matrix_b)
            result = result + temp
            
        # Add some scalar operations
        result = result * 0.9999
    
    # Force some memory pressure with intermediate results
    intermediate_results = []
    for i in range(3):
        intermediate_results.append(result + np.random.random((matrix_size, matrix_size)) * 0.001)
    
    # Calculate some statistics to ensure work isn't optimized away
    stats = {
        'mean': float(np.mean(result)),
        'std': float(np.std(result)),
        'min': float(np.min(result)),
        'max': float(np.max(result)),
        'task_id': task_id,
        'duration': time.time() - start_time
    }
    
    return stats


# Simple function to run the benchmark in a notebook
def run_benchmark(client, task_type='cpu', num_tasks=100, matrix_size=1000, iterations=20):
    """Run a benchmark with the specified parameters using client.map"""
    
    print(f"Starting Dask benchmark with {num_tasks} {task_type} tasks")
    print(f"Connected to Dask cluster: {client.dashboard_link}")
    
    # Display system information
    print("\n--- System Information ---")
    print(f"CPU cores: {psutil.cpu_count(logical=False)} physical, {psutil.cpu_count(logical=True)} logical")
    print(f"Memory: {psutil.virtual_memory().total / (1024**3):.1f} GB total")
    
    # Get cluster information and number of workers
    workers_info = client.scheduler_info()['workers']
    num_workers = len(workers_info)
    print(f"Number of workers: {num_workers}")
    
    # Prepare task arguments based on the task type
    if task_type == 'cpu':
        task_args = [(i, matrix_size, iterations) for i in range(num_tasks)]
        args_transposed = list(zip(*task_args))
        
        # Start the benchmark
        print("Submitting tasks using client.map...")
        start_time = time.time()
        
        # Use client.map to submit all tasks at once
        futures = client.map(cpu_intensive_task, *args_transposed)
        
    else:
        raise ValueError(f"Unknown task type: {task_type}. Perhaps it needs to be implemented!")
    
    # Wait for tasks to complete - show progress
    total_tasks = len(futures)
    print(f"Waiting for {total_tasks} tasks to complete...")
    
    # Track progress
    def print_progress(futures):
        completed = sum(f.done() for f in futures)
        print(f"Completed: {completed}/{total_tasks} tasks ({completed/total_tasks*100:.1f}%)")
    
    # Wait for all futures to complete
    while not all(f.done() for f in futures):
        print_progress(futures)
        time.sleep(2)
    
    # Gather results
    print("Gathering results...")
    results = client.gather(futures)
    
    total_duration = time.time() - start_time
    print(f"Benchmark completed in {total_duration:.2f} seconds")
    
    # Convert results to DataFrame
    df = pd.DataFrame(results)
    df['task_type'] = task_type
    
    # Show some basic analysis
    print("\n--- Benchmark Analysis ---")
    print(f"Total execution time: {total_duration:.2f} seconds")
    
    # Calculate statistics
    task_stats = df.groupby('task_type')['duration'].agg(['count', 'mean', 'std', 'min', 'max'])
    display(HTML("<h3>Task Statistics</h3>"))
    display(task_stats)
    
    # Calculate throughput
    tasks_per_second = total_tasks / total_duration
    tasks_per_worker_second = tasks_per_second / num_workers if num_workers > 0 else 0
    
    print(f"\nThroughput:")
    print(f"- Total tasks: {total_tasks}")
    print(f"- Tasks per second: {tasks_per_second:.2f}")
    print(f"- Tasks per worker per second: {tasks_per_worker_second:.2f}")
    
    # Plot a histogram of task durations
    plt.figure(figsize=(10, 6))
    sns.histplot(df['duration'], kde=True)
    plt.title(f'Distribution of {task_type.upper()} Task Durations')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Count')
    plt.show()
    
    return df, total_duration









if __name__=='__main__':
    if python_version() != '3.11.7':
        raise ValueError(f'Python version is incorrect: {python_version()} should be 3.11.7')
    gateway = Gateway(address="http://traefik-dask-gateway", auth="jupyterhub")

    # instantiate CPU 100 option
    cluster = gateway.new_cluster(profile='cpu100')
   
    # Adaptively scale between 2 and 3 workers
    cluster.adapt(minimum=2, maximum=3)

    client = cluster.get_client()

    plugin = PipInstall(packages=[
    "tornado==6.4.1"
    ])
    
    # essentially pip installs the package on the cluster
    client.register_plugin(plugin)

    # now, run the benchmark

    with performance_report(filename="dask-report_existing_client.html"):
        with dask.config.set(scheduler='distributed'):
            
            # Run the benchmark
            results, duration = run_benchmark(
                client=client,
                task_type='cpu',
                num_tasks=100,
                matrix_size=1000,
                iterations=20
            )
    









    