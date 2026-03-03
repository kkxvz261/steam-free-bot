import requests
import os
import sys

def send_msg(text):
  # 깃허브 Secrets에 저장한 값을 불러옴.
  token = os.environ['TELEGRAM_TOKEN']
  chat_id = os.environ['TELEGRAM_CHAT_ID']

  # 비밀번호 잘 가져왔는지 확인
  if not token or not chat_id:
    printf(f"에러: Secrets 설정을 확인해라. (TOKEN: {bool(token)}, ID: {bool(chat_id)})")
    return
    
  url = f"https://api.telegram.org/bot{token}/sendMessage"
  payload = {'chat_id': chat_id, 'text': text}

  response = requests.post(url, data=payload)

  if response.status_code == 200:
    print("✅ 텔레그램 전송 성공")
  else:
    print(f"❌ 전송 실패. 에러 코드: {response.status_code}")
    print(f"메시지: {response.text}")

if __name__ == "__main__":
  send_msg("방금 코드를 수정. 성공.")

# 나중에 여기에 진짜 크롤링 코드를 넣을 수 있음. 
test_message = "✅ 깃허브 알리미가 성공적으로 설치됨\n이제 매일 무료 게임 소식을 확인."
send_msg(test_message)
