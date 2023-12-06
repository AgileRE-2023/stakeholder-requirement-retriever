-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2023 at 07:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `getbyhistory_history`
--

CREATE TABLE `getbyhistory_history` (
  `id_history` int(11) NOT NULL,
  `date_generated` datetime(6) NOT NULL,
  `exp_date` datetime(6) NOT NULL,
  `requirements` varchar(200) NOT NULL,
  `id_prodi_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `getbyhistory_history`
--

INSERT INTO `getbyhistory_history` (`id_history`, `date_generated`, `exp_date`, `requirements`, `id_prodi_id`) VALUES
(1, '2023-12-04 17:02:22.480097', '2023-12-04 17:02:22.480097', '[{\"term\": \"biomedical engineer\", \"score\": 2.18439482350391, \"summary\": \"Biomedical engineering (BME) or medical engineering is the application of engineering principles and design concepts to medicine', 26),
(2, '2023-12-04 17:13:35.352796', '2023-12-04 17:13:35.352796', '[{\"term\": \"drug discovery\", \"score\": 1.2319775117173757, \"summary\": \"In the fields of medicine, biotechnology and pharmacology, drug discovery is the process by which new candidate medications are dis', 27),
(3, '2023-12-04 17:15:58.694428', '2023-12-04 17:15:58.694428', '[{\"term\": \"environmental engineer\", \"score\": 1.2362399834798814, \"summary\": \"Environmental engineers conduct hazardous-waste management studies to evaluate the significance of such hazards, advise on ', 28),
(4, '2023-12-04 17:20:46.406273', '2023-12-04 17:20:46.406273', '[{\"term\": \"cover letter\", \"score\": 0.8996710946119771, \"summary\": \"A cover letter, covering letter, motivation letter, motivational letter, or a letter of motivation is a letter of introduction attach', 30),
(5, '2023-12-04 17:24:01.953033', '2023-12-04 17:24:01.953033', '[{\"term\": \"radiation oncology\", \"score\": 1.3125067986230585, \"summary\": \"Radiation therapy or radiotherapy (RT, RTx, or XRT) is a treatment using ionizing radiation, generally provided as part of canc', 31),
(6, '2023-12-04 17:25:56.534190', '2023-12-04 17:25:56.534190', '[{\"term\": \"data analysis\", \"score\": 1.03695989361392, \"summary\": \"Data analysis is the process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information', 32),
(7, '2023-12-04 17:32:58.382260', '2023-12-04 17:32:58.382260', '[{\"term\": \"speech language pathology\", \"score\": 1.5201514421869178, \"summary\": \"Speech\\u2013language pathology (or speech and language pathology) is a field of healthcare expertise practiced globally.', 34),
(8, '2023-12-04 17:35:59.483338', '2023-12-04 17:35:59.483338', '[{\"term\": \"library system\", \"score\": 0.7805260870571215, \"summary\": \"A library system is a central organization created to manage and coordinate operations and services in or between different centers', 35),
(9, '2023-12-04 17:37:45.081711', '2023-12-04 17:37:45.081711', '[{\"term\": \"international relation\", \"score\": 1.8815858850041653, \"summary\": \"International relations (IR) are the interactions among sovereign states. The scientific study of those interactions is als', 36),
(10, '2023-12-04 17:40:45.607923', '2023-12-04 17:40:45.607923', '[{\"term\": \"faculty member\", \"score\": 0.9702695976605605, \"summary\": \"Academic staff, also known as faculty (in North American usage) or academics (in British, Australia, and New Zealand usage), are va', 37),
(11, '2023-12-04 17:42:45.510615', '2023-12-04 17:42:45.510615', '[{\"term\": \"public administration\", \"score\": 1.5177070686832261, \"summary\": \"Public Administration or Public Policy and Administration (an academic discipline) is the implementation of public policy, a', 38),
(12, '2023-12-04 17:46:57.416807', '2023-12-04 17:46:57.416807', '[{\"term\": \"social problem\", \"score\": 0.6851597381297408, \"summary\": \"A social issue is a problem that affects many people within a society. It is a group of common problems in present-day society and ', 39),
(13, '2023-12-04 17:50:01.288149', '2023-12-04 17:50:01.288149', '[{\"term\": \"veterinary medicine\", \"score\": 1.5402743257385447, \"summary\": \"Veterinary medicine is the branch of medicine that deals with the prevention, management, diagnosis, and treatment of disease,', 40),
(14, '2023-12-04 17:52:19.732674', '2023-12-04 17:52:19.732674', '[{\"term\": \"financial institution\", \"score\": 0.9370200349186708, \"summary\": \"A financial institution, sometimes called a banking institution, is a business entity that provides service as an intermedia', 41),
(15, '2023-12-04 17:54:23.774059', '2023-12-04 17:54:23.774059', '[{\"term\": \"delta dental\", \"score\": 0.9268529050268806, \"summary\": \"The Delta Dental Plans Association, also known as simply Delta Dental, is an American network of dental insurance companies composed ', 42),
(16, '2023-12-04 17:58:07.436506', '2023-12-04 17:58:07.437420', '[{\"term\": \"office manager\", \"score\": 1.4146492626569929, \"summary\": \"Office management is a profession involving the design, implementation, evaluation, and maintenance of the process of work within a', 43),
(17, '2023-12-04 18:00:13.691040', '2023-12-04 18:00:13.691040', '[{\"term\": \"hotel management\", \"score\": 1.03148676282199, \"summary\": \"A hotel manager, hotelier, or lodging manager is a person who manages the operation of a hotel, motel, resort, or other lodging-rel', 44),
(18, '2023-12-04 18:02:22.604961', '2023-12-04 18:02:22.604961', '[{\"term\": \"end user\", \"score\": 1.4193174495807415, \"summary\": \"In product development, an end user (sometimes end-user) is a person who ultimately uses or is intended to ultimately use a product. The ', 45),
(19, '2023-12-04 18:06:33.905813', '2023-12-04 18:06:33.905813', '[{\"term\": \"control system\", \"score\": 2.2796949165448983, \"summary\": \"A control system manages, commands, directs, or regulates the behavior of other devices or systems using control loops. It can rang', 46),
(20, '2023-12-04 18:09:31.091836', '2023-12-04 18:09:31.091836', '[{\"term\": \"clinical laboratory\", \"score\": 2.117082065370883, \"summary\": \"A medical laboratory or clinical laboratory is a laboratory where tests are conducted out on clinical specimens to obtain infor', 47),
(21, '2023-12-04 18:10:34.280633', '2023-12-04 18:10:34.280633', '[{\"term\": \"occupational safety\", \"score\": 0.7829829616768966, \"summary\": \"Occupational safety and health (OSH) or occupational health and safety (OHS), also known simply as occupational health or occu', 48),
(22, '2023-12-04 18:11:50.141389', '2023-12-04 18:11:50.141389', '[{\"term\": \"physical therapy\", \"score\": 2.187266890275691, \"summary\": \"Physical therapy (PT), also known as physiotherapy, is one of the allied health professions. It is provided by physical therapists', 49),
(23, '2023-12-04 18:14:00.768507', '2023-12-04 18:14:00.768507', '[{\"term\": \"patient care\", \"score\": 1.4787250723343102, \"summary\": \"Health care, or healthcare, is the improvement of health via the prevention, diagnosis, treatment, amelioration or cure of disease, i', 50),
(24, '2023-12-04 18:17:20.356156', '2023-12-04 18:17:20.356156', '[{\"term\": \"income tax\", \"score\": 1.3869826477060943, \"summary\": \"An income tax is a tax imposed on individuals or entities (taxpayers) in respect of the income or profits earned by them (commonly call', 51),
(25, '2023-12-04 18:19:56.515633', '2023-12-04 18:19:56.515696', '[{\"term\": \"customer service\", \"score\": 1.162063053394426, \"summary\": \"Customer service is the assistance and advice provided by a company to those people who buy or use its products or services. Each ', 52),
(26, '2023-12-04 18:21:17.185497', '2023-12-04 18:21:17.185497', '[{\"term\": \"body care\", \"score\": 0.511549274692125, \"summary\": \"Personal care products are consumer products which are applied on various external parts of the body such as skin, hair, nails, lips, ext', 53);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `getbyhistory_history`
--
ALTER TABLE `getbyhistory_history`
  ADD PRIMARY KEY (`id_history`),
  ADD KEY `getByHistory_history_id_prodi_id_617589bc_fk_getByQuer` (`id_prodi_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `getbyhistory_history`
--
ALTER TABLE `getbyhistory_history`
  MODIFY `id_history` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `getbyhistory_history`
--
ALTER TABLE `getbyhistory_history`
  ADD CONSTRAINT `getByHistory_history_id_prodi_id_617589bc_fk_getByQuer` FOREIGN KEY (`id_prodi_id`) REFERENCES `getbyquery_prodi` (`id_prodi`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
