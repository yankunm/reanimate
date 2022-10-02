#  Reanimate
## The codebase of Reanimate for SBUHack 2022
## Team members: YanKun (Alex) Meng, Jeffery Luo, Federick Yeh, Xingzhi (Jacky) Guo

## Inspiration

You've had a full day of classes. You grumble as you find a seat in the library, finally forced to study. You flip open the textbook to page 727, only to be greeted by a wall of text and a single image along the margin. How eager are you to power through? Not very, is probably your answer. reanimate aims to use AR to reinvent the way you read textbooks, keeping you engaged and constantly learning. reanimate will also enable authors and publishers, particular in academia, to communicate to their audiences more effectively.

## What it does

We realize that when learning any subject, understanding the process is much more important than just seeing the final result. Animations are the perfect resource here, but not feasible for physical (or even digital) prints. Through the use of AR, reanimate will bring all the static figures in your textbooks to life, unlocking a completely new way to learn at the tip of your fingers. And to all authors and publishers: we're offering a new way to make all your resources more accessible and to curate feedback about the usage and effectiveness of your works.

## How we built it

Using Python and OpenCV, we were able to construct a working prototype that uses your webcam feed or a network camera feed. By detecting and matching markers, we can isolate the region that marker(s) occupy and overlay the desired animation on top, adjusting for perspective.

## Challenges we ran into

One of the challenges we ran into was polishing a front-end for reanimate. While we were able to simulate the look and feel of our project on a webpage, the I/O cost of reading and writing individuals frames rendered reanimate infeasible for real-time use. We ultimately decided to put a pause on our work in this direction, but we're confident that with some more time, reanimate will be able easily accessible to our users via the web.

## Accomplishments that we're proud of

We're extremely proud that a we were able to create a working prototype within the span of this 48 hour hackathon. All of our team members are very passionate about this project, as it aims to solve a problem very close to our hearts and to the hearts of all college students around the world. Out next steps are very clear, and you can bet we'll take this project as far as it'll go!

## What we learned

Through our collaboration on this journey, we were each able to gain insight into various computer vision tools and libraries, learning their inner workings and applying them in a creative setting. We also explored the state of AR technology, in particular the difference between marker and marker-less AR and how they are each implemented.

## What's next for reanimate

Our next steps are headed towards greater immersion. One way we intend to accomplish this is by removing the reliance on markers, so that there can be a truly seamless experience from image to animation. We're also trying to support 3D animations, which will enable our users to transmit and receive knowledge on another level.
