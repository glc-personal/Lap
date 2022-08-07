# Lap
Application which finds potential laps for nice scenic drives near you. 

# Current State:
Currently just an idea. Would like to start with images from google maps (images of the birds eye view for sections of road), use image processing to find only the roads on these images, annotate curved roads, and then use these images and their masks to train a neural network to find curved roads. Then once there is an accurate model, a user can do a search for "laps" near them. Users can then rate the lap, keep best times on a leaderboard, and more. This could be a phone application, or hardware could be made for a headsup display for navigational purposes ("Turn left here", "25 mph turn coming up", etc)

# Note(s):
This is currently in developement with the use of python for quick test of funcionality.

# Module(s):
geocoder: used for getting the current lattitude and longitude of the user.
