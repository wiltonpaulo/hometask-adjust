# Task 02

## Imagine a server with the following specs:

- 4 times Intel(R) Xeon(R) CPU E7-4830 v4 @ 2.00GHz
- 64GB of ram
- 2 tb HDD disk space
- 2 x 10Gbit/s nics

The server is used for SSL offloading and proxies around 25000 requests per second.

Please let us know which metrics are interesting to monitor in that specific case and how would you do that?  What are the challenges of monitoring this?

---
- Important topics to consider
  - SSL are a bit complex to analyze because performance could be affect for somany factors.
  - Basically the proxy will use a large amount of tcp connections, network traffic, processing SSL handshakes
  - We have to consider what king of encription will be used, because it affects cpu performance.
  - The average size of pages can affects the bandwidth and the time that a process hangs cpu processing.

- I assume that the nginx will be used.
Reason: https://www.nginx.com/resources/wiki/community/why_use_it/

- A good way to monitor the proxy is configure the module ngx_http_status
There a lot of good metrics that we can see in real time like:
    idle and active connections, ssl handshakes, requests, caches, etc
Further information: http://nginx.org/en/docs/http/ngx_http_status_module.html

- Another interesting point for nginx as a reverse proxy with SSL Offloading is that we can use workers to distribute the tasks between processors.
Option: worker_processes 3; (For 3 Intel processors)

- Thinking just to use linux command lines. I sugest the following
  - ifstat - Command line that shows statistics for network traffic
  - iostat(need to install systat) - Command line that shows input and output data to local disk utilization and memory/swap
  - top: command shows and overview with, memory, swap, process, load average and so on.
  - netstat - command line shows a variety of network connections like established, active and wait connections
  - dstat - This command agregates informations about other commands like vmstat, iostat, ifstat, etc

- Netdata
  - By that cenario given, I hardly recommend a netdata instalation. The main reasons are: The good looking dashboard, autodetect and integration with nginx and you can send to other monitoring systems like zabbix or sensu.
  Link to instalation: https://learn.netdata.cloud/docs/agent/packaging/installer/
  Link to plugin: https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/nginx/

- Benchmark
  - Tools like "ab" (apache benchmark) can simulate the real world access. It comes with apache instalation.
  - A good way is randomize requests with a good variety of URLs and simulate the 25k requests.