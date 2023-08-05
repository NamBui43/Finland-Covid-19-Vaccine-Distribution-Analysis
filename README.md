# Finland-Vaccine-Distribution-Analysis
Course project for Aalto University CS-A1155 - Databases for Data Science 2023.

Implement a database system for managing production and distribution of vaccines.

Analysis of vaccine distribution within the Finnish healthcare system using SQL queries and Python pandas library.

## Introduction
During the Covid pandemic, the global vaccination campaign necessitates the implementation of a robust and comprehensive database system which is capable of managing the complicated logistics of vaccine production and distribution. Furtheremore, adopting an efficient data-driven approach for the production and distribution of vaccines is crucial, as it shed lights on key patterns, bottlenecks, and opportunities for improvement in the supply chain. 

The first goal of the project is to implement a database system for managing information about different entities involved in the production and distribution of vaccines. The database should be capable of following the entire lifecycle of a vaccine – from manufacturing, merged into a batch, through hospitals and clinics, to the hands of medical workers, and injected into the patient. The database should also be capable of storing health conditions of patients before and after vaccinations, such as symptomps and side-effects. 

The second goal is to 
uncover and provide valuable insights into the vaccine distribution within the Finnish healthcare system. By presenting a tangible case study of vaccine distribution in Finland, this project aims to provide a pragmatic demonstration of how data-driven approaches can optimize the management of healthcare resources, contribute to informed decision-making, and ultimately, advance public health outcomes.

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

## Analysis of the dataset
10 problems



 We implemented the database using PostgreSQL instead of SQLite, as
PostgreSQL DBMS is widely adopted in real-world projects, and offers
broader control over the database





