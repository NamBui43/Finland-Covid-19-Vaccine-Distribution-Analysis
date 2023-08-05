CREATE DOMAIN Weekday AS VARCHAR(10) CHECK ( 
    value IN (
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday'
    )
);

CREATE DOMAIN GenderDomain AS CHAR(1) CHECK (
    value IN ('F', 'M', 'O')
);

CREATE TABLE IF NOT EXISTS VaccineData(
    vaccineID VARCHAR(10) NOT NULL,
    name VARCHAR(50) NOT NULL,  
    nrOfDoses INT NOT NULL CHECK (nrOfDoses = 1 OR nrOfDoses = 2),
    tempMin INT NOT NULL, 
    tempMax INT NOT NULL, 

    PRIMARY KEY (vaccineID)
);

CREATE TABLE IF NOT EXISTS Manufacturer(
    ID VARCHAR(10) NOT NULL,
    origin VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    vaccineID VARCHAR(10) NOT NULL,

    FOREIGN KEY (vaccineID) REFERENCES VaccineData(vaccineID),
    PRIMARY KEY (ID)
);

CREATE TABLE IF NOT EXISTS MedicalFacility(
    name VARCHAR(100) NOT NULL,
    address VARCHAR(200) NOT NULL, 
    phone VARCHAR(20) NOT NULL,

    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS VaccinationBatch(
    batchID VARCHAR(10) NOT NULL,
    amount INT NOT NULL,
    manufDate DATE NOT NULL,
    expDate DATE NOT NULL,
    manufID VARCHAR(10) NOT NULL,
    vaccineID VARCHAR(10) NOT NULL,
    initialReceiver VARCHAR(100) NOT NULL,

    FOREIGN KEY (vaccineID) REFERENCES VaccineData(vaccineID),
    FOREIGN KEY (manufID) REFERENCES Manufacturer(ID),
    FOREIGN KEY (initialReceiver) REFERENCES MedicalFacility(name),
    PRIMARY KEY (batchID)
);

CREATE TABLE IF NOT EXISTS TransportationLog(
    ID INT NOT NULL,
    departureDate DATE NOT NULL,
    arrivalDate DATE NOT NULL,
    batchID VARCHAR(10) NOT NULL,
    senderName VARCHAR(100) NOT NULL,
    receiverName VARCHAR(100) NOT NULL,

    FOREIGN KEY (senderName) REFERENCES MedicalFacility(name),
    FOREIGN KEY (receiverName) REFERENCES MedicalFacility(name),
    FOREIGN KEY (batchID) REFERENCES VaccinationBatch(batchID),
    PRIMARY KEY (ID)
);



CREATE TABLE IF NOT EXISTS StaffMember(
    ssNo VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    birthday DATE NOT NULL,
    vaccinationStatus INT NOT NULL CHECK (vaccinationStatus = 0 OR vaccinationStatus = 1),
    role VARCHAR(10) NOT NULL CHECK (role IN ('doctor', 'nurse')),
    employer VARCHAR(100) NOT NULL,

    FOREIGN KEY (employer) REFERENCES MedicalFacility(name),
    PRIMARY KEY(ssNo)
);

CREATE TABLE IF NOT EXISTS VaccinationShift(
    location VARCHAR(100) NOT NULL,
    weekday Weekday NOT NULL,
    worker VARCHAR(50) NOT NULL,

    FOREIGN KEY (location) REFERENCES MedicalFacility(name),
    FOREIGN KEY (worker) REFERENCES StaffMember(ssNo),
    PRIMARY KEY (location, weekday, worker)
);

CREATE TABLE IF NOT EXISTS VaccinationEvent(
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    batchID VARCHAR(10) NOT NULL,
    
    FOREIGN KEY (location) REFERENCES MedicalFacility(name),
    FOREIGN KEY (batchID) REFERENCES VaccinationBatch(batchID),
    PRIMARY KEY (date, location)
);

/*Maybe remove the vaccinationStatus because we are asked to create vaccinationStatus in query 5 */
CREATE TABLE IF NOT EXISTS Patient(
    ssNo VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    birthday DATE NOT NULL,
    gender GenderDomain NOT NULL,
    PRIMARY KEY (ssNo)
);

CREATE TABLE IF NOT EXISTS Symptom(
    name VARCHAR(50) NOT NULL,
    critical INT NOT NULL CHECK (critical = 0 OR critical = 1),

    PRIMARY KEY (name)
);

CREATE TABLE IF NOT EXISTS Diagnosed(
    patient VARCHAR(50) NOT NULL,
    symptom VARCHAR(50) NOT NULL,
    date DATE NOT NULL,

    FOREIGN KEY (patient) REFERENCES Patient(ssNo),
    FOREIGN KEY (symptom) REFERENCES Symptom(name),
    PRIMARY KEY (patient, symptom, date)
);

CREATE TABLE IF NOT EXISTS Attend(
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    patient VARCHAR(50) NOT NULL,

    FOREIGN KEY (date, location) REFERENCES VaccinationEvent(date, location),
    FOREIGN KEY (patient) REFERENCES Patient(ssNo),
    PRIMARY KEY (date, location, patient)
);




