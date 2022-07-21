# file metadata gathering
 
If need to RE-build, first remove the running container:
docker rm /cs-hunter-richards-file-metadata 

docker build -t cs-hunter-richards-file-metadata:0.0.1 .

Use a bind mount to extract the csv to the working directory.

docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$pwd,target=/app/deliverable cs-hunter-richards-file-metadata:0.0.1

cat interview.csv
