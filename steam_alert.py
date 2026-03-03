import requests
import os
import sys

def send_msg(text):
  # 깃허브 Secrets에 저장한 값을 불러옴.
  token = os.environ['TELEGRAM_TOKEN']
  chat_id = os.environ['TELEGRAM_CHAT_ID']

def check_steam_free():
  # 스팀 공식 api를 통해 '특별 할인' 중인 게임 가져오기.
  url = "https://store.steampowered.com/api/featuredcategories/?l=korean"
  res = requests.get(url).json()
  # '제한 시간 무료' 또는 '100% 할인' 상품 찾기
  specials = res.get('specials', {}).get('items', [])
  free_games = []

  for game in specials:
    # 가격이 0이거나 할인율이 100%인 경우
    if game.get('discount_percent') == 100 or game.get('final_price') == 0:
      name = game.get('name')
      game_id = game.get('id')
      link = f"https://store.steampowered.com/app/{game_id}"
      free_games.append(f"🎁 *{name}*\n{link}")

  if free_games:
    result_text = "🔥 **스팀 무료 게임** 🔥\n\n" + "\n\n".join(free_games)
    send_msg(result_text)
  else:
    print("현재 무료 게임 없음.")

  """
  msg = "오늘의 스팀 무료 게임 확인하기:\nhttps://store.steampowered.com/search/?maxprice=free&specials=1"
  send_msg(msg)


  # 비밀번호 잘 가져왔는지 확인
  if not token or not chat_id:
    print(f"에러: Secrets 설정을 확인해라. (TOKEN: {bool(token)}, ID: {bool(chat_id)})")
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
"""
  
if __name__ == "__main__":
  check_steam_free()

