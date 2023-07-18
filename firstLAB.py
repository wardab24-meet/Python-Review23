def create_youtube_video (title , description):
	youtube_video = {"title": title, "description":description, 'likes': 0 , 'disslickes': 0 , 'comments':{}}
	return youtube_video
def likes(youtube_video) :
	if "likes" in youtube_video 
		youtube_video["likes"]+=1
		return youtube_video
def  disslickes(youtube_video)
	if "disslickes" in youtube_video 
		youtube_video["disslickes"]+=1
		return youtube_video

def add_comment(youtubevideo, username, comment_text):
    youtubevideo['comments'][username] = comment_text
    return youtubevideo

youtubevideo = {
    'title': 'Amazing Video',
    'views': 1000,
    'likes': 500,
    'comments': {}
}

youtubevideo = add_comment(youtubevideo, 'User1', 'Great video!')
youtubevideo = add_comment(youtubevideo, 'User2', 'Awesome content!')
youtubevideo = add_comment(youtubevideo, 'User3', 'Loved it!')

print(youtubevideo)

youtubevideo['likes'] += 495
