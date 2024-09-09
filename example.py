import os
import massbots

mb = massbots.Api(
    token=os.environ["TOKEN"],
    bot_id=os.environ["BOT_ID"]
)

video = mb.video("dQw4w9WgXcQ")
download = video.download("1080p")

# SDK has download result polling implemented already
result = download.wait_until_ready()

# The file_id is now available to your bot
print(result.file_id)

# Get the channel of the video
channel = mb.channel(video.channel_id)

print(channel.title,channel.subscriber_count)

# Get the balance of the account
print(mb.balance())

# Search for a videos
print(mb.search("rick astley"))
