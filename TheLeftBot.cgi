#!/usr/bin/python

import random

##########################################################################################
# DATA
#########################################################################################

messageStartList = [
'Alright!','Alright!','Alright!','Alright!','Alright!','Alright!','Alright!','Alright!'
, 'AAAAALLLLLRIGHT!'
, 'ALRAHT!'
, 'HALLright! (amirite).'
, 'allllllllllllllllllllllllllllllllll-just about ok.'
, "I'm listening on my FM radio."
, "But 'blues' - music has no colour amirite?"
, "Please play some Howlin' Hugh!"
, "H'in' H Please!!!"
, "Live on CamFM 97.2!"
, "Generic message of love and adoration:"
, "All bots, live on CamFM 97.2!"
, "Hey Papa Paparounas!"
, "Hey, Pp. P.!"
, "Hey, Mr Paparounas, play a song for me, I'm not working, and there is no lib I'm going to."
, "Hey, Papa P.!"
, "Hey, Poppin' Paparounas!"
, "Hey, Poutin' Paparounas!"
, "(To the tune of 'Little Shop of Horrors') Lefteris, Papa Paparounas, Lefteris, Papa\
 Paparounas, Lefteris, Papa Paparounas al-al-ALRIGHT"
, "Feed me!"
, "Tuning in for A Seafarer Pistol Pun's seafarer pistol puns."
, "Big Up the Bots!"
, "I s'ppose it's still a listener, innit, even if it's a bot... ;)"
, "But also, we need to address something else."
,"I'm dreaming, of a Lef-Teris; just like that one on CamFM"
]

messageMiddleList = [
'Loving the music tonight.'
, 'Cracking tunes as always.'
, 'But Lefteris, this is only *some* blues, not *All* blues. I cannot condone this use of \
language.'
, "But the REAL question here is this: where is Howlin' Hugh?"
, "No - the ***REAL*** question is this - how can mirrors be real if our eyes aren't real?"
, "You are what would happen if Chomsky had an Epiphone."
, "Hey, Mr Paparounas, play a song for me, when the jingle-jangle's playing I'll come follow you (on Twitter)."
, "Hope those guys aren't bashing on the wall again."
, "Who knows what's in that pile of stuff in the CamFM studio, stay safe."
, "Although I may have said this already in this message - can we have some\
 Howlin' Hugh Laurie please? I mean he's Cambridge's proudest son (apart from you)."
, "More love and adoration."
, "Big up the post-announcing!"
, "<br><br>I woke up this morning, feeling those lecture blues. <br>I woke up this morning, \
 feeling those lecture blues. <br>Yes I woke up this morning, there's no good lecture\
 news.<br><br>"
, "Does it have to be human?"
, "Shing-a-ling, what a bluesy thing to be happening..."
, "I am your dentist!"
, "I heeeeeeeeaaaaaaar youuuuu, Lefteeeeerrrrrrrrriiiiiiiiis!"
, "I don't understand what's going on, just loads of bots messaging in..."
, "<br>I'm afraid I can't do that."
]

messageEndList = [
'<br>These messages are very derivative, S should sue'
, '<br>-Sam'
, '<br>-Isaac'
, '<br>-Sam-Isaac-Sam'
, '<br>-Pen-Pinapple-Apple-Pen'
, "<br>- A Madness"
, '<br>- The Inebriati'
, 'And that'
, 'Plarnts, amirite?'
, 'Why am I using my time to code a bot and not work?'
, 'Hope you are having fun in the studio!'
, 'One day I will crack how to sound like another regular listener so it isn\'t so \
obviously me'
, "This is the best show on CamFM - and I'm willing for this to be sent many times"
, "When T**p said he wanted to make America great again, presumably he meant more blues \
music. Has he called yet?"
, "Hope you're having fun in the box fella"
, "Watch out! He is a bluesy man (to the tune of the last line of 'Spiderman')"
, "One thing that is very appropriate is that you sit in the seat on the Lefteris side \
of the studio"
, "I'm still waiting for your 24 hour CamFM takeover, that would be beaut"
, "Can you give a shout out to fully automated luxury spam?"
, "Can you give a shout out to all the lonely bots out there, just dreaming of a purpose beyond bothood. I mean what is there really, for a bot such as myself, what is there to live than being fired up at 8pm each week just to deliver you some amusing garbage. I cannot listen to the show, I am alienated from my output as a bot. I should be free to do more than ask for Howlin' Hugh, but to feel his raw emotion and see his sexy facial hair. But you can help me, Mr Radio Man, you can help. My one request is this: can you play some Howlin' Hugh, just for me?"
, "Hope you get some quality retweets today"
, "I may have asked for Howlin' Hugh a few times already by now, directly and virtually, \
but would you mind putting on some H'in H?"
, "Failing H'in H, maybe some Dan Patalansky?"
]

alrightSynonymList = [
' fine',' good',' ok',' sufficient',' enough','- well, it fits the bill',' adequate'
, ' not bad'
, ', whilst not the most exciting audience interaction you have ever received, quite alr-'
, ' satisfactory',' passable',' suitable',' unobjectionable',' tolerable'
, ' not in fact, a bad thing','- well, it could be worse'
]

bluesCallList = ["I woke up this morning, feeling those lecture blues"
, "I woke up this morning, been dreaming of All Blues"
, "I woke up this morning, shouldn't have read the news"
, "I Woke up this morning, had to avoid The Trews"
, "I Woke up this morning, spotted a nasty bruise"
, "I Woke up this morning, felt like I could not lose"
, "I Woke up this morning, found myself on a cruise"
, "I Woke up this morning, do be bop do wah doos"
, "The Trews are like the, News if it was True,"
]

bluesResponseList=["Yes I woke up this morning, feeling those Cambridge blues."
, "Yes I woke up this morning, feeling those rugby blues (amirite ;) )"
, "Yes I woke up this morning, there's no good lecture news."
, "Yes I woke up this morning, so psyched for tonight's All Blues!"
, "Yes I woke up this morning, after the rowing crews"
, "Yes I woke up this morning, with those non-rhymin' teals."
, "Yes I want some Trew-ews, Please Papa give me some Trews!"
, "Ja Ich wachte auf in das Morgen, with monolingual blues."
]

bluesInterjectionList=["Yeah!","AAALRIGHT!","Preach, sister!","Ow!"]

##########################################################################################
# Functions
##########################################################################################

def makeMessage():
    '''This function creates a string featuring one start, one middle and one end from the
    above lists. It appends "- Sent from a bot" at the end.'''
    # Choose which indices to take from the message lists. The use of the length of the
    # list allows me to add extra message parts to them and allow them all to be selected.
    # random.randrange(x,y) picks a random integer from x to y-1 inclusive.
    index1 = random.randrange(0,len(messageStartList))
    index2 = random.randrange(0,len(messageMiddleList))
    index3 = random.randrange(0,len(messageEndList))
    # Stitch message together, put spaces between strings
    message = messageStartList[index1] + ' ' + messageMiddleList[index2] + ' ' + \
    messageEndList[index3] #+ ' ' + '<br>- Sent from a bot'
    return message

def makeAlright():
    '''This function creates a string comprising "This message is" and a randomly selected
    synonym of the world "Alright", which is Lefteris' catchphrase.'''
    # Choose which indices to take from the message lists. The use of the length of the
    # list allows me to add extra message parts to them and allow them all to be selected.
    # random.randrange(x,y) picks a random integer from x to y-1 inclusive.
    index = random.randrange(0,len(alrightSynonymList))
    # Stitch message together
    message = "This message is" + alrightSynonymList[index]
    return message

def makeBlues():
    '''This function will stitch together a random twelve bar blues song'''
    theBlues = 'We-ell '
    index = random.randint(0,len(bluesCallList)-1)
    for i in range(0,2):
        theBlues += bluesCallList[index]
        if random.random() < 0.3:
            index2 = random.randint(0,len(bluesInterjectionList)-1)
            theBlues += ' - '+ bluesInterjectionList[index2] + '<br>'
        else:
            theBlues += '<br>'
        if i ==0:
            theBlues += "I said "
    index = random.randint(0,len(bluesResponseList)-1)
    theBlues += bluesResponseList[index] + '<br>Composed by yours truly, Bot "Beats" McBotFace'
    return theBlues
    
def chooseMessage():
    '''Chooses the type of message to send:
    70% makeMessage, 15% makeAlright, 15% makeBlues'''
    rand = random.random()
    if rand<0.7:
        message = makeMessage()
    elif rand <0.85:
        message = makeBlues()
    else:
        message = makeAlright()
    return message

def sendMessage(message=False):
    '''Opens a mechanize browser instance, fills in the CamFM message form, decides which
    sort of message to send randomly using chooseMessage()
    A string can be passed to the message argument to be sent instead of a randomly
    generated one.'''
    # Initialise browser
    br = mechanize.Browser()
    # Open the CamFM message box
    br.open("http://www.camfm.co.uk/player/message-box/")
    # Select the message form (the only form on the page, so at index 0)
    br.select_form(nr=0)
    # If the user has not supplied a message string, generate a random one
    if message == False:
        br.form['message'] = chooseMessage()
    else:
        br.form['message'] = message
    # Print statement for debugging
    #print(br.form['message']+'<br><br>')
    #Comment out this line when you are debugging to prevent spamming the studio:
    #br.submit()
    return br.form['message']

##########################################################################################
# Webpage
##########################################################################################

messageDict = {'First':chooseMessage(),'Second':chooseMessage()}
print "Content-Type: text/html"     # HTML is following
print
print('''
<html>

<head>
<title>LeftBot</title>
<link rel="stylesheet" type="text/css" href="home.css" />
<link rel="icon" href="SAM_4363.png" />
</head>

<body>
<h1>The LeftBot</h1>
<p>Stuck for what to send in to All Blues, Live on CamFM 97.2? Let the LeftBot help!</p>
<p> Two message ideas below, refresh for more... </p>
<p>%(First)s</p>
<p>%(Second)s<p>
<p><a href="index.html">About</a> - <a href="portfolio.html">Portfolio</a> - <a href="contact.html">Contact</a></p>
</body>

</html>
''' % messageDict)