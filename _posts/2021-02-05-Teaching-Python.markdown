---
layout: post
title:  "Python in an afternoon"
date:   2020-10-20 12:00:00 +0100
categories: made_things
---

When I started my PhD at the John Innes Centre (JIC),
I knew that I wanted to get involved with its [international undergraduate summer school][iuss],
which I had attended as a student.

At the organising meeting, I volunteered to take charge of the bioinformatics training.
I was given an afternoon to teach the undergrads something useful about coding - a
tall order, especially given their varied levels of experience.

During my degree, I had taught myself Python using the excellent [Computating For Biologists][cfb]
by Ran Liebeskind-Hadas and Eliot Bush, supplemented with problems on [Rosalind][ros].
I decided to use the latter for the training session as it has short coding problems
centred around biological themes which validate the output of your program. This meant
I could set everyone off on the same tasks, they would be marked automatically and
everyone could progress at their own pace.

Most of the students didn't know any Python already, and a few hadn't done any coding
at all, which is where [replit][replit] came in. I had been introduced to
the site when I was on the summer school as a way for us all to run code, but I thought
I could take it a little further for my class. I set up a few repls to demonstrate
different parts of the session. The first was a biological 'Hello World' - [calculating][gcrepl]
the [GC content][gcc] of a short strand of DNA. This is a nice example to introduce
some basic coding concepts: variables, functions, loops and flow control. Then I set them
off with two sets of hints. One was a [quick guide][qg] to some Python concepts they would
need, and the other was a set of [templates][templates] to give them some ideas about
how to tackle each problem from an algorithmic and syntactic point of view. I also
gave them printed cheat sheets with some syntax reminders so they wouldn't be constantly
switching tabs.

With guides set up, they were able to jump in and start coding. I had several PhD
students and postdocs with me to help give one-to-one advice in the class, though
they didn't need too much of it; most of them were keen to see how much they could
do independently. Overall, both years that I have run the course
(last year's summer school was cancelled due to the pandemic) I've been impressed
with how quickly the students get into the tasks. The core approach of attempting
simple problems allows them to build up confidence, and the [replit][replit] platform
is great both for distributing my code and letting them experiment with their own.

[iuss]:https://www.jic.ac.uk/training-careers/summer-schools/international-undergraduate/
[cfb]: https://www.cs.hmc.edu/twiki/bin/view/CFB
[ros]: http://rosalind.info
[replit]:https://repl.it
[gcc]: https://en.wikipedia.org/wiki/GC-content
[gcrepl]: https://repl.it/@sam_deans/GCcontentcalculator#main.py
[qg]: https://repl.it/@sam_deans/Starting-out-with-Python-3#main.py
[templates]:https://repl.it/@sam_deans/Rosalind-Templates#main.py
