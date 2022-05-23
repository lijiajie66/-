import json
from ronglian_sms_sdk import SmsSDK
from celery_tasks.main import celery_app

accId = '8aaf0708802d0d850180449a48a50546'
accToken = 'a45c897a96d64a4481cd1f810c323fc7'
appId = '8aaf0708802d0d850180449a49d6054d'


@celery_app.task(name='send_message')
def send_message(mobile, code, exc_time):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    datas = (code, exc_time//60)
    resp = sdk.sendMessage(tid, mobile, datas)
    resp_info = json.loads(resp).get('statusCode')
    return True if resp_info == '000000' else False
