
# Job Match Recommendation Engine

Job recommendation engine that matches jobseekers to jobs based on their skills. It reads data from two CSV files (`jobseekers.csv` and `jobs.csv`) and outputs a ranked list of job recommendations for each jobseeker.

## How to use

    python cli.py <jobs.csv> <jobseekers.csv>



## Output

    jobseeker_id,jobseeker_name,job_id,job_title,matching_skill_count,matching_skill_percent
    1,Alice,5,Ruby Developer,3,100
    1,Alice,2,.NET Developer,3,75
    1,Alice,7,C# Developer,3,75
    1,Alice,4,Dev Ops Engineer,4,50
    2,Bob,3,C++ Developer,4,100
    2,Bob,1,Go Developer,3,75


## Export to file
 

    python cli.py <jobs.csv> <jobseekers.csv> > output.csv



## Tests
 

    python -m unittest discover tests/




