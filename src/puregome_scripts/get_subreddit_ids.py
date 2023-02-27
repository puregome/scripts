# adapted from https://github.com/Watchful1/Sketchpad/blob/master/postDownloader.py
import requests
from datetime import datetime
import traceback

url = "https://api.pushshift.io/reddit/submission/search?limit=1000&sort=desc&subreddit={}&before="

start_time = datetime.utcnow()

def downloadFromUrl(subreddit):
	filename_sub = f"submissions_content_{subreddit}.txt"
	filename_ids = f"submissions_ids_{subreddit}.txt"
	print(f"Saving {subreddit} ids to {filename_ids} and {filename_sub}")

	count = 0
	handle = open(filename_sub, 'w')
	handle_ids = open(filename_ids, 'w')
	previous_epoch = int(start_time.timestamp())
	while True:
		new_url = url.format(subreddit)+str(previous_epoch)
		json = requests.get(new_url, headers={'User-Agent': "python:coronamessagesnl:v0.2 (by u/marijnschraagen)"})
		json_data = json.json()
		if 'data' not in json_data:
			break
		objects = json_data['data']
		if len(objects) == 0:
			break

		for object in objects:
			previous_epoch = object['created_utc'] - 1
			count += 1
			handle_ids.write(str(object['id'])+"\n")
			if object['is_self']:
				if 'selftext' not in object:
					continue
				try:
					handle.write(str(object['id']))
					#handle_ids.write(str(object['id'])+"\n")
					handle.write(" : ")
					handle.write(str(object['score']))
					handle.write(" : ")
					handle.write(datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d"))
					handle.write("\n")
					text = object['selftext']
					textASCII = text.encode(encoding='ascii', errors='ignore').decode()
					handle.write(textASCII)
					handle.write("\n-------------------------------\n")
				except Exception as err:
					print(f"Couldn't print post: {object['url']}")
					print(traceback.format_exc())

		print("Saved {} submissions through {}".format(count, datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))

	print(f"Saved {count} submissions")
	handle.close()
	handle_ids.close()


for subreddit in "coronanetherlands CoronaNL CoronavirusNL".split():
    downloadFromUrl(subreddit)
