# Open source Linux Forensics.



## Collecting Volaite Data
    
    Indecent resport by live anaylsis.

    what do we collect ?

    Date and time:
    * Clock my be skeed
    * Might be diffrent timezone.

    Network interfaces:
    * Funny networks
    * Promiscuous mode ?

    Network connections
    Open ports
    Programs associted with ports
    Running porcess
    Open files
    Routing tables
    Mounted filesystems.
    Loaded Keren modules.



## Architecture
    Client:
        Collecting data.
        Spec:
            Written in Python

    Server:
        Anyalze data.

        Spec:
            Writen in Python + Flask
            Database: TBD

    Docker:
        TBD




