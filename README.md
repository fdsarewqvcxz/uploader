# Cloud Storage with Flask
Cloud Storage API 입니다.

Nginx, Flask, MySQL, Docker를 사용하였습니다.

## API demo URI
https://upload-now-box.cf

## Installation
```commandline
git clone https://github.com/fdsarewqvcxz/uploader.git
pip install -r ./uploader/uploader/requirements.txt
```

+ `uploader/data/nginx/app.conf` file의 domain을 수정

+ `uploader/uploader/utils/` 하위에 secret.json 생성 후 아래 내용을 입력
```json
{
  "secret_key": "server secret key",
  "database_uri": "database uri",
  "aws_access_key_id": "access key id",
  "aws_secret_access_key": "secret access key"
}
```

+ `init-letsencrypt.sh`과 `run-uploader.sh`를 차례로 실행

## [API Document](API_doc.md)

## References
+ https://pentacent.medium.com/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71
