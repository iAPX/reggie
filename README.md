# Reggie

Regexp tool.
Regexp to structured language. Structured language to regexp. Unit tests.

I dislike regexp. In fact I hate that.<br/>
Unreadable. Impossible to maintain correctly. Complexity. In many cases used without sanity (numbers).<br/>
And by the way some popular regexp proved to be security holes with time...<br/>

How do I handle that?<br/>
By making regexp readable, testable and eventually useable.<br/>

Read [the story behing Reggie](./doc/STORY.md).

First goal is to generate a regexp identifying a localhost IP Address, including non-normalized and non base 10 ones.
Second goal is to generate a regexp identifying valid email address.


## Usage
`python {command} {filename[.reg]}`

Commands:
- create : ask for a regexp and create the file describing it
- export : export the content of the [.reg] file as a regexp on stdout
- tests : generate tests cases from the file


## Documentation
See [full documentation](./doc/README.md)
