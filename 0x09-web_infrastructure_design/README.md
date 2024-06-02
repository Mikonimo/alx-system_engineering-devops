## README

This repository contains three tasks for designing web infrastructures with increasing levels of complexity, from a simple web stack to a secured and monitored distributed web infrastructure. Each task is designed to teach and explain key concepts in web infrastructure design, including server roles, DNS, load balancing, security, and monitoring.

### Task 0: Simple Web Stack

#### Overview

A simple web stack is often composed of a single server with all necessary components to host a website. In this task, we design a one-server infrastructure to host a website reachable via www.foobar.com.

#### Requirements

- **1 server**
- **1 web server (Nginx)**
- **1 application server**
- **1 set of application files (your code base)**
- **1 database (MySQL)**
- **1 domain name (foobar.com) configured with a `www` record that points to your server IP (8.8.8.8)**

#### Concepts to Explain

1. **Server**: A physical or virtual machine that hosts the entire web infrastructure, running all necessary software components.
2. **Domain Name**: A human-readable address (foobar.com) that points to the server's IP address (8.8.8.8). It allows users to access the website easily.
3. **DNS Record (www)**: The `www` record in `www.foobar.com` is a CNAME record that points to the server's IP address. This record helps route traffic to the correct server.
4. **Web Server (Nginx)**: Handles incoming HTTP requests, serves static files, and forwards dynamic requests to the application server.
5. **Application Server**: Runs the application code (e.g., PHP, Python) to generate dynamic content and handle business logic.
6. **Database (MySQL)**: Stores and manages data for the website. The application server interacts with the database to retrieve and store data.
7. **Communication**: The server communicates with the user's computer via HTTP/HTTPS, sending and receiving requests and responses.

#### Issues with this Infrastructure

- **Single Point of Failure (SPOF)**: If the server fails, the entire website goes down.
- **Downtime for Maintenance**: Updating or deploying new code requires restarting services, causing temporary downtime.
- **Scalability**: A single server may struggle with high traffic, leading to performance issues or outages.

#### File

- [0-simple_web_stack](https://github.com/Mikonimo/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/0-simple_web_stack)

### Task 1: Distributed Web Infrastructure

#### Overview

In this task, we design a more robust infrastructure with multiple servers, a load balancer, and a primary-replica database setup to improve performance and reliability.

#### Requirements

- **2 servers**
- **1 web server (Nginx)**
- **1 application server**
- **1 load-balancer (HAproxy)**
- **1 set of application files (your code base)**
- **1 database (MySQL)**

#### Concepts to Explain

1. **Additional Elements**: 
   - **Load Balancer**: Distributes incoming traffic across multiple servers to balance the load and improve availability.
   - **Primary-Replica Database**: Ensures high availability and scalability. The primary node handles write operations, while replicas handle read operations.
2. **Load Balancer Distribution Algorithm**: The algorithm (e.g., round-robin, least connections) determines how traffic is distributed across servers. Round-robin distributes traffic evenly, while least connections sends traffic to the server with the fewest connections.
3. **Active-Active vs. Active-Passive Setup**:
   - **Active-Active**: Both servers are actively handling traffic, improving load distribution and fault tolerance.
   - **Active-Passive**: One server is active while the other is on standby, ready to take over if the active server fails.
4. **Primary-Replica Cluster**: The primary node handles all write operations, while replica nodes handle read operations. Replicas are synchronized with the primary to ensure data consistency.
5. **Infrastructure Issues**:
   - **SPOF**: Still present if the load balancer or primary database fails.
   - **Security**: No firewall or HTTPS, leaving the system vulnerable to attacks.
   - **Monitoring**: Lack of monitoring makes it difficult to detect and respond to issues.

#### File

- [1-distributed_web_infrastructure](https://github.com/Mikonimo/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/1-distributed_web_infrastructure)

### Task 2: Secured and Monitored Web Infrastructure

#### Overview

This task involves designing a secure and monitored web infrastructure that serves encrypted traffic and includes multiple servers, firewalls, and monitoring tools.

#### Requirements

- **3 firewalls**
- **1 SSL certificate to serve www.foobar.com over HTTPS**
- **3 monitoring clients (data collectors for Sumologic or other monitoring services)**

#### Concepts to Explain

1. **Additional Elements**:
   - **Firewalls**: Protect the servers by controlling incoming and outgoing network traffic based on security rules.
   - **SSL Certificate**: Encrypts traffic between the user's browser and the server, ensuring data security and integrity.
   - **Monitoring Clients**: Collect and send data to monitoring services for analysis and alerting.
2. **Firewalls**: Provide a barrier between the trusted internal network and untrusted external networks, helping to prevent unauthorized access.
3. **HTTPS Traffic**: Ensures data transmitted between the user and the server is encrypted and secure.
4. **Monitoring**: Used to track the performance and health of the infrastructure, detect issues, and alert administrators.
5. **Data Collection by Monitoring Tool**: Monitoring clients collect metrics (CPU usage, memory usage, request rates) and send them to a central monitoring service.
6. **Monitoring Web Server QPS (Queries Per Second)**: Set up monitoring to track and analyze the number of requests per second handled by the web server, helping to identify performance bottlenecks.
7. **Infrastructure Issues**:
   - **SSL Termination at Load Balancer**: Can expose unencrypted traffic between the load balancer and application servers.
   - **Single MySQL Write Server**: Limits write scalability and introduces a SPOF for write operations.
   - **Homogeneous Server Components**: Running all services on every server can lead to resource contention and complex maintenance.

#### File

- [2-secured_and_monitored_web_infrastructure](https://github.com/Mikonimo/alx-system_engineering-devops/blob/master/0x09-web_infrastructure_design/2-secured_and_monitored_web_infrastructure)
