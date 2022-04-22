#created by Kayla Carter for pet finder project 
#future additions by Sarah and Andreas

import mysql.connector
from mysql.connector import errorcode

connection = mysql.connector.connect(
  user = 'root',
  password= 'root',
  host= 'localhost',
)
cursor = connection.cursor(dictionary=True)

DB_NAME='AnimalPicker'


TABLES= {}

TABLES['location']= (
	"CREATE TABLE `location`("
	"  `location_name` VARCHAR(32) NOT NULL, "
	"  `phone_number` VARCHAR(12) NOT NULL, " 
	"  `street` VARCHAR(32) NOT NULL," 
	"  `city` Varchar(10) NOT NULL," 
	"  `state` VARCHAR(6) NOT NULL," 
	"  `zip` INTEGER(5) NOT NULL, " 
	"  `website` VARCHAR(65) NOT NULL, "
	"  PRIMARY KEY (`location_name`) "
	"  )ENGINE=InnoDB"
)		

TABLES['price'] = (
    "CREATE TABLE `price` ("
    "  `price_id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `species` enum('dog','cat') NOT NULL,"
    "  `age` enum('young','adult', 'senior'),"
    "  `declawed` enum('yes','no','na'),"
    "  `total_price` DECIMAL(10,2) NOT NULL,"
    "  PRIMARY KEY (`price_id`, `species`, `age`, `declawed`)"
    ") ENGINE=InnoDB"
)

TABLES['animals']= (
	"CREATE TABLE `animals`("
	"  `pet_id` int(60) NOT NULL AUTO_INCREMENT," 
	"  `species` enum('dog','cat') NOT NULL, "
	"  `name` VARCHAR(32) NOT NULL,"
	"  `breed` VARCHAR(32) NOT NULL,"
  "  `age` enum('young','adult', 'senior')," 
	"  `weight` Varchar(10) NOT NULL,"
	"  `sex` VARCHAR(10) NULL,"
	"  `spayed_or_neutured` enum ('yes', 'no'),"
	"  `color` VARCHAR(30) NOT NULL,"
	"  `vaccination` enum('yes','no', 'unknown'),"
	"  `declawed` enum('yes','no', 'na'),"
	"  `personailty_statement` VARCHAR(300),"
	"  `location_name` VARCHAR(32) NOT NULL,"
  "  `price_id` int(11),"
  "  PRIMARY KEY (`pet_id`)," 
  "  CONSTRAINT `animal_ibfk_1` FOREIGN KEY (`location_name`) "
  "     REFERENCES `location` (`location_name`),"
  "  CONSTRAINT `animal_ibfk_2` FOREIGN KEY (`price_id`) "
  "     REFERENCES `price` (`price_id`)"
	"  )ENGINE=InnoDB"
)

TABLES['customer_account']= (
  "CREATE TABLE `customer_account`("
  "  `customer_id` int(11) NOT NULL AUTO_INCREMENT," 
  "  `street` VARCHAR(32) NOT NULL," 
  "  `city` Varchar(10) NOT NULL," 
  "  `state` VARCHAR(6) NOT NULL," 
  "  `zip` INTEGER(5) NOT NULL, "
  "  `balance` DECIMAL(10,2) NOT NULL,"
  "  `first_name` varchar(14) NOT NULL,"
  "  `last_name` varchar(16) NOT NULL,"
  "  PRIMARY KEY (`customer_id`) "
  "  )ENGINE=InnoDB"
) 

TABLES['adopted_animals'] = (
  "CREATE TABLE `adopted_animals` ("
  "  `pet_id` int(60) NOT NULL AUTO_INCREMENT," 
  "  `date_adopted` date NOT NULL,"
  "  `customer_id` int(11) NOT NULL,"
  "  PRIMARY KEY (`pet_id`, `customer_id`),"
  "  CONSTRAINT `adopted_animals_ibfk_1` FOREIGN KEY (`pet_id`) "
  "     REFERENCES `animals` (`pet_id`),"
  "  CONSTRAINT `adopted_animals_ibfk_2` FOREIGN KEY (`customer_id`) "
  "     REFERENCES `customer_account` (`customer_id`)"
    ") ENGINE=InnoDB"
)

TABLES['match_questions'] = (
  "CREATE TABLE `match_questions` ("
  "  `match_id` int(60) NOT NULL AUTO_INCREMENT," 
  "  `What species?` enum('dog','cat') NOT NULL, " 
  "  `What age?` enum('young','adult', 'senior')," 
  "  `Is the animal declawed?` enum('yes','no'),"
  "  PRIMARY KEY (`match_id`)"
  ") ENGINE=InnoDB"
)

TABLES['adoption_form'] = (
  "CREATE TABLE `adoption_form` ("
  "  `form_id` int(60) NOT NULL AUTO_INCREMENT," 
  "  `residence_type` enum('home','apartment'),"
  "  `email` VARCHAR(20) UNIQUE,"
  "  `phone_number` VARCHAR(12) NOT NULL, "
  "  `customer_id` int(11) NOT NULL,"
  "  `match_id` int(60) NOT NULL,"
  "  PRIMARY KEY (`form_id`),"
  "  CONSTRAINT `adoption_form_ibfk_1` FOREIGN KEY (`customer_id`) "
  "     REFERENCES `customer_account` (`customer_id`),"
  "  CONSTRAINT `adoption_form_ibfk_2` FOREIGN KEY (`match_id`) "
  "     REFERENCES `match_questions` (`match_id`)"
  ") ENGINE=InnoDB"
)


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        connection.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
add_location= ("INSERT INTO location"
  "(location_name, phone_number, street, city , state, zip, website)"
  "VALUES( %s, %s, %s,%s, %s,%s, %s)"
)
data_location=[
  ('One of A Kind Pet Rescue', '330-865-6200', '1929 West Market St.', 'Akron', 'Ohio', '44313', 'https://www.oneofakindpets.com'),
  ('Humane Society of Summit County', '330-487-0333', '7996 Darrow Rd.', 'Twinsburg','Ohio', '44087', 'https://www.summithumane.org/adopt')
]
cursor.executemany(add_location, data_location)


add_price=("INSERT INTO price"
  "(price_id, species, age ,declawed, total_price)"
  "VALUES( %s, %s, %s,%s, %s)"
)
data_price=[
  ('1','dog','young','na','375.00'),
  ('2','dog','adult','na','275.00'),
  ('3','dog','senior','na','150.00'),
  ('4','cat','young','na','120.00'),
  ('5','cat','adult','na','75.00'),
  ('6','cat','senior','na','60.00'),
  ('7','cat','adult','yes','120.00')
]
cursor.executemany(add_price, data_price)


add_animal = ("INSERT INTO animals"
  "(pet_id, species, name,breed, age, weight, sex, spayed_or_neutured,color, vaccination, declawed, personailty_statement, location_name, price_id) "
  "VALUES (%s, %s, %s,%s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)"
  )
# Insert animal info
data_animal= [
  ('1','dog','Max','Terrier','adult', 'medium', 'male', 'yes', 'Tan/White ', 'unknown', 'na', " Ace is hoping for a human to spend his time with, but he's not looking to rush into anything. He can be a little timid when it comes to new people, but once he went to his foster home he blossomed very quickly and became an oversized lap dog! ", 'Humane Society of Summit County', '2' ),
  ('2','dog','Larry','Terrier','adult', 'medium','male', 'yes','Brindle', 'unknown','na', "Larry is independent and enjoys time by himself, but he will gladly curl up with you on the couch to watch some tv or take a nap. He is selective with his canine friends, so he would need a slow introduction to see if they'd be a good match", 'Humane Society of Summit County', '2'),
  ('3','dog','Bismark','Rottweiler','adult','medium','male','yes','Black/Tan','unknown','na',"Bismark is a goofy pup who loves to run around and play! He is shy when meeting new people. Once he is comfortable, he is a very affectionate pup who loves to curl up on your lap for some love!", 'Humane Society of Summit County', '2'),
  ('4','dog','Pop Pop','Shepherd','senior','medium','male','yes','Black','unknown','na',"Pop pop is a spunky old man looking to spend his glory days out of the shelter and in a forever home. Although he might be older, he has a lot of energy.He loves to play with toys and follow his favorite people around for attention.", 'Humane Society of Summit County', '3'),
  ('5','dog','Sassy','Chow Chow','senior','medium','female','yes','Red','unknown','na',"Sassy is an overall laid back dog who enjoys going on walks but mostly enjoys relaxing at home. Sassy does show potential to live with another dog in the home.",'Humane Society of Summit County', '3'),
  ('6','dog','Frieda','Cane Corso','young','large','female','yes','Black','unknown','na',"Frieda is a gentle giant who can't get enough love. She can be sensitive when meeting new people, but once she knows you she is sweet as can be. Frieda loves being outside and going on walks.", 'Humane Society of Summit County', '1'),
  ('7','dog','Bella','Retriever','adult','large','female','yes','Black','unknown','na',"Bella is a sensitive soul who can take some time to adjust to new faces and places, but once she knows you she is a total sweetheart. She prefers slow introductions and may take some time to adjust.",'Humane Society of Summit County', '2'),
  ('8','dog','Rita','Boxer','senior','large','female','yes','Black','unknown','na',"Rita is a super sweet girl looking to find her forever home. Rita absolutely loves going on long walks and enjoys running around the yard playing.Rita does show potential to live with other dogs in her forever home.",'Humane Society of Summit County', '3' ),
  ('9','dog','Butch Cassidy','Dachshund','young','small','male','yes','Black','unknown','na',"Butch Cassidy is shy when meeting new people, so he may take some time before he is comfortable with new people. He loves to go on walks every day and can't wait to get outside to explore all the new scents for the day.",'Humane Society of Summit County', '1' ),
  ('10','dog','Lydia', 'Terrier', 'adult','small','female','yes','White','unknown','na'," Lydia is a friend to all and absolutely loves meeting new people. She is a gentle pup who wants nothing more than some belly rubs and a few treats. When she's feeling playful she enjoys playing with toys and loves to go on walks outside.",'Humane Society of Summit County', '2'),

  ('11','cat','Gizmo','Domestic Shorthair','senior','medium','male','yes','Brown/White','unknown','no',"Gizmo is a laid-back cat who enjoys napping in his cat bed or bird watching through the window. If you're looking for an easy going cat to add to your family, then Gizmo may be the perfect cat for you!",'Humane Society of Summit County','6'),
  ('12','cat','Asha','Domestic Medium Hair','adult','small','female','yes','Black/White','unknown','no',"Asha really enjoys being pet and loves playing with her toys. Her favorite toy has balls that move on a circular track so she can keep chasing them and they never get lost!",'Humane Society of Summit County', '5' ),
  ('13','cat','Router','Domestic Shorthair','adult','medium','male','yes','Brown','unknown','no',"Router is a cutie that has a calm personality and would love to be adopted into a home that has the patience and love he needs to blossom into a confident cat.", 'Humane Society of Summit County', '5'),
  ('14','cat','Chisel','Domestic Shorthair','adult','medium','male','yes','Grey/White','unknown','no',"Chisel has come out of his shell once with the help of a few tasty treats. He is an independent cat, but he absolutely LOVES treats and will even eat them from your hand. Chisel enjoys to play as well.",'Humane Society of Summit County','5'),
  ('15','cat','Boogey','Domestic Shorthair','adult','medium','male','yes','Brown/White','unknown','no',"As soon as you walk in the room he is eager to greet you with a meow or one of his favorite toys. He loves playing and will play with most toys, but especially loves the want toy.",'Humane Society of Summit County', '5'),
  ('16','cat','Lillian','Domestic Shorthair','young','small','female','yes','Black','unknown','no',"Lillian can be shy when first meeting new people and prefers it when you let her come to you when she is ready. She enjoys wand toys and chewy soft treats, but mostly spends her time laying around in her favorite cat bed.",'Humane Society of Summit County','4'),
  ('17','cat','Emu','Domestic Shorthair','young','medium','female','yes','Orange','unknown','no',"She is shy with new people and spends most of her time napping in her favorite box or people watching through the window.She is still growing and learning to be a confident cat",'Humane Society of Summit County', '4'),
  ('18','cat','Quest','Domestic Shorthair','adult','large','male','yes','Brown','unknown','no',"Quest is shy when first meeting new people but once you sit with him for a little bit he slowly comes up to you and enjoys pets.", 'Humane Society of Summit County','2'),
  ('19','cat','Daffy Duck','Siamese','adult','medium','male','yes','Cream','unknown','no',"Daffy Duck would probably be more comfortable being adopted into a home with another resident cat. He would love a low traffic home where he has plenty of time to come out of his shell. Daffy Duck is a sweet and gentle guy.",'Humane Society of Summit County','5'),
  ('20','cat','Tweety','Siamese','adult','medium','female','yes','Cream','unknown','no',"Tweety is nervous when meeting new people, and will need a lot of time and patience in her forever home. Tweety would do best in a low traffic home where she has plenty of time to come out of her shell and gain confidence.",'Humane Society of Summit County','5'),

  ('21','dog','Yukon','Labrador Retriever','adult','large','male','yes','Tan/White','yes','na',"Yukon is a big boy who loves to spend quiet time, one-on-one with his person. Loud, large crowds make him very uncomfortable and nervous.",'One of A Kind Pet Rescue', '2'),
  ('22','dog','Tuxedo','Boston Terrier','senior','small','male','yes','Black/White','yes','na',"He is really a good boy but can be a little moody in his senior years. Tuxedo likes to burrow down in his blankets and wrap himself up like a burrito when he is sleepy.", 'One of A Kind Pet Rescue', '3'),
  ('23','dog','Teddy','Labrador Retriever','adult','large','male','yes','Brown/Black','yes','na',"He is a great boy who loves treats and takes them gently. Going slow would be best for this big guy!", 'One of A Kind Pet Rescue', '2'),
  ('24','dog','Roscoe','Chow Chow','adult','medium','male','yes','Red','yes','na',"He loves to be with people and has lots of love and kisses to give. He takes his treats like a champ and loves to ride in the car!", 'One of A Kind Pet Rescue', '2'),
  ('25','dog','Liv','Terrier','adult','medium','female','yes','White/Brown','yes','na',"She craves attention and affection from people and does not care to share it with other dogs.  She strikes you as an orphaned toddler who is craving a loving home with rules, hot meals, and a place to belong.", 'One of A Kind Pet Rescue', '2'),
  ('26','dog','Lila','Terrier','adult','medium','female','yes','Tan/White','yes','na',"She is a sweet girl. She is curious when outside, and loves treats! She is becoming confused about who to trust and really needs a family who can guide her in the right direction.", 'One of A Kind Pet Rescue', '2'),
  ('27','dog','Henrey','Yorkshire Terrier Yorkie','adult','small','male','yes','Black/Tan','unknown','na',"He is only about three years old but seem older due to his sometimes-grumpy nature. He loves to strut along on the leash and knows that he is a man on a mission.", 'One of A Kind Pet Rescue', '2'),
  ('28','dog','Grady','Australian Shepherd','adult','medium','male','yes','Black/White','yes','na',"Grady has eaten well throughout his life and seems to know how to keep his calm. He is a great walker and has become a favorite among all of our volunteers.", 'One of A Kind Pet Rescue', '2'),
  ('29','dog','Gloria','Terrier','adult','medium','female','yes','Grey/White','yes','na',"She is a wonderful companion when with her people. Gloria can become over-stimulated at times, so her new home will have to take it slow and steady with her.", 'One of A Kind Pet Rescue', '2'),
  ('30','dog','Ellie','Bullmastiff','adult','medium','female','yes','Tan/White','yes','na',"This girl always wears a smile and is happy to be with anyone. She is such a great walking companion, but occasionally rolls on her back for belly rubs.", 'One of A Kind Pet Rescue', '2'),

  ('31','cat','Shameka','Domestic Short Hair','adult','medium','female','yes','Grey','yes','no',"You must approach her quietly and gently. Her trust will need to be earned. But once it is, she will be the most loyal cat you have ever had.", 'One of A Kind Pet Rescue', '5'),
  ('32','cat','Robin','Domestic Short Hair','senior','small','male','yes','Black/White','yes','yes',"Robin is content just tucked away inside his covered cat bed. He is not a fan of loud noises, and likes people to approach him slowly and gently.", 'One of A Kind Pet Rescue', '7'),
  ('33','cat','PJ','Domestic Short Hair','adult','medium','male','yes','Brown/White','yes','no',"When PJ can't find a human to cuddle with, he just cuddles up with his toys. Because he's all about cuddles! PJ is super gentle and affectionate.", 'One of A Kind Pet Rescue', '5'),
  ('34','cat','Karen','Domestic Short Hair','adult','medium','female','yes','Black','yes','no',"She likes toys and definitely likes treats. She needs a family with a gentle an quiet approach. She would do best in a quiet home.", 'One of A Kind Pet Rescue', '5'),
  ('35','cat','Jonah','Domestic Short Hair','adult','medium','male','yes','Grey/White','yes','na',"Jonah is literally just the sweetest. He's so calm and quiet. When you pet him, he pushes into you in the cutest way.", 'One of A Kind Pet Rescue', '7'),
  ('36','cat','Jimmy','Domestic Short Hair','adult','small','male','yes','Grey/White','yes','no',"He is so absolutely adorable. And he'll let you know when he wants your attention. He might actually demand it from you if you're within his sight.", 'One of A Kind Pet Rescue', '5'),
  ('37','cat','Fatima','Domestic Short Hair','adult','medium','female','yes','Grey/White','yes','no',"Fatima is a very nervous kitty. It's difficult to get anywhere near her, as she runs away.", 'One of A Kind Pet Rescue', '5'),
  ('38','cat','Bud E.','Domestic Long Hair','senior','large','male','yes','Brown','yes','yes',"He rolls around for more affection once you start petting him. Bud E. does great with other cats, but he's not a fan of dogs.", 'One of A Kind Pet Rescue', '7'),
  ('39','cat','Angel Foot','Domestic Short Hair','adult','medium','male','yes','White','yes','no',"Angel Foot is as sweet as they come. He's a slow moving, laid back cat. And he's very gentle.", 'One of A Kind Pet Rescue', '5'),
  ('40','cat','Dudley','Domestic Short Hair','senior','medium','male','yes','Orange','yes','no',"He's a very gentle guy, and seems to really enjoy affection.", 'One of A Kind Pet Rescue', '6'),

]
cursor.executemany(add_animal, data_animal)

connection.commit()
cursor.close()
connection.close()

