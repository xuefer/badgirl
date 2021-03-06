-- MySQL dump 8.21
--
-- Host: localhost    Database: moobot
-- -------------------------------------------------------
-- Server version	3.23.49-log

--
-- Table structure for table 'alias'
--

CREATE TABLE alias (
  nick varchar(31) NOT NULL default '',
  realnick varchar(31) NOT NULL default '',
  type varchar(20) NOT NULL default '',
  UNIQUE KEY nick (nick)
) TYPE=MyISAM;

--
-- Table structure for table 'aliasregex'
--

CREATE TABLE aliasregex (
  regex varchar(64) NOT NULL default '',
  realnick varchar(31) NOT NULL default '',
  UNIQUE KEY regex (regex)
) TYPE=MyISAM;

--
-- Table structure for table 'data'
--

CREATE TABLE data (
  data varchar(128) NOT NULL default '',
  type varchar(20) NOT NULL default '',
  created_by varchar(100) default NULL,
  PRIMARY KEY  (data,type)
) TYPE=MyISAM;

--
-- Table structure for table 'factoids'
--

CREATE TABLE factoids (
  factoid_key varchar(64) NOT NULL default '',
  requested_by varchar(150) default NULL,
  requested_time decimal(11,0) default NULL,
  requested_count int(11) default NULL,
  created_by varchar(150) default NULL,
  created_time decimal(11,0) default NULL,
  modified_by varchar(150) default NULL,
  modified_time decimal(11,0) default NULL,
  locked_by varchar(64) default NULL,
  locked_time decimal(11,0) default NULL,
  factoid_value text,
  PRIMARY KEY  (factoid_key)
) TYPE=MyISAM;

CREATE TABLE IF NOT EXISTS `factoidlink` (
  `linkfrom` varchar(64) NOT NULL,
  `linkto` varchar(64) NOT NULL,
  `linktype` varchar(64) NOT NULL,
  `created_by` varchar(150) NOT NULL,
  `created_time` decimal(11,0) NOT NULL,
  `weight` decimal(4,0) NOT NULL,
  PRIMARY KEY  (`linkfrom`,`linkto`),
  KEY `linkto` (`linkto`(4)),
  KEY `linktype` (`linktype`(4))
) TYPE=MyISAM;

--
-- Table structure for table 'grants'
--

CREATE TABLE grants (
  hostmask varchar(100) NOT NULL default '',
  priv_type varchar(20) NOT NULL default '',
  PRIMARY KEY  (hostmask,priv_type)
) TYPE=MyISAM;

--
-- Table structure for table 'poll'
--

CREATE TABLE poll (
  question text,
  poll_num int(11) NOT NULL auto_increment,
  PRIMARY KEY  (poll_num)
) TYPE=MyISAM;

--
-- Table structure for table 'poll_options'
--

CREATE TABLE poll_options (
  poll_num int(11) NOT NULL default '0',
  option_key varchar(20) NOT NULL default '',
  option_text varchar(80) default NULL,
  PRIMARY KEY  (poll_num,option_key)
) TYPE=MyISAM;

--
-- Table structure for table 'poll_votes'
--

CREATE TABLE poll_votes (
  voter_nickmask varchar(128) NOT NULL default '',
  option_key varchar(20) NOT NULL default '',
  poll_num int(11) NOT NULL default '0',
  PRIMARY KEY  (voter_nickmask,option_key,poll_num)
) TYPE=MyISAM;

--
-- Table structure for table 'seen'
--

CREATE TABLE seen (
  nickid int(10) unsigned NOT NULL auto_increment,
  nick varchar(31) NOT NULL default '',
  hostmask varchar(150) default NULL,
  time decimal(11,0) default NULL,
  message text,
  type varchar(20) NOT NULL default '',
  PRIMARY KEY  (nickid)
  UNIQUE KEY nick (nick)
) TYPE=MyISAM;

--
-- Table structure for table 'stats'
--

CREATE TABLE stats (
  nick varchar(31) NOT NULL default '',
  type varchar(20) NOT NULL default '',
  counter double default NULL,
  PRIMARY KEY  (nick,type)
) TYPE=MyISAM;

--
-- Table structure for table 'webstats'
--

CREATE TABLE webstats (
  nick varchar(255) NOT NULL default '',
  count decimal(10,0) NOT NULL default '0',
  quote text,
  quote_time decimal(11,0) default NULL,
  channel varchar(255) default NULL,
  type varchar(30) default 'privmsg'
) TYPE=MyISAM;

--
-- Table structure for table 'urls'
--

CREATE TABLE IF NOT EXISTS `url` (
  `nick` varchar(64) NOT NULL,
  `time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
  `string` text NOT NULL,
  `url_id` int(11) NOT NULL auto_increment,
  `url` varchar(256) NOT NULL default '',
  `url_hash` varbinary(32) NOT NULL default '',
  `title` varchar(256) NOT NULL default '',
  `hostid` int(10) unsigned NOT NULL,
  `nickid` int(10) unsigned NOT NULL,
  PRIMARY KEY  (`url_id`),
  KEY `url_hash` (`url_hash`(4))
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS `urlhost` (
  `hostid` int(10) unsigned NOT NULL auto_increment,
  `host` varchar(64) NOT NULL,
  `scheme` enum('http','https') NOT NULL,
  `port` smallint(5) unsigned NOT NULL,
  PRIMARY KEY  (`hostid`),
  UNIQUE KEY `host` (`host`,`scheme`,`port`)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS `ability` (
  `abilityid` smallint(5) unsigned NOT NULL auto_increment,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY  (`abilityid`)
) ENGINE=MyISAM;

CREATE TABLE IF NOT EXISTS `userability` (
  `nick` varchar(30) NOT NULL,
  `abilityid` smallint(6) unsigned NOT NULL,
  `channel` varchar(32) NOT NULL,
  `score` smallint(5) unsigned NOT NULL,
  `bynick` varchar(30) NOT NULL,
  PRIMARY KEY  (`nick`,`channel`,`abilityid`),
  KEY `channel` (`channel`(3))
) ENGINE=MyISAM;

-- used by ims module
CREATE TABLE `birthday` (
  `nick` varchar(20) NOT NULL default '',
  `birthday` date NOT NULL default '0000-00-00',
  PRIMARY KEY  (`nick`)
) ENGINE=MyISAM;

CREATE TABLE bottime (
  nick varchar(30) NOT NULL,
  tz_offset smallint(3) NOT NULL DEFAULT 0,
  PRIMARY KEY (nick)
);
