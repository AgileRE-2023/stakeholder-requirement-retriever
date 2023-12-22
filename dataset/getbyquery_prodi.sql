-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2023 at 08:19 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jobrequirements`
--

-- --------------------------------------------------------

--
-- Table structure for table `getbyquery_prodi`
--

CREATE TABLE `getbyquery_prodi` (
  `id_prodi` int(11) NOT NULL,
  `nama_prodi` varchar(50) NOT NULL,
  `subject` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `getbyquery_prodi`
--

INSERT INTO `getbyquery_prodi` (`id_prodi`, `nama_prodi`, `subject`) VALUES
(1, 'Data Science Technology', '1'),
(2, 'Electrical Engineering', '1'),
(3, 'Industrial Engineering', '1'),
(4, 'Nanotechnology Engineering', '1'),
(5, 'Robotics and Artificial Intelligence Engineering', '1'),
(6, 'Dental Medicine', '2'),
(7, 'Accounting', '4'),
(8, 'Development Economics', '4'),
(9, 'Islamic Economics', '4'),
(10, 'Management', '4'),
(11, 'Aquaculture', '3'),
(12, 'Fisheries Product Industry Technology', '3'),
(13, 'English Language and Literature', '0'),
(14, 'Historical Science', '0'),
(15, 'Indonesial Language and Literature', '0'),
(16, 'Japanese Studies', '0'),
(17, 'Law', '4'),
(18, 'Medical Education', '2'),
(19, 'Midwifery', '2'),
(20, 'Nursing', '2'),
(21, 'Pharmacy', '2'),
(22, 'Psychology', '2'),
(23, 'Nutrition Study Program', '2'),
(24, 'Public Health', '2'),
(25, 'Biology', '2'),
(26, 'Biomedical Engineering', '2'),
(27, 'Chemistry', '3'),
(28, 'Environmental Engineering', '3'),
(29, 'Information Systems', '1'),
(30, 'Mathematics', '3'),
(31, 'Physics', '3'),
(32, 'Statistics', '4'),
(33, 'Antropology', '4'),
(34, 'Communication Sciences', '4'),
(35, 'Information and Library Science', '4'),
(36, 'International Relations', '4'),
(37, 'Political Science', '4'),
(38, 'Public Administation', '4'),
(39, 'Sociology', '4'),
(40, 'Veterinary Medicine', '2'),
(41, 'Banking and Finance', '4'),
(42, 'Dental Engineering', '2'),
(43, 'Digital Office Management', '4'),
(44, 'Hotel Management', '4'),
(45, 'Informatics Engineering', '1'),
(46, 'Instrumentation and Control Engineering Technology', '1'),
(47, 'Medical Laboratory Technology', '2'),
(48, 'Occupational Safety and Health Study Program', '2'),
(49, 'Physiotherapy', '2'),
(50, 'Radiology Imaging Technology', '2'),
(51, 'Taxation', '4'),
(52, 'Tourism Destination', '4'),
(53, 'Traditional Medicine', '2');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `getbyquery_prodi`
--
ALTER TABLE `getbyquery_prodi`
  ADD PRIMARY KEY (`id_prodi`),
  ADD UNIQUE KEY `nama_prodi` (`nama_prodi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `getbyquery_prodi`
--
ALTER TABLE `getbyquery_prodi`
  MODIFY `id_prodi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
