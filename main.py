from typing import List, Dict, Optional


def readPatientsFromFile(filename):
    """
    Reads patient data from a plaintext file.

    fileName: The name of the file to read patient data from.
    Returns a dictionary of patient IDs, where each patient has a list of visits.
    The dictionary has the following structure:
    {
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        patientId (int): [
            [date (str), temperature (float), heart rate (int), respiratory rate (int), systolic blood pressure (int), diastolic blood pressure (int), oxygen saturation (int)],
            ...
        ],
        ...
    }
    """
    #Importing data from txt file
    patients = {}
    try: 
        file = open(filename, 'r')
    except FileNotFoundError:
        print("The file patients.txt could not be found.")
        patients = {}
    #Reading data from speficic lines
    data = file.readlines()
    for line_num, line in enumerate(data):
        line_num += 1
        sections = line.split(',')
        if len(sections) != 8:
            print(f"Invalid number of sections ({len(sections)}) in line: {line}")

        #Trying each case, and raising errors if it triggers
        try:
            patientId = int(sections[0])
            visitData = [sections[1]]
            value = float(sections[2])
            if not 35 <= value <= 42:
                raise ValueError(f"Invalid temperature value ({value}) in line: {line}")
            visitData.append(value)

            value = float(sections[3])
            if not 30 <= value <= 180:
                raise ValueError(f"Invalid heart rate value ({value}) in line: {line}")
            visitData.append(value)

            value = float(sections[4])
            if not 5 <= value <= 40:
                raise ValueError(f'Invalid respirator rate value ({value}) in line: {line}')
            visitData.append(value)

            value = float(sections[5])
            if not 70 <= value <= 200:
                raise ValueError(f'Invalid systolic blood pressure value ({value}) in line: {line}')
            visitData.append(value)

            value = float(sections[6])
            if not 40 <= value <= 120:
                raise ValueError(f'Invalid diastolic blood pressuree value ({value}) in line: {line}')
            visitData.append(value)

            value = float(sections[7])
            if not 70 <= value <= 100:
                raise ValueError(f'Invalid oxygen saturation value ({value}) in line: {line}')
            visitData.append(value)

            if patientId in patients:
                patients[patientId].append (visitData)
            else:
                patients[patientId] = [visitData]
        except ValueError as e:
            print(str(e))
        except:
            print("An unexpected error occured while reading the file")
    
    #Closing file
    file.close()
    return patients

def displayPatientData(patients, patientId=0):
    """
    Displays patient data for a given patient ID.

    patients: A dictionary of patient dictionaries, where each patient has a list of visits.
    patientId: The ID of the patient to display data for. If 0, data for all patients will be displayed.
    """
    #Opening file and storing
    file = open("patients.txt", 'r')
    patients = {}
    for line in file:
        sections = line.strip().split(',')
        if len(sections) != 8:
            continue
        patientOrder = int(sections[0])
        
        #Checking if it is in the txt file
        if patientOrder not in patients:
            patients[patientOrder] = {'visits' : []}
        
        #Storing it into a list
        visitData = { 
            "Visit Date:" : sections[1],
            "Temperature:" : float(sections[2]) ,
            "Heart Rate:" : float(sections[3]),
            "Respiratory Rate:" : float(sections[4]),
            "Systolic Blood Pressure:" : float(sections[5]),
            "Diastolic Blood Pressure:" : float(sections[6]),
            "Oxygen Saturation:" : float(sections[7]), # Add a % sign
        }
        patients[patientOrder]['visits'].append(visitData)
    file.close()

    #Printing everything if inputing 0, specific areas if inputing anything else
    if patientId == 0:
        for patient_Id, patients in patients.items():
            print(f"Patient ID:{patient_Id}")
            for visit in patients['visits']:
                print(f" Visit Date: {visit['Visit Date:']}")
                print(f" Temperatrue: {visit['Temperature:']:.2f} C")
                print(f" Visit Date: {visit['Visit Date:']}")
                print(f"  Temperature: {visit['Temperature:']:.2f} C")
                print(f"  Heart Rate: {visit['Heart Rate:']} bpm")
                print(f"  Respiratory Rate: {visit['Respiratory Rate:']} bpm")
                print(f"  Systolic Blood Pressure: {visit['Systolic Blood Pressure:']} mmHg")
                print(f"  Diastolic Blood Pressure: {visit['Diastolic Blood Pressure:']} mmHg")
                print(f"  Oxygen Saturation: {visit['Oxygen Saturation:']} %")
                print()
    elif int(patientId) in patients:
        for visit in patients[int(patientId)]["visits"]:
            print(f" Visit Date: {visit['Visit Date:']}")
            print(f"  Temperature: {visit['Temperature:']:.2f} C")
            print(f"  Heart Rate: {visit['Heart Rate:']} bpm")
            print(f"  Respiratory Rate: {visit['Respiratory Rate:']} bpm")
            print(f"  Systolic Blood Pressure: {visit['Systolic Blood Pressure:']} mmHg")
            print(f"  Diastolic Blood Pressure: {visit['Diastolic Blood Pressure:']} mmHg")
            print(f"  Oxygen Saturation: {visit['Oxygen Saturation:']} %")
            print()
    else:
        print(f"Patient with ID {patientId} not found.")



def displayStats(patients, patientId=0):
    """
    Prints the average of each vital sign for all patients or for the specified patient.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    patientId: The ID of the patient to display vital signs for. If 0, vital signs will be displayed for all patients.
    """

    if patientId.isdigit():
        patientId = int(patientId)

    if patientId == 0:
                
                #Opening txt file
                with open('patients.txt', 'r') as f:
                    lines = f.readlines()
            
                #Creating empty list
                totalTemperature = []
                totalHeartRate = []
                totalRespiratoryRate = []
                totalSystolicBlood = []
                totalDiastolicBlood = []
                totalOxygenSaturation = []

                #Storing data into empty list
                for line in lines:
                    sections  = line.strip().split(',')
                    totalTemperature.append(float(sections[2]))
                    totalHeartRate.append(float(sections[3]))
                    totalRespiratoryRate.append(float(sections[4]))
                    totalSystolicBlood.append(float(sections[5]))
                    totalDiastolicBlood.append(float(sections[6]))
                    totalOxygenSaturation.append(float(sections[7]))

                #Calculating averages
                averageTemperature = sum(totalTemperature) / len(totalTemperature)
                averageHeartRate = sum(totalHeartRate) / len(totalHeartRate)
                averageRespiratoryRate = sum(totalRespiratoryRate) / len(totalRespiratoryRate)
                averageSystolicBlood = sum(totalSystolicBlood) / len(totalSystolicBlood)
                averageDiastolicBlood = sum(totalDiastolicBlood) / len(totalDiastolicBlood)
                averageOxygenSaturation = sum(totalOxygenSaturation) / len(totalOxygenSaturation)
            
                #Printing for all patients 
                print('Vital signs for All Patients')
                print(f"  Average temperature: {averageTemperature:.2f} C")
                print(f"  Average heart rate: {averageHeartRate:.2f} bpm")
                print(f"  Average respiratory rate: {averageRespiratoryRate:.2f} bpm")
                print(f"  Average systolic blood pressure: {averageSystolicBlood:.2f} mmHg")
                print(f"  Average diastolic blood pressure: {averageDiastolicBlood:.2f} mmHg")
                print(f"  Average oxygen saturation: {averageOxygenSaturation:.2f} %")

    
    else:
            #Creating a new variable for if anything but 0
            patientStats = patients[patientId]
            totalTemperature = []
            totalHeartRate = []
            totalRespiratoryRate = []
            totalSystolicBlood = []
            totalDiastolicBlood = []
            totalOxygenSaturation = []  

            #Exactly the same as above
            for visit in patientStats:
                totalTemperature.append(visit[1])
                totalHeartRate.append(visit[2])
                totalRespiratoryRate.append(visit[3])
                totalSystolicBlood.append(visit[4])
                totalDiastolicBlood.append(visit[5])
                totalOxygenSaturation.append(visit[6])


        
            #Calculating averages
            averageTemperature = sum(totalTemperature) / len(totalTemperature)
            averageHeartRate = sum(totalHeartRate) / len(totalHeartRate)
            averageRespiratoryRate = sum(totalRespiratoryRate) / len(totalRespiratoryRate)
            averageSystolicBlood = sum(totalSystolicBlood) / len(totalSystolicBlood)
            averageDiastolicBlood = sum(totalDiastolicBlood) / len(totalDiastolicBlood)
            averageOxygenSaturation = sum(totalOxygenSaturation) / len(totalOxygenSaturation)
            
            print(f'Vital Signs for Patient {patientId}')
            print(f"  Average temperature: {averageTemperature:.2f} C")
            print(f"  Average heart rate: {averageHeartRate:.2f} bpm")
            print(f"  Average respiratory rate: {averageRespiratoryRate:.2f} bpm")
            print(f"  Average systolic blood pressure: {averageSystolicBlood:.2f} mmHg")
            print(f" Average diastolic blood pressure: {averageDiastolicBlood:.2f} mmHg")
            print(f"  Average oxygen saturation: {averageOxygenSaturation:.2f} mmHg")


    return



def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2, fileName):
    """
    Adds new patient data to the patient list.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to add data to.
    patientId: The ID of the patient to add data for.
    date: The date of the patient visit in the format 'yyyy-mm-dd'.
    temp: The patient's body temperature.
    hr: The patient's heart rate.
    rr: The patient's respiratory rate.
    sbp: The patient's systolic blood pressure.
    dbp: The patient's diastolic blood pressure.
    spo2: The patient's oxygen saturation level.
    fileName: The name of the file to append new data to.
    """

    #We are going to split the dates into year. month, day
    year, month, day = date.split('-')
    # Check if date format is valid
    if len(date) != 10 or len(year) != 4 or len(month) != 2 or len(day) != 2 or date[4] != '-' or date[7] != '-':
        print("Invalid date format. Please enter date in the format 'yyyy-mm-dd'.")
    
    #Check if inputing proper month or day (12 months 31 days)
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        print("Invalid Date. Please enter a valid date.")
        return
    
    if month < 1 or month > 12 or day < 1 or day > 31:
        print("Invalid Date. Please enter a valid date.")
        return
    
    # Check if temperature is valid
    if not (35.0 <= temp <= 42.0):
        print("Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.")
        return

    # Check if heart rate is valid
    if not (30 <= hr <= 180):
        print("Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.")
        return

    # Check if respiratory rate is valid
    if not (5 <= rr <= 40):
        print("Invalid respiratory rate. Please enter a respiratory rate between 5 and 40 bpm.")
        return

    # Check if systolic blood pressure is valid
    if not (70 <= sbp <= 200):
        print("Invalid systolic blood pressure. Please enter a systolic blood pressure between 70 and 200 mmHg.")
        return

    # Check if diastolic blood pressure is valid
    if not (40 <= dbp <= 120):
        print("Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 40 and 120 mmHg.")
        return

    # Check if oxygen saturation level is valid
    if not (70 <= spo2 <= 100):
        print("Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%.")
        return

    # Open the file in append mode
    with open(fileName, 'a') as f:
        # Write the new data to the file
        f.write("%s,%s,%.1f,%d,%d,%d,%d,%d\n" % (patientId, date, temp, hr, rr, sbp, dbp, spo2))


    # Add the new data to the patient's visit history
    if patientId in patients:
        patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])
    else:
        patients[patientId] = [[date, temp, hr, rr, sbp, dbp, spo2]]

        


def findVisitsByDate(patients, year=None, month=None):
    """
    Find visits by year, month, or both.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    year: The year to filter by.
    month: The month to filter by.
    return: A list of tuples containing patient ID and visit that match the filter.
    """

    #Making an empty list to store visits
    visits = []
    for patientId, patientVisits in patients.items():
        for visit in patientVisits:
            visitDate = visit[0]
            #Seperating the date into year, month, day
            visitYear, visitMonth, visitDay = visitDate.split('-')
            if year is not None and int(visitYear) != year:
                continue
            if month is not None and int(visitMonth) != month:
                continue
            #Appending empty list with new information
            visits.append((patientId, visit))

    #Returning list
    return visits






def findPatientsWhoNeedFollowUp(patients):
    """
    Find patients who need follow-up visits based on abnormal vital signs.

    patients: A dictionary of patient IDs, where each patient has a list of visits.
    return: A list of patient IDs that need follow-up visits to to abnormal health stats.
    """

    #filling in data 
    followup_patients = []
    patients = {}
    file = open('patients.txt', 'r')
    for line in file:
            data = line.strip().split(",")
            if len(data) != 8:
                continue
            patientId = int(data[0])
            visit = {
                "date": (data[1]),
                "Heart Rate": float(data[2]),
                "Systolic Blood Pressure": float(data[3]),
                "Diastolic Blood Pressure": float(data[4]),
                "Oxygen Saturation": float(data[5])
            }
            if patientId not in patients:
                patients[patientId] = [visit]
            else:
                patients[patientId].append(visit)

    #Checking if patient fits area needed for a follow up
    for patientId, visits in patients.items():
            for visit in visits:
                heartRate = visit["Heart Rate"]
                systolicBlood = visit["Systolic Blood Pressure"]
                diastolicBlood = visit["Diastolic Blood Pressure"]
                oxygenSaturation = visit["Oxygen Saturation"]

                if heartRate > 100 or heartRate < 60 or systolicBlood > 140 or diastolicBlood > 90 or oxygenSaturation < 90:
                    followup_patients.append(patientId)
                    break
    


    return followup_patients




def deleteAllVisitsOfPatient(patients, patientId, filename):
    """
    Delete all visits of a particular patient.

    patients: The dictionary of patient IDs, where each patient has a list of visits, to delete data from.
    patientId: The ID of the patient to delete data for.
    filename: The name of the file to save the updated patient data.
    return: None
    """

    #first check if patient exists
    if patientId not in patients:
        print(f"No data found for patient with ID {patientId}")
        return

    #Deletes patient
    del patients[patientId]
    print(f"Data for patient {patientId} has been deleted.")
    
    #Opens file in writting mode to delete patient
    with open(filename, 'w') as file:
        for patient_id, visits in patients.items():
            for visit in visits:
                #Feel like I can optimize this but don't know how
                visitData = ','.join([str(patient_id), visit[0], str(visit[1]), str(visit[2]), str(visit[3]),
                                      str(visit[4]), str(visit[5]), str(visit[6])])

                file.write(visitData + '\n')










###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################

def main():
    patients = readPatientsFromFile('patients.txt')
    while True:
        print("\n\nWelcome to the Health Information System\n\n")
        print("1. Display all patient data")
        print("2. Display patient data by ID")
        print("3. Add patient data")
        print("4. Display patient statistics")
        print("5. Find visits by year, month, or both")
        print("6. Find patients who need follow-up")
        print("7. Delete all visits of a particular patient")
        print("8. Quit\n")

        choice = input("Enter your choice (1-8): ")
        if choice == '1':
            displayPatientData(patients)
        elif choice == '2':
            patientID = int(input("Enter patient ID: "))
            displayPatientData(patients, patientID)
        elif choice == '3':
            patientID = int(input("Enter patient ID: "))
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                temp = float(input("Enter temperature (Celsius): "))
                hr = int(input("Enter heart rate (bpm): "))
                rr = int(input("Enter respiratory rate (breaths per minute): "))
                sbp = int(input("Enter systolic blood pressure (mmHg): "))
                dbp = int(input("Enter diastolic blood pressure (mmHg): "))
                spo2 = int(input("Enter oxygen saturation (%): "))
                addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2, 'patients.txt')
            except ValueError:
                print("Invalid input. Please enter valid data.")
        elif choice == '4':
            patientID = input("Enter patient ID (or '0' for all patients): ")
            displayStats(patients, patientID)
        elif choice == '5':
            year = input("Enter year (YYYY) (or 0 for all years): ")
            month = input("Enter month (MM) (or 0 for all months): ")
            visits = findVisitsByDate(patients, int(year) if year != '0' else None,
                                      int(month) if month != '0' else None)
            if visits:
                for visit in visits:
                    print("Patient ID:", visit[0])
                    print(" Visit Date:", visit[1][0])
                    print("  Temperature:", "%.2f" % visit[1][1], "C")
                    print("  Heart Rate:", visit[1][2], "bpm")
                    print("  Respiratory Rate:", visit[1][3], "bpm")
                    print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
                    print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
                    print("  Oxygen Saturation:", visit[1][6], "%")
            else:
                print("No visits found for the specified year/month.")
        elif choice == '6':
            followup_patients = findPatientsWhoNeedFollowUp(patients)
            if followup_patients:
                print("Patients who need follow-up visits:")
                for patientId in followup_patients:
                    print(patientId)
            else:
                print("No patients found who need follow-up visits.")
        elif choice == '7':
            patientID = input("Enter patient ID: ")
            deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()
