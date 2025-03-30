--1.	SQL Schema Creation:
if not exists (select name from sys.databases where name='Petcare')
	begin
		create database PetCare;
		print 'Database created';
	end;
else 
	begin
		print 'Database Exists';
	end;	

USE PetCare;


if not exists (select name from sys.tables where name='Pets')
	begin
		create table Pets(PetID int primary key identity(1,1),Name varchar(100) not null
		,Age int not null ,Breed varchar(100) not null,Type varchar(100) not null,AvailableForAdoption bit not null);
	end;
else 
	begin
		print 'Table Exists';
	end;	

if not exists (select name from sys.tables where name='Shelters')
	begin
		create table Shelters (ShelterID int primary key identity(1,1), Name varchar(100) not null, Location varchar(100)
		not null);
	end;
else 
	begin
		print 'Table Exists';
	end;

if not exists (select name from sys.tables where name='Donations')
	begin
		create table Donations (DonationID int primary key identity(1,1), DonorName varchar(100) not null,
		DonationType varchar(20) not null, DonationAmount decimal(10,2) not null, DonationItem varchar(100) not null,
		DonationDate datetime not null);
	end;
else 
	begin
		print 'Table Exists';
	end;

if not exists (select name from sys.tables where name='AdoptionEvents')
	begin
		create table AdoptionEvents (EventID int primary key identity(1,1),
		EventName varchar(100) not null, EventDate datetime not null, Location varchar(100) not null);
	end;
else 
	begin
		print 'Table Exists';
	end;

if not exists (select name from sys.tables where name='Participants')
	begin
		create table Participants (ParticipantID int primary key identity(1,1), ParticipantName varchar(100) not null,
		ParticipantType varchar(100) not null, EventID int, foreign key (EventID) references AdoptionEvents(EventID));
	end;
else 
	begin
		print 'Table Exists';
	end;

-- Insert Sample Data into Pets Table
INSERT INTO Pets (Name, Age, Breed, Type, AvailableForAdoption)
VALUES 
('Buddy', 3, 'Golden Retriever', 'Dog', 1),
('Whiskers', 2, 'Persian', 'Cat', 1),
('Charlie', 1, 'Labrador', 'Dog', 0),
('Mittens', 4, 'Siamese', 'Cat', 1),
('Max', 5, 'German Shepherd', 'Dog', 1);

-- Insert Sample Data into Shelters Table
INSERT INTO Shelters (Name, Location)
VALUES 
('Happy Paws Shelter', 'New York'),
('Furry Friends Haven', 'Los Angeles'),
('Paw Palace', 'Chicago'),
('Safe Haven for Pets', 'Houston'),
('Rescue and Care Center', 'Miami');

-- Insert Sample Data into Donations Table
INSERT INTO Donations (DonorName, DonationType, DonationAmount, DonationItem, DonationDate)  
VALUES  
('John Doe', 'Cash', 150.00, 'N/A', '2025-03-27 10:30:00'),  
('Jane Smith', 'Food', 0.00, 'Dog Food Pack', '2025-03-26 14:45:00'),  
('Emily Johnson', 'Medicine', 0.00, 'Pet Vaccines', '2025-03-25 09:15:00'),  
('Michael Brown', 'Cash', 500.00, 'N/A', '2025-03-24 16:20:00'),  
('Sarah Wilson', 'Toys', 0.00, 'Chew Toys & Balls', '2025-03-23 11:10:00'),  
('David Martinez', 'Supplies', 0.00, 'Pet Beds & Blankets', '2025-03-22 13:50:00');  

-- Insert Sample Data into AdoptionEvents Table
INSERT INTO AdoptionEvents (EventName, EventDate, Location)
VALUES 
('Spring Pet Adoption Drive', '2025-04-15', 'New York'),
('Furry Friends Fest', '2025-05-10', 'Los Angeles'),
('Pet Rescue Meet & Greet', '2025-06-05', 'Chicago'),
('Happy Paws Adoption Day', '2025-07-20', 'Houston'),
('Summer Pet Adoption Fair', '2025-08-12', 'Miami');

-- Insert Sample Data into Participants Table
INSERT INTO Participants (ParticipantName, ParticipantType, EventID)
VALUES 
('John Doe', 'Guest', 1),
('Jane Smith', 'Guest', 2),
('Emily Johnson', 'Organization', 3),
('Michael Brown', 'Guest', 4),
('Sarah Wilson', 'Organization', 5);

--3.	Retrieve Available Pets:
--	Write an SQL query to list pets available for adoption.Output should include the pet's Name, Age, Breed, and Type.
select Name,Age,Breed from Pets where AvailableForAdoption=1;

--4.	Retrieve Event Participants:
--Write an SQL query to list participant names and types for a specific event based on EventID.

declare @EventId int=1;

select ParticipantName,ParticipantType from Participants where EventID=@EventId;

--5.	Update Shelter Information (Stored Procedure):
--Create a stored procedure to update a shelter’s name and location.The procedure should take ShelterID, NewName, and NewLocation as parameters.


go
create procedure UpdateShelterNameAndLocation
@ShelterId int,
@NewName varchar(100),
@NewLocation varchar(100)

as begin

update Shelters set Name=@NewName, Location=@NewLocation where ShelterID=@ShelterId;
end;

--6.	Calculate Shelter Donations:
--Write an SQL query to calculate the total donation amount per shelter.The output should include Shelter Name and Total Donation Amount.

--7.	Retrieve Pets Without Owners:
--Write an SQL query to list all pets that do not have an owner (OwnerID IS NULL).

select PetID,Name from Pets where AvailableForAdoption=1;

SELECT 
    YEAR(DonationDate) AS DonationYear,
    MONTH(DonationDate) AS DonationMonth,
    SUM(DonationAmount) AS TotalDonation
FROM Donations
GROUP BY YEAR(DonationDate), MONTH(DonationDate)
ORDER BY DonationYear DESC, DonationMonth DESC;


select PetID,Name from Pets where Age between 1 and 3 or Age>5;



