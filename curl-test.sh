#!/bin/bash

curl -X Post http://127.0.0.1:5000/api/timeline_post -d 'name=Test&email=test@test.com&content=Testing my endpoints.'
curl http://127.0.0.1:5000/api/timeline_post 
curl -X DELETE http://127.0.0.1:5000/api/timeline_post/0
curl http://127.0.0.1:5000/api/timeline_post 