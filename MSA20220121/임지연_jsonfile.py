# jsonlab06.py 의 with를 모두 try-except로 변경
import json
# 파일 읽어들일 때 s 절대 붙이지 않기
try:
    jsonFile = open("datalab\\mydata.json", "rb") 
    tempData = json.load(jsonFile)
    # tempData = json.loads(jsonFile) # 한 파일 안에서 읽고 쓸 때만 s를 붙임 (ex. 변수 안에서)
    resultData1 = tempData["name"]
    resultData2 = tempData["age"]
    resultData3 = tempData["address"]
    resultData3_1 = tempData["address"][0]
    resultData4 = tempData["email"]
    resultData4_1 = tempData["email"]["id"]
    resultData5 = tempData["empcheck"]
except Exception as error:
    print("에러: " + error)
else:
    jsonFile.close



jsonData1 = { # 파이썬 딕셔너리 안에 리스트가 있는 형테
	"empid" : 12345677,
	"name": "홍길동",
	"info" : [
		{"date" : "2022-01-21", "home" : "서울시"},
		{"dep": "개발", "email": "aaa@aaa.co.kr"}
	]
}

try:
    writeFile = open("datalab\\mydata2.json", "w") 
    json.dump(jsonData1, writeFile)
except Exception as error:
    print("에러: " + error)
else:
    writeFile.close


# 한글 처리o
try:
    writeFile = open("datalab\\mydata3.json", "w", encoding="utf-8") 
    json.dump(jsonData1, writeFile, ensure_ascii=False)
except Exception as error:
    print("에러: " + error)
else:
    writeFile.close



# 들여쓰기o, 한글이 문제가 있음
try:
    writeFile = open("datalab\\mydata4.json", "w") 
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception as error:
    print("에러: " + error)
else:
    writeFile.close
  

    
# 들여쓰기o, 한글 처리o
try:
    writeFile = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4)
except Exception as error:
    print("에러: " + error)
else:
    writeFile.close



temp = 0