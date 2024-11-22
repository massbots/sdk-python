import os
import sys

sys.path.append(os.getcwd())

import massbots


mb = massbots.Api(
    token=os.environ["TOKEN"],
    bot_id=os.environ["BOT_ID"],
)

print(f"Balance: {mb.balance()}")

print(f"Stats: {mb.stats()}")

video = mb.video("dQw4w9WgXcQ")
print(f"Video: {video.title}")

download = video.download("1080p")

# SDK has download result polling implemented already
result = download.wait_until_ready()

# The file_id is now available to your bot
print(result.file_id)

channel = mb.channel(video.channel_id)
print(f"Channel: {channel.title}")

channel_feed = mb.channel_feed(channel.id)
print(f"Channel feed: {channel_feed}")

search = mb.search("Rick Astley")
print(f"Search: {len(search)} items")

# Get the available formats from API
formats = video.formats()
print(formats)

# Transfer all cached formats instantly
cached = formats.filter(cached=True)
for format in cached.keys():
    result = video.download(format)
    # The file_id is now available to your bot
    print(result.file_id)
