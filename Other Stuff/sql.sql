CREATE TABLE `leads` (
  `idleads` int NOT NULL,
  `leadname` varchar(45) NOT NULL,
  `stage` varchar(45) DEFAULT NULL,
  `leadstate` varchar(45) DEFAULT NULL,
  `leadcity` varchar(45) DEFAULT NULL,
  `leadphone` varchar(45) NOT NULL,
  `leademail` varchar(45) NOT NULL,
  `leadwebsite` varchar(45) DEFAULT NULL,
  `leadmailing` varchar(45) DEFAULT NULL,
  `leadzip` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idleads`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `employee` (
  `idemployee` int NOT NULL,
  `fnemployee` varchar(45) NOT NULL,
  `lnemployee` varchar(45) NOT NULL,
  `employeepassword` varchar(45) NOT NULL,
  `employeeemail` varchar(45) NOT NULL,
   `employeeusername` varchar(45) NOT NULL,
  PRIMARY KEY (`idemployee`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `customers` (
  `idcustomers` int NOT NULL,
  `customername` varchar(45) NOT NULL,
  `customerbusiness` varchar(45) DEFAULT NULL,
  `customerwebsite` varchar(45) DEFAULT NULL,
  `customerstate` varchar(45) DEFAULT NULL,
  `customerphone` varchar(45) NOT NULL,
  `customeremail` varchar(45) NOT NULL,
  `customerstartcity` varchar(45) DEFAULT NULL,
  `customerbigcity` varchar(45) DEFAULT NULL,
  `adrunning` tinyint DEFAULT NULL,
  PRIMARY KEY (`idcustomers`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
