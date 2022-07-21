# file metadata gathering
 
If need to RE-build, first remove the running container:
docker rm /cs-hunter-richards-file-metadata 
 
docker build -t cs-hunter-richards-file-metadata-image .

docker run --name cs-hunter-richards-file-metadata cs-hunter-richards-file-metadata-image:latest



To extract the CSV file...

Option 1 - docker cp method:
docker cp cs-hunter-richards-file-metadata:/app/interview.csv .
cat interview.csv

Option 2 - use a bind mount.
docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$pwd,target=/app/deliverable cs-hunter-richards-file-metadata-image:latest
