import requests
import subprocess
import time
import webbrowser

# send simple http request with json body
def check_availability():
    url = "https://atleta.cc/api/graphql"
    headers = {
        "Content-Type": "application/json"
    }
    data = {"operationName":"GetRegistrationsForSale","variables":{"id":"nhIVueqEDrvO","tickets":"null","limit":10},"query":"query GetRegistrationsForSale($id: ID!, $tickets: [String!], $limit: Int!) {\n  event(id: $id) {\n    id\n    registrations_for_sale_count\n    filtered_registrations_for_sale_count: registrations_for_sale_count(\n      tickets: $tickets\n    )\n    sold_registrations_count\n    tickets_for_resale {\n      id\n      title\n      __typename\n    }\n    registrations_for_sale(tickets: $tickets, limit: $limit) {\n      id\n      ticket {\n        id\n        title\n        __typename\n      }\n      ticket {\n        id\n        title\n        __typename\n      }\n      time_slot {\n        id\n        start_date\n        start_time\n        title\n        multi_date\n        __typename\n      }\n      promotion {\n        id\n        title\n        __typename\n      }\n      upgrades {\n        id\n        product {\n          id\n          title\n          is_ticket_fee\n          __typename\n        }\n        product_variant {\n          id\n          title\n          __typename\n        }\n        __typename\n      }\n      resale {\n        id\n        available\n        total_amount\n        fee\n        public_url\n        public_token\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}
    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    
    # get field data.event.registrations_for_sale_count
    return(response.json()["data"]["event"]["registrations_for_sale_count"])

def notify():
    subprocess.Popen(['notify-send', "MARATHON TICKETS AVAILABLE"])
    return

def open_browser():
    webbrowser.open("https://www.tcsamsterdammarathon.nl/startbewijs-vraag-aanbod")
    return

def main():
    while True:
        print("Checking availability...")
        if check_availability() != 0:
            print("Tickets available!")
            notify()
            open_browser()
        else:
            print("No tickets available.")

        # check every 2 minutes
        time.sleep(120)

if __name__ == "__main__":
    main()
