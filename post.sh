
read -p "Enter Your Roll No: "  roll

curl --header "Content-Type: application/json"  --request POST  --data '{"rollno":"'$roll'"}'  http://localhost:8080/coins