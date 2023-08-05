# Finland-Vaccine-Distribution-Analysis
Course project for Aalto University CS-A1155 - Databases for Data Science 2023.

Implement a database system for managing production and distribution of vaccines.

Analyse vaccine distribution within the Finnish healthcare system using SQL queries and Python pandas library.

## Introduction
During the Covid pandemic, the global vaccination campaign necessitates the implementation of a robust and comprehensive database system which is capable of managing the complicated logistics of vaccine production and distribution. Furtheremore, adopting an efficient data-driven approach for the production and distribution of vaccines is crucial, as it shed lights on key patterns, bottlenecks, and opportunities for improvement in the supply chain. 

The first goal of the project is to implement a database system for managing information about different entities involved in the production and distribution of vaccines. The database should be capable of following the entire lifecycle of a vaccine – from manufacturing, merged into a batch, through hospitals and clinics, to the hands of medical workers, and injected into the patient. The database should also be capable of storing health conditions of patients before and after vaccinations, such as symptomps and side-effects. 

The second goal is to 
uncover and provide valuable insights into the vaccine distribution within the Finnish healthcare system. By presenting a tangible case study of vaccine distribution in Finland, this project aims to provide a pragmatic demonstration of how data-driven approaches can optimize the management of healthcare resources, contribute to informed decision-making, and ultimately, advance public health outcomes.

## Data description and problem analysis
The dataset used for this project can be accessed via 'vaccine-distribution-data.xlsx'. The dataset has 12 sub-datasets, including: VaccineType, Manufacturer, VaccineBatch, VaccinationStations, Transportation, StaffMembers, Shifts, Patients, VaccinePatients, Symptoms, and Diagnosis. Each sub-dataset contains different information regarding 3 types of vaccines, transportation of vaccine batches, treatment plans, and patient data. 

Firstly, a comprehensive database system is designed and implemented to keep track of all datapoints in the 12 sub-datasets. Subsequently, an in-depth analysis was performed on 5 sub-datasets, including StaffMembers, Patients, VaccinePatients, Symptoms, and Diagnosis to uncover important trends and patterns within the Finnish healthcare system. 


