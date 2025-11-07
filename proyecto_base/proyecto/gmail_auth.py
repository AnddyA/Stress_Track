from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

# Scopes de Gmail: enviar correos
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials/credentials.json', SCOPES)
    creds = flow.run_local_server(port=8080)
    with open('credentials/token.pickle', 'wb') as token:
        pickle.dump(creds, token)
    print("✅ Token generado y guardado.")

if __name__ == '__main__':
    main()
