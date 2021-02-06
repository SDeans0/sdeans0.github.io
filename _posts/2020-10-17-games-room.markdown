---
layout: post
title:  "Word Games With Friends"
date:   2020-08-06 12:00:00 +0100
categories: made_things
---

Bored of the zoomification of daily life, I spent a couple of weekends in the first
lockdown trying to make it more interesting. I wanted to play some games on calls
where nobody had anything new to talk about. Originally, I was aiming to create a
card game web app that I could use with my family, but one of my friends suggested
a couple of simple word games that would be easier to code up first, so there are a
few on there now. I was glad that he did, because the iteration for the first version
was much easier with a simpler end point in mind.

In my PhD I mainly code in Python, so I thought it would be fun to try
a Flask backend; an earlier incarnation of this website had used Django, which
is a wonderful tool but overkill for a simple site. I decided to use websockets
to handle communication between the browser and the server, with the latter mainly
acting as a dumb go-between able to broadcast to all the players of a game. For this,
I used the excellent Flask-SocketIO library, hooked up to a PostGres database. The
choice of the latter was constrained by what was free on Heroku, which is hosting
the site and handily updates the code immediately after each fresh push to GitHub.

I coded three simple games, which all followed the same basic structure. The first
player to arrive generates a 'room', a new instance of the game which other players
can join and access but which is isolated from anyone else who happens to be playing.
This has its own URL, which can be shared with the other players. Whenever a player
connects to a room, a websocket is opened between the room and the server, which
keeps track of the unique id of all the connections in that room. Then when the game
begins, the server gives back the appropriate randomised state (either a random word
or a hand from a shuffled deck of cards) to each player's browser. The browser stores
the state of the game; any information that needs to be passed between the players,
such as written messages or played cards, does so via socket messages pinged via the server.

I've been pretty pleased with the finished product. The games have had some repeat
value among my friends, and judging by the odd text requesting tech support, among
my family too. 
