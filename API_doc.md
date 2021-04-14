# API Document
## Index
* [Users](#users-title)
  + [/users](#users-sub-title)
    - [[POST] 회원가입](#post-users)
  + [/auth](#auth-sub-title)
    - [[POST] Login](#post-auth)
* [Files](#files-title)
  + [/files](#files-sub-title)
    - [[POST] file upload](#post-files)
  + [/files/<file_id>](#files-fileid-sub-title)
    - [[GET] file download](#get-files)
    - [[DELETE] file delete](#delete-files)
* [Config](#config-title)
  + [/ping](#ping-sub-title)
    - [[GET] for health check](#get-ping)

## Users <a id="users-title"></a>
### /users <a id="users-sub-title"></a>
#### [POST] register user <a id="post-users"></a>
새 계정을 생성합니다.

* Body

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|username|None|사용자 아이디|formData|string|true|
|password|None|사용자 비밀번호|formData|SHA256 encrypted string|true|

* Response (status code: 200)
```json
{
  "new_user": 1
}
```

* Example

```commandline
curl -X "POST" "https://upload-now-box.cf/users" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "username": "firstuser",
  "password": "20504cdfddaad0b590ca53c4861edd4f5f5cf9c348c38295bd2dbf0e91bca4c3"
}'
```

### /auth <a id="auth-sub-title"></a>
#### [POST] Login <a id="post-auth"></a>
Login API 입니다. access_token으로 JWT token을 반환합니다.

* Body

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|username|None|사용자 아이디|formData|string|true|
|password|None|사용자 비밀번호|formData|SHA256 encrypted string|true|

* Response (status code: 200)
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQwODExNiwianRpIjoiMWQ4ZmIxNjAtNDQ3My00ZDJlLTg1NDItNzNlZjBjNTFiM2FmIiwibmJmIjoxNjE4NDA4MTE2LCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjQsImV4cCI6MTYxOTAxMjkxNiwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjI6NDc6NTUifQ.gqOjDBVegv-jACs8n1AK2BZdL2D_Ueu2-qsYLA5RAtQ"
}
```

* Exception

  + "User not found": username에 해당하는 유저가 존재하지 않을 경우
  + "Password error": password 검증에 실패할 경우

* Example
```commandline
curl -X "POST" "https://upload-now-box.cf/auth" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "username": "firstuser2",
  "password": "20504cdfddaad0b590ca53c4861edd4f5f5cf9c348c38295bd2dbf0e91bca4c3"
}'
```

## Files <a id="files-title"></a>
### /files <a id="files-sub-title"></a>
#### [POST] file upload <a id="post-files"></a>

* Body
  
|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file|None|file for upload|formData|multipart|true|

* Response (status code: 200)
```json
{
  "file_id": 5
}
```

* Example
```commandline
curl -X "POST" "https://upload-now-box.cf/files" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQxMDU3MSwianRpIjoiMjM2MmI5YzgtZjc1OS00NDAxLTljNTQtZWEyYWYxNTkwMzk3IiwibmJmIjoxNjE4NDEwNTcxLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImV4cCI6MTYxOTAxNTM3MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjM6Mjk6MjcifQ.-rFVaVoap2UsfC8QrltNE32qZfGEpcbZzHf-SBpe1hk' \
     -H 'Content-Type: multipart/form-data; charset=utf-8; boundary=__X_PAW_BOUNDARY__' \
     -F "file="
```

### /files/<file_id> <a id="files-fileid-sub-title"></a>
#### [GET] file download <a id="get-files"></a>
* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file_id|None|file_id for download|path|integer|true|

* Response (status code: 200)
  + file

* Example
```commandline
curl "https://upload-now-box.cf/files/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQxMDU3MSwianRpIjoiMjM2MmI5YzgtZjc1OS00NDAxLTljNTQtZWEyYWYxNTkwMzk3IiwibmJmIjoxNjE4NDEwNTcxLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImV4cCI6MTYxOTAxNTM3MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjM6Mjk6MjcifQ.-rFVaVoap2UsfC8QrltNE32qZfGEpcbZzHf-SBpe1hk'
```

#### [DELETE] file delete <a id="delete-files"></a>
* Parameter

|Parameter|Default value|Description|Param type|Data type|Required|
|---|---|---|---|---|---|
|file_id|None|file_id for download|path|integer|true|

* Response (status code: 200)
```json
{
  "success": true
}
```

* Example
```commandline
curl -X "DELETE" "https://upload-now-box.cf/files/2" \
     -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxODQxMDU3MSwianRpIjoiMjM2MmI5YzgtZjc1OS00NDAxLTljNTQtZWEyYWYxNTkwMzk3IiwibmJmIjoxNjE4NDEwNTcxLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjEsImV4cCI6MTYxOTAxNTM3MSwiY3JlYXRlZF9hdCI6IjIwMjEtMDQtMTRUMjM6Mjk6MjcifQ.-rFVaVoap2UsfC8QrltNE32qZfGEpcbZzHf-SBpe1hk'
```

## Config <a id="config-title"></a>
### /ping <a id="ping-sub-title"></a>
#### [GET] for health check <a id="get-ping"></a>
* Response (status code: 200)
```json
{
  "result": "pong"
}
```

* Example
```commandline
curl "https://upload-now-box.cf/ping"
```
