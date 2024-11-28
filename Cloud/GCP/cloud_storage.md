# How does Cloud Storage work?
Cloud Storage uses remote servers to save data, such as files, business data, videos, or images. Users upload data to servers via an internet connection, where it is saved on a virtual machine on a physical server. To maintain availability and provide redundancy, cloud providers will often spread data to multiple virtual machines in data centers located across the world. If storage needs increase, the cloud provider will spin up more virtual machines to handle the load. Users can access data in Cloud Storage through an internet connection and software such as web portal, browser, or mobile app via an application programming interface (API).

Cloud Storage is available in four different models:

### Public
Public Cloud Storage is a model where an organization stores data in a service provider’s data centers that are also utilized by other companies. Data in public Cloud Storage is spread across multiple regions and is often offered on a subscription or pay-as-you-go basis. Public Cloud Storage is considered to be “elastic” which means that the data stored can be scaled up or down depending on the needs of the organization. Public cloud providers typically make data available from any device such as a smartphone or web portal.

### Private
Private Cloud Storage is a model where an organization utilizes its own servers and data centers to store data within their own network. Alternatively, organizations can deal with cloud service providers to provide dedicated servers and private connections that are not shared by any other organization. Private clouds are typically utilized by organizations that require more control over their data and have stringent compliance and security requirements.

### Hybrid
A hybrid cloud model is a mix of private and public cloud storage models. A hybrid cloud storage model allows organizations to decide which data it wants to store in which cloud. Sensitive data and data that must meet strict compliance requirements may be stored in a private cloud while less sensitive data is stored in the public cloud. A hybrid cloud storage model typically has a layer of orchestration to integrate between the two clouds. A hybrid cloud offers flexibility and allows organizations to still scale up with the public cloud if need arises. 

### Multicloud
A multicloud storage model is when an organization sets up more than one cloud model from more than one cloud service provider (public or private). Organizations might choose a multicloud model if one cloud vendor offers certain proprietary apps, an organization requires data to be stored in a specific country, various teams are trained on different clouds, or the organization needs to serve different requirements that are not stated in the servicers’ Service Level Agreements. A multicloud model offers organizations flexibility and redundancy.

# Use case problems

## Problem 1
I am currently experiencing an issue with the resolution of Cloud Storage domain from one of my servers. I have two servers hosted by different cloud providers. When resolving storage.googleapis.com on one of my servers, Google's name servers return an IP address located in Amsterdam (for example 142.250.179.187). This is unexpected because both my server and Google's datacenter are located in the US. So the request from my server goes through datacenter in Europe and back to the US resulting in a significant latency. My other server, hosted by a different provider, resolves the domain correctly (142.251.116.207) and there are no latency issues.


### **Understanding the Problem**
When your machine tries to connect to `storage.googleapis.com` (Google Cloud Storage) domain, it needs to figure out the IP address for that domain name. This process is called **DNS resolution** (Domain Name System resolution). Here's what's happening:

1. **Server 1 (Problematic Server):**
   - When Server 1 asks Google's name servers for the IP address of `storage.googleapis.com`, it is given an IP address in Amsterdam (e.g., `142.250.179.187`).
   - This is strange because your server is located in the US, and you'd expect it to connect to a nearby data center in the US if your cloud storage location is US.
   - Instead, the request goes to Amsterdam (in Europe) and then back to the US, causing high latency (a delay in data transfer).

2. **Server 2 (Working Server):**
   - Server 2 resolves `storage.googleapis.com` to an IP address in the US (e.g., `142.251.116.207`).
   - Because the data doesn’t travel far, there’s no latency issue.

The root of the problem seems to be **how Server 1 resolves the domain name**. This could be due to:
   - A misconfigured DNS resolver on Server 1. Server 1 asks the wrong DNS Server for the IP address of `storage.googleapis.com`. Or, the DNS server has the wrong IP address for `storage.googleapis.com`.
   - The DNS server used by Server 1 (e.g., your hosting provider's DNS or custom DNS settings) returning suboptimal(Too much optimization) results. Like it has returned an IP address for some other request before and cached it and suboptimally returning that IP address from the cache. 

---

### **Why Does This Happen?**
When you ask for the IP address of a domain, your server contacts a **DNS server** to get an answer. Depending on the DNS server it uses:
- It may give you the nearest IP address of the requested domain to your server.
- Or, it may give you an IP address based on the DNS server’s own location (not your server’s location).

In this case, the DNS server used by Server 1 seems to be returning an IP address in Europe because:
- It might be configured poorly. DNS server has IP address in Amsterdam against the domain name `storage.googleapis.com`.
- It might not correctly account for your server's actual location.

---

### **Steps to Fix the Issue**
Here’s how you can troubleshoot and resolve this problem:

#### **1. Check Your Server's DNS Settings**
   - DNS settings determine which DNS server your server uses to resolve domain names. Check which DNS server Server 1 is using:
     - If it's your hosting provider's default DNS, consider switching to a public DNS service like **Google Public DNS** or **Cloudflare DNS**.
   - To change the DNS settings:
     - Edit your `/etc/resolv.conf` file (Linux).
     - Add the following lines for Google Public DNS:
       ```
       nameserver 8.8.8.8
       nameserver 8.8.4.4
       ```
     - Or, for Cloudflare DNS:
       ```
       nameserver 1.1.1.1
       nameserver 1.0.0.1
       ```
     - Save the file and restart your network service.

#### **2. Flush Your DNS Cache**
   - Your server might be caching the incorrect IP address. Flushing the DNS cache will force the server to resolve the domain name again.
   - Run the following command:
     ```
     sudo systemd-resolve --flush-caches
     ```
   - Alternatively, restart the DNS resolver service:
     ```
     sudo systemctl restart systemd-resolved
     ```

#### **3. Test Domain Resolution**
   - After updating the DNS server settings, check if `storage.googleapis.com` resolves to a US-based IP address:
     ```
     nslookup storage.googleapis.com
     ```
   - Look for an IP address starting with `142.251...` (indicating a US-based data center).

#### **4. Verify Google Cloud Storage Bucket Region**
   - If you control the Google Cloud Storage bucket, confirm that it is located in the **US region**. Even though this is less likely to be the issue, mismatched bucket regions could contribute to routing inefficiencies.
   - To check or change the bucket’s region:
     - Go to the Google Cloud Console > Storage > Buckets.
     - Review the region listed for your bucket (e.g., `us-central1` or `us-east1`).

#### **5. Try From Another DNS Server**
   - If you still face issues, try running the DNS query from another server or tool to verify that the problem is isolated to Server 1:
     ```
     dig storage.googleapis.com @8.8.8.8
     ```
   - Replace `8.8.8.8` with other public DNS servers to compare results.

#### **6. Contact Your Hosting Provider**
   - If the issue persists, your hosting provider's DNS configuration might be causing the problem. Contact their support and explain the issue.

---

### **Preventing Similar Issues in the Future**
1. **Use Reliable DNS Services:** Public DNS providers like Google (8.8.8.8) or Cloudflare (1.1.1.1) are optimized for performance and usually provide accurate results.
2. **Verify Bucket Region:** Ensure your data and servers are in geographically aligned regions.
3. **Regular Monitoring:** Periodically test domain resolution to catch and address anomalies early.

## Problem 2
We have 3 different Google Cloud Storage buckets from which we are continuously deleting objects, based on an object-specific retention period (our own business logic). One bucket ("bucket 1") is multi-region (us), and the other two ("buckets 2 and 3") are regional (us-central1). Right now, we are averaging around 18 deletes per second on bucket 1 (multi-region), 30 deletes per second on bucket 2, and 220 deletes per second on bucket 3. These deletes are performed by Node.js workers running in GKE pods, also running in us-central1. 

Our bucket 3 deletes are obviously the highest-throughput. They are on their own, separate 5 GKE nodes. However, at times, bucket 3 deletes will pause, and when that happens, the rate of deletes for buckets 1 and 2 will jump to about 90 deletes/second.

We have also seen similar correlation between delete and write/upload throughput, although it's more complicated to compare, since uploads are customer-driven.

Given these are 3 entirely separate buckets, it doesn't seem like they should bottleneck each other with deletes. Also, none of these buckets are exceeding the 1,000/s API limit for write/upload; the closest is bucket 3 which sometimes peaks around 850/s, but doesn't reach 1,000.

Are there shared resources that could be causing these throughputs to be shared?

Yes, there are shared resources in Google Cloud Storage that could explain why the throughput of one bucket affects others, even though the buckets are separate. Here’s what’s happening under the hood:

---

### **Shared Resources in Google Cloud Storage**
Google Cloud Storage manages requests through an extensive backend infrastructure. Even though your buckets are logically distinct, some of the underlying systems are shared, especially when buckets and operations are in the same region.

#### **1. Regional Resource Contention**
- **How it works:**
  - Buckets in the same region (`us-central1` in your case) share certain infrastructure, like:
    - **Load balancers** that handle incoming requests.
    - **Storage servers** that manage the physical storage of data.
    - **Network bandwidth** within the region.
  - Operations (like deletes or uploads) from multiple buckets may compete for these shared resources.

- **Impact:**
  - When Bucket 3 has a high delete throughput, it may use a significant portion of these shared resources, leaving less for Buckets 1 and 2.
  - When Bucket 3 pauses, those resources are freed up, allowing Buckets 1 and 2 to process their operations faster.

---

#### **2. Backend Throttling**
- **How it works:**
  - Google Cloud enforces certain **quota limits and throttling** mechanisms to prevent any single user or workload from overloading the system. These limits can be:
    - **Per-bucket limits** (like 1,000 operations per second for write/delete operations).
    - **Regional limits** (a hidden limit that applies to all operations within a region).
  - If the backend detects high usage from one bucket (e.g., Bucket 3’s 220 deletes/second), it might slow down that bucket or throttle overall usage within the region to maintain stability.

- **Impact:**
  - When Bucket 3’s activity is throttled, Buckets 1 and 2 might temporarily have more access to backend resources, leading to a spike in their throughput.

---

#### **3. API Request Management**
- **How it works:**
  - API requests (like deletes, uploads, or metadata updates) are processed through shared **API gateways** and backend service endpoints in each region.
  - If many requests are coming from your GKE workers in `us-central1` for Buckets 2 and 3, the API gateway might prioritize or balance these requests dynamically.

- **Impact:**
  - High activity from Bucket 3 could temporarily saturate the API gateway, causing delays for Bucket 2 or even Bucket 1 (despite Bucket 1 being multi-regional).

---

#### **4. Network Bandwidth and GKE Location**
- **How it works:**
  - Your GKE pods and regional buckets are all in `us-central1`. These pods connect to Cloud Storage through Google’s internal network, which has immense capacity but is not unlimited.
  - If Bucket 3’s workers are making a very high volume of requests, they might saturate your connection or hit bandwidth limits.

- **Impact:**
  - Even if Bucket 1 is multi-regional, the requests to it are coming from `us-central1`, so they could still be affected by contention in that region.

---

### **Why Shared Resources Cause Throughput Correlation**
Because these buckets and operations share the same backend infrastructure, their performance isn’t completely isolated. High activity in one bucket can create contention for shared resources, leading to:

1. **Bottlenecks**: When one bucket is heavily used (e.g., Bucket 3), it might dominate backend resources, slowing down others.
2. **Dynamic Resource Reallocation**: When a busy bucket slows down or pauses, resources are freed up, allowing other buckets to process requests faster.

---

### **What Can Be Done to Reduce Resource Sharing?**
Here are some strategies to minimize the impact of shared resources:

1. **Use Batch Deletes** (which you’re already doing):
   - These reduce the number of API calls, lowering the chance of hitting regional API or resource limits.

2. **Separate Buckets by Region**:
   - Moving buckets or GKE workers to different regions can prevent them from competing for the same resources.

3. **Distribute Requests Across Time**:
   - Stagger operations for different buckets to avoid simultaneous high activity.

4. **Monitor and Optimize Quotas**:
   - Use Cloud Monitoring to track resource usage, latency, and errors. Adjust workflows if you see one bucket dominating resources.
  
#### Why Does It Work Better?
Batch deletes solve many of the problems you were having because they reduce the number of API calls and optimize how Google Cloud handles your requests:

**Fewer API Calls = Less Overhead:**

Before, each delete required its own API call. This means:
- Each call took time to establish a connection.
- Each call added to your total regional API quota.
- With batch deletes, a single API call replaces hundreds of smaller ones, drastically reducing overhead.

**Better Backend Efficiency:**

Google Cloud’s backend can handle batch operations more efficiently because:
- It processes the requests in bulk, reducing the time spent managing individual connections.
- It can optimize how it performs these operations internally.

**Reduces Regional Resource Contention:**

Batch operations are less likely to hit hidden regional limits because they’re processed differently. Google Cloud can prioritize them more effectively and avoid the bottlenecks caused by many small, separate requests.

**Improved Throughput:**

With batch deletes, you’re now achieving up to 500 deletes per second, which is far beyond what you managed with individual delete calls. This means you can clean up your buckets faster and more reliably.

**Decoupling Effects Between Buckets:**

Batch deletes minimize the impact of one bucket's activity on another. Since you're using fewer overall API calls, the regional backend isn’t overloaded, so operations on one bucket no longer interfere with others.
