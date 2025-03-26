create table Organizations(OrgId int primary key identity(1,1),OrgName varchar(100) unique not null,Country varchar(50));
create table Series(SeriesId int primary key identity(1,1),SeriesName varchar(100) unique not null,OrgId int,TotalEpisodes int,StartYear int,TRP decimal(5,2),NoOfViews bigint, foreign key (OrgId) references Organizations(OrgId));

create table Cartoons(CharacterId int identity(1,1) primary key,CharacterName nvarchar(100) not null, SeriesId int ,PopularityScore Decimal(10,2), foreign key (SeriesId) references Series(SeriesId));

INSERT INTO Organizations (OrgName, Country) VALUES 
('Disney', 'USA'),
('Warner Bros', 'USA'),
('Nickelodeon', 'USA'),
('Toei Animation', 'Japan'),
('Studio Ghibli', 'Japan');


INSERT INTO Series (SeriesName, OrgId, TotalEpisodes, StartYear, TRP, NoOfViews) VALUES
('Tom and Jerry', 2, 500, 1940, 9.5, 500000000),
('SpongeBob SquarePants', 3, 300, 1999, 8.7, 350000000),
('Dragon Ball Z', 4, 291, 1989, 9.2, 450000000),
('Naruto', 4, 720, 2002, 9.0, 400000000),
('Mickey Mouse Clubhouse', 1, 150, 2006, 8.5, 320000000);



INSERT INTO Cartoons (CharacterName, SeriesId, PopularityScore) VALUES
('Tom', 1, 9.8),
('Jerry', 1, 9.9),
('SpongeBob', 2, 9.0),
('Patrick Star', 2, 8.5),
('Goku', 3, 9.7),
('Vegeta', 3, 9.5),
('Naruto Uzumaki', 4, 9.6),
('Sasuke Uchiha', 4, 9.2),
('Mickey Mouse', 5, 9.1),
('Donald Duck', 5, 8.9);


--filter the series on the basis of TRP

select SeriesName,Trp,NoOfViews from Series where TRP>8.0;


--Sort series by TRP

select SeriesName,Trp,NoOfViews from Series order by TRP desc;

--Filter out the most popular cartoon character

select top 1 CharacterName,PopularityScore from Cartoons order by PopularityScore Desc;

-- Most watched series

select top 1SeriesName,NoOfViews from Series order by NoOfViews desc;






