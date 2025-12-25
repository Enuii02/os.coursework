
### Lynis testing

Initial score:
![Pasted image 20251216144745.png](./images/initial_score.png)

After:
![Photoshop_fWNdHTzrWv.png](./images/Photoshop_fWNdHTzrWv.png)

### Network security testing results 

nmap output:
![Pasted image 20251216160714.png](./images/Pasted_image_20251216160714.png)

![Pasted image 20251216160900.png](./images/nmap_output.png)

![WindowsTerminal_ADRqkHXn7Q.png](./images/WindowsTerminal_ADRqkHXn7Q.png)

OS detection:
![WindowsTerminal_wKUzCQRaJs.png](./images/WindowsTerminal_wKUzCQRaJs.png)


### Access Control:

AppArmor output: 
![WindowsTerminal_9j2Pp1pxFr.png](./images/WindowsTerminal_9j2Pp1pxFr.png)

### Running services:

![Pasted image 20251219221601.png](./images/after.png)

#### Important services:

- NetworkManager.service – Manages all network connections; essential for network access.
- ssh.service – Allows secure remote administration of the system.
- apparmor.service – Provides mandatory access control for security.
- auditd.service – Tracks security-relevant events for monitoring and compliance.
- rsyslog.service – Collects and manages system logs for troubleshooting.
- cron.service – Schedules automated system tasks and maintenance jobs.
- systemd-timesyncd.service – Keeps system time accurate via NTP.
- ufw.service – Firewall service for network security.
- open-vm-tools.service – Integration tools for VMware environments.
- pmcd.service – Core daemon for Performance Co-Pilot, important for monitoring system performance.

*More in depth audit done in [Week 5](Week_5.md) lab task section*
