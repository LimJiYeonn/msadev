# 위탁의료기관 조회서비스
# pip install flask 설치 진행
# API요청 할 pip install 

from flask import Flask #, request
import json
import requests # 별도의 모듈이니까 설치 필요

# 변수 선언 - 프로그램의 이름 저장하는 변수 (파일 이름 저장 변수)
# app 개발 또는 application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작, 기본 값은 = app.py 파일을 생성

# if __name__ == "__main__": 나중에 접근 할 것이다. 

# 함수 선언
# 시작할 때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로 지정 - 앞에서 선언한 app 변수를 사용    # route 어트리뷰트 신호, flask의 규칙
def FlaskLab(): # 요청 - 메서드(함수) 이름 요청에서 사용하는 것 
    return "Flask 데이터 응답" # 응답 - return 에서 돌려주는 데이터가 응답


@app.route("/data1")
def FlaskData(): #startPage, pageCount, address): # 요청 받음
    keyValue = r"Kfmb8V7kr4%2F2NQMjEhJR%2BzKjZHBL6rGCk2oLifgAOsamsyHp9WKyHh6UjRJoeT23cIHDuCWfMUxnHeAF1Qrhsw%3D%3D" 
    address = r"%5BorgZipaddr%3A%3ALIKE%5D=%EC%84%B1%EB%B6%81%EA%B5%AC"  

    dataURL = "http://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond" + address # 또는 본인 사는 지역구
    dataURL += "&serviceKey=" + keyValue
    
    # http://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10&cond%5BorgZipaddr%3A%3ALIKE%5D=%EC%84%B1%EB%B6%81%EA%B5%AC&serviceKey=Kfmb8V7kr4%2F2NQMjEhJR%2BzKjZHBL6rGCk2oLifgAOsamsyHp9WKyHh6UjRJoeT23cIHDuCWfMUxnHeAF1Qrhsw%3D%3D
    
    # http://api.odcloud.kr/api/apnmOrg/v1/list?page=1&perPage=10&cond%5BorgZipaddr%3A%3ALIKE%5D=%EC%84%B1%EB%B6%81%EA%B5%AC&serviceKey=Kfmb8V7kr4%2F2NQMjEhJR%2BzKjZHBL6rGCk2oLifgAOsamsyHp9WKyHh6UjRJoeT23cIHDuCWfMUxnHeAF1Qrhsw%3D%3D
    dataResult = requests.get(dataURL)
    #공공데이터 요청 후 데이터 받기 : flask - request / requests 기능 사용"

    result = json.loads(dataResult)
    return result # 공공데이터 결과 값 응답