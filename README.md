# NCNdetector - Next Cloud nude detector
If you admin of small (khe khe ))) ) Nextcloud server, you may want to comply legal rules of your country. So i made a tool that helps me add tags to all photo an Nextcloud service that may be comlay as nude.
Tool analyze user directory on NextCloud server for nsfw files and add tags to files.

Tradeoffs
    taken a NudeDetector as a decoder
    File list, file name for processing takes from Nextcloud but "worker" access it ass locally mounted docker volume - just performance optimization
    due too privacy and legal reason i don't commit dataset for test.
