from AutomateInsta import StoryViewer

username = 'username'
password = 'password'



viewer = StoryViewer(username=username, password=password,target_profile="profile", n_profiles=10)
viewer.start()
