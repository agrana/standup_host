import os
import random
import pymsteams
import time
from standup_host import config


def send_to_teams(message):
    """
    Send a message to teams using a webhook.
    [Tutorial](www.create_the_webhoook.com)
    """
    teams_webhook = config.teams_webhook
    teams_message = pymsteams.connectorcard(teams_webhook)
    teams_message.text(message)
    teams_message.send()


def stand_up_host():
    """
    Main loop.
    """
    team_names = config.team_names
    """
    # List of Names.
    # Strings
    """
    random.shuffle(team_names)
    for name in team_names:
        input("Press any key to get a name")
        print("Next is name is: %s " % (name))
        while True:
            print("%s is updating: " % (name))
            start_time = time.perf_counter()
            yesterday = input("What %s did yesterday: " % (name))
            today = input("And %s today is goning to today: " % (name))
            blockers = input("What is blocking %s: " % (name))
            stop_time = time.perf_counter() - start_time
            print("%s talked for %d seconds" % (name, stop_time))
            send_to_teams(
                """
                          \n# **%s**
                          \n- **Yesterday:** *%s*
                          \n- **Today:** *%s*
                          \n- **Blockers:** ***%s***
                          \nSeconds took: **%d**
                          """
                % (name, yesterday, today, blockers, stop_time)
            )
            break
    print("And... we are all done!!")


if __name__ == "__main__":
    stand_up_host()
