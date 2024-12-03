-- Inserting data into the Users table
INSERT INTO `mydb3`.`Users` (`name`, `email`, `phone_number`, `registration_date`)
VALUES 
('John Doe', 'john.doe@example.com', '1234567890', '2024-01-01'),
('Jane Smith', 'jane.smith@example.com', '0987654321', '2024-01-02'),
('Alice Johnson', 'alice.j@example.com', '5551234567', '2024-01-03'),
('Bob Brown', 'bob.b@example.com', '7779876543', '2024-01-04'),
('Charlie Green', 'charlie.g@example.com', '1112233445', '2024-01-05'),
('Dave White', 'dave.w@example.com', '6668889990', '2024-01-06'),
('Eva Black', 'eva.b@example.com', '9990001112', '2024-01-07'),
('Frank Blue', 'frank.b@example.com', '3334445556', '2024-01-08'),
('Grace Yellow', 'grace.y@example.com', '7775553332', '2024-01-09'),
('Hannah Red', 'hannah.r@example.com', '8886664441', '2024-01-10'),
('Ivan Purple', 'ivan.p@example.com', '2229990001', '2024-01-11'),
('Julia Pink', 'julia.p@example.com', '4445556662', '2024-01-12'),
('Kyle Orange', 'kyle.o@example.com', '6667778883', '2024-01-13'),
('Liam Gray', 'liam.g@example.com', '5559993334', '2024-01-14'),
('Mia Violet', 'mia.v@example.com', '1118887775', '2024-01-15');

-- Inserting data into the Courses table
INSERT INTO `mydb3`.`Courses` (`titel_course`, `description_course`, `duration_course`)
VALUES 
('Intro to Cybersecurity', 'A basic course on cybersecurity concepts', 30),
('Data Science Essentials', 'Learn the fundamentals of data science', 45),
('Advanced C++ Programming', 'Master complex C++ topics and techniques', 60),
('Database Design', 'Introduction to relational database design', 40),
('Cloud Computing Basics', 'Overview of cloud infrastructure and services', 50),
('Python for Beginners', 'Learn Python programming from scratch', 35),
('Machine Learning Fundamentals', 'Understanding key machine learning algorithms', 60),
('Web Development with JavaScript', 'Build dynamic websites with JS', 40),
('Linux Administration', 'Manage Linux systems and networks', 55),
('Software Testing', 'Learn how to test software effectively', 45),
('Blockchain Technology', 'Understand blockchain concepts and applications', 50),
('DevOps Practices', 'Implement DevOps tools and practices', 60),
('Cybersecurity Threats', 'Advanced concepts in cybersecurity defense', 65),
('Mobile App Development', 'Create mobile applications using Android and iOS', 70),
('AI Ethics', 'Explore ethical concerns around AI', 35);

-- Inserting data into the Enrollments table
INSERT INTO `mydb3`.`Enrollments` (`user_id`, `course_id`, `enrollment_date`)
VALUES 
(1, 1, '2024-01-15'),
(2, 2, '2024-01-16'),
(3, 3, '2024-01-17'),
(4, 4, '2024-01-18'),
(5, 5, '2024-01-19'),
(6, 6, '2024-01-20'),
(7, 7, '2024-01-21'),
(8, 8, '2024-01-22'),
(9, 9, '2024-01-23'),
(10, 10, '2024-01-24'),
(11, 11, '2024-01-25'),
(12, 12, '2024-01-26'),
(13, 13, '2024-01-27'),
(14, 14, '2024-01-28'),
(15, 15, '2024-01-29');

-- Inserting data into the Modules table
INSERT INTO `mydb3`.`Modules` (`course_id`, `titel_module`, `description_module`)
VALUES 
(1, 'Module 1: Basics of Cybersecurity', 'Introduction to core cybersecurity concepts'),
(2, 'Module 1: Data Science Introduction', 'Understanding data science fundamentals'),
(3, 'Module 1: C++ Syntax', 'Overview of basic C++ syntax and operations'),
(4, 'Module 1: Database Design Principles', 'Exploring key principles in relational databases'),
(5, 'Module 1: Cloud Basics', 'Introduction to cloud services and providers'),
(6, 'Module 1: Python Fundamentals', 'Learn basic Python syntax and structures'),
(7, 'Module 1: Machine Learning Overview', 'Introduction to ML algorithms and models'),
(8, 'Module 1: JavaScript Basics', 'Learning JavaScript syntax and functions'),
(9, 'Module 1: Linux File System', 'Understanding the Linux file system and structure'),
(10, 'Module 1: Testing Basics', 'Key concepts in software testing and QA'),
(11, 'Module 1: Blockchain Principles', 'Exploring how blockchain works'),
(12, 'Module 1: DevOps Introduction', 'Key DevOps tools and concepts'),
(13, 'Module 1: Cybersecurity Advanced Topics', 'Deeper look at modern cybersecurity threats'),
(14, 'Module 1: Mobile App Basics', 'Introduction to Android and iOS development'),
(15, 'Module 1: AI Ethics Overview', 'Exploring the ethics of AI development');

-- Inserting data into the Notifications table
INSERT INTO `mydb3`.`Notifications` (`user_id`, `course_id`, `message`, `sent_date`, `is_read`)
VALUES 
(1, 1, 'You are behind in Cybersecurity', '2024-01-20', 0),
(2, 2, 'Complete your module on Data Science', '2024-01-21', 0),
(3, 3, 'Test reminder: C++ Programming', '2024-01-22', 1),
(4, 4, 'New module available: Database Design', '2024-01-23', 0),
(5, 5, 'Progress reminder: Cloud Computing', '2024-01-24', 1),
(6, 6, 'Python for Beginners update', '2024-01-25', 0),
(7, 7, 'Machine Learning assignment due', '2024-01-26', 0),
(8, 8, 'JavaScript session tomorrow', '2024-01-27', 1),
(9, 9, 'New Linux Administration module', '2024-01-28', 0),
(10, 10, 'Software Testing module update', '2024-01-29', 1),
(11, 11, 'Blockchain course announcement', '2024-01-30', 0),
(12, 12, 'DevOps course feedback', '2024-01-31', 1),
(13, 13, 'Complete Cybersecurity by deadline', '2024-02-01', 0),
(14, 14, 'Mobile App Development session', '2024-02-02', 0),
(15, 15, 'New AI Ethics discussion available', '2024-02-03', 1);

-- Inserting data into the Progress table
INSERT INTO `mydb3`.`Progress` (`enrollment_id`, `module_id`, `completed_date`, `is_completed`, `progress_percentage`)
VALUES 
(1, 1, '2024-02-01', 1, 100.00),
(2, 2, '2024-02-02', 0, 50.00),
(3, 3, '2024-02-03', 1, 100.00),
(4, 4, '2024-02-04', 1, 100.00),
(5, 5, '2024-02-05', 0, 40.00),
(6, 6, '2024-02-06', 1, 100.00),
(7, 7, '2024-02-07', 0, 75.00),
(8, 8, '2024-02-08', 0, 60.00),
(9, 9, '2024-02-09', 1, 100.00),
(10, 10, '2024-02-10', 0, 30.00),
(11, 11, '2024-02-11', 1, 100.00),
(12, 12, '2024-02-12', 0, 85.00),
(13, 13, '2024-02-13', 1, 100.00),
(14, 14, '2024-02-14', 0, 20.00),
(15, 15, '2024-02-15', 1, 100.00);

-- Inserting data into the Tests table
INSERT INTO `mydb3`.`Tests` (`module_id`, `titel_test`, `description_test`, `created_date`)
VALUES 
(1, 'Cybersecurity Basics Test', 'Test on basic cybersecurity concepts', '2024-02-01'),
(2, 'Data Science Introduction Test', 'Test on introductory data science topics', '2024-02-02'),
(3, 'C++ Syntax Test', 'Test on basic C++ syntax and usage', '2024-02-03'),
(4, 'Database Design Test', 'Test on relational database design principles', '2024-02-04'),
(5, 'Cloud Computing Test', 'Test on fundamental cloud computing concepts', '2024-02-05'),
(6, 'Python Fundamentals Test', 'Test on Python basics', '2024-02-06'),
(7, 'Machine Learning Algorithms Test', 'Test on fundamental machine learning algorithms', '2024-02-07'),
(8, 'JavaScript Syntax Test', 'Test on JavaScript syntax and functions', '2024-02-08'),
(9, 'Linux Administration Test', 'Test on Linux system administration', '2024-02-09'),
(10, 'Software Testing Test', 'Test on key concepts in software testing', '2024-02-10'),
(11, 'Blockchain Technology Test', 'Test on blockchain fundamentals', '2024-02-11'),
(12, 'DevOps Practices Test', 'Test on essential DevOps practices', '2024-02-12'),
(13, 'Cybersecurity Threats Test', 'Advanced cybersecurity concepts test', '2024-02-13'),
(14, 'Mobile App Development Test', 'Test on Android and iOS development', '2024-02-14'),
(15, 'AI Ethics Test', 'Test on the ethical issues in AI', '2024-02-15');

-- Inserting data into the Questions table
INSERT INTO `mydb3`.`Questions` (`test_id`, `text`, `number_points`)
VALUES 
(1, 'What is a firewall?', 10),
(1, 'Describe phishing.', 10),
(2, 'What is a data frame?', 10),
(2, 'Describe the concept of overfitting.', 10),
(3, 'What is a pointer in C++?', 10),
(3, 'Explain the difference between stack and heap memory.', 10),
(4, 'What is a primary key?', 10),
(4, 'Explain normalization in databases.', 10),
(5, 'What is IaaS?', 10),
(5, 'Describe the difference between public and private cloud.', 10),
(6, 'What is a list in Python?', 10),
(6, 'Describe the use of decorators in Python.', 10),
(7, 'What is supervised learning?', 10),
(7, 'Explain the concept of gradient descent.', 10),
(8, 'What is an event in JavaScript?', 10),
(8, 'Describe the DOM structure.', 10);

-- Inserting data into the Answers table
INSERT INTO `mydb3`.`Answers` (`question_id`, `text`, `is_correct`)
VALUES 
(1, 'A firewall is a network security system that monitors and controls incoming and outgoing network traffic.', 1),
(1, 'A firewall is a software used for data encryption.', 0),
(2, 'Phishing is a type of social engineering attack.', 1),
(2, 'Phishing is a software vulnerability.', 0),
(3, 'A data frame is a data structure in pandas that holds data in tabular form.', 1),
(3, 'A data frame is a type of neural network.', 0),
(4, 'Overfitting occurs when a model performs well on training data but poorly on test data.', 1),
(4, 'Overfitting means the model underfits the data.', 0),
(5, 'A pointer is a variable that stores the memory address of another variable.', 1),
(5, 'A pointer is a variable used to store values directly.', 0),
(6, 'The stack is a faster memory allocation region, whereas the heap is for dynamic memory allocation.', 1),
(6, 'Stack and heap refer to sorting algorithms.', 0),
(7, 'A primary key is a column or set of columns that uniquely identifies each row in a table.', 1),
(7, 'A primary key is used for sorting data.', 0),
(8, 'Normalization is a process of organizing data in a database to reduce redundancy.', 1),
(8, 'Normalization increases data redundancy.', 0);

-- Inserting data into the Test_Attempts table
INSERT INTO `mydb3`.`Test_Attempts` (`user_id`, `test_id`, `attempt_date`, `score`)
VALUES 
(1, 1, '2024-02-10', 85.00),
(2, 2, '2024-02-11', 90.00),
(3, 3, '2024-02-12', 95.00),
(4, 4, '2024-02-13', 80.00),
(5, 5, '2024-02-14', 70.00),
(6, 6, '2024-02-15', 88.00),
(7, 7, '2024-02-16', 92.00),
(8, 8, '2024-02-17', 85.00),
(9, 9, '2024-02-18', 75.00),
(10, 10, '2024-02-19', 78.00),
(11, 11, '2024-02-20', 83.00),
(12, 12, '2024-02-21', 87.00),
(13, 13, '2024-02-22', 90.00),
(14, 14, '2024-02-23', 91.00),
(15, 15, '2024-02-24', 89.00);
