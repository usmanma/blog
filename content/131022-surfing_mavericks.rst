Surfing Mavericks
#################

:date: 2013-10-22

So today was meant to be for starting of challenge app. 

As usual, distractions were aplenty and so I never got round to it. 

Today was the release of Mavericks_, and with a price tag of free, it was hard 
to resist. As a result I spent most of the day backing up, formatting and fresh 
installing it.

.. _Mavericks: http://www.apple.com/osx/

Setup
=====

First thing to do is download Mavericks from the App Store.

Then simply install it.

TODO: Write full instructions

Some tips that might be useful in mean time:

Disable Dashboard
    To disable the dashboard, type this in terminal::
        
        defaults write com.apple.dashboard mcx-disabled -boolean YES && killall Dock

    Replace **YES** with **NO** to reverse this decision.

Coding
    Generally, I found absolutely no need so far to install homebrew or macports 
    mostly due to the core OS being very up to date once Command Line Tools are 
    installed.
    
    Command line tools have been removed from xcode, so grab them from 
    `Apple Developer website <https://developer.apple.com>`_ and save yourself 2GB of 
    bandwidth. These now also include the latest version of git, as well as a 
    version of hg.
    
    Also Python is now 2.7.5 so no need to overwrite with custom install. Python 
    site-packages are separate from packages installed as part of OS, so there 
    is no worries about cross contamination.
    
    Beyond that if most of your development is done using vagrant with virtualbox 
    you will not need anything.
