import mysql.connector

db_conector = mysql.connector.connect(
  host='localhost',
  user='mar03',
  password='Jfk$oqO',
  database='IT_STEP'
)

db_cursor = db_conector.cursor()

create_user_table = """
CREATE Table IF NOT EXISTS User (
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);
"""

create_profile_table = """
CREATE Table IF NOT EXISTS Profile (
  id INT PRIMARY KEY,
  user_id INT,
  bio VARCHAR(200),
  profile_picture VARCHAR(255)
  FOREIGN KEY (user_id) REFERENCES User(id)
);
"""

db_cursor.execute(create_user_table)
db_cursor.execute(create_profile_table)

user_data = [
    ("Mari04", "Mari4@gmail.com"),
    ("Ana707", "anaana@gmail.com"),
    ("MK", "MK9@gmail.com"),
    ("DavidM", "david303@gmail.com"),
    ("Arthur", "arthur@gmail.com")
]

insert_user_data = "INSERT INTO User (username, email) VALUES (%s, %s)"

for user in user_data:
    db_cursor.execute(insert_user_data, user)

profile_data = [
    (1, "Bio for Mari04", "Mari04_profile_picture.jpg"),
    (2, "Bio for Ana707", "Ana707_profile_picture.jpg"),
    (3, "Bio for MK", "MK_profile_picture.jpg"),
    (4, "Bio for DavidM", "DavidM_profile_picture.jpg"),
    (5, "Bio for Arthur", "Arthur_profile_picture.jpg")
]

insert_profile_data = "INSERT INTO Profile (id, user_id, bio, profile_picture) VALUES (%s, %s, %s, %s)"

for profile in profile_data:
    db_cursor.execute(insert_profile_data, profile)

db_conector.commit()

db_cursor.close()
db_conector.close()