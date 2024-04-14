# 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები
CREATE TABLE Author(
    AuthorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL
);

# 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID 
CREATE TABLE Books(
    BooksID INT PRIMARY KEY AUTO_INCREMENT,
    BookName VARCHAR(100) NOT NULL,
    PublicationYear INT,
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
);
 
# 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს
INSERT INTO Author(`FirstName`, `LastName`)
VALUES
('Jemal', 'Karchkhadze'),
('Otar', 'Chiladze'),
('Konstantine', 'Gamsakhurdia'),
('Mikheil', 'Javakhishvili'),
('Guram', 'Rcheulishvili')
;

INSERT INTO Books(`BookName`, `PublicationYear`, `AuthorID`)
VALUES
('Mdgmuri', 1979, 1),
('Gzaze Erti Kaci Midioda', 1973, 2),
('Qaravani', 1988, 1),
('Didostatis marjvena', 1939, 3),
('Kurdgheli', 1927, 4)
;

# 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას
UPDATE Books
set PublicationYear = 1984
WHERE BookName = 'Qaravani'
;
 
# 5. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან
DELETE FROM Author;
DELETE FROM Books;

# 6. წაშალეთ Author და Books ცხრილები
DROP TABLE Author;
DROP TABLE Books;