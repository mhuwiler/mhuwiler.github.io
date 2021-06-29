#<conf>{"title": "HTCondor batch system", "navtitle": "HTCondor basics", "toc":1}

HTCondor is a High Throughput grid engine, available to schedule jobs on Lxplus. Here is a summary of the most useful commands related to its use. 


### Listing the submitted jobs 

To list the jobs running (under the current username), the followig command can be used: 

	condor_q

### Submitting jobs

To submit a HTCondor job, do: 

	condor_submit SubmitCondor.sh

where SubmitCondor.sh is the submitscript. 

### Running diagnostics

To run diagnostics on jobs that are in Hold status, one can use: 

	condor_q -analyze 

or also (gives more thorough output): 

	condor_q -better-analyze


### Removing jobs 

To remove a given job, type the following command: 

	condor_rm [jobid]

To remove all jobs you submitted, use: 

	condor_rm [username]
