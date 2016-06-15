from azure.storage.queue import QueueService
import json

class TimeLineWorker:

    QUEUE_KEY = ''
    ACCOUNT_NAME = ''
    QUEUE_NAME = ''

    def __init__(self):
        self.queue_service = QueueService(account_name=TimeLineWorker.ACCOUNT_NAME, 
                                          account_key=TimeLineWorker.QUEUE_KEY)

    def insert_message(self):
        obj = {
            "message": "test message",
            "other_key": 10
        }
        message = unicode(json.dumps(obj))
        self.queue_service.put_message(TimeLineWorker.QUEUE_NAME, message)

    def get_next_message(self):
        messages = self.queue_service.get_messages(TimeLineWorker.QUEUE_NAME)
        for message in messages:
            print message.content
            self.queue_service.delete_message(TimeLineWorker.QUEUE_NAME, message.id, message.pop_receipt)


if __name__ == '__main__':
    timeline_worker = TimeLineWorker()
    print "Insert message"
    timeline_worker.insert_message()
    print "Get message "
    timeline_worker.get_next_message()
    print "Insert new message but not get after"
    timeline_worker.insert_message()
