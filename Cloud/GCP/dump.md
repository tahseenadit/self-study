Google core principles include defense in depth, at scale, and by default.
Over time, your design decisions will evolve and change. The change history provides the context that your teams require to align initiatives, avoid duplication, and measure performance changes effectively over time. Change logs are particularly valuable when you onboard a new cloud architect who is not yet familiar with your current design, strategy, or history.
Where feasible, use fully managed services to minimize the risks, time, and effort associated with managing and maintaining baseline systems.

If you're already running your workloads in production, test with managed services to see how they might help to reduce operational complexities. If you're developing new workloads, then start simple, establish a minimal viable product (MVP), and resist the urge to over-engineer. You can identify exceptional use cases, iterate, and improve your systems incrementally over time.

In a loosely coupled architecture, an application can run its functions independently, regardless of the various dependencies.

A decoupled architecture gives you increased flexibility to do the following:

Apply independent upgrades.
Enforce specific security controls.
Establish reliability goals for each subsystem.
Monitor health.
Granularly control performance and cost parameters.
You can start the decoupling process early in your design phase or incorporate it as part of your system upgrades as you scale.

Stateful applications rely on various dependencies to perform tasks, such as local caching of data. Stateful applications often require additional mechanisms to capture progress and restart gracefully. Stateless applications can perform tasks without significant local dependencies by using shared storage or cached services. A stateless architecture enables your applications to scale up quickly with minimum boot dependencies. The applications can withstand hard restarts, have lower downtime, and provide better performance for end users.

Throughput and stability
DORA’s four keys can be divided into metrics that show the throughput of software changes, and metrics that show stability of software changes. This includes changes of any kind, including changes to configuration and changes to code.

Throughput
Throughput measures the velocity of changes that are being made. DORA assesses throughput using the following metrics:

Change lead time - This metric measures the time it takes for a code commit or change to be successfully deployed to production. It reflects the efficiency of your delivery pipeline.
Deployment frequency - This metric measures how often application changes are deployed to production. Higher deployment frequency indicates a more efficient and responsive delivery process.
Stability
Stability measures the quality of the changes delivered and the team’s ability to repair failures. DORA assesses stability using the following metrics:

Change fail percentage - This metric measures the percentage of deployments that cause failures in production, requiring hotfixes or rollbacks. A lower change failure rate indicates a more reliable delivery process.
Failed deployment recovery time - This metric measures the time it takes to recover from a failed deployment. A lower recovery time indicates a more resilient and responsive system.

Infrastructure as a service (IaaS)	IaaS services include Compute Engine, Cloud Storage, and networking services such as Cloud VPN, Cloud Load Balancing, and Cloud DNS.
IaaS provides compute, storage, and network services on demand with pay-as-you-go pricing. You can use IaaS if you plan on migrating an existing on-premises workload to the cloud using lift-and-shift, or if you want to run your application on particular VMs, using specific databases or network configurations.

In IaaS, the bulk of the security responsibilities are yours, and our responsibilities are focused on the underlying infrastructure and physical security.

Platform as a service (PaaS)	PaaS services include App Engine, Google Kubernetes Engine (GKE), and BigQuery.
PaaS provides the runtime environment that you can develop and run your applications in. You can use PaaS if you're building an application (such as a website), and want to focus on development not on the underlying infrastructure.

In PaaS, we're responsible for more controls than in IaaS. Typically, this will vary by the services and features that you use. You share responsibility with us for application-level controls and IAM management. You remain responsible for your data security and client protection.

Software as a service (SaaS)	SaaS applications include Google Workspace, Google Security Operations, and third-party SaaS applications that are available in Google Cloud Marketplace.
SaaS provides online applications that you can subscribe to or pay for in some way. You can use SaaS applications when your enterprise doesn't have the internal expertise or business requirement to build the application themselves, but does require the ability to process workloads.

In SaaS, we own the bulk of the security responsibilities. You remain responsible for your access controls and the data that you choose to store in the application.

Function as a service (FaaS) or serverless	
FaaS provides the platform for developers to run small, single-purpose code (called functions) that run in response to particular events. You would use FaaS when you want particular things to occur based on a particular event. For example, you might create a function that runs whenever data is uploaded to Cloud Storage so that it can be classified.

FaaS has a similar shared responsibility list as SaaS. Cloud Run functions is a FaaS application.

The cloud provider always remains responsible for the underlying network and infrastructure, and customers always remain responsible for their access policies and data.

Simplify system design to accommodate flexibility where possible, and document security requirements for each component. Incorporate a robust secured mechanism to account for resiliency and recovery.

Take humans out of the workstream by automating deployment and other admin tasks.

Shift security left
DevOps and deployment automation let your organization increase the velocity of delivering products. To help ensure that your products remain secure, incorporate security processes from the start of the development process. For example, you can do the following:

Test for security issues in code early in the deployment pipeline.
Scan container images and the cloud infrastructure on an ongoing basis.
Automate detection of misconfiguration and security anti-patterns. For example, use automation to look for secrets that are hard-coded in applications or in configuration.

Be aware that when a Google Cloud organization is created, all users in your domain are granted the Billing Account Creator and Project Creator roles by default. 
