"""
This file is used for data cleaning and data pre-processing using pandas.
"""

import pandas as pd


# **********************************************************
# Reading Excel files and load data into pandas dataframes *
# **********************************************************

# Insert paths to the spreadsheets here
df_vaccine_type = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineType")
df_manufacturer = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Manufacturer")
df_vaccine_batch = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccineBatch")
df_vaccination_stations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinationStations")
df_transportation_log = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Transportation log")
df_staff_members = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="StaffMembers")
df_shifts = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Shifts")
df_vaccinations = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Vaccinations")
df_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Patients")
df_vaccine_patients = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="VaccinePatients")
df_symptoms = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Symptoms")
df_diagnosis = pd.read_excel('data/vaccine-distribution-data.xlsx', sheet_name="Diagnosis")


# *******************************************************************************************
# Data preprocessing and data cleaning with pandas                                          *
# Exporting dataframes to cleaned .csv files for populating the tables in Postgres database *
# *******************************************************************************************

# VaccineData
vaccine_data = df_vaccine_type[[col for col in df_vaccine_type if not col.startswith('Unnamed:')]]
vaccine_data.columns = ['vaccineid', 'name', 'nrofdoses', 'tempmin', 'tempmax']
print('VaccineData: ')
print(vaccine_data.head())
vaccine_data.to_csv('data/CSVs/VaccineData.csv', index = False)

# Manufacturer
manufacturer = df_manufacturer[[col for col in df_manufacturer if not col.startswith('Unnamed:')]]
manufacturer.columns = ['id', 'origin', 'phone', 'vaccineid']
print('Manufacturer: ')
print(manufacturer.head())
manufacturer.to_csv('data/CSVs/Manufacturer.csv', index = False)

# Vaccinationbatch
vaccinationBatch = df_vaccine_batch[[col for col in df_vaccine_batch if not col.startswith('Unnamed:')]]
vaccinationBatch.columns = ['batchid', 'amount', 'vaccineid', 'manufid', 'manufdate', 'expdate', 'initialreceiver']
vaccinationBatch = vaccinationBatch.reindex(columns = ['batchid', 'amount', 'manufdate', 'expdate', 'manufid', 'vaccineid', 'initialreceiver'])
vaccinationBatch['manufdate'] = pd.to_datetime(vaccinationBatch['manufdate'])
vaccinationBatch['expdate'] = pd.to_datetime(vaccinationBatch['expdate'])
vaccinationBatch = vaccinationBatch.dropna(axis = 0, subset=['manufdate', 'expdate'])
print('VaccinationBatch: ')
print(vaccinationBatch.head())
vaccinationBatch.to_csv('data/CSVs/VaccinationBatch.csv', index=False)

# MedicalFacility
medicalFacility = df_vaccination_stations[[col for col in df_vaccination_stations if not col.startswith('Unnamed:')]]
medicalFacility.columns = ['name', 'address', 'phone']
print('MedicalFacility:')
print(medicalFacility)
medicalFacility.to_csv('data/CSVs/MedicalFacility.csv', index = False)

# TransportationLog
transportationLog = df_transportation_log[[col for col in df_transportation_log if not col.startswith('Unnamed:')]]
transportationLog.columns = ['batchid', 'receivername', 'sendername',  'arrivaldate', 'departuredate']
transportationLog['id'] = transportationLog.index
transportationLog = transportationLog.reindex(columns = ['id', 'departuredate', 'arrivaldate', 'batchid', 'sendername', 'receivername'])
transportationLog['departuredate'] = pd.to_datetime(transportationLog['departuredate'])
transportationLog['arrivaldate'] = pd.to_datetime(transportationLog['arrivaldate'])
transportationLog = transportationLog.dropna(axis=0, subset=['departuredate', 'arrivaldate'])
print('TransportationLog: ')
print(transportationLog.head())
transportationLog.to_csv('data/CSVs/TransportationLog.csv', index = False)

# StaffMembers
staffMember = df_staff_members[[col for col in df_staff_members if not col.startswith('Unnamed:')]]
staffMember.columns = ['ssno', 'name', 'birthday', 'phone', 'role', 'vaccinationstatus', 'employer']
staffMember = staffMember.reindex(columns = ['ssno', 'name', 'phone', 'birthday', 'vaccinationstatus', 'role', 'employer'])
print('StaffMember: ')
print(staffMember.head())
staffMember.to_csv('data/CSVs/StaffMember.csv', index = False)

# VaccinationShift
vaccination_shifts = df_shifts[[col for col in df_shifts if not col.startswith('Unnamed:')]]
vaccination_shifts = vaccination_shifts.rename(columns={'station': 'location'})
print('VaccinationShitfs: ')
print(vaccination_shifts.head())
vaccination_shifts.to_csv('data/CSVs/VaccinationShift.csv', index = False)

# VaccinationEvent
vaccination_event = df_vaccinations[[col for col in df_vaccinations if not col.startswith('Unnamed:')]]
vaccination_event.columns = ['date', 'location', 'batchid']
vaccination_event['date'] = pd.to_datetime(vaccination_event['date'],errors='coerce')
vaccination_event = vaccination_event.dropna(axis=0, subset=['date'])
print('VaccinationEvent: ')
print(vaccination_event.head())
vaccination_event.to_csv('data/CSVs/VaccinationEvent.csv', index=False)

# Patient 
patient = df_patients[[col for col in df_patients if not col.startswith('Unnamed:')]]
patient = patient.rename(columns={'date of birth': 'birthday', 'ssNo': 'ssno'})
print('Patient: ')
print(patient.head())
patient.to_csv('data/CSVs/Patient.csv', index = False)

# Attend
attend = df_vaccine_patients[[col for col in df_vaccine_patients if not col.startswith('Unnamed:')]]
attend.columns = ['date', 'location', 'patient']
attend['date'] = pd.to_datetime(attend['date'], errors='coerce')
attend = attend.dropna(axis=0, subset=['date'])
print('Attend: ')
print(attend.head())
attend.to_csv('data/CSVs/Attend.csv', index = False)

# Symptom
symptom = df_symptoms[[col for col in df_symptoms if not col.startswith('Unnamed:')]]
symptom = symptom.rename(columns = {'criticality':'critical'})
print('Symptom:')
print(symptom.head())
symptom.to_csv('data/CSVs/Symptom.csv', index = False)

# Diagnosed
diagnosed = df_diagnosis[[col for col in df_diagnosis if not col.startswith('Unnamed:')]]
diagnosed.columns = ['patient', 'symptom', 'date']
diagnosed['date'] = pd.to_datetime(diagnosed['date'], errors='coerce')
diagnosed = diagnosed.dropna(axis=0, subset=['date'])
print('Diagnosed')
print(diagnosed)
diagnosed.to_csv('data/CSVs/Diagnosed.csv', index = False)