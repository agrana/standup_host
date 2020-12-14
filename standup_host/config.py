"""
Configuration options for standup host.

team_names
teasm_webhook

"""
import os

team_names = ["Paul", "Jhon", "Ringo", "George"]
""" List of team members. """
teams_webhook = os.getenv("TEAMS_WEBHOOK")
""" Webhook to send the updates."""
