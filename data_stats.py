import pandas as pd

# Load the PATIENTS.csv file
patients_df = pd.read_csv('./hq_data/physionet.org/files/mimiciii/1.4/PATIENTS.csv')

# Get statistics for PATIENTS.csv
total_rows_patients = len(patients_df)
unique_patients_patients = patients_df['SUBJECT_ID'].nunique()

print("PATIENTS.csv Statistics:")
print(f"Total number of rows: {total_rows_patients}")
print(f"Number of unique patients: {unique_patients_patients}")
print()

# Load the EVENTNOTES.csv file
eventnotes_df = pd.read_csv('./hq_data/physionet.org/files/mimiciii/1.4/NOTEEVENTS.csv')

# Get statistics for EVENTNOTES.csv
total_rows_eventnotes = len(eventnotes_df)
unique_patients_eventnotes = eventnotes_df['SUBJECT_ID'].nunique()
unique_patient_hospital_admission = eventnotes_df.groupby(['SUBJECT_ID', 'HADM_ID']).ngroups

print("EVENTNOTES.csv Statistics:")
print(f"Total number of rows: {total_rows_eventnotes}")
print(f"Number of unique patients: {unique_patients_eventnotes}")
print(f"Number of unique patients with hospital admission: {unique_patient_hospital_admission}")

admission_df = pd.read_csv('./hq_data/physionet.org/files/mimiciii/1.4/ADMISSIONS.csv')

# Get statistics for EVENTNOTES.csv
total_rows_admissions = len(admission_df)
unique_patients_admission_df= admission_df['SUBJECT_ID'].nunique()

print("ADMISSIONS.csv Statistics:")
print(f"Total number of rows: {total_rows_admissions}")
print(f"Number of unique patients: {unique_patients_admission_df}")

diagnosis_df = pd.read_csv('./hq_data/physionet.org/files/mimiciii/1.4/DIAGNOSES_ICD.csv')

# Get statistics for EVENTNOTES.csv
total_rows_diagnosis = len(diagnosis_df)
unique_patients_diagnosis_df= diagnosis_df['SUBJECT_ID'].nunique()

print("DIAGNOSES.csv Statistics:")
print(f"Total number of rows: {total_rows_diagnosis}")
print(f"Number of unique patients: {unique_patients_diagnosis_df}")
