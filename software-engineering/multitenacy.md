## History of multitenant applications
Multitenant applications have evolved from—and combine some characteristics of—three types of services:

**Timesharing**: From the 1960s companies rented space and processing power on mainframe computers (time-sharing) to reduce computing expenses. Often they also reused existing applications, with simply a separate entry field on the logon screen to specify a customer-account ID. On the basis of this ID, the mainframe's accountants could charge the individual customers for CPU, memory and disk/tape usage actually incurred.

**Hosted applications**: From the 1990s traditional application service providers (ASPs) hosted (then-existing) applications on behalf of their customers. Depending on the limitation of the underlying application, ASPs were forced to host applications on separate machines (if multiple instances of the applications could not be executed in the same physical machine) or as separate processes. Multitenant applications represent a more mature architecture[4] which enables a similar service with lower operational cost.

**Web applications**: Popular consumer-oriented web applications (such as Hotmail) developed with a single application instance serving all customers. Multitenant applications represent a natural evolution from this model, offering additional customization to groups of users within (say) the same client organization.

## Differentiation from virtualization
In a multitenancy environment, multiple customers share the same application, running on the same operating system, on the same hardware, with the same data-storage mechanism. The distinction between the customers is achieved during application design, thus customers do not share or see each other's data. Compare this with virtualization where components are transformed, enabling each customer application to appear to run on a separate virtual machine.

In the context of software development, **multitenancy** refers to an architectural approach where a single instance of an application serves multiple customer groups or "tenants" with shared infrastructure, while keeping their data isolated. **Single-tenancy**, in contrast, involves a dedicated instance of the application for each customer, often seen in on-premises software where each client has their own installation of the software on their own servers.

Here's a breakdown of why supporting both a multitenant (cloud-based) version and a single-tenant (on-premises) version of a product can be costly for software vendors:

1. **Two Distinct Architectures**: Multitenant applications are usually designed from the ground up to handle multiple users or organizations within the same instance, with built-in data isolation and security features to prevent data crossover. In single-tenant systems, however, each tenant has its own isolated environment, which is simpler to set up for a single tenant but does not scale well across many customers. Converting a single-tenant app to support multitenancy often requires substantial architectural changes, such as redesigning the database structure, adding layers of access control, and enhancing resource management to handle different tenants’ data securely.

2. **Maintenance and Feature Parity**: Supporting two distinct products—a multitenant version for the cloud and a single-tenant version for on-premises customers—means maintaining separate codebases or extensive configuration differences. When new features are added, the development and testing teams must ensure they work correctly in both versions, which increases development time, testing complexity, and maintenance costs.

3. **Infrastructure and Support Costs**: Multitenant applications often require infrastructure designed to support multiple clients dynamically, such as scaling server resources based on demand, automating data backups, and managing shared resources like storage and databases. For single-tenant, on-premises customers, vendors might also need to provide additional support, such as helping customers with their own installations, monitoring issues, and troubleshooting, which increases overall support costs.

4. **Security and Compliance**: Multitenant systems need extra layers of security and compliance to protect data privacy across multiple tenants in the same environment. For single-tenant, on-premises setups, security and compliance configurations can differ based on each client’s environment, adding further overhead.

### Why the Cost Impact?
Maintaining two architectures creates redundant work and limits the vendor's ability to focus exclusively on a single product. These costs often stem from the need to:

- Hire additional development and support staff.
- Increase testing to ensure stability and compatibility across two environments.
- Handle different deployment and release processes.
- Offer customized support and maintenance, particularly for on-premises versions.

In essence, vendors supporting both multitenant (typically cloud) and single-tenant (on-premises) versions must balance the needs of two different products. This leads to higher operational costs, slower innovation cycles, and sometimes difficult trade-offs in feature delivery.

An increasingly viable alternative route to multitenancy that eliminates the need for significant architectural change is to use virtualization technology to host multiple isolated instances of an application on one or more servers. Indeed, when applications are repackaged as virtual appliances the same appliance image can be deployed in ISV hosted, on-premises or trusted-third party locations and even migrated from one deployment site to another over time.
