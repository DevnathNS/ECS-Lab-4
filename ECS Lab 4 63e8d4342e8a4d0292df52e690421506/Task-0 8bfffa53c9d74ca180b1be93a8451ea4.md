# Task-0

*Description: Create a Host-only Adapter on your VirtualBox for your guest VM. Refer to blog articles and learn how to configure and communicate between host and guest VM using this Network adapter. Using a Host-only Adapter will simplify the remaining tasks.*

**Step 1:** Go to File —> Tools —> Network Manager or click *Ctrl + H* to open the host-only networks menu

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled.png)

**Step 2:** Click on Create. Check “configure adapter manually”

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%201.png)

**Step-3:** Go to the DHCP server tab and check the Enable Server option

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%202.png)

**Step-4:** Click on “Apply” and close

**Step-5:** Go to the network settings of the guest VM and change the adapter to host-only adapter

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%203.png)

## Finding IP address of host machine

Open Network and Sharing Center from the Control Panel and go to the “Change Adapter Options” section. Find the ethernet connection corresponding to the Virtualbox host-only network

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%204.png)

In this case, it is eth3

Now, go to cmd and type in the command *ipconfig*

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%205.png)

Ping it from the guest machine just to be sure

![Untitled](Task-0%208bfffa53c9d74ca180b1be93a8451ea4/Untitled%206.png)