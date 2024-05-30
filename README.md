Simple script to check if there are resale tickets available for the Amsterdam Marathon 2024, through the open GraphQL API. Once there are new tickets available on the offical resale page, it sends a notification (only works on linux for now) and opens the page in a browser window (all operating systems). Leave the program running in the background and just wait.
# Usage
Install notify-send for receiving notifications:
```
sudo apt install notify-send
```
Run the code:
```
python3 main.py
```
It will check for new tickets every 20 seconds.

