import requests
data = {
    'postId' : 10,
    'name' : 'yongin',
    'email' : 'yongin1212@dgsw.hs.kr',
    'body' : 'requests practice'
}
#서버에 데이터 전송 
r = requests.post("https://jsonplaceholder.typicode.com/comments", json=data)
print(r.json())

#서버에서 데이터 받기
r2 = requests.get("https://jsonplaceholder.typicode.com/users")
print(r2.json())