# Indy-API

	cd start_docker
	docker build -t client_docker .

	docker images # 제대로 이미지가 만들어 졌는지 확인

	sh ./client_start.sh "docker_image"

	docker ps # 도커 컨테이너가 제대로 실행이 되었는지 확인
### did 발급
	sh ./sh_generate_did.sh "CONTAINER_ID 또는 NAME" "Wallet ID" "Wallet Verkey"   # 도커 컨테이너에 접근하여 원격으로 DID를 발급받고 해당 결과를 텍스트 파일로 리턴

### did 재발급 (가져오기)
	sh ./sh_get_did.sh "CONTAINER_ID 또는 NAME" "Wallet ID" "Wallet Verkey"
