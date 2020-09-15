# usage: coronamessagesnl.py submission_ids_* 

import csv
import os
import praw
import re
import sys

FILECREDENTIALS = "../credentials.txt"
OUTDIR = "downloads/"

credentials_file = open(FILECREDENTIALS)
myclient_id = credentials_file.readline().rstrip()
myclient_secret = credentials_file.readline().rstrip()
myuser_agent = credentials_file.readline().rstrip()

reddit = praw.Reddit(client_id=myclient_id,
                        client_secret=myclient_secret,
                        user_agent=myuser_agent)

def main():
   for inFileName in sys.argv[1:]:
      subreddit_name = re.sub(r"\.txt$","",inFileName.split("_")[2])
      # from get_subreddit_ids.py
      file_in = open(f"submissions_ids_{subreddit_name}.txt")
      threads = file_in.read().splitlines()
   
      for thread_id in threads:
         print(subreddit_name, thread_id)
         get_comments(subreddit_name, thread_id)

def get_comments(subreddit_name, thread_id):
   if not os.path.isdir(OUTDIR): os.mkdir(OUTDIR)
   file_out = open(OUTDIR+f'{subreddit_name}_{thread_id}.csv', 'w', encoding = 'utf8', newline = '')
   comments_out = csv.writer(file_out,
                          delimiter = ',',
                          quotechar = '"',
                          doublequote = True,
                          quoting = csv.QUOTE_NONNUMERIC)
   comments_out.writerow(['created','subreddit','id','author','parent','score','body'])


   submission = reddit.submission(id = thread_id)
   print(submission.title)

   submission.comment_sort = 'new'
   submission.comments.replace_more(limit = None)
   top_level_comments = list(submission.comments)

   print("number of comments:", len(submission.comments.list()))

   for comment in submission.comments.list():
      comments_out.writerow([int(comment.created_utc), subreddit_name, comment.id, comment.author, comment.parent_id, comment.score, comment.body])

   file_out.close()

if __name__ == '__main__':
   main()

# Megathread: Coronavirus COVID-19 in Nederland

# https://www.reddit.com/search/?q=mondkapjes
# https://www.reddit.com/search/?q=corona%20subreddit%3Athenetherlands&sort=new
# via pushshift? of PRAW?
# https://www.reddit.com/r/redditdev/comments/ao7cvo/praw_keyword_search_scraper/

#https://www.reddit.com/r/coronanetherlands/
#https://www.reddit.com/r/dutch/
#https://www.reddit.com/r/CoronaNL/
#https://www.reddit.com/r/thenetherlands/


## https://stackoverflow.com/questions/53988619/praw-6-get-all-submission-of-a-subreddit
# https://www.reddit.com/r/pushshift/comments/b7onr6/max_number_of_results_returned_per_query/
# https://github.com/Watchful1/Sketchpad/blob/master/postDownloader.py
