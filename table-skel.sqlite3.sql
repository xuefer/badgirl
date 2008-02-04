CREATE TABLE alias (
  nick TEXT NOT NULL DEFAULT '',
  realnick TEXT NOT NULL default '',
  type TEXT NOT NULL default '',
  UNIQUE (nick)
) ;


CREATE TABLE aliasregex (
  regex TEXT NOT NULL default '',
  realnick TEXT NOT NULL default '',
  UNIQUE (regex)
) ;


CREATE TABLE data (
  data TEXT NOT NULL default '',
  type TEXT NOT NULL default '',
  created_by TEXT default NULL,
  PRIMARY KEY (data,type)
) ;


CREATE TABLE factoids (
  factoid_key TEXT NOT NULL default '',
  requested_by TEXT default NULL,
  requested_time NUMBERIC default NULL,
  requested_count INTEGER default NULL,
  created_by TEXT default NULL,
  created_time NUMBERIC default NULL,
  modified_by TEXT default NULL,
  modified_time NUMBERIC default NULL,
  locked_by TEXT default NULL,
  locked_time NUMBERIC default NULL,
  factoid_value text,
  PRIMARY KEY (factoid_key)
) ;


CREATE TABLE grants (
  hostmask TEXT NOT NULL default '',
  priv_type TEXT NOT NULL default '',
  PRIMARY KEY (hostmask,priv_type)
) ;


CREATE TABLE poll (
  question text,
  poll_num INTEGER PRIMARY KEY
) ;


CREATE TABLE poll_options (
  poll_num INTEGER NOT NULL default '0',
  option_key TEXT NOT NULL default '',
  option_text TEXT default NULL,
  PRIMARY KEY (poll_num,option_key)
) ;


CREATE TABLE poll_votes (
  voter_nickmask TEXT NOT NULL default '',
  option_key TEXT NOT NULL default '',
  poll_num INTEGER NOT NULL default '0',
  PRIMARY KEY (voter_nickmask,option_key,poll_num)
) ;


CREATE TABLE seen (
  nick TEXT NOT NULL default '',
  hostmask TEXT default NULL,
  time NUMBERIC default NULL,
  message text,
  type TEXT NOT NULL default '',
  PRIMARY KEY (nick)
) ;


CREATE TABLE stats (
  nick TEXT NOT NULL default '',
  type TEXT NOT NULL default '',
  counter NUMBERIC default NULL,
  PRIMARY KEY (nick,type)
) ;


CREATE TABLE webstats (
  nick TEXT NOT NULL default '',
  count NUMBERIC NOT NULL default '0',
  quote TEXT,
  quote_time NUMBERIC default NULL,
  channel TEXT default NULL,
  type TEXT default 'privmsg'
) ;


CREATE TABLE url (
  nick TEXT NOT NULL,
  time TEXT NOT NULL,
  string TEXT NOT NULL,
  url_id INTEGER PRIMARY KEY
) ;

CREATE TABLE IF NOT EXISTS ability (
  abilityid INTEGER PRIMARY KEY,
  name TEXT NOT NULL
) ;

CREATE TABLE IF NOT EXISTS userability (
  nick TEXT NOT NULL,
  abilityid INTEGER NOT NULL,
  channel TEXT NOT NULL,
  score INTEGER NOT NULL,
  bynick TEXT NOT NULL,
  PRIMARY KEY (nick,channel,abilityid),
  UNIQUE (channel)
) ;

CREATE TABLE birthday (
  nick TEXT NOT NULL default '',
  birthday TEXT NOT NULL default '0000-00-00',
  PRIMARY KEY (nick)
) ;

