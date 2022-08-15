from AutomateInsta import StoryViewer

# First instagram Account for Testing
# username = 'playing_underrated_games'
# password = '19Arka99'

# Second Instagram Account for Testing
username = 'test_911_test'
password = 'Agni@Arka911'

# Initializing StoryViewer with username, password, target_profile and number of profiles to visit.
viewer = StoryViewer(username=username, password=password, target_profile="arcturuschild", n_profiles=10)
viewer.start()
