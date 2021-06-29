#<conf>{"title": "Slurm job environment hacks", "navtitle": "slurm basics", "toc":0}

To access a list of running jobs, one can do: 

	squeue

To only see one's jobs: 

	squeue -u [username]

To get the number of jobs running: 

	squeue | grep [username] | wc -l 

To get info about the queues (name, wall time, etc...): 

	sinfo

To cancel jobs: 

	scancel [jobid]

Or to cancell all your jobs: 

	scancel -u [username]

A more comprehensive list of commands can be found here: https://slurm.schedmd.com/man_index.html
