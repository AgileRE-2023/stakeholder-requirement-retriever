-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 12 Des 2023 pada 02.11
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

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
-- Struktur dari tabel `getbyquery_prodi`
--

CREATE TABLE `getbyquery_prodi` (
  `id_prodi` int(11) NOT NULL,
  `nama_prodi` varchar(50) NOT NULL,
  `subject` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `getbyquery_prodi`
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
(53, 'Traditional Medicine', '2'),
(54, 'Actuarial Science', '4'),
(55, 'Naval Architecture and Shipbuilding Engineering', '1'),
(56, 'Marine Engineering', '1'),
(57, 'Ocean Engineering', '1'),
(58, 'Sea Transportation Engineering', '1'),
(59, 'Offshore Engineering', '1'),
(60, 'Mechanical Engineering', '1'),
(61, 'Chemical Engineering', '1'),
(62, 'Engineering Physics', '1'),
(63, 'Materials and Metallurgical Engineering', '1'),
(64, 'Food Engineering', '1'),
(65, 'Informatics', '1'),
(66, 'Information Technology', '1'),
(67, 'Computer Engineering', '1'),
(68, 'Civil Engineering', '1'),
(69, 'Architecture', '0'),
(70, 'Urban and Regional Planning', '4'),
(71, 'Geomatics Engineering', '1'),
(72, 'Geophysics Engineering', '3'),
(73, 'Product Design', '0'),
(74, 'Business Management', '4'),
(75, 'Interior Design', '0'),
(76, 'Visual Communication Design', '0'),
(77, 'Development Studies', '4'),
(78, 'Civil Infrastructure Engineering', '1'),
(79, 'Industrial Mechanical Engineering', '1'),
(80, 'Automation Electronic Engineering', '1'),
(81, 'Industrial Chemical Engineering', '1'),
(82, 'Instrumentation Engineering', '1'),
(83, 'Business Statistics', '4'),
(84, 'Technology Management', '4');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `getbyquery_prodi`
--
ALTER TABLE `getbyquery_prodi`
  ADD PRIMARY KEY (`id_prodi`),
  ADD UNIQUE KEY `nama_prodi` (`nama_prodi`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `getbyquery_prodi`
--
ALTER TABLE `getbyquery_prodi`
  MODIFY `id_prodi` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
