# Indy-API
```
cd start_docker
docker build -t client_docker

docker images # 제대로 이미지가 만들어 졌는지 확인

sh ./client_start.sh "docker_image"

docker ps # 도커 컨테이너가 제대로 실행이 되었는지 확인

sh ./api.sh "CONTAINER_ID 또는 NAME" "이메일 해시값"   # 도커 컨테이너에 접근하여 원격으로 DID를 발급받고 해당 결과를 텍스트 파일로 리턴
```
