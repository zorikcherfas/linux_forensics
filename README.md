# Open source Linux Forensics.

    
    Indecent resport by live anaylsis.

    what do we collect ?
    
        Using netcat to minimize contamination
        Collecting volatile data
        date and time
        network interfaces 
        funny networks
        promiscuous mode?
        network connections
        open ports
        programs associated with ports
        running processes
        open files
        routing tables
        mounted filesystems
        loaded kernel modules
        Collecting data to determine if dead analysis is justified
        kernel version
        uptime
        filesystem datetime stamps
        hash values for system files
        current user logins
        login history
        system logs
        user accounts
        user history files
        hidden files and directories
        sending off suspicious files for further study
        Dumping RAM
        Making the decision to dump RAM
        Using fmem
        Using LiME
        Using /proc/kcore



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




