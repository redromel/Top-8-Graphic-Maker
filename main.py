# TODO:  Loser Identifier for Grands
# TODO:  Better Error Handling when querying
# TODO:  NiceGUI Implementation for fun

from dotenv import load_dotenv
import requests
from event_listner import *
from queries import *
from query_parser import *
from writer import *
from nicegui import ui
from constants import *

load_dotenv()
key = os.getenv('smashgg_api')

api_url = 'https://api.start.gg/gql/alpha'
phase_id = 1749308
# phase_id = 1276356 
player_id = 16105
slug = 'tournament/genesis-9-1/event/melee-singles'
t_slug = 'tournament/py-testing-tourney-2'
t_id = 704088
vars = {'slug': slug}

#keep iterating through pages until pageInfo = 0 and nodes = []
vars2 = {"phaseId": phase_id, "page": 1, "perPage": 30}
vars3 = {'playerId': player_id}
vars4 = {'slug': t_slug}
vars5 = {'tournamentId':  t_id}
header = {"Authorization": "Bearer " + key, 'Cache-Control': 'no-cache', 'Pragma': 'no-cache'}
payload = {'query': PLAYER_QUERY, 'variables': vars3}
payload2 = {'query': BRACKET_GRAPHIC_QUERY, 'variables': vars2}
payload3 = {'query': BRACKET_QUERY, 'variables': vars2}
payload4 = {'query': EVENT_QUERY, 'variables': vars4}
payload5 = {'query': STREAM_QUERY, 'variables': vars5}






        

def main():
  ...




  
  #  *Grabbing Events and Phases based on tournament slug
  # slug_input = ui.input(label='start.gg tournament slug',placeholder='tournament/tournament-name/').props('size=80').props('rounded outlined dense')

  # slug_button = ui.button('Submit', on_click=lambda e: get_events(e.sender, slug_input, event_select))

  # event_select = ui.select(label='Select Event',
  #                          options=['Insert Slug'],
  #                          on_change=lambda e: get_phases(e,phase_select),
  #                          value='Insert Slug').classes('w-50')
  
  # phase_select = ui.select(label='Select Phase',
  #                          options=['Insert Slug'],
  #                          on_change=lambda e: print(e.value),
  #                          value='Insert Slug')

  # event_select.disable()
  # phase_select.disable()





if __name__ in {"__main__", "__mp_main__"}:
  main()
  ui.run()