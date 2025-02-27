-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        10.3.39-MariaDB - mariadb.org binary distribution
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- 导出  表 zy.中药 结构
CREATE TABLE IF NOT EXISTS `中药` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `药名` varchar(255) DEFAULT NULL,
  `价格` decimal(10,2) DEFAULT NULL,
  `常用量` varchar(20) DEFAULT NULL,
  `中药拼音` varchar(255) DEFAULT NULL,
  `备注` text DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=702 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.中药 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `中药` DISABLE KEYS */;
/*!40000 ALTER TABLE `中药` ENABLE KEYS */;

-- 导出  表 zy.基本设置 结构
CREATE TABLE IF NOT EXISTS `基本设置` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `账号` varchar(50) NOT NULL DEFAULT '',
  `医生` varchar(50) DEFAULT NULL,
  `诊金` decimal(10,2) DEFAULT 0.00,
  `诊所名称` varchar(255) DEFAULT NULL,
  `处方抬头` varchar(255) DEFAULT NULL COMMENT '报表主标题',
  `配药` varchar(255) DEFAULT NULL,
  `诊所电话` varchar(20) DEFAULT NULL,
  `诊所地址` varchar(255) DEFAULT NULL,
  `密码` varchar(50) DEFAULT NULL,
  `密码提示` varchar(50) DEFAULT NULL,
  `医生拼音` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.基本设置 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `基本设置` DISABLE KEYS */;
INSERT INTO `基本设置` (`user_id`, `账号`, `医生`, `诊金`, `诊所名称`, `处方抬头`, `配药`, `诊所电话`, `诊所地址`, `密码`, `密码提示`, `医生拼音`) VALUES
	(25, 'admin', '张大夫', 50.00, '常清净草堂', '中医处方笺', '单佩瑶', '123456', '西池2号', '', '', 'ZDF');
/*!40000 ALTER TABLE `基本设置` ENABLE KEYS */;

-- 导出  表 zy.常规资料 结构
CREATE TABLE IF NOT EXISTS `常规资料` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `姓名` varchar(50) DEFAULT NULL,
  `病历号` int(11) DEFAULT NULL,
  `性别` varchar(20) DEFAULT NULL,
  `年龄` varchar(20) DEFAULT NULL,
  `身份证号` varchar(50) DEFAULT NULL,
  `日期时间` datetime DEFAULT NULL,
  `患者照片` varchar(255) DEFAULT NULL,
  `诊断` text DEFAULT NULL,
  `诊断拼音` varchar(255) DEFAULT NULL,
  `住址` varchar(255) DEFAULT NULL COMMENT '患者住址',
  `电话` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `姓名拼音` varchar(100) DEFAULT NULL,
  `剂数` tinyint(4) DEFAULT NULL,
  `针灸次数` tinyint(4) DEFAULT NULL,
  `用法` text DEFAULT NULL,
  `计价` decimal(10,2) DEFAULT NULL,
  `年龄月` varchar(50) DEFAULT NULL,
  `血压` varchar(20) DEFAULT NULL,
  `病证` text DEFAULT NULL,
  `先煎后下1` varchar(255) DEFAULT NULL,
  `先煎后下2` varchar(255) DEFAULT NULL,
  `先煎后下3` varchar(255) DEFAULT NULL,
  `先煎后下4` varchar(255) DEFAULT NULL,
  `先煎后下5` varchar(255) DEFAULT NULL,
  `先煎后下6` varchar(255) DEFAULT NULL,
  `先煎后下7` varchar(255) DEFAULT NULL,
  `先煎后下8` varchar(255) DEFAULT NULL,
  `先煎后下9` varchar(255) DEFAULT NULL,
  `先煎后下10` varchar(255) DEFAULT NULL,
  `先煎后下11` varchar(255) DEFAULT NULL,
  `先煎后下12` varchar(255) DEFAULT NULL,
  `先煎后下13` varchar(255) DEFAULT NULL,
  `先煎后下14` varchar(255) DEFAULT NULL,
  `先煎后下15` varchar(255) DEFAULT NULL,
  `先煎后下16` varchar(255) DEFAULT NULL,
  `先煎后下17` varchar(255) DEFAULT NULL,
  `先煎后下18` varchar(255) DEFAULT NULL,
  `先煎后下19` varchar(255) DEFAULT NULL,
  `先煎后下20` varchar(255) DEFAULT NULL,
  `药物1` varchar(255) DEFAULT NULL,
  `药物2` varchar(255) DEFAULT NULL,
  `药物3` varchar(255) DEFAULT NULL,
  `药物4` varchar(255) DEFAULT NULL,
  `药物5` varchar(255) DEFAULT NULL,
  `药物6` varchar(255) DEFAULT NULL,
  `药物7` varchar(255) DEFAULT NULL,
  `药物8` varchar(255) DEFAULT NULL,
  `药物9` varchar(255) DEFAULT NULL,
  `药物10` varchar(255) DEFAULT NULL,
  `药物11` varchar(255) DEFAULT NULL,
  `药物12` varchar(255) DEFAULT NULL,
  `药物13` varchar(255) DEFAULT NULL,
  `药物14` varchar(255) DEFAULT NULL,
  `药物15` varchar(255) DEFAULT NULL,
  `药物16` varchar(255) DEFAULT NULL,
  `药物17` varchar(255) DEFAULT NULL,
  `药物18` varchar(255) DEFAULT NULL,
  `药物19` varchar(255) DEFAULT NULL,
  `药物20` varchar(255) DEFAULT NULL,
  `用量1` varchar(20) DEFAULT NULL,
  `用量2` varchar(20) DEFAULT NULL,
  `用量3` varchar(20) DEFAULT NULL,
  `用量4` varchar(20) DEFAULT NULL,
  `用量5` varchar(20) DEFAULT NULL,
  `用量6` varchar(20) DEFAULT NULL,
  `用量7` varchar(20) DEFAULT NULL,
  `用量8` varchar(20) DEFAULT NULL,
  `用量9` varchar(20) DEFAULT NULL,
  `用量10` varchar(20) DEFAULT NULL,
  `用量11` varchar(20) DEFAULT NULL,
  `用量12` varchar(20) DEFAULT NULL,
  `用量13` varchar(20) DEFAULT NULL,
  `用量14` varchar(20) DEFAULT NULL,
  `用量15` varchar(20) DEFAULT NULL,
  `用量16` varchar(20) DEFAULT NULL,
  `用量17` varchar(20) DEFAULT NULL,
  `用量18` varchar(20) DEFAULT NULL,
  `用量19` varchar(20) DEFAULT NULL,
  `用量20` varchar(20) DEFAULT NULL,
  `单价1` varchar(10) DEFAULT NULL,
  `单价2` varchar(10) DEFAULT NULL,
  `单价3` varchar(10) DEFAULT NULL,
  `单价4` varchar(10) DEFAULT NULL,
  `单价5` varchar(10) DEFAULT NULL,
  `单价6` varchar(10) DEFAULT NULL,
  `单价7` varchar(10) DEFAULT NULL,
  `单价8` varchar(10) DEFAULT NULL,
  `单价9` varchar(10) DEFAULT NULL,
  `单价10` varchar(10) DEFAULT NULL,
  `单价11` varchar(10) DEFAULT NULL,
  `单价12` varchar(10) DEFAULT NULL,
  `单价13` varchar(10) DEFAULT NULL,
  `单价14` varchar(10) DEFAULT NULL,
  `单价15` varchar(10) DEFAULT NULL,
  `单价16` varchar(10) DEFAULT NULL,
  `单价17` varchar(10) DEFAULT NULL,
  `单价18` varchar(10) DEFAULT NULL,
  `单价19` varchar(10) DEFAULT NULL,
  `单价20` varchar(10) DEFAULT NULL,
  `诊金` decimal(10,2) NOT NULL COMMENT '当次就诊使用的诊金',
  `药费` decimal(10,2) DEFAULT NULL,
  `针灸费用` decimal(10,2) DEFAULT NULL,
  `辨证` text DEFAULT NULL,
  `总费用` decimal(10,2) DEFAULT NULL,
  `针灸或其他` text DEFAULT NULL,
  `备注` text DEFAULT NULL,
  `病证照片1` varchar(255) DEFAULT NULL,
  `病证照片2` varchar(255) DEFAULT NULL,
  `病证照片3` varchar(255) DEFAULT NULL,
  `病证照片4` varchar(255) DEFAULT NULL,
  `病证照片5` varchar(255) DEFAULT NULL,
  `主治医生` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=347 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.常规资料 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `常规资料` DISABLE KEYS */;
/*!40000 ALTER TABLE `常规资料` ENABLE KEYS */;

-- 导出  表 zy.方剂选方 结构
CREATE TABLE IF NOT EXISTS `方剂选方` (
  `编号` int(255) NOT NULL AUTO_INCREMENT,
  `方名` varchar(255) DEFAULT NULL,
  `说明` varchar(255) DEFAULT NULL,
  `方剂选方拼音` varchar(255) DEFAULT NULL,
  `单价1` decimal(6,4) DEFAULT NULL,
  `单价2` decimal(6,4) DEFAULT NULL,
  `单价3` decimal(6,4) DEFAULT NULL,
  `单价4` decimal(6,4) DEFAULT NULL,
  `单价5` decimal(6,4) DEFAULT NULL,
  `单价6` decimal(6,4) DEFAULT NULL,
  `单价7` decimal(6,4) DEFAULT NULL,
  `单价8` decimal(6,4) DEFAULT NULL,
  `单价9` decimal(6,4) DEFAULT NULL,
  `单价10` decimal(6,4) DEFAULT NULL,
  `单价11` decimal(6,4) DEFAULT NULL,
  `单价12` decimal(6,4) DEFAULT NULL,
  `单价13` decimal(6,4) DEFAULT NULL,
  `单价14` decimal(6,4) DEFAULT NULL,
  `单价15` decimal(6,4) DEFAULT NULL,
  `单价16` decimal(6,4) DEFAULT NULL,
  `单价17` decimal(6,4) DEFAULT NULL,
  `单价18` decimal(6,4) DEFAULT NULL,
  `单价19` decimal(6,4) DEFAULT NULL,
  `单价20` decimal(6,4) DEFAULT NULL,
  `剂量1` varchar(20) DEFAULT NULL,
  `剂量2` varchar(20) DEFAULT NULL,
  `剂量3` varchar(20) DEFAULT NULL,
  `剂量4` varchar(20) DEFAULT NULL,
  `剂量5` varchar(20) DEFAULT NULL,
  `剂量6` varchar(20) DEFAULT NULL,
  `剂量7` varchar(20) DEFAULT NULL,
  `剂量8` varchar(20) DEFAULT NULL,
  `剂量9` varchar(20) DEFAULT NULL,
  `剂量10` varchar(20) DEFAULT NULL,
  `剂量11` varchar(20) DEFAULT NULL,
  `剂量12` varchar(20) DEFAULT NULL,
  `剂量13` varchar(20) DEFAULT NULL,
  `剂量14` varchar(20) DEFAULT NULL,
  `剂量15` varchar(20) DEFAULT NULL,
  `剂量16` varchar(20) DEFAULT NULL,
  `剂量17` varchar(20) DEFAULT NULL,
  `剂量18` varchar(20) DEFAULT NULL,
  `剂量19` varchar(20) DEFAULT NULL,
  `剂量20` varchar(20) DEFAULT NULL,
  `药物1` varchar(255) DEFAULT NULL,
  `药物2` varchar(255) DEFAULT NULL,
  `药物3` varchar(255) DEFAULT NULL,
  `药物4` varchar(255) DEFAULT NULL,
  `药物5` varchar(255) DEFAULT NULL,
  `药物6` varchar(255) DEFAULT NULL,
  `药物7` varchar(255) DEFAULT NULL,
  `药物8` varchar(255) DEFAULT NULL,
  `药物9` varchar(255) DEFAULT NULL,
  `药物10` varchar(255) DEFAULT NULL,
  `药物11` varchar(255) DEFAULT NULL,
  `药物12` varchar(255) DEFAULT NULL,
  `药物13` varchar(255) DEFAULT NULL,
  `药物14` varchar(255) DEFAULT NULL,
  `药物15` varchar(255) DEFAULT NULL,
  `药物16` varchar(255) DEFAULT NULL,
  `药物17` varchar(255) DEFAULT NULL,
  `药物18` varchar(255) DEFAULT NULL,
  `药物19` varchar(255) DEFAULT NULL,
  `药物20` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=427 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.方剂选方 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `方剂选方` DISABLE KEYS */;
/*!40000 ALTER TABLE `方剂选方` ENABLE KEYS */;

-- 导出  表 zy.用法 结构
CREATE TABLE IF NOT EXISTS `用法` (
  `编号` int(255) NOT NULL AUTO_INCREMENT,
  `用法` text DEFAULT NULL,
  `煎法` text DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.用法 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `用法` DISABLE KEYS */;
/*!40000 ALTER TABLE `用法` ENABLE KEYS */;

-- 导出  表 zy.病证 结构
CREATE TABLE IF NOT EXISTS `病证` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `临床表现` text DEFAULT NULL,
  `病证拼音` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.病证 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `病证` DISABLE KEYS */;
/*!40000 ALTER TABLE `病证` ENABLE KEYS */;

-- 导出  表 zy.经验选方 结构
CREATE TABLE IF NOT EXISTS `经验选方` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `方名` varchar(50) DEFAULT NULL,
  `说明` text DEFAULT NULL,
  `经验选方拼音` varchar(50) DEFAULT NULL,
  `单价1` decimal(6,4) DEFAULT NULL,
  `单价2` decimal(6,4) DEFAULT NULL,
  `单价3` decimal(6,4) DEFAULT NULL,
  `单价4` decimal(6,4) DEFAULT NULL,
  `单价5` decimal(6,4) DEFAULT NULL,
  `单价6` decimal(6,4) DEFAULT NULL,
  `单价7` decimal(6,4) DEFAULT NULL,
  `单价8` decimal(6,4) DEFAULT NULL,
  `单价9` decimal(6,4) DEFAULT NULL,
  `单价10` decimal(6,4) DEFAULT NULL,
  `单价11` decimal(6,4) DEFAULT NULL,
  `单价12` decimal(6,4) DEFAULT NULL,
  `单价13` decimal(6,4) DEFAULT NULL,
  `单价14` decimal(6,4) DEFAULT NULL,
  `单价15` decimal(6,4) DEFAULT NULL,
  `单价16` decimal(6,4) DEFAULT NULL,
  `单价17` decimal(6,4) DEFAULT NULL,
  `单价18` decimal(6,4) DEFAULT NULL,
  `单价19` decimal(6,4) DEFAULT NULL,
  `单价20` decimal(6,4) DEFAULT NULL,
  `剂量1` varchar(20) DEFAULT NULL,
  `剂量2` varchar(20) DEFAULT NULL,
  `剂量3` varchar(20) DEFAULT NULL,
  `剂量4` varchar(20) DEFAULT NULL,
  `剂量5` varchar(20) DEFAULT NULL,
  `剂量6` varchar(20) DEFAULT NULL,
  `剂量7` varchar(20) DEFAULT NULL,
  `剂量8` varchar(20) DEFAULT NULL,
  `剂量9` varchar(20) DEFAULT NULL,
  `剂量10` varchar(20) DEFAULT NULL,
  `剂量11` varchar(20) DEFAULT NULL,
  `剂量12` varchar(20) DEFAULT NULL,
  `剂量13` varchar(20) DEFAULT NULL,
  `剂量14` varchar(20) DEFAULT NULL,
  `剂量15` varchar(20) DEFAULT NULL,
  `剂量16` varchar(20) DEFAULT NULL,
  `剂量17` varchar(20) DEFAULT NULL,
  `剂量18` varchar(20) DEFAULT NULL,
  `剂量19` varchar(20) DEFAULT NULL,
  `剂量20` varchar(20) DEFAULT NULL,
  `药物1` varchar(255) DEFAULT NULL,
  `药物2` varchar(255) DEFAULT NULL,
  `药物3` varchar(255) DEFAULT NULL,
  `药物4` varchar(255) DEFAULT NULL,
  `药物5` varchar(255) DEFAULT NULL,
  `药物6` varchar(255) DEFAULT NULL,
  `药物7` varchar(255) DEFAULT NULL,
  `药物8` varchar(255) DEFAULT NULL,
  `药物9` varchar(255) DEFAULT NULL,
  `药物10` varchar(255) DEFAULT NULL,
  `药物11` varchar(255) DEFAULT NULL,
  `药物12` varchar(255) DEFAULT NULL,
  `药物13` varchar(255) DEFAULT NULL,
  `药物14` varchar(255) DEFAULT NULL,
  `药物15` varchar(255) DEFAULT NULL,
  `药物16` varchar(255) DEFAULT NULL,
  `药物17` varchar(255) DEFAULT NULL,
  `药物18` varchar(255) DEFAULT NULL,
  `药物19` varchar(255) DEFAULT NULL,
  `药物20` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.经验选方 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `经验选方` DISABLE KEYS */;
/*!40000 ALTER TABLE `经验选方` ENABLE KEYS */;

-- 导出  表 zy.诊断 结构
CREATE TABLE IF NOT EXISTS `诊断` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `诊断` text DEFAULT NULL,
  `诊断拼音` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=279 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.诊断 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `诊断` DISABLE KEYS */;
/*!40000 ALTER TABLE `诊断` ENABLE KEYS */;

-- 导出  表 zy.辨病选方 结构
CREATE TABLE IF NOT EXISTS `辨病选方` (
  `编号` int(255) NOT NULL AUTO_INCREMENT,
  `方名` varchar(255) DEFAULT NULL,
  `说明` varchar(255) DEFAULT NULL,
  `辨病选方拼音` varchar(255) DEFAULT NULL,
  `单价1` decimal(6,4) DEFAULT NULL,
  `单价2` decimal(6,4) DEFAULT NULL,
  `单价3` decimal(6,4) DEFAULT NULL,
  `单价4` decimal(6,4) DEFAULT NULL,
  `单价5` decimal(6,4) DEFAULT NULL,
  `单价6` decimal(6,4) DEFAULT NULL,
  `单价7` decimal(6,4) DEFAULT NULL,
  `单价8` decimal(6,4) DEFAULT NULL,
  `单价9` decimal(6,4) DEFAULT NULL,
  `单价10` decimal(6,4) DEFAULT NULL,
  `单价11` decimal(6,4) DEFAULT NULL,
  `单价12` decimal(6,4) DEFAULT NULL,
  `单价13` decimal(6,4) DEFAULT NULL,
  `单价14` decimal(6,4) DEFAULT NULL,
  `单价15` decimal(6,4) DEFAULT NULL,
  `单价16` decimal(6,4) DEFAULT NULL,
  `单价17` decimal(6,4) DEFAULT NULL,
  `单价18` decimal(6,4) DEFAULT NULL,
  `单价19` decimal(6,4) DEFAULT NULL,
  `单价20` decimal(6,4) DEFAULT NULL,
  `剂量1` varchar(20) DEFAULT NULL,
  `剂量2` varchar(20) DEFAULT NULL,
  `剂量3` varchar(20) DEFAULT NULL,
  `剂量4` varchar(20) DEFAULT NULL,
  `剂量5` varchar(20) DEFAULT NULL,
  `剂量6` varchar(20) DEFAULT NULL,
  `剂量7` varchar(20) DEFAULT NULL,
  `剂量8` varchar(20) DEFAULT NULL,
  `剂量9` varchar(20) DEFAULT NULL,
  `剂量10` varchar(20) DEFAULT NULL,
  `剂量11` varchar(20) DEFAULT NULL,
  `剂量12` varchar(20) DEFAULT NULL,
  `剂量13` varchar(20) DEFAULT NULL,
  `剂量14` varchar(20) DEFAULT NULL,
  `剂量15` varchar(20) DEFAULT NULL,
  `剂量16` varchar(20) DEFAULT NULL,
  `剂量17` varchar(20) DEFAULT NULL,
  `剂量18` varchar(20) DEFAULT NULL,
  `剂量19` varchar(20) DEFAULT NULL,
  `剂量20` varchar(20) DEFAULT NULL,
  `药物1` varchar(255) DEFAULT NULL,
  `药物2` varchar(255) DEFAULT NULL,
  `药物3` varchar(255) DEFAULT NULL,
  `药物4` varchar(255) DEFAULT NULL,
  `药物5` varchar(255) DEFAULT NULL,
  `药物6` varchar(255) DEFAULT NULL,
  `药物7` varchar(255) DEFAULT NULL,
  `药物8` varchar(255) DEFAULT NULL,
  `药物9` varchar(255) DEFAULT NULL,
  `药物10` varchar(255) DEFAULT NULL,
  `药物11` varchar(255) DEFAULT NULL,
  `药物12` varchar(255) DEFAULT NULL,
  `药物13` varchar(255) DEFAULT NULL,
  `药物14` varchar(255) DEFAULT NULL,
  `药物15` varchar(255) DEFAULT NULL,
  `药物16` varchar(255) DEFAULT NULL,
  `药物17` varchar(255) DEFAULT NULL,
  `药物18` varchar(255) DEFAULT NULL,
  `药物19` varchar(255) DEFAULT NULL,
  `药物20` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=286 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.辨病选方 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `辨病选方` DISABLE KEYS */;
/*!40000 ALTER TABLE `辨病选方` ENABLE KEYS */;

-- 导出  表 zy.辩证 结构
CREATE TABLE IF NOT EXISTS `辩证` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `辩证` text DEFAULT NULL,
  `辩证拼音` varchar(50) DEFAULT NULL,
  `说明` text DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.辩证 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `辩证` DISABLE KEYS */;
/*!40000 ALTER TABLE `辩证` ENABLE KEYS */;

-- 导出  表 zy.针灸 结构
CREATE TABLE IF NOT EXISTS `针灸` (
  `编号` int(11) NOT NULL AUTO_INCREMENT,
  `项目` varchar(255) DEFAULT NULL,
  `价格` decimal(10,2) DEFAULT NULL,
  `项目拼音` varchar(255) DEFAULT NULL,
  `备注` text DEFAULT NULL,
  PRIMARY KEY (`编号`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=696 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci ROW_FORMAT=DYNAMIC;

-- 正在导出表  zy.针灸 的数据：~0 rows (大约)
/*!40000 ALTER TABLE `针灸` DISABLE KEYS */;
/*!40000 ALTER TABLE `针灸` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
