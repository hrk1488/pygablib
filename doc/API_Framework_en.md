# Gab API

This was compiled from the @doc Gab.Ai feed.

## Logging in
### GET Request https://gab.ai/auth/login (enable cookies)
Get the value of the hidden input named "_token"
### POST Request https://gab.ai/auth/login with these parameters: "username", "password", "_token", (optionally "remember")
You can now store the laravel_session/remember cookie

## Follow someone
### POST Request https://gab.ai/users/<user id>/follow with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the user exists, you now follow him. If its account is private, your follow is now pending

## Unfollow someone
### POST Request https://gab.ai/users/<user id>/follow?_method=delete with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the user exists, you're not following him anymore


## Get your feed
### GET Request https://gab.ai/feed with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
You get a JSON of your feed

## Get someone else's posts
### GET Request https://gab.ai/feed/<username>; with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the user exists, you get a JSON of its last 28 posts

## Get your Pulse feed
### GET Request https://gab.ai/api/pulse with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
You get a JSON of your Pulse feed

## Logging out
### GET Request https://gab.ai/auth/logout with the remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
The validity of your cookies is revoked, you're disconnected.

## Like a post
### POST Request https://gab.ai/posts/<post id>/like with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the post exists, you liked it

## Dislike a post
### POST Request https://gab.ai/posts/<post id>/dislike with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the post exists, you disliked it

## Removing a like
### POST Request https://gab.ai/posts/<post id>/like?_method=delete with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the post exists, you removed your liked

## Removing a dislike
### POST Request https://gab.ai/posts/<post id>/dislike?_method=delete with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
If the post exists, you removed your dislike

## Search
### GET Request https://gab.ai/api/search?sort=<sort>&q=...; with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
You get a JSON of the search results
List of available sorts: date, relevance, score

## Get your notifications
### GET Request https://gab.ai/api/notifications?type=<type>; with the "remember_82e5d2c56bdd0811318f0cf078b78bfc" or "laravel_session" cookie set
You get a JSON of your notifications
List of available types: null, 1, 2, 3, 4, spam

## Note on Rate-limiting

Things that can't get you rate-limited (don't abuse them):
* Logging in/out
* (dis)liking posts 
* (un)following users
* fetching your timeline
* deleting/editing posts
* reporting posts
* changing your profile/username/password
* posting

Rate-limiting is by IP, not by account (for now)
