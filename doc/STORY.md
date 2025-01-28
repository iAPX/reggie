# The story behind Reggie

On an interview by a "tech lead", I was asked to write a Regexp to identify "the" localhost IP[v4] Address.<br/>
I stared at him, and then told that it was too long for the half-four remaining.<br/>
He thought I was dumb. He took me time to understand he didn't understand his own question.<br/>

Four important points about localhost and its IP addresses representations:<br/>
- localhost is *NOT* 127.0.0.1 but 127.0.0.1/8 (IPv4)
- IPv4 adresses could be expressed in base 10 (decimal), base 8 (octal) or base 16 (hexadecimal)
- IPv4 adresses don't have to be normalized (base 10 x.y.z.a) and could be expressed as x, x.y, x.y.z, for example 2130706433 is correct for normalized base 10 127.0.0.1!
- regexp is not the right tool to play with numbers, definitely

On the security side:<br/>
- It was a question about security and first thing first you should go from domain or IPv4 address to normalized base 10 IPv4 address. IPv6 is a total different story.
- Then you should identify any private IPv4, that should include the one of your server, starting with "127", "192.168", "176" and so on.
- No regexp needed in fact with base 10 normalized IPv4 adresses. Waste of time, CPU ressource, memory, for nothing!
- You could also use unsigned 32 bit arithmetic and logic operations for IPv4. Faster way.

This experience motivated me to create Reggie, a tool to write regexp, and also enable me to eventually answer this problem in decimal, octal and hexadecimal and with different IPv4 addresses notations for 127.0.0.1/8.
And thus prove it is incredibly complex and as often for regexp a sink hole.

Second funny goal: create an email validation regexp respecting RFC and its unit tests.
And yes _@2130706433 is a perfectly valid email address, 127.0.0.256 is not an IP address but a subdomain name, main domain being "256".
