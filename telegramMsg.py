import requests
import logging
import json

log = logging.getLogger(__name__)

def sendMessageToGroup(message,silent=True):
    """ Send POST message to group  """
    # your own telegram group/chat id

    chatID          = '<chat_id>'
    bottoken        = '<telegram-bot-token>'

    h={
        'http.useragent' : 'Garden.Poolbot',
        'Content-Type'   : 'application/json',
        'User-Agent'     : 'Pool/Garden',
        'Accept-Encoding': 'gzip'
    }

    url = 'https://api.telegram.org/bot' + bottoken + '/sendMessage'

    payload = {
        'chat_id'                   :   chatID,
        'text'                      :   message,
        'disable_notification'      :   str(silent),
        'parse_mode'                :   'Markdown',
        'disable_web_page_preview'  :   'False'
    }

    log.debug("Data = {}".format(payload))

    try:
        r = requests.post(url, headers=h, json = payload, timeout=30)
        log.debug("Sending POST request to {}: request url = {}".format(url,r.url))
    except Exception as e:
        log.error('Error Connecting to telegram server: {}'.format(e))
        return False

    if r.status_code == 200: #200 = 'OK'
        log.debug("Message sent to group: {}".format(message))
        response = r.json()
        messageID = response.get('result').get('message_id')
        log.debug("Request returned {}, len = {}".format(response, len(response)))
        log.info("Sent message has ID = {}".format(messageID))
        return messageID
    else:
        log.error ("Error sending message to group: {}".format(r.status_code))
        if r.json():
            log.info("Description: {}".format(r.json()))
