In order to use this program, you will have to install and operate a virtual machine with Vagrant and Virtual Box.

If you haven't already installed them, the instructions to do so are as follows:

	1. Download VirtualBox from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
		a. Install the platform package for whatever OS you have.

	2. Download Vagrant from: https://www.vagrantup.com/downloads.html
		a. Install the version for the OS you have.
			i. If you're on Windows, make sure to grant network permissions to Vagrant or make a firewall exception when prompted.


Whether or not you've already installed Vagrant and a Virtual Machine, do the following:

	3. Download and unzip the file for FSND-Virtual-Machine:
https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
		a. If you're using Windows, you may get a time-out error. To fix it, you've got to use a new Vagrant file configuration to replace your current Vagrant File, you can get it here:
		https://s3.amazonaws.com/video.udacity-data.com/topher/2019/March/5c7ebe7a_vagrant-configuration-windows/vagrant-configuration-windows.zip
	    b. Get onto your terminal and type out “cd Downloads/FSND-Virtual-Machine/vagrant” (This is assuming that FSND-Virtual-Machine is in the Downloads folder, otherwise enter the name of the folder it's located in instead of Downloads.)
		i. Then, enter "vagrant up" to set up the virtual machine. Once it's done downloading and installing, enter "vagrant ssh" to log in to the machine.



If you've followed the above steps, your virtual machine should be ready to go. The next step is to place the folder you've downloaded which contains this README, "catalog" inside of the vagrant folder in FSND-Virtual-Machine. Replace the "catalog" that is already inside the vagrant folder with this one.


Now, assuming you're logged in to the machine (you can log back in at any time by cd-ing into the vagrant folder and typing "vagrant ssh"), follow these next steps to run the program:


	1. Enter "cd /vagrant" to go to the vagrant directory.
	2. Enter "cd catalog" to enter the catalog directory.
	3. Enter "python database_populate.py" before you run the project proper! This creates the categories for users to put their items into. This is crucial!
		a. If you have a version of python other than plain python, you may have to add the version number to the query above, such as "python3 database_populate.py". You'll have to do this for the next query as well.
	4. Now, enter "python project.py" to start up the web server!


Once you've done this, the web server is up and ready to go! To get to your new web server, just boot up the web browser of your choice and type in the search bar:

	http://localhost:5000

You'll then be taken to the website's main page! From there, you can log in by clicking the "Login" text in the top right corner, and once you're on the login page, click the Google+ sign-in button in the top left and follow directions from there. Once you're logged in, the website will let you know, and you're clear to begin creating, editing, and deleting items from the site!

The way you do this is simple: just click on the Category you'd like to add/edit/delete an item in. If you're creating an item, click the "Add Item" button, and from there you can add a name and description and have it committed with just a press of the submit button! If you're editing or deleting, click the text that says "Edit" or "Delete" under an item, and if you're the one who added that item in the first place you'll be taken to another page where you can choose whether or not to go through with it. If you don't own an item, you won't be able to edit or delete it!

Once you're ready to log off, click the "Logoff" button in the top-right corner or any given webpage on this site, and you'll be securely logged off! While logged off, obviously you can't edit or delete items, but you also can't create anything.

Have fun!

