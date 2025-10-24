Oct 24, 2025

## \[Cooking\] Demo \- Transcript

### 00:00:00

   
**Lucas Cufré:** What's up?  
**Shak \-:** Hey, Lucas.  
**Naji Osmat:** how are you?  
**Lucas Cufré:** All good. All good. Sinking up all the issues to the rest of the team.  
**Naji Osmat:** Yeah, they're they're most of them are quite small.  
**Lucas Cufré:** Yeah. Yeah. Yeah. Pretty much just nitpicky stuff. Some things really don't uh have any logic with uh beneath them, but it's okay. For instance, the width of the column here, it's reported as 364 pixels when it currently is 310\. That's way too nitpicky, but it's okay. We can solve it.  
**Naji Osmat:** better have it the way uh the way it's been made. Um, did you did you manage to take a look at the um um I think the the biggest one that I I I found was uh linking your other uh your other other social  
**Lucas Cufré:** No, that that that was solved yesterday like 10 20 minutes after I I started seeing the the issues.  
**Naji Osmat:** Okay. Okay.  
**Lucas Cufré:** Yeah, that that is already fixed in dev.  
**Naji Osmat:** I haven't Okay.  
   
 

### 00:01:14

   
**Lucas Cufré:** uh we have we are waiting to have a certain batch of fixes and then we deploy to prod.  
**Naji Osmat:** Okay. Okay. That's good then. That's good.  
**Lucas Cufré:** Yep. It was the only situation in which we found that uh that particular issue uh it had something to do with the way that the back end was validating the security password but that is fixed already.  
**Naji Osmat:** Okay. Good. Good to hear.  
**Gregory Chapman's Presentation:** Okay.  
**Lucas Cufré:** Okay.  
**Gregory Chapman's Presentation:** Is the Is the notion um ready, Lucas?  
**Lucas Cufré:** Yeah.  
**Gregory Chapman's Presentation:** Up to date?  
**Lucas Cufré:** So, oh crap. My bad. Uh Shik and Zayn are both uh invited as guests. Uh I forgot that you both were not. So, I'm going to uh I am finishing adding them up right now as we speak.  
**Gregory Chapman's Presentation:** Yeah, if you can just add me so I can try. is um Ali are Ali's comments in the  
**Lucas Cufré:** They are mostly UI things. Many of these have been solved already.  
   
 

### 00:02:20

   
**Gregory Chapman's Presentation:** Yeah.  
**Lucas Cufré:** Uh but some need to be reviewed. So I'm going to be uh assigning them to the team in uh today in a little while. So let me just share my screen so we can see the current state of affairs. Uh let me update this before so you have everything. Yep, there we go. Okay. So I want to go over the is it sharing? Yeah, it is. I want to go over the the notion quickly because uh we have a bit of a thing to discuss with with Zane here regarding the next road map and I want to leverage that time.  
**Gregory Chapman's Presentation:** Yeah. Yeah, just just when we're going over this, Lucas, um for us it's important to understand time frames of when these will be sorted. So when you're going over them, if you can just touch over that specifically.  
**Lucas Cufré:** Mhm. Okay. So, for many of the Okay, let's go over here real quickly. This is the last uh the the last page that I've shared with both Yoshi and and Zane.  
   
 

### 00:03:43

   
**Lucas Cufré:** Basically what we are showing here it's the breakdown of the tasks and the the domain that they are assigned to if it is backend front end indexer etc etc. Um so as you can see the backend issues are pretty much non-existent. They are really small. We have a different story when it comes to front end. So as you can see there we have already some that are testing. We have some that are in progress. I don't expect to have uh more than by end of Monday uh to get like about 80 to 90% there. They are really really small things like for instance this uh the token avatar should be 34 34 pixels each uh on each direction or like changing uh changing a batch that was exported wrongly. So many of these are are going to be fixed mostly by by Monday. I don't expect you to have to wait any longer than than Monday to be honest. There are some things that are going to take a little bit more time.  
   
 

### 00:04:55

   
**Lucas Cufré:** For instance, the normalization of the uh error messages. Those are going to take a little bit more time. So, don't hold me accountable on that. Um, as well as the update of the uh number representation definition. So we've reviewed our our schema for representing numbers and how to how to round up, how to round down uh and everything. So this is we're going to build a utility that it's going to have to be reapplied to each number. So that is going to take a little bit more time. Namely not for adapting more so to to detect in which places those numbers are not up to standard up to the newly standard. Then as you can see in the exercise it's pretty much done. I don't know if that works for you, Craig. As a ballpark estimation.  
**Gregory Chapman's Presentation:** Um, what do we think Zane on that?  
**Zen \-:** So, majority of these you said would be done by Monday.  
**Lucas Cufré:** Yep.  
**Zen \-:** I'm just curious because a lot of these were very basic QA things that would have been  
   
 

### 00:06:16

   
**Lucas Cufré:** So, yeah. So I'll let me go for instance in a few things. There are some things that we had already uh assigned. For instance, this 24 pixels x 24 pixels. If we go into uh the design that we had, those right there changed in the latest iteration when we modified it. Uh there are some things that were being tackled in another issues. So these are the ones that you guys detected. If we go into the complete backlog, there are some of these that, let me see, have already been detected and were, for instance, flagged as something that we had to fix. For instance, here, as you can see, there are many of these that were already flagged and we were tackling. So basically Ali found them before we could push. So this uh the the FL the issues right now that we are seeing are basically a double check for most of this. So you can see here that so yeah it was actually so I have no excuses for that.  
   
 

### 00:07:27

   
**Zen \-:** cuz we we thought we thought that um and this was what was communicated that QA was finished on last Friday on your side.  
**Lucas Cufré:** It was this was what when this was last edited yesterday. So evidently some of these were uh were missing.  
**Zen \-:** Yeah, this was created yesterday.  
**Lucas Cufré:** Yep. The day before actually the 22nd but yeah Wednesday. So now that you have access to the screen you can review if you wish to do so. Jesus, where is that? But basically what you can see right here are all of those and the breakdown by status.  
**Gregory Chapman's Presentation:** Basically, what you're going to do  
**Lucas Cufré:** So as you can see we have eight tests, seven are in progress, 23 have been reported and five are already done which are for instance the uh hiding of the stable coins in specials uh the disclaimer for uh DCA and a few things on the indexer side.  
**Zen \-:** And you said, Lucas, that there's two QA engineers working right now full-time.  
**Lucas Cufré:** currently. Uh yeah, up until last week there were two.  
   
 

### 00:08:59

   
**Lucas Cufré:** This week, one of them had to take a leave of absence because a family member was uh was hospitalized. So I am picking up the the QA tasks for that. Uh but I am also working on other things as well. So I am not as fully develop fully involved in QA as as this person would be would have been.  
**Zen \-:** Okay.  
**Lucas Cufré:** Okay. So I'll keep you guys posted through the telegram channel regarding the state of these issues. Um but moving on uh there was something in that you've raised to me uh today regarding the VMV support and I would like to discuss that a little bit more if it is okay with you.  
**Gregory Chapman's Presentation:** Ju just before we go into that, Luca, there's one thing that I noticed, or rather Naji noticed was missing.  
**Zen \-:** Yeah.  
**Lucas Cufré:** Yep.  
**Gregory Chapman's Presentation:** Um, and this is more on Leo's side, I think, but we don't have P\&L cards in there at the moment.  
**Lucas Cufré:** Mhm.  
**Gregory Chapman's Presentation:** Um, so I flagged this for Leo. The designs he's done um aren't really P\&L cards.  
   
 

### 00:10:11

   
**Lucas Cufré:** Yeah.  
**Gregory Chapman's Presentation:** Um, so I I think he should be working on that right now.  
**Lucas Cufré:** Mhm.  
**Gregory Chapman's Presentation:** But that's something that I I think needed.  
**Lucas Cufré:** Okay.  
**Gregory Chapman's Presentation:** You know, certainly it's it's it's an important thing we need to add in. We can't we can't overlook that even if it is a simple thing.  
**Lucas Cufré:** Okay.  
**Gregory Chapman's Presentation:** Um, so as soon as Leo has that, um, let's get that in place because that that's a very basic thing that I think people will notice is missing.  
**Lucas Cufré:** Okay. Okay. Sure. Sure. Sure. Sure. Uh I remember that we discussed the idea about adding penal cards, but we never got around to how they would work. So if Leo is tackling that, uh it's defining the the design. Uh now we can we can take a look at that.  
**Gregory Chapman's Presentation:** Yeah, the the designs it can be they're quite standardized designs uh for PNL cards.  
**Lucas Cufré:** Mhm.  
**Gregory Chapman's Presentation:** It's not it's not complex in that sense.  
   
 

### 00:11:01

   
**Gregory Chapman's Presentation:** Um we we just need to you know um get them get them done basically.  
**Lucas Cufré:** Mhm. Okay. Okay. Great. That works for me. Um, okay. So, I really want to get deep into this B\&B issue mainly because we have to do some some we have to understand where to tackle this from. So the idea here it's mainly being pushed because Axiom had uh integrated BMV as a sport chain. I understand that they have a pretty massive memecoin ecosystem. From our point of view what we would need to solve are mainly three points of contact. The most important one it's the indexer. The other one it's the wallet the wallet handle. uh yeah the the world management system uh on on uh on the code base and uh the routing service for transactions namely the way that we are handling that for Solena it's by using our own customuilt uh indexer service mainly because uh when we started in Solena there were no readym made solutions that we could uh leverage for the type of system that we wanted to implement on the wallet side.  
   
 

### 00:12:21

   
**Lucas Cufré:** Uh that's already being taken care of mainly because we already solved that EVM compatibility issue when we integrated Hyperlquid. So that would not be a problem per se or we don't expect that to be a problem per se. The two points that are the most uh the most important ones to discuss are the routing system and the indexer. So I've done some quick research regarding the available uh routing services or DEX aggregators however we want to call them. Uh there are several ones we need to uh understand the pricing for each one of those and the the architecture for integration. But as I've seen it, we have 1 in open ocean, punk swap, Rubik and with 1 in being the most mature and with a proven reliability. So the idea for us would be to start understanding the the architecture uh implications for uh this provider mainly than with open ocean because it has the most expensive coverage right after uh 1 in. But the part that I want to discuss in depth is the indexer solution. Um there are a few possibilities.  
   
 

### 00:13:43

   
**Lucas Cufré:** We have the ability to go again with a custom route that would be completely on us and we would be the complete owners of everything from the indexer the indexing of new blocks to the management and maintenance uh of it all. Uh it would take a little bit of time uh to have that solved but uh on the flip side we would have complete knowledge of the inner workings and how to uh keep it up and running. On the other side, uh if we want to leverage ready-made solutions as we've discussed previously with the with R's input, we can go with uh with a ready-made solution like uh the graph which already provides a solution for for EDM uh indexing and it is pretty solid, pretty standard. uh the main situation with that would be that we would add another potential point of rakage and dependency uh on our system. So what I'm trying to say here is let's say that for whatever reason the graph has an outage sort of like what happened with AWS uh we would be tied down to that and we could possibly do nothing about it.  
   
 

### 00:14:59

   
**Lucas Cufré:** We um on the other side if they uh we need to do more research on this but um that is a subscription service and we would be tied down to uh the protocols that they index the speed at which they they keep their teams on maintenance and the way that they upgrade for each one of the iterations on the contracts up and running. Yeah. Martin  
**Martin Aranda:** I just wanted to clarify that sub graph is not uh the graph is not a an out ofthe-box solution. We depend on them for the indexing but exactly what do we want to index and in what uh format that we will get the data is a custom solution. So we may probably need to uh to do still some maintenance there and and support new protocols manually even with that service.  
**Lucas Cufré:** So, Nimly, what I'm trying to get out of this conversation is which level of reliability and dependency are we okay with assuming? Should we go with uh a readym made solution as our first choice and we dive deep into that position or uh do we want to bite the bullet and build uh a completely uh custom one which both are good solutions with their pros and cons?  
   
 

### 00:16:21

   
**Lucas Cufré:** That's what I'm trying to understand.  
**Shak \-:** I think in terms of the graph obviously there's one more issue and that is a latency issue and considering the speed at which we require data um I'm not that confident at the graph honestly uh it is good for dashboard or good for an analytics type of tool but not good for the u the purpose that we have right now and obviously as Martin mentioned uh we still need to um you can say do some of the maintenance work on the graph as Obviously the one costing that we can cut is obviously a storage cost. Uh we don't need to store the data on our end that is totally handled by the graph uh and they will just provide the interface for it. But still we need to build subgraph and all the you can say indexing architecture for it on our end as well. So in my opinion if you ask me I think we should go towards the custom route because that's fast uh we can control that and obviously the latencies is one of the major things that I am looking at right now which can be a bottleneck if we move forward with subgraph at this identical.  
   
 

### 00:17:27

   
**Martin Aranda:** Yes, I believe the same and I'm exploring right now. I've been doing some research on a framework to build indexers on on EVM that is already mature and maybe that will be an hybrid solution because it's a custom design. We will have to interpret the transactions ourselves but it's already built on some foundation. So we wouldn't have to start from scratch and we can ended up serving it to something like click house as we already have for for Salana. I think that will be the the fastest route on on development side but with the requirements of a speed that we need.  
**Lucas Cufré:** Okay. So if we are in agreement there, uh what we're going to be doing uh ideally over today would be to do a deep dive into the research and come up with the document with our uh with our ideas as to how to move forward and a time estimate for such. Just to be super clear on this, we are expecting to manage VNV the same way that we want to uh we we already support Sena.  
   
 

### 00:18:34

   
**Lucas Cufré:** So basically all type of order uh of the order types that we currently support the ability to bridge VMV to to Hyperlid which I am not exactly sure that Hyperlid supports. So, I'm going to review that. And uh pretty much that that's it. Is this uh the the expected route.  
**Zen \-:** I think if Shaib is happy with it, I'm happy with it.  
**Shak \-:** Yeah, Lucas. Yeah, we can do that.  
**Lucas Cufré:** Okay. Okay. then we'll do a deep dive on that and we'll uh send you guys a document with with our research findings and our time estimates.  
**Zen \-:** Would you be able to do the video tonight, Lucas, cuz um I needed to send it before end of week.  
**Lucas Cufré:** Um and regarding the videos in I'm going to be uh retaping it and sending you that uh over the next couple hours. No, no, in like give me a couple of hours and I can send it to you.  
**Zen \-:** Okay. And regarding the document, how long will it take um when to expect it?  
   
 

### 00:19:46

   
**Lucas Cufré:** Martin. Uh, I think we could get something by end of day today.  
**Zen \-:** Perfect.  
**Martin Aranda:** Yeah, sure. I couldn't take some time for that.  
**Zen \-:** Cool. Thank you.  
**Lucas Cufré:** Okay. Uh, aside from that, I know that I still owe you guys an email with uh the information for the next road map. So, I think I can get everything together in a bundle and send it to you guys in the same email.  
**Zen \-:** Awesome.  
**Lucas Cufré:** Great.  
**Naji Osmat:** Lucas, did you did you cover with Zayn what you were telling us about having engineers on on call?  
**Lucas Cufré:** Great.  
**Naji Osmat:** I don't remember where we left off but I think that's to to decide  
**Lucas Cufré:** Yes. No. Yeah. Yeah. Yeah. Completely. I I did discuss that. I've sent an email and we've both agreed on on a way to move forward. The idea would be that once we know that we are going to be adding actual users into the platform, we're going to be uh adding working cards around the clock to to maintain uptime.  
   
 

### 00:20:48

   
**Lucas Cufré:** Uh regarding that and now that you've mentioned it, uh I need to to uh raise two things to you guys. The first one is that uh up until like half an hour ago uh on ramper hasn't uh given us the the thumbs up. So we cannot uh we're going to not start integration on there but they've already charged the the first $200 for the for the service the essential plan that we had agreed on initially. So I don't know guys I I think Greg you told me that you had a direct channel with somebody within the organization. If you can ping this uh to them that would be super appreciated and on the other side uh we need to agree on the initial metrics to start integrating. We are considering posto as a solution for for metric erh tracking which is a a pretty it is a pretty good solution that is pretty much inexpensive but we need to have your uh your thumbs up regarding that. I can resurface the email if you want uh so you can give me the your your thoughts on that.  
   
 

### 00:21:59

   
**Naji Osmat:** Yes, please please read the email.  
**Lucas Cufré:** Does that work?  
**Naji Osmat:** I I know you mentioned this on Monday and I haven't haven't um seen the email.  
**Lucas Cufré:** Okay. Okay. I'll I'll resurface that uh with a follow-up email. And again, if you guys can get in touch with somebody at on Ramper, I would highly appreciate it because that is pretty much the thing that it's keeping us to to test everything from end to end. Great.  
**Zen \-:** Awesome. Thank you, Lucas. Martin Yeah.  
**Gregory Chapman's Presentation:** Thank you Okay, Zane, we're going to carry on the testing. Um, but we'll see what we can we'll see what we can do, basically.  
**Zen \-:** Um I'm traveling back um on Sunday night. So from Monday I'll landing Monday midday I think.  
**Gregory Chapman's Presentation:** Okay. I think Naji also lands on Monday or  
**Zen \-:** Yeah. So I'll um I'll I'll be able to join in on the testing then. I just don't have I don't have my um that specific computer with me right now.  
   
 

### 00:23:31

   
**Zen \-:** So, um, and regarding the speed and stuff, you said it was clunky.  
**Gregory Chapman's Presentation:** Okay. I I've sent Shik and Naji money for testing.  
**Zen \-:** What did you mean by clunky?  
**Gregory Chapman's Presentation:** No, it was more clunky in the sense of the overall feel because in speed it's quite it's quite quick. Speed is not it's not slow. We're putting through different kinds of orders. They're fairly quick. Um but I think the overall impression um no not before.  
**Zen \-:** Have you used Axiom?  
**Gregory Chapman's Presentation:** Um I've used Blex and I've used GMGM. I haven't used actually on I think I think after we fix these things, I think we're okay.  
**Zen \-:** So in comparison to let's say GMGN um did you feel like cooking was a bit like a little bit behind could be improved in the speed category though?  
**Gregory Chapman's Presentation:** I think we're when when you're looking at it's like fractions of a second, isn't it?  
**Zen \-:** Did you feel like compared to GMGN it was a little bit slower but almost there or  
   
 

### 00:24:38

   
**Gregory Chapman's Presentation:** It's not it's not like a big noticeable difference. I'd have to like side by side press a transaction at the same time basically and tell you it  
**Zen \-:** yeah that's what um that's what I'm going to do on Tuesday. Um, I'm just going to do sideby-side comparisons with Padre, GMGN, Axium, uh, Blex, etc. Just to get a feel because, um, it's more than the speed on the trade settlement. It's like how fast things load, how fast the chart loads, stuff like that.  
**Gregory Chapman's Presentation:** Yeah, this is what I mean. I think I think we're we're good up until the point where we have a lot of users, which is what we can't simulate basically.  
**Zen \-:** Yeah. Yeah. Um, I meant more for like, you know, first impressions because Rob and all these guys are like super deep in the trenches and the once we greenlight it in the next couple of days, they're going to get their  
**Gregory Chapman's Presentation:** Um.  
**Zen \-:** first hands on it and they've not they've not used the product ever.  
   
 

### 00:25:28

   
**Zen \-:** Like they've seen videos but they've never used it. So, um, has Leo given an ET on the piano cards?  
**Gregory Chapman's Presentation:** I I think they're more going to notice we haven't got things like P\&L cards at the moment, which is why I mentioned that. Um, so yeah, I I I think I think as long as we fix these things, um, no, I I messaged him this morning and told him what it should be. Um, he had, yeah, he's seen the messages, reacted.  
**Zen \-:** You messaged me group, right?  
**Gregory Chapman's Presentation:** He's he's he's come back. He has responded on it, so he should be working on it now. Um, but his his P\&L cards weren't P\&L cards. I'll show you what he did. His P\&L cards were uh he only did them for mobile for some reason. Um, his P\&L cards were like this. That's not a P\&L card. That's a chart with a share. That doesn't say your P\&L.  
   
 

### 00:26:16

   
**Gregory Chapman's Presentation:** A P\&L card should be like this. It should say how much profit and loss you've made. You know, his P\&L cards were just this is a graph and and a referral code. Um, did you say he did it for mobile?  
**Zen \-:** Didn't you say he did it for mobile?  
**Gregory Chapman's Presentation:** Uh, yeah, he he only did it for mobile. I couldn't find the desktop version. I asked him to tag me the desktop version. He didn't. So, I if I can't find it and he's not tagging yet, he's not done it.  
**Zen \-:** Yeah.  
**Gregory Chapman's Presentation:** Um, so I've asked him to to do them. Um, and then we get those in. But yeah, o overall I think we I think we'll be good. I think they probably will have some feedback. Um, but it's probably high level stuff that we wouldn't pick up on. Um, so long as sexing  
**Zen \-:** As long as as long as yourself, Naji, Ali, and Shakib are being very stringent, then I think they won't pick up on anything to be honest.  
   
 

### 00:27:13

   
**Gregory Chapman's Presentation:** Okay. Yeah. No, I we we've been we've been like the things me Nadi sending it for me and him. Shib sent a couple of points, but the things me and Nad is like um you know the wrong it had the wrong percentage on um profit. So it was taking it um 2% because it was taking it on the it said naji was 2% up um because it was taking it on the whole size but nagi it shouldn't be taking on the whole size it should be taking it on your contribution on purp for example um so yeah the we're we pulled up enough things I think we've given him like 20 or 30 fixes um I think those things will make a  
**Zen \-:** Yeah. Yeah. Yeah.  
**Gregory Chapman's Presentation:** difference so um yeah let's see on Monday when they've got them in. Um we're going to keep testing over the weekend anyway. Um but yeah, when you land, um try it out with Naji. I think I think we'll be I think we'll be good basically to hand over Yeah.  
   
 

### 00:28:17

   
**Zen \-:** Yeah. Okay. Awesome. All right. Just keep updated and then um just keep putting pressure on Lucas because I noticed on the weekend they get super relaxed throughout the weekend.  
**Gregory Chapman's Presentation:** Yeah. No, no worries. I will be on it. Um, I'm also waiting the Q. That's fine.  
**Zen \-:** Just make sure to put pressure on them because Lucas did um say to me that they'll be working throughout the weekend like a few weeks back during the handover period. So, um, just keep putting pressure on them throughout the weekend and let me know if they're not replying or anything.  
**Gregory Chapman's Presentation:** It's fine. I'll keep pressing. Um, I did think their QA should have picked up a lot of these things, but um  
**Zen \-:** Yeah, I thought so, too. They've got um one QA resources paid for, but then there's another that they've added as a gesture because they've first one just f\*\*\*\*\* up so many times.  
**Gregory Chapman's Presentation:** Yeah, Ali Ali picked up a fair few things that I think their QA should have.  
   
 

### 00:29:04

   
**Zen \-:** And um that's why I asked Yeah, I guess that's why we're we're there anyway, though.  
**Gregory Chapman's Presentation:** Um, so yeah. Um, is what it is. We we we got it. Um, I'm also available for Yeah, I think I think that's a thing we've seen across the board with everyone with Danielle with everyone.  
**Zen \-:** Like at the end of the day, like Rob and all these guys could just contact Rob Labs and just do it. Like we're not we're only there because we're quality assurance, you know? So yeah.  
**Gregory Chapman's Presentation:** So, um, yeah. And then QQ, um, I'm waiting for some API talk, some stuff that Jordan's doing.  
**Zen \-:** Yeah.  
**Gregory Chapman's Presentation:** Um, but he he knows he should have that to me by Monday, basically.  
**Zen \-:** Okay. Awesome. Awesome. Yeah. Um I'm going to zero down on a lot of this stuff next week when I'm back. Um, it's just hard here time zone wise and um, even Wi-Fi is like super bad. I don't know why it's just always super bad.  
**Gregory Chapman's Presentation:** Yeah, no worries. No worries. Um, yeah, I think we're good anyway. It's just a lot of stuff they set on top of that.  
**Zen \-:** Yeah. Yeah. Cool. Okay. Let me know if you need anything else for Okay.  
**Gregory Chapman's Presentation:** Cool. No, I think that's everything. Um, yeah. No, I think that's good. I've got most stuff handled. Um, the numbers I gave for you. The number the number I giving you for Danielle. Okay, I'll give you the numbers for the next three months basically.  
**Zen \-:** Uh yeah. Yeah, they're they're okay. They're okay. I also don't want to like push too hard because um we've changed a lot of things recently.  
**Gregory Chapman's Presentation:** Yeah, I think he I think he's compromised with this a lot this time.  
**Zen \-:** So yeah. Yeah.  
   
 

### Transcription ended after 00:32:39

*This editable transcript was computer generated and might contain errors. People can also change the text after it was created.*