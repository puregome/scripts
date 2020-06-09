import praw
import csv

credentials_file = open("credentials.txt")
myclient_id = credentials_file.readline().rstrip()
myclient_secret = credentials_file.readline().rstrip()
myuser_agent = credentials_file.readline().rstrip()

reddit = praw.Reddit(client_id=myclient_id,
                        client_secret=myclient_secret,
                        user_agent=myuser_agent)

def main():
   # r/thenetherlands weekly Megathread: Coronavirus COVID-19 in Nederland
   #threads = {'02': 'fg6nz6', '03': 'fhjmce', '04': 'filu7c', '05': 'fjdhbi', '06': 'fk9v9h', '07': 'fldu9y', '08': 'fn3yxt', '09': 'fnxpx8', '10': 'fph5pb', '11': 'frtesk', '12': 'fu0w1d', '13': 'fxja6g', '14': 'g25oxd', '15': 'g5ne1u'}
   subreddit_name = "CoronaNL"
   #subreddit_name = "coronanetherlands"
   # from get_subreddit_ids.py
   file_in = open(f"submissions_ids_{subreddit_name}.txt")
   threads = file_in.read().splitlines()
   
   for thread_id in threads:
      print(subreddit_name, thread_id)
      get_comments(subreddit_name, thread_id)

def get_comments(subreddit_name, thread_id):
   file_out = open(f'comments/{subreddit_name}_{thread_id}.csv', 'w', encoding = 'utf8', newline = '')
   comments_out = csv.writer(file_out,
                          delimiter = ',',
                          quotechar = '"',
                          doublequote = True,
                          quoting = csv.QUOTE_NONNUMERIC)
   comments_out.writerow(['created','id','author','parent','score','body'])


   submission = reddit.submission(id = thread_id)
   print(submission.title)

   submission.comment_sort = 'new'
   submission.comments.replace_more(limit = None)
   top_level_comments = list(submission.comments)

   print("number of comments:", len(submission.comments.list()))

   for comment in submission.comments.list():
      comments_out.writerow([int(comment.created_utc), comment.id, comment.author, comment.parent_id, comment.score, comment.body])

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

