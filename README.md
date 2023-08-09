# Finland-Vaccine-Distribution-Analysis
Course project for Aalto University CS-A1155 - Databases for Data Science 2023.

Implement a database system for managing production, distribution, and injection of vaccines.

Analysis of vaccine distribution within the Finnish healthcare system using SQL queries and Python pandas library.

## Introduction
During the Covid pandemic, the global vaccination campaign necessitates the implementation of a robust and comprehensive database system which is capable of managing the complicated logistics of vaccine production and distribution. Furtheremore, adopting an efficient data-driven approach for the production and distribution of vaccines is crucial, as it shed lights on key patterns, bottlenecks, and opportunities for improvement in the supply chain. 

The first goal of the project is to implement a database system for managing information about different entities involved in the production and distribution of vaccines. The database should be capable of following the entire lifecycle of a vaccine – from manufacturing, merged into a batch, through hospitals and clinics, to the hands of medical workers, and injected into the patient. The database should also be capable of storing health conditions of patients before and after vaccinations, such as symptomps and side-effects. 

The second goal is to uncover and provide valuable insights into the vaccine distribution within the Finnish healthcare system. By presenting a tangible case study of vaccine distribution in Finland, this project aims to provide a pragmatic demonstration of how data-driven approaches can optimize the management of healthcare resources, contribute to informed decision-making, and ultimately, advance public health outcomes.

## Data description and problem analysis
The dataset used for this project can be accessed via 'vaccine-distribution-data.xlsx'. The dataset has 12 sub-datasets, including: VaccineType, Manufacturer, VaccineBatch, VaccinationStations, Transportation, StaffMembers, Shifts, Patients, VaccinePatients, Symptoms, and Diagnosis. Each sub-dataset contains different information regarding 3 types of vaccines, transportation of vaccine batches, treatment plans, and patient data. 

Firstly, a comprehensive database system is designed and implemented to keep track of all datapoints in the 12 sub-datasets. Subsequently, an in-depth analysis was performed on 5 sub-datasets, including StaffMembers, Patients, VaccinePatients, Symptoms, and Diagnosis to uncover important insights and patterns within the Finnish healthcare system. 

## Implementation of the database
To gain clear understanding of each sub-dataset and the relations between them, we first construct an UML model, which can be accessed via 'UML.png'. The UML model is then turned into a relational schema, which can be accessed via 'relational_schema.pdf'.

For creating the database, we create 2 files, 'table_creation.sql' and 'table_creation.py', which are located within folder 'code'. 
  - 'table_creation.sql' contains the query for creating the tables in the database. Constraints of the tables are also included in this file. The tables here are created according the the relational schema created earlier.   
  - 'table_creation.sql' contains the python code to connect to user's PostgreSQL database and execute the file 'table_creation.sql'. Users can run this file to create the tables within their databases.

For populating the database with the data in the dataset, we split the task into several files:
  - In folder 'data', 'data_preprocessing.py' handles the data cleaning process and splits each sub_dataset in the dataset into a seperate csv file. 
  - In folder 'code', 'table_creation.py' connects to user's PostgreSQL database and populates the tables in the database with CSV files created by the file 'data_preprocessing.py' above. Users can run this file to populate the database

## Analysis of the vaccine distribution within Finnish healthcare system
To analyze the dataset, we designed and solved 10 problems, each of which reveals different patterns and correlations in the distribution of Covid-19 vaccines within the Finnish healthcare system. The code implementation for these problems can be accessed via 'data_analysis.ipynb' in folder 'data'.

Problem 1: Create a dataframe for patients and symptoms containing the following columns: (1) ssNO, (2) gender, (3) dateOfBirth, (4)symptom, (5) diagnosisDate. Create a table named ”PatientSymptoms” using the command to sql with options index = True, if exists = "replace".
  -  Based on this dataframe, one can analyze patterns related to gender, age, symptoms reported, and the dates when these symptoms occurred
  -  One could also explore correlations between specific symptoms and gender, or analyze the frequency of different symptoms over time
  -  Additionally, one could calculate statistics such as the average age and age range of individuals reporting specific symptoms, or identify any trends in the occurrence of symptoms
  
Problem 2: Create a dataframe for patients and vaccines containing the following columns: (1)patientssNO, (2)date1, (3)vaccinetype1, (4) date2, (5) vaccinetype2. The attribute ”date1” and ”date2” refer to the date when the first and/or second dose were given to a patient respectively. Similarly,
”vaccinetype1” and ”vaccinetype2” are the type of vaccine used for the first and/or second dose.
  - Vaccination timeline: one can analyze the time intervals between the first and second doses for different vaccine types
  - Vaccine types: one can study the distribution of vaccine types used for the first and second doses and assess any changes in the type of vaccine administered as a second dose.
  - Double-dose vaccination rate: one can calculate the double-does vaccination rate and observe any trends

Problem 3: Create a dataframe using the table ”PatientSymptoms” and separate it into two dataframes, one for males and one for females.
  -  One can see that for female patients, the most three frequent symptoms are muscle ache, headache, and feelings of illness
  -  for male patients, the most frequent symptoms are joint pain, muscle ache, and fever

Problem 4: Create a dataframe using table ”Patient” and add the
”ageGroup” column for each patient. The age groups are
”0-10”, ”10-20”, ”20-40”, ”40-60”, ”60+”.
  -  One can examine the distribution of individuals across different age groups to understand the age demographics

Problem 5: Using the same dataframe in problem 4, add a
column describing each patient’s vaccination status. The
statuses are defined as ”0” for not vaccinated, ”1” for
vaccinated once, and ”2” for fully-vaccinated

Problem 6: For each age group, calculate the percentage of people who
have received zero, one, or two doses of vaccines. Show the
results in a dataframe, where the index is the vaccination
status from problem 5 and the columns are the age groups.
  - Vaccination Rates by Age Group: one can calculate the percentage of individuals in each age group who have received different doses of vaccines This will help you understand the vaccination coverage within each age group
  - Age Group with Highest/Lowest Vaccination: identify which age group has the highest and lowest vaccination rates based on the different doses received. This can help target vaccination campaigns

Problem 7: Create a dataframe for symptoms with three additional columns: ’V01’, ’V02’, and ’V03’. The columns should tell the relative frequency of the symptom with the following values:

≥ 0.1: ”very common”; ≥ 0.05: ”common”; > 0.0: ”rare”; 0.0: ”-”
  -  One can identify which are the most common symptoms among patients after they receive certain type of vaccines. 
  -  One can also identify which symptoms are not due to vaccines, which can help with treatment plans.

Problem 8: Estimate the amount of vaccines (as a percentage) that should be reserved for each vaccination to minimize waste.

Problem 9: Plot the total number of vaccinated patients with respect to date

Problem 10: Suppose that we found out that the nurse with ssNo
”19740919-7140” has been tested positive for corona on
15.5.2021. This problem aims to find out the social security numbers and
names of the patients and staff members that the nurse may
have met in vaccination events in the past 10 days. 

## Requirements
The code for this project was written in Python 3.8 and requires the following libraries:
  -  psycopg2
  -  sqlalchemy
  -  pandas
  -  numpy





