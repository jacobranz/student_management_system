-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: localhost    Database: grades
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `course_ID` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `creds` int DEFAULT NULL,
  `professor_ID` int DEFAULT NULL,
  PRIMARY KEY (`course_ID`),
  KEY `professor_ID` (`professor_ID`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`professor_ID`) REFERENCES `professor` (`professor_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,'Physics 101',4,99),(2,'Math 150',3,99),(3,'English 120',5,99),(4,'Music 100',2,99);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollment`
--

DROP TABLE IF EXISTS `enrollment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollment` (
  `student_ID` int DEFAULT NULL,
  `course_ID` int DEFAULT NULL,
  KEY `student_ID` (`student_ID`),
  KEY `course_ID` (`course_ID`),
  CONSTRAINT `enrollment_ibfk_1` FOREIGN KEY (`student_ID`) REFERENCES `student` (`student_ID`),
  CONSTRAINT `enrollment_ibfk_2` FOREIGN KEY (`course_ID`) REFERENCES `course` (`course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollment`
--

LOCK TABLES `enrollment` WRITE;
/*!40000 ALTER TABLE `enrollment` DISABLE KEYS */;
INSERT INTO `enrollment` VALUES (24,1),(24,2),(24,4);
/*!40000 ALTER TABLE `enrollment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gradebook`
--

DROP TABLE IF EXISTS `gradebook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gradebook` (
  `student_ID` int DEFAULT NULL,
  `course_ID` int DEFAULT NULL,
  `assignment` varchar(255) DEFAULT NULL,
  `score` float DEFAULT NULL,
  `weight` int DEFAULT NULL,
  KEY `student_ID` (`student_ID`),
  KEY `course_ID` (`course_ID`),
  CONSTRAINT `gradebook_ibfk_1` FOREIGN KEY (`student_ID`) REFERENCES `student` (`student_ID`),
  CONSTRAINT `gradebook_ibfk_2` FOREIGN KEY (`course_ID`) REFERENCES `course` (`course_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gradebook`
--

LOCK TABLES `gradebook` WRITE;
/*!40000 ALTER TABLE `gradebook` DISABLE KEYS */;
INSERT INTO `gradebook` VALUES (24,1,'Midterm 1',80.3,25),(24,1,'Midterm 2',94.1,25),(24,1,'Group Project',86.4,10),(24,4,'Project 1',80.3,40),(24,4,'Project 2',98.2,40),(24,2,'Project 1',78.2,40),(24,2,'Project 2',86.9,40),(24,4,'Project 3',86.2,20),(24,2,'Project 3',78.9,20),(24,1,'Final',74.3,40),(24,2,'Final',90.2,20),(24,4,'Final',92.3,20);
/*!40000 ALTER TABLE `gradebook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `professor`
--

DROP TABLE IF EXISTS `professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `professor` (
  `professor_ID` int NOT NULL AUTO_INCREMENT,
  `first_name` char(255) DEFAULT NULL,
  `last_name` char(255) DEFAULT NULL,
  `age` smallint DEFAULT NULL,
  `qualifications` char(255) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  PRIMARY KEY (`professor_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `professor`
--

LOCK TABLES `professor` WRITE;
/*!40000 ALTER TABLE `professor` DISABLE KEYS */;
INSERT INTO `professor` VALUES (99,'Jansen','Day',40,'Bachelors','2022-02-09');
/*!40000 ALTER TABLE `professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_ID` int NOT NULL AUTO_INCREMENT,
  `first_name` char(255) DEFAULT NULL,
  `last_name` char(255) DEFAULT NULL,
  `age` smallint DEFAULT NULL,
  `grade_level` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`student_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (24,'Jacob','Ranz',21,'14');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-09 13:50:37
