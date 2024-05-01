#Wehelp 

Task 2 

●Create a new database named website

<img width="1174" alt="Screenshot 2024-05-01 at 11 46 57" src="https://github.com/twkclaire/WeHelpProjects/assets/163644958/6bbe2461-d1ad-42ea-8903-973e5cf00e3d">

●Create a new table named member, in the website database
![Screenshot 2024-05-01 at 12 02 45](https://github.com/twkclaire/WeHelpProjects/assets/163644958/e95f45b2-ffe3-4231-b2d0-d9b682124766)


Task 3

● INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
![Screenshot 2024-05-01 at 12 07 46](https://github.com/twkclaire/WeHelpProjects/assets/163644958/8a368bdf-892c-4255-9f57-6e170c463988)




● SELECT all rows from the member table.
![Screenshot 2024-05-01 at 12 08 18](https://github.com/twkclaire/WeHelpProjects/assets/163644958/01871327-d032-4e78-b3e1-3fc6c765847a)




● SELECT all rows from the member table, in descending order of time.
![Screenshot 2024-05-01 at 12 08 35](https://github.com/twkclaire/WeHelpProjects/assets/163644958/6055b03a-52fc-4b8e-83e1-8ee8bfafd54a)




● SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
![Screenshot 2024-05-01 at 12 08 56](https://github.com/twkclaire/WeHelpProjects/assets/163644958/992e2de7-7645-48c9-8cea-54d4a849910a)





● SELECT rows where username equals to test.
![Screenshot 2024-05-01 at 12 09 50](https://github.com/twkclaire/WeHelpProjects/assets/163644958/d6cf952b-419a-4daa-929a-08f2db351cb0)






● SELECT rows where name includes the es keyword.
![Screenshot 2024-05-01 at 12 10 17](https://github.com/twkclaire/WeHelpProjects/assets/163644958/990a7ea7-c28f-491f-8176-27316038682b)







● SELECT rows where both username and password equal to test.
![Screenshot 2024-05-01 at 12 10 40](https://github.com/twkclaire/WeHelpProjects/assets/163644958/80534dbb-8dea-4234-b24e-69050037aaa7)







● UPDATE data in name column to test2 where username equals to test.
![Screenshot 2024-05-01 at 12 11 07](https://github.com/twkclaire/WeHelpProjects/assets/163644958/35fccb08-26e9-4bcd-8469-e43e6be9986a)









Task 4

● SELECT how many rows from the member table.
![Screenshot 2024-05-01 at 12 18 12](https://github.com/twkclaire/WeHelpProjects/assets/163644958/f261f748-75f7-450c-b449-25de280b6714)


● SELECT the sum of follower_count of all the rows from the member table.
![Screenshot 2024-05-01 at 12 18 36](https://github.com/twkclaire/WeHelpProjects/assets/163644958/f634406f-49f4-482d-8f5a-ab98a68c486c)



● SELECT the average of follower_count of all the rows from the member table.
![Screenshot 2024-05-01 at 12 18 53](https://github.com/twkclaire/WeHelpProjects/assets/163644958/cc0a0392-e091-4afc-b97f-4d8884390108)



● SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
![Screenshot 2024-05-01 at 12 19 09](https://github.com/twkclaire/WeHelpProjects/assets/163644958/90e11555-43d4-44ac-b454-169eab098b01)




Task5 
● Create a new table named message, in the website database.
![Screenshot 2024-05-01 at 12 24 26](https://github.com/twkclaire/WeHelpProjects/assets/163644958/c79d9ba0-f3e4-41bf-80bb-5948637ffa96)

Insert arbitrary data which will be later used to join member table
![Screenshot 2024-05-01 at 12 25 06](https://github.com/twkclaire/WeHelpProjects/assets/163644958/6e46d566-ed1e-4479-a858-a0f9e49649f0)


● SELECT all messages, including sender names. We have to JOIN the member table to get that.
![Screenshot 2024-05-01 at 12 27 14](https://github.com/twkclaire/WeHelpProjects/assets/163644958/41e22519-602e-422a-8986-429692b84329)


● SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
![Screenshot 2024-05-01 at 12 29 48](https://github.com/twkclaire/WeHelpProjects/assets/163644958/f4960bf7-d789-4371-88ed-ce56dd8ae644)




● Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
● Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
