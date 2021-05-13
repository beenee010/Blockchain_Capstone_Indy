# Indy-API

	cd start_docker
	docker build -t client_docker .

	docker images # 제대로 이미지가 만들어 졌는지 확인

	sh ./client_start.sh "docker_image"

	docker ps # 도커 컨테이너가 제대로 실행이 되었는지 확인
### did 발급
	sh ./sh_generate_did.sh "CONTAINER_ID 또는 NAME" "Wallet ID" "Wallet Verkey"   # 도커 컨테이너에 접근하여 원격으로 DID를 발급받고 해당 결과를 텍스트 파일로 리턴
- did를 발급받기 위한 sh 스크립트 파일
- api.sh --> sh_generate_did.sh 파일명 변경

### did 재발급 (가져오기)
	sh ./sh_get_did.sh "CONTAINER_ID 또는 NAME" "Wallet ID" "Wallet Verkey"
- did를 가져오기 위한 sh 스크립트 파일
- json형태로 로컬에 복사됨 (경로는 /home/deploy)
- json을 확인하면 "did" 키를 사용하여 value 받아오기

### Dockerfile 수정
- 기존 코드와 모두 동일하고, get_did.py 파일 ADD 커맨드 추가 (오류가 있다면 파일명 오류)
