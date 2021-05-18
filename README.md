# simpleWebServer
Summer Project 2021

Ignore the junk folder it is a archive i made while messing with flask

It is made in Flask Python

`db.json` is our json data where all roll of Y18,19,20 is kinnda mentioned and more.  
Eg:
 ```[
  {
    "coins": 444, 
    "roll": "180001"
  }, 
  {
    "coins": 452, 
    "roll": "180002"
  }, 
  {
    "coins": 665, 
    "roll": "180003"
... 
```

`rollCoin.py` will randamize values of coins in `db.json`

Finally, the main file `coins.py` it's easy to understand just run the file the home page is quite obvious.  

you can do either of follwoing:  
- To view the entire list of database:
- To see Number of coins to a roll number:

it is on port 8080.

you can also serach by using `localhost:8080/coins?rollno=<roll no.>`  

or using `curl --header "Content-Type: application/json"  --request POST  --data '{"rollno":"'$roll'"}'  http://localhost:8080/coins`

or simple use `post.sh` it will prompt for roll no
