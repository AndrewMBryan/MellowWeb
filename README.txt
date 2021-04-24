

Welcome to our Mellow Flow Capstone Project!

This document is for understanding the elements and files within our Project

1. In the Other Stuff folder there are 3 Items
  a. Google folder
    The Google folder is a implementation of the google places API
    This project helps to get potenial leads for mellow flow
    *I ask that you do not run national companies due to the cost of the api*

  b. Mellow Flow App folder
    The MellowFlowApp folder is a python project that implements autoposting
    This is done though the use of selenium and chromeweb drivers

  c. Sql.sql
    Sql.sql is the schema for the database we are using for the website

2. The Twillio Folder
  twillio is what we used to implement browser to phone calling
  as of right now this does not work on our free hosted website
  the cause of this is the website is using http, not https
  http does not support webRTC while https does support webRTC
  In order to bypass this issue for testing please download
  a WAMP or XAMPP and navigate to the folder using your browser
  localhost/MellowWeb/twillio/
  please call 6179990005 for testing as this is currently the only approved number

3. The Mellow Flow Advertising Website
  a. Our Demo website can be asscessed at http://mellowweb.byethost5.com/
  b. To test the login feature use the credentials Username:davieboy Password:123 for our pretend employee famed actor and comedian David Spade
  c. The only data in the database connected to the website is test data that we used to verify behavior, to test the databasequery.php you must first type the table you want to query (leads and customers) then type the query itself for example (idcustomers = 1 or leadname = 'test') it is important that you use the single quotes for string values. 
  
