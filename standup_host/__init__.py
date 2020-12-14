"""

# Standup host. 

Given a list of individuals participating in a standup meeting. 
I want to randomly pick one and ask him about Yesterday, Today and what is Blocking. 
I want to messure the time in seconds that the individual took to update. 
Then send the response to a channell. 
Keep getting names from the list till is finished. 

Configuration:
    - config.py configuration file imported in all the modules of the package.
    - team_names = list containing strings with the names of the team members.
    - teams_webhook = webhook to send notification to MS Teams.

Requirements:
    - random
    - pymsteams
    - time

"""
