CREATE DATABASE `scraping` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use scraping;

CREATE TABLE `pages` (
	  `id` bigint(7) NOT NULL AUTO_INCREMENT,
	  `title` varchar(200) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	  `content` varchar(10000) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
	  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
	  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
