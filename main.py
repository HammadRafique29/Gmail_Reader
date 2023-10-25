from simplegmail import Gmail
from simplegmail.query import construct_query

class GetEmail():
    def __init__(self, client_secret="client_secret.json", token="gmail_token.json", type='offline'):
        self.gmail = Gmail(client_secret_file=client_secret, creds_file=token, access_type=type)
    
    def GetMessageFromParams(self, params):
        try:
            messages = self.gmail.get_messages(query=construct_query(query_params))
            return [ {"To":mes.recipient, "From":mes.sender, "Subject":mes.subject, "Date":mes.date, "Preview":mes.snippet, "Plain":mes.plain} for mes in messages ]
        except Exception as e:
            print(e)     
    
    def GetInboxMessages(self):
        messages = self.gmail.get_unread_inbox()
        return [ {"To":mes.recipient, "From":mes.sender, "Subject":mes.subject, "Date":mes.date, "Preview":mes.snippet, "Plain":mes.plain} for mes in messages ]
    

# Visit https://github.com/jeremyephron/simplegmail for More Details

query_params = {
    "newer_than": (1, "day"),        
    "unread": True,                  
}
data = GetEmail().GetInboxMessages()
for email in data:
    print(email['Preview'])
    


