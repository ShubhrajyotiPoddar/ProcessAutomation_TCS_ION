-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2025 at 06:06 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automatrix`
--

-- --------------------------------------------------------

--
-- Table structure for table `p2_bot_table`
--

CREATE TABLE `p2_bot_table` (
  `id` int(11) NOT NULL,
  `Transaction Site` varchar(45) DEFAULT NULL,
  `Party Category` varchar(45) DEFAULT NULL,
  `Party Account Code` varchar(255) DEFAULT NULL,
  `Party Account Description` varchar(255) DEFAULT NULL,
  `Party Code` varchar(255) DEFAULT NULL,
  `Party Description` varchar(255) DEFAULT NULL,
  `Voucher Type` varchar(255) DEFAULT NULL,
  `Voucher Number` varchar(255) DEFAULT NULL,
  `Voucher Date` date DEFAULT NULL,
  `Supplier Invoice No or Customer PO No` varchar(255) DEFAULT NULL,
  `Outstanding or Unadjusted Amount in Domestic Currency` decimal(12,2) DEFAULT NULL,
  `Header Narration` varchar(2555) DEFAULT NULL,
  `Status` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `p2_bot_table`
--

INSERT INTO `p2_bot_table` (`id`, `Transaction Site`, `Party Category`, `Party Account Code`, `Party Account Description`, `Party Code`, `Party Description`, `Voucher Type`, `Voucher Number`, `Voucher Date`, `Supplier Invoice No or Customer PO No`, `Outstanding or Unadjusted Amount in Domestic Currency`, `Header Narration`, `Status`) VALUES
(1, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR01268', 'BANKA BEHARI PAUL', 'Credit Note', '3136/25/379', '2025-01-28', NULL, '-100000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22873,Being amount received on 28/01/2025 against sale of materials, and Ref No. is S52397802', 1),
(2, '31', 'NBH-ADM', 'L02030106007', 'Security Deposit of WEST TRIPURA', 'DELR01289', 'CHANDIMATA IRON', 'Party Journal Voucher', '3136/23/339', '2023-03-03', NULL, '-4000000.00', 'This is Voucher Corresponding to Party Journal voucher 22103/Mar-23/44, BEING THE AMOUNT OF RS.40 LACS TRANSFERRED FROM SECURITY DEPOSIT OF JOY CHANDIMATA STEEL TO SECURITY DEPOSIT OF CHANDIMATA IRON', 1),
(3, '31', 'NBH-ADM', 'L02030106007', 'Security Deposit of WEST TRIPURA', 'DELR01289', 'CHANDIMATA IRON', 'Credit Note', '3136/24/7', '2023-04-12', NULL, '-826853.14', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/214,Being amount received on 12/04/2023 against sale of materials, and Ref No. is S68496716', 1),
(4, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DIST00019', 'PRATHIK STEELS', 'Credit Note', '3136/24/79', '2023-06-06', NULL, '-14347.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/3564,BEING AMOUNT RECEIVED ON 06.06.2023.', 1),
(5, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR01468', 'MAA TARA HARDWARE.', 'Credit Note', '3136/25/36', '2024-04-26', NULL, '-58.86', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/1944,Being amount received on 26/04/2024 against sale of materials, and Ref No. is S47322683', 1),
(6, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR01468', 'MAA TARA HARDWARE.', 'Party Journal Voucher', '3136/25/90', '2024-06-21', NULL, '-1584.00', 'This is Voucher Corresponding to Party Journal voucher 31103/Jun-24/1, Being amount transfer from Accounting Site 22 to Accounting Site 31.', 1),
(7, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR01471', 'SHINE IRON STORES', 'Credit Note', '3136/25/264', '2024-10-25', NULL, '-994.81', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/15609,BEING AMOUNT RECEIVED ON 25-10-2024 REF NO. SBINR52024102557909854 ', 1),
(8, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR01482', 'MAJUMDAR ENTERPRISE-SONAMURA ROAD', 'Credit Note', '3136/23/175', '2022-11-01', NULL, '-61.35', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/23/4156,BEING AMOUNT RECEIVED ON 19/10/2022', 1),
(9, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR02171', 'DAYAL IRON STORE & CEMENT HOUSE', NULL, '3136/20/88', '2020-03-18', NULL, '-563.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/20/6355,BEING AMOUNT RECEIVED ON 17/03/20', 1),
(10, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR02314', 'MADAN GOPAL TRADERS', 'Party Journal Voucher', '3136/23/308', '2023-02-10', NULL, '-6219.84', 'This is Voucher Corresponding to Party Journal voucher 22103/Feb-23/65, BEING AMOUNT TRANSFER FROM ACCOUNTING SITE -22 ACCOUNT CODE A02020106002 TO ACCOUNTING SITE - 31 ACCOUNTING CODE A02020207003.', 1),
(11, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR02401', 'LILA RANI CARRYING & HARDWARE CENTER', 'Credit Note', '3136/24/276', '2023-11-24', NULL, '-1855.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/16347,Being amount received on 24/11/2023 against sale of materials, and Ref No. is S11835022', 1),
(12, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DIST00097', 'ABIR ENTERPRISE', 'Credit Note', '3136/25/376', '2025-01-27', NULL, '-4000000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22844,Being amount received on 27/01/2025 against sale of materials, and Ref No. is 43637230283', 1),
(13, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR02938', 'LAXMAN SAHA', 'Credit Note', '3136/25/137', '2024-07-19', NULL, '-5158.29', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/8199,BEING AMOUNT RECEIVED ON 19-7-2024', 1),
(14, '31', 'NBH-ADM', 'A02020207004', 'DEBTORS (Realedge) SOUTH TRIPURA', 'DELR03051', 'SAHA STEEL', 'Credit Note', '3136/25/335', '2024-12-30', NULL, '-2606.39', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/20103,Being amount received on 30/12/2024 against sale of materials, and Ref No. is S74837791', 1),
(15, '31', 'NBH-ADM', 'A02020207004', 'DEBTORS (Realedge) SOUTH TRIPURA', 'DELR03051', 'SAHA STEEL', 'Credit Note', '3136/25/378', '2025-01-28', NULL, '-260000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22872,Being amount received on 28/01/2025 against sale of materials, and Ref No. is S52095665', 1),
(16, '31', 'NBH-ADM', 'A02020207004', 'DEBTORS (Realedge) SOUTH TRIPURA', 'DELR03252', 'STEEL HOUSE', 'Credit Note', '3136/25/383', '2025-01-29', NULL, '-533120.74', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22920,Being amount received on 29/01/2025 against sale of materials, and Ref No. is S58212860', 1),
(17, '31', 'NBH-ADM', 'A02020106002', 'DEBTORS FOR KHOWAI', 'DELR03634', 'RAMKRISHNA HARDWARE & SENITATION GOODS', 'Credit Note', '3136/25/382', '2025-01-29', NULL, '-270000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22918,Being amount received on 29/01/2025 against sale of materials, and Ref No. is S57773568', 1),
(18, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR03694', 'RAMKRISHNA ENTERPRISE', 'Party Journal Voucher', '3136/24/315', '2023-12-28', NULL, '-1118.88', 'This is Voucher Corresponding to Party Journal voucher 22103/Dec-23/95, BEING AMOUNT TRANSFER FROM 22 ACCOUNT CODE A02020106002 AND 31 ACCOUNT CODE A02020207003', 1),
(19, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03752', 'DHARAMRAJI TRADERS', 'Credit Note', '3136/25/377', '2025-01-24', NULL, '-265975.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22852,Being amount received on 23/01/2025 against sale of materials, and Ref No. is S14812650', 1),
(20, '31', 'NBH-ADM', 'A02020207006', 'DEBTORS (Realedge) GOMATI', 'DELR03755', 'JOYKALI HARDWARE', 'Credit Note', '3136/25/331', '2024-12-27', NULL, '-1347.68', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/19879,Being amount received on 27/12/2024 against sale of materials, and Ref No. is S54394087', 1),
(21, '31', 'NBH-ADM', 'A02020207006', 'DEBTORS (Realedge) GOMATI', 'DELR03755', 'JOYKALI HARDWARE', 'Credit Note', '3136/25/362', '2025-01-21', NULL, '-271330.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22131,Being amount received on 21/01/2025 against sale of materials, and Ref No. is S94851991', 0),
(22, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03773', 'AMAR-INDUSTRIES', 'Party Journal Voucher', '3136/25/325', '2024-12-24', NULL, '-5624.11', 'This is Voucher Corresponding to Party Journal voucher 22103/Dec-24/71, BEING AMOUT TRANSFERRED FROM ACCOUNTING SITE 22 TO ACCOUTING SITE 31', 0),
(23, '31', 'NBH-ADM', 'A02020207002', 'DEBTORS(Realedge) SEPHAIJALA', 'DELR03781', 'SREE GURU IRON', 'Credit Note', '3136/24/412', '2024-03-15', NULL, '-1290.90', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/26190,Being amount received on 15/03/2024 against sale of materials, and Ref No. is S62823983', 0),
(24, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR03791', 'SUDIP DEY', 'Credit Note', '3136/25/360', '2025-01-20', NULL, '-4905.46', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22079,Being amount received on 20/01/2025 against sale of materials, and Ref No. is S87035263', 0),
(25, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03817', 'KIRAN HARDWARE', 'Credit Note', '3136/25/328', '2024-12-23', NULL, '-5143.07', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/19691,BEING AMOUNT RECEIVED ON 26-12-2024.', 0),
(26, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03817', 'KIRAN HARDWARE', 'Credit Note', '3136/25/374', '2025-01-27', NULL, '-260000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22772,Being amount received on 27/01/2025 against sale of materials, and Ref No. is S41416567', 0),
(27, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR03818', 'KALPANA STORES', 'Credit Note', '3136/25/312', '2024-12-12', NULL, '-1583.47', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/18574,Being amount received on 12/12/2024 against sale of materials, and Ref No. is S28623474', 0),
(28, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR03862', 'MUKTA HARDWARS', 'Credit Note', '3136/24/269', '2023-11-18', NULL, '-1802.90', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/15903,BEING AMOUNT RECEIVED ON 18-11-2023. REF NO. S51905068', 0),
(29, '31', 'NBH-ADM', 'A02020207004', 'DEBTORS (Realedge) SOUTH TRIPURA', 'DELR03874', 'BISWAKARMA GRIL FACTORY', 'Credit Note', '3136/23/230', '2022-12-07', NULL, '-41804.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/23/4880,BEING AMOUNT RECEIVED ON 07-12-2022.', 0),
(30, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR03907', 'SAKIB TRADERS', 'Credit Note', '3136/24/31', '2023-04-27', NULL, '-809.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/503,BEING AMOUNT RECEIVED ON 27.04.2023.', 0),
(31, '76', 'NBH-ADM', 'A02020106004', 'DEBTORS FOR SEPHAIJALA', 'DIST00199', 'PODDER CONSTRUCTION', 'Party Journal Voucher', '7636/24/27', '2024-01-10', NULL, '-8031.00', 'This is Voucher Corresponding to Party Journal voucher 74103/Jan-24/15, BEING AMOUNT TRANSFER FROM 74 TO 76.', 0),
(32, '31', 'NBH-ADM', 'A02020207007', 'DEBTORS (Realedge) DHALAI', 'DELR03957', 'LOK NATH ENTERPRISE', 'Credit Note', '3136/25/261', '2024-10-31', NULL, '-2390.85', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/15533,Being amount received on 31/10/2024 against sale of materials, and Ref No. is S27030734', 0),
(33, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03958', 'JOY RAM IRON STORES', 'Credit Note', '3136/25/293', '2024-11-28', NULL, '-2830.50', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/17439,Being amount received on 28/11/2024 against sale of materials, and Ref No. is S78344829', 0),
(34, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03958', 'JOY RAM IRON STORES', 'Credit Note', '3136/25/363', '2025-01-22', NULL, '-99995.28', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22235,Being amount received on 22/01/2025 against sale of materials, and Ref No. is S1796341', 0),
(35, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03958', 'JOY RAM IRON STORES', 'Credit Note', '3136/25/375', '2025-01-28', NULL, '-170856.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22784,Being amount received on 28/01/2025 against sale of materials, and Ref No. is S50599224', 0),
(36, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR03973', 'SARKAR HARDWARE STORE', 'Credit Note', '3136/25/370', '2025-01-25', NULL, '-54606.64', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22572,Being amount received on 25/01/2025 against sale of materials, and Ref No. is S28830732', 0),
(37, '76', 'NBH-ADM', 'A02020106001', 'DEBTORS FOR DHALAI', 'DIST00203', 'BISWAKARMA HARDWARE', 'Credit Note', '7636/24/15', '2023-06-15', NULL, '-2413.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 7419/24/142,BEING AMOUNT RECEIVED ON 15.06.2023.', 0),
(38, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR04000', 'JYOTI STEEL', 'Credit Note', '3136/24/41', '2023-04-27', NULL, '-7688.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/547,BEING AMOUNT RECEIVED ON 27.04.2023.', 0),
(39, '31', 'NBH-ADM', 'A02020207006', 'DEBTORS (Realedge) GOMATI', 'DELR04014', 'S.P. TRADERS', 'Credit Note', '3136/25/178', '2024-08-20', NULL, '-907.45', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/10460,Being amount received on 20/08/2024 against sale of materials, and Ref No. is S32675981', 0),
(40, '31', 'NBH-ADM', 'A02020106009', 'Debtors For Retail (Tripura) - No Scheme', 'DELR04078', 'BADAL PAUL', 'Party Journal Voucher', '3136/24/136', '2023-07-25', NULL, '-3208.00', 'This is Voucher Corresponding to Party Journal voucher 22103/Jul-23/180, Being Amount Transfer From Customer Code - CUST01330 to Customer Code-DELR04078.', 0),
(41, '31', 'NBH-ADM', 'A02020207001', 'DEBTORS (Realedge) WEST TRIPURA', 'DELR04101', 'RUMA IRON', 'Credit Note', '3136/25/359', '2025-01-20', NULL, '-76837.89', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22064,Being amount received on 20/01/2025 against sale of materials, and Ref No. is S86410305', 0),
(42, '31', 'NBH-ADM', 'A02020207007', 'DEBTORS (Realedge) DHALAI', 'DELR04147', 'B.M. STEEL INDUSTRY', 'Credit Note', '3136/24/298', '2023-12-18', NULL, '-4294.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/24/18192,Being amount received on 18/12/2023 against sale of materials, and Ref No. is S55123076', 0),
(43, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR04193', 'BARDHAN STEEL INDUSTRISE', 'Credit Note', '3136/24/333', '2024-01-06', NULL, '-1388.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2221/24/2,BEING AMOUNT RECEIVED ON 06-012024', 0),
(44, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR04348', 'DEEP STEEL INDUSTRY', 'Credit Note', '3136/25/184', '2024-08-26', NULL, '-2759.57', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/10798,Being amount received on 26/08/2024 against sale of materials, and Ref No. is S80214912', 0),
(45, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR04348', 'DEEP STEEL INDUSTRY', 'Credit Note', '3136/25/365', '2025-01-22', NULL, '-300000.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22362,Being amount received on 22/01/2025 against sale of materials, and Ref No. is S5150489', 0),
(46, '31', 'NBH-ADM', 'A02020207005', 'DEBTORS (Realedge) NORTH TRIPURA', 'DELR04348', 'DEEP STEEL INDUSTRY', 'Credit Note', '3136/25/366', '2025-01-22', NULL, '-238704.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22363,Being amount received on 22/01/2025 against sale of materials, and Ref No. is S5161563', 0),
(47, '31', 'NBH-ADM', 'A02020207003', 'DEBTORS (Realedge) KHOWAI', 'DELR04458', 'BIPUL DATTA', 'Credit Note', '3136/25/358', '2025-01-20', NULL, '-1614.29', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22062,Being amount received on 20/01/2025 against sale of materials, and Ref No. is S86373204', 0),
(48, '31', 'NBH-ADM', 'A02020106007', 'DEBTORS FOR WEST TRIPURA', 'DELR04460', 'SWASTIK IRON & STEEL CENTER', 'Credit Note', '3136/25/380', '2025-01-28', NULL, '-5.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22855,Being amount received on 28/01/2025 against sale of materials, and Ref No. is S48811244', 0),
(49, '31', 'NBH-ADM', 'A02020106004', 'DEBTORS FOR SEPHAIJALA', 'DELR04472', 'BALAJI TRADERS', 'Credit Note', '3136/25/381', '2025-01-27', NULL, '-1.00', 'Inter Unit Credit Note for the Inter Unit Receipt voucher: 2219/25/22863,Being amount received on 27/01/2025 against sale of materials, and Ref No. is S41747310', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `p2_bot_table`
--
ALTER TABLE `p2_bot_table`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `p2_bot_table`
--
ALTER TABLE `p2_bot_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
