# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request
# FLASK = = = = = = = = = = = 

# CRED = = = = = = = = = = =
import googleapiclient.discovery
from google.oauth2 import service_account as google_oauth2_service_account
# CRED = = = = = = = = = = =

# QUICKSTART = = = = = = = = = = =
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# QUICKSTART = = = = = = = = = = =

# Flask app should start in global layout
app = flask.Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


@app.route('/authentication')
def authentication():
    creds = google_oauth2_service_account.Credentials.from_service_account_info(
        {
            "type": "service_account",
            "project_id": "my-project-90818-learn-hun",
            "private_key_id": "cf8bd4105633c3cac528d1c8c4c66cc3b825e837",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeQrDkS5Rq/khX\nNoU01bLEbZHj/JjzwlcozMB0uRP+H9NYJytYrl4+vqhi3+EApY+bKpU/iB/A9tPC\nVIYjhXeACCXtNq6sz8hQDN6y+cKW5K4i2yd1xpeIlAXjo4M/uRIarlffgEi3MOAX\nRtTDskXvECuu2rXsIbgQEBzpCwJQhaVWnOHk4ONTJnEKSjvtuHXRZUc6GrabLrLU\nb4h1nDYh8+IVoUxpcZg0sW9XWpXw2O3kh8o6ADy4aH2KB9Sv4yktLLNcVWrqisei\nekA93NnWji5pG2DKuqjrmaZGA9SwOA5gT34EfrbL8zVFaEGgV7yp5ytrTg5vmtaw\nP36j58iJAgMBAAECggEAG5iV900NjYWXECwX2LFtuW5AuwBEHHc2Ew12/rN6Hr0m\ncW/tEUrgcLD2tD0FI0N7UcuAWGJwZQm1PaTW+hEvGAJzuJQpK8WUkI7Z81v1WDH6\ngmX0EMenC0ACceIEhCNNmpztgjHAnD73yF9HwPMQWkIX1+bXw5vSmGxy2hkbF3ac\nKehAlVB584QC8L191WtWPpx27pdNy2ncnlW6Xaail8NtGlCELLGrmicQUjgxZhsU\ngEZh/ZrTYm4ion5mWCYtbSvuXN++9Zy6kIdpYiFOroQuEr48L6l0KLmVvNsuZ1D0\nk4xdXJxtx0kacGr0tyg1VV3vut14vcSlDqbeDUy7DQKBgQC/5LuQVTJT3FiJ13sb\nCyJIuFVQAX2p1+TXsiKJh9Copaua0tvXygJtbGFEVmYKS3VwiC8OyESQQhATFORE\nYZYpek0UwhNggekg+asiMMSnPc/hHkxQdsxmT34sfmuooSeDvqrVPw6BW3i7Hb6Q\nB7lfydH+v6VejPKWm2q7sm6UpQKBgQDTIZJ/rdgknqnIENgcHwRJoKS3j2RcCvnK\nu0pXoumA9xq1/JFOCuGmRnscyga0d17fYGpER3iR5NL2YAksMSUEDyj+yFupHyfS\nTZzVVaeYNW3OKjDXwUDGYh2D3JkF7P6zeC9LLBkvwuhllvwC1URewWARBpreVGpH\nuZGRo6CLFQKBgHnO9yTif+TtzSIKr3F2OtgQcs8rcxpaGkC1KelFVjWHnIvV54lu\nCOZu0rtvYKyOQ8kgGUb351XvKYcDTvb9PzWrFbzkiSpMrLCq62/zpxFGUmvjMKwv\nDQaw1TXnNe3ABnZBlO1yboG8j8GvWuTQkmJ0mSFtg8qmC+OAWls1I66lAoGAZCvL\njBR5Nnao6ylCv6Tfrecv/39jCGCUv2E5FndO/kc/PxUEA9kZ0oAiLTiVEc6JDsZ5\n5MdcJyxAA3DxKSxv+YsP0kJRat5DUH5OaNFo4MiIvoY6AkPIbddjVYq2d59IAPKG\nzc2wbX62MG0ASH/THnn1EF7n35CBlGIw9L6DjzkCgYEAu0LhdTHuuM6DOAfh4ohw\n0oj2770Dyw0vQImp+4qbdocLqXIVOZYEIywGfi+OLuSxrSYsw2BuTAPAtIEmkuHx\n4cvV/XxcWWPY30B4Z2irOBIsIXJjfAO/DyCyDaX7Cmoy+NgoCwRSRzDeOiQ7ysw8\nhwrS/OoTx3BhHYJt+NO6qIM=\n-----END PRIVATE KEY-----\n",
            "client_email": "appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com",
            "client_id": "115405775326578876255",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/appointment-scheduler%40my-project-90818-learn-hun.iam.gserviceaccount.com"
        },
        scopes=['https://www.googleapis.com/auth/calendar'],
        subject='appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com'
    )
    return creds


@app.route('/webhook', methods=['GET', 'POST'])

#def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    # return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour) + datetime.timedelta(hours=t.minute // 30))

def check_open():
    # current_dateTime = datetime.datetime.now() + datetime.timedelta(hours=3)
    current_dateTime = datetime.datetime.now()
    # 2022-10-07 16:03:58.003427

    # hour_rounder !!! current_dateTime_rounded = hour_rounder(current_dateTime)
    # 2022-10-07 15:00:00
    current_dateTime_rounded = current_dateTime

    hour_minute = current_dateTime_rounded.strftime('%H:%M')
    print("HOUR:", hour_minute)

    open_start_time = ["08:00", "08:00", "08:00", "08:00", "08:00", "08:00", "11:00"]
    open_end_time = ["17:00", "17:00", "17:00", "17:00", "17:00", "13:00", "18:00"]

    weekDays = ("hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat", "vasárnap")
    week_day = current_dateTime.weekday()
    # print("week day: ", week_day)

    week_day_name = weekDays[week_day]
    # print("week_day_name:", week_day_name)

    # print("open_start_time:", open_start_time[week_day])
    # print("open_end_time:", open_end_time[week_day])

    # Textual month, day and year	
    # d2 = current_dateTime.strftime("%Y %B, %d")
    # 2022 October, 01

    if hour_minute < open_start_time[week_day]:
        # print("KORAN", hour_minute, "<", open_start_time[week_day])
        text = "KORÁN. A mai nyitás " + open_start_time[week_day] + " a zárás " + open_end_time[week_day]

    if hour_minute >= open_end_time[week_day]:
        # print("KESON", hour_minute, ">=", open_end_time[week_day])
        text = "KÉSŐN. A mai nyitás " + open_start_time[week_day] + " a zárás " + open_end_time[week_day]

    if hour_minute >= open_start_time[week_day] and hour_minute <= open_end_time[week_day]:
        # print("KOZOTTE", open_start_time[week_day], "<", hour_minute, "<", open_end_time[week_day])
        text = "True"

    # return checked_open

    return text



def webhook():
    # text = main()
    text = check_open()

    if text == "True":
        text_param = main()
        text = text_param['text']
        event_id = text_param['event_id']

        res = {
            "fulfillment_response": {
                "messages": [
                    {
                        "text": {
                            "text": [
                                text
                            ]
                        }
                    }
                ]
            },
            "session_info": {
                "session": "session_name",
                "parameters": {
                    "event_id": event_id
                }
            }
        }

    return res


def main():
    print("DEF MAIN")
    req = request.get_json(force=True)
    print(json.dumps(req, indent=4))

    year = req.get('sessionInfo').get('parameters').get('date').get('year')
    month = req.get('sessionInfo').get('parameters').get('date').get('month')
    day = req.get('sessionInfo').get('parameters').get('date').get('day')

    hours = req.get('sessionInfo').get('parameters').get('time').get('hours')
    minutes = req.get('sessionInfo').get('parameters').get('time').get('minutes')

    summary = req.get('sessionInfo').get('parameters').get('summary')
    location = req.get('sessionInfo').get('parameters').get('location')

    # print("DATE TIME PARAMETERS:", year, month, day, hours, minutes, "summary: ", summary, "location: ",  location)
    # DATE TIME PARAMETERS: 2022.0 10.0 9.0 12.0 0.0 summary:  q location:  q

    dt_parameter_string = str(int(year)) + "," + str(int(month)) + "," + str(int(day)) + "," + str(
        int(hours)) + "," + str(int(minutes))
    # DATE TIME PARAMETERS STRING:  2022,10,9,12,0

    datetime_dt_parameter_string = datetime.datetime.strptime(dt_parameter_string, '%Y,%m,%d,%H,%M')
    # 2022-09-25 00:00:00

    # start_date = datetime.datetime(2017, 10, 30, 00, 00, 00, 0).isoformat() + 'Z'

    start = datetime_dt_parameter_string.isoformat("T", "seconds")
    # 2022-10-09T12:00:00

    # startZ = datetime_dt_parameter_string.isoformat() + 'Z'
    # 2022-10-09T12:00:00Z

    end = (datetime_dt_parameter_string + datetime.timedelta(hours=1)).isoformat("T", "seconds")

    creds = authentication()
    service = build("calendar", "v3", credentials=creds)

    # event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',sendUpdates='all',
    event_result = service.events().insert(calendarId='61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com',
                                           body={
                                               "summary": summary,
                                               "location": location,
                                               "description": "This is the description (parkolo/targyalo, stb)",
                                               "start": {"dateTime": start, "timeZone": "Europe/Budapest"},
                                               "end": {"dateTime": end, "timeZone": "Europe/Budapest"},
                                               "recurrence": {
                                                   "RRULE": "FREQ=DAILY;COUNT=2"
                                               },
                                               "attendees": {
                                                   "email": "tsystems.ai@gmail.com",
                                                   "email": "sbrin@example.com",
                                               },
                                               "reminders": {
                                                   "useDefault": False,
                                                   "overrides": [
                                                       {"method": "email", "minutes": 24 * 60},
                                                       {"method": "popup", "minutes": 10},
                                                   ],
                                               },
                                               "colorId": 6,
                                           }
                                           ).execute()

    text = "Event created. Starts: " + event_result['start']['dateTime'] + " Ends: " + event_result['end'][
        'dateTime'] + " id: " + event_result['id']

    # start_event = datetime.datetime.strptime(event_result['start']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')
    # end_event = datetime.datetime.strptime(event_result['end']['dateTime'],'%Y-%m-%dT%H:%M:%S%z')

    text_param = {}
    text_param['text'] = text
    text_param['event_id'] = event_result['id']

    # return text
    return text_param

    app.run()
