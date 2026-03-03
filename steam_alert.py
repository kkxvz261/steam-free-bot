import requests
import os

def send_msg(text):
  # 깃허브 Secrets에 저장한 값을 불러옴.
  token = os.environ['TELEGRAM_TOKEN']
  chat_id = os.environ['TELEGRAM_CHAT_ID']
  url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id{chat_id}&text={text}"
  requests.get(url)

# 나중에 여기에 진짜 크롤링 코드를 넣을 수 있음. 
test_message = "✅ 깃허브 알리미가 성공적으로 설치됨\n이제 매일 무료 게임 소식을 확인."
send_msg(test_message)
