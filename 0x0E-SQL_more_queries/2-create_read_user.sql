-- Creates a database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE user IF NOT EXISTS user_0d_2@localhost;
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
 