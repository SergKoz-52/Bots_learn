import requests
import time

from src.conf import GenConf

BOT_CONF = GenConf('spk1bot')
API_URL: str = 'https://api.telegram.org/bot'
API_CATS_URL: str = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN: str = BOT_CONF.token
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('

offset: int = -2
counter: int = 0
cat_response: requests.Response
cat_link: str

while counter < 10:
    print('attempt =', counter)
    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?'
                    f'chat_id={chat_id}&photo={cat_link}'
                )
            else:
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendMess'
                    f'age?chat_id={chat_id}&text={ERROR_TEXT}'
                )

    time.sleep(1)
    counter += 1
