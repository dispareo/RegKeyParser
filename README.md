# RegKeyParser

# General Info
 - Author: Mark Bayley
 - Data 12/9/2022
 - DSU Project for CSC 840 (Cyber Ops I)
 
# **Introduction**

_**Why a registry parser?**_

This tool is meant to be used in forensic investigations. There are existing registry parsers, but they are slow and usually point and click. Some scripts exist, but they're very heavy and pull out pages and pages of data. This is meant to be a "quick and dirty" and only grabs some of the most common registry keys. It can, of course, be modified to fit your specific corporate environment - chances are, your organization will likely have your own keys you will want to be aware of. 

_**Why do I care?**_

Often, malware will use registry keys as a form of persistence. Shells and base64 encoding are sometimes added to the registry keys and obfuscated.
This script will search for the most common places that malware plants itself (sun as the run and runonce keys that launch upon start/login).

Registry keys are just one part of a forensic investigation, but are often a more tedious part. Modified registry keys are a common Indicator of Compromise, so a quick way to print out the most common keys and values is very valuable in an investigation. Speed is often crucial to an effective triage, containment and remediation strategy, so having a more robust option like reg explorer sacrifices precious time. 

# Three Big Ideas

1. Malware almost always edits registry keys somewhere, somehow. It's just a matter of where. 
2. The ability to quickly detect changes in registry keys can significantly enhance triage and containment.
3. While other registry parsers exist, they are often slow and safe extraction of the hive to run it through another parser can be time consuming. This can be run immediately on a machine if it has python. 

# Future Direction
The next step for this particular script is to add in another script that sorts out scheduled tasks and connections. This also would benefit from improved Threat Intelligence regarding the most common registry keys. 


# Additional Resources
https://resources.infosecinstitute.com/topic/windows-systems-and-artifacts-in-digital-forensics-part-i-registry/
https://www.sans.org/posters/?focus-area=digital-forensics&msc=dfir-lp
