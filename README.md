# AffinityAnswers-Tasks
## Round 1:
1. Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file.
    ### Assumptions: 
    The model is created for "English" language. 

## Round 2:
1. The following questions test your aptitude for interacting with databases. The questions are based off the following public SQL DB: https://docs.rfam.org/en/latest/database.html

    - How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger? (hint: use the biological name of the tiger)
    - Find all the columns that can be used to connect the tables in the given database.
    - Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables)
    - We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)

2. This question is to test your aptitude for writing small shell scripts on Unix. You are given this URL https://www.amfiindia.com/spages/NAVAll.txt. Write a shell script that extracts the Scheme Name and Asset Value fields only and saves them in a csv file. 
