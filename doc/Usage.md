# Usage
`python {command} {filename[.reg]}`

Commands:
- create : ask for a regexp and create the file describing it
- export : export the content of the [.reg] file as a regexp on stdout
- tests : generate tests cases from the file


## create
Create a [.reg] file describing formally the regexp.<br/>
Even if some optimizations are done, it might not be optimal, but it would be readable.<br/>
Readability and understandability of regexp is one of the goal of this project.


## export
Export the formally defined regpex from the file as a regexp string.<br/>
It might also not be optimal, but will totally respect what you entered on this file, either manually by creating/editing it, either automatically through the "create" process.


## tests
Generate on stdout the different test-case:<br/>
- Should pass
- Should fail

Notice that all cases won't be covered as it might lead to an exponential expansion.<br/>
What will be typically covered:
- One or two pass cases for each terminal node, for example 'A' and 'Z' for A-Z, or 'x' for x.
- One or two fail cases for each terminal node, for example '@' and '[' for A-Z, or 'y' for x.
- One pass and one fail case for maximum repetition numbers or length when specified
- One fail case for each lacking a subpart, for example 'xx', 'Ax', 'xA' for xA-Zx (3 fail case for 3 subpart)
