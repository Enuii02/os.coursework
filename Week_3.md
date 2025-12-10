## Stress test:

|             | CPU       | RAM       | I/O       | Network   | Server application |
| ----------- | --------- | --------- | --------- | --------- | ------------------ |
| Application | stress-ng | stress-ng | stress-ng | stress-ng | Minecraft server   |

### Justification 

- Stress-ng was chosen because of its flexibility, safety, and accessibility on different Linux distributions.
- Minecraft game server was chosen because of it's realistic nature. It represents a common real-world workload.

### Installation

#### stress-ng
![Pasted image 20251210120509.png](./images/Pasted_image_20251210120509.png)


#### Minecraft server

installing Java
![Pasted image 20251210120811.png](./images/Pasted_image_20251210120811.png)
![Pasted image 20251210120936.png](./images/Pasted_image_20251210120936.png)

firewall configuration
![Pasted image 20251210121034.png](./images/Pasted_image_20251210121034.png)

Installing the game
![Pasted image 20251210121106.png](./images/Pasted_image_20251210121106.png)

After some additional configuration, the server is running
![Pasted image 20251210121330.png](./images/Pasted_image_20251210121330.png)
![Pasted image 20251210121340.png](./images/Pasted_image_20251210121340.png)

Enter the server from game

![Pasted image 20251210124416.png](./images/Pasted_image_20251210124416.png)

![Minecraft_ 1.18.2 - Multiplayer (3rd-party Server) 10_12_2025 12_53_11.png](./images/Minecraft__1.18.2_-_Multiplayer_(3rd-party_Server)_10_12_2025_12_53_11.png)

The virtual machine could not keep up with the demands. Especially the CPU as indicated by the server console, and memory as shown below.

Cockpit interface
![Pasted image 20251210125432.png](./images/Pasted_image_20251210125432.png)

server console
![Pasted image 20251210125512.png](./images/Pasted_image_20251210125512.png)

after increasing the amount of CPUs to 5 and increasing the available RAM for the virtual machine, the server became stable.

![Pasted image 20251210132640.png](./images/Pasted_image_20251210132640.png)

### Resource profiles

| **Workload**       | **Command**                                             | **CPU**      | **RAM**         | **I/O** | **Network** |
| ------------------ | ------------------------------------------------------- | ------------ | --------------- | ------- | ----------- |
| CPU-Intensive      | `stress-ng --cpu 0 --cpu-method all --timeout 60s`      | High (~100%) | Low             | Low     | None        |
| RAM-Intensive      | `stress-ng --vm 2 --vm-bytes 80% --timeout 60s`         | Low          | High (~80% RAM) | Low     | None        |
| Disk/I/O-Intensive | `stress-ng --hdd 2 --hdd-bytes 2G --io 2 --timeout 60s` | Low          | Low             | High    | None        |
| Network Stack      | `stress-ng --sock 4 --tcp 2 --udp 2 --timeout 60s`      | Low          | Low             | Low     | Moderate    |
| Mixed Load         | `stress-ng --cpu 2 --vm 1 --io 1 --timeout 60s`         |              |                 |         |             |

### Monitoring Strategy

For all applications, the main monitoring approach will be checking the real-time GUI in the Cockpit application. For terminal based monitoring, `htop` can be used in an additional terminal.

---
## Lab activities:

Result for `ps aux` shows a list of running processes. 
- `ps` process status command
- `a` show all users
- `u` format the output
- `x` processes not attached to the terminal
 
![Screenshot 2025-11-28 110344 1.png](./images/Screenshot_2025-11-28_110344_1.png)

Result for `ps -ef`.

![Screenshot 2025-11-28 110553.png](./images/Screenshot_2025-11-28_110553.png)

Result for `top` shows continuously updated list of processes. 

![Screenshot 2025-11-28 110626.png](./images/Screenshot_2025-11-28_110626.png)


Result for `htop`.

![23.png](./images/23.png)

### Linux process states

- (R) Running - The process is running or is waiting for the CPU resources.
- (S) Interruptible/Sleeping - The process is waiting for input/output from the user or other application. It can be interrupted with a signals.
- (D) Uninterruptible sleep - The process cannot be interrupted by signals, usually used while waiting on a hardware condition.
- (Z) Zombie - The process has finished, but the entry is still visible in the table.
- (T) Stopped - The process has been stopped with a signal such as SIGSTOP or SIGSTP

**Process lifecycle**

![Screenshot 2025-11-28 134524.png](./images/Screenshot_2025-11-28_134524.png)

![Screenshot 2025-11-28 134507.png](./images/Screenshot_2025-11-28_134507.png)

![Screenshot 2025-11-28 134545 1.png](./images/Screenshot_2025-11-28_134545_1.png)

### Foreground vs Background

- Foreground process would be used when it is interactive from the terminal.
- Background process would be used when the terminal should be free to access by other processes.

Difference between kill and kill -9

- kill - graceful termination
- kill -9 forceful termination

### Generating SSH Keys

![24.png](./images/24.png)

![Pasted image 20251128171942.png](./images/Pasted_image_20251128171942.png)



The reason why ed25519 is preferred over RSA, is that it is more secure. Because of the elliptic curve cryptography it offers higher security while requiring less resources.

before:

![Pasted image 20251207145326.png](./images/Pasted_image_20251207145326.png)

after:

![Pasted image 20251207145226.png](./images/Pasted_image_20251207145226.png)

Trying to ssh from a different device without the public key

![Pasted image 20251207145807.png](./images/Pasted_image_20251207145807.png)

- `PermitRootLogin` no - disables logging in directly as the root user over ssh
- `PubkeyAuthentication yes` - enables public key authentication 
- `PasswordAuthentication no` - disables password based ssh login

ssh login:

![Pasted image 20251207153848.png](./images/Pasted_image_20251207153848.png)

Setting up firewall from ssh.

![Screenshot 2025-12-07 153621.png](./images/Screenshot_2025-12-07_153621.png)

User creation:

![Pasted image 20251207164704.png](./images/Pasted_image_20251207164704.png)

Administrative tasks

![Pasted image 20251207164927.png](./images/Pasted_image_20251207164927.png)

ssh enter:

![Pasted image 20251207170621.png](./images/Pasted_image_20251207170621.png)

Admin task:

![Pasted image 20251207171249.png](./images/Pasted_image_20251207171249.png)

### Challenges encountered

After making a new admin user on the server virtual machine, I had to add the public ssh key to the `.ssh` folder for the new admin user in order to access the ssh. This had to be done as in the previous task the password authentication has bees disabled and the only way to establish connection was trough public key authentication.


