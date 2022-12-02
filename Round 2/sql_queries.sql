/*
Question 1 
How many types of tigers can be found in the taxonomy table of the dataset? What is the "ncbi_id" of the Sumatran Tiger?
*/

select species from taxonomy where species like '% tiger)%' or species like '%(tiger)%';

select ncbi_id from taxonomy where species like '%Sumatran tiger%';



/* 
Question 2
Find all the columns that can be used to connect the tables in the given database.
*/

select table_name,column_name,constraint_name,  referenced_table_name, referenced_column_name from information_schema.key_column_usage where referenced_table_name is not null;



/*
Question 3
Which type of rice has the longest DNA sequence? (hint: use the rfamseq and the taxonomy tables) 
*/

select taxonomy.species, max(rfamseq.length) from taxonomy inner join rfamseq on taxonomy.ncbi_id=rfamseq.ncbi_id where taxonomy.species like '% rice)%' or taxonomy.species like '%(rice)%';


/*
Question 4
We want to paginate a list of the family names and their longest DNA sequence lengths (in descending order of length) where only families that have DNA sequence lengths greater than 1,000,000 are included. Give a query that will return the 9th page when there are 15 results per page. (hint: we need the family accession ID, family name and the maximum length in the results)
*/

select f.rfam_acc, f.rfam_id, rf.length from family f, rfamseq rf, full_region fr where f.rfam_acc= fr.rfam_acc and rf.rfamseq_acc = fr.rfamseq_acc and rf.length >= 1000000 order by rf.length desc limit 120, 15;


