# Identity
An identity is a name that uniquely identifies the person who is interacting with a Google service. Google uses email addresses for this purpose. A person's email address is considered that person's Google identity.


To use Google Cloud, users and workloads need an identity that Google Cloud can recognize.

# Authentication
The process of verifying the association between a person and an identity is called authentication or sign-in, making the person prove that this is indeed their identity. A person might have multiple email addresses. Because Google services use an email address as identity, such a person would be considered to have multiple identities

# Identity vs User Account

Identity and user account are not same. We associate identity with a user account. A user account is a data structure. So a user account has attributes. User accounts are not created on the fly, but need to be provisioned before the first sign-on. 

In most cases, there is a one-to-one relationship between user accounts and identities. But then again, you can delete an identity but that won't delete the data and configuration of the user account. You can change the associated identity of the user account.

Have you ever faced a scenario where you have one email address and then you have multiple accounts to choose for login (i.e organization account and private account with the same email address) ? That is the case where you have one identity associated with multiple user accounts. In such a case, a user is shown a ballot screen during authentication in which they select the user account to use.

Any user interface or API can not directly reference the user account, it has to reference the identity(i.e email address) associated with the user account which is an indirect way of referencing user account.

## Types of user account

User account itself are two types:
- Consumer user account
- Managed user account

### Consumer user account

If you own a Gmail email address like alice@gmail.com, then your Gmail account is a consumer account. Similarly, if you use the Create account link on the Google Sign-In page and during sign-up you provide a custom email address that you own, such as alice@example.com, then the resulting account is also a consumer account.

When we refer to a **consumer account** as an **unmanaged user account**, it’s because this account was created by an individual using their personal Google account setup rather than being set up and managed by an organization. Here's a breakdown of what this means and why it matters:

#### What is an Unmanaged User Account?

An **unmanaged user account** (also called a “personal Google account”) is a **Google account that a user created on their own** using a personal email address, without going through a formal setup by an organization's IT team. It becomes a particular concern when the email address used by this unmanaged account matches the primary or secondary domain of an organization that uses **Google Workspace** or **Cloud Identity**.

For example:
- Suppose a company, "example.com," sets up Google Workspace or Cloud Identity for its employees.
- Now, assume an employee or contractor, Alex, creates a personal Google account using `alex@example.com` before the company starts using Google Workspace or Cloud Identity.
- When the company later starts using Google services officially, that personal account (`alex@example.com`) is in conflict with the organization’s setup because `example.com` is now a managed domain within Google Workspace or Cloud Identity.

#### Why is it Called Unmanaged?

The term **unmanaged** is used because:
- This consumer account (`alex@example.com`) wasn’t created, supervised, or controlled by the organization’s IT administrators.
- It exists outside the organization’s Google Workspace or Cloud Identity system, meaning the organization cannot apply policies, access controls, or data retention policies to it.
- The organization has no way to control or recover this account, even though it uses the same domain (`@example.com`) as the company.

#### Why is This a Problem?

When employees use **unmanaged accounts** with the company domain, it can cause:
- **Security Issues:** The company has no control over the data in these unmanaged accounts, even though they appear to be "company" accounts.
- **Confusion and Duplication:** If the organization sets up an official Google Workspace account for `alex@example.com`, there could now be two different `alex@example.com` accounts: one managed (under Workspace) and one unmanaged (consumer account).
- **Access Control Issues:** The unmanaged account may have access to certain company resources (like shared Google Drive files or documents) that should ideally be controlled by the organization.

#### How is This Typically Resolved?

Google provides options for organizations to resolve this by:
1. **Inviting Unmanaged Users to Join the Organization:** The organization can prompt users with unmanaged accounts on their domain (e.g., `alex@example.com`) to transfer their accounts into the organization’s managed system. This way, the unmanaged account becomes a managed account under Cloud Identity or Google Workspace.
2. **Account Transfer and Data Migration:** Google provides tools for migrating data from unmanaged accounts to managed accounts, so users don’t lose their data when they switch.

### Managed user account

Managed user accounts work similarly to consumer user accounts, but they can be fully controlled by administrators of the Cloud Identity or Google Workspace account. So, to be a managed user account, it has to be in cloud identity or google workspace. It requires to have one more thing. The identity of a managed user account is defined by its primary email address. The primary email address has to use a domain that corresponds to one of the primary, secondary, or alias domains added to the Cloud Identity or Google Workspace account. 

So, cloud identity or google workspace is the entry point for an organization's IAM and the first task is to set up cloud identity or google workspace for that organization. A Cloud Identity or Google Workspace account is created when a company signs up for Cloud Identity or Google Workspace and corresponds to the notion of a tenant. 

**What is a Tenant?**

A tenant in this context refers to a group of users in an organization who share common access to the company's Google resources, managed under one account. Think of it like a private workspace for the company. Only people within the company (the "tenant") have access to this specific workspace with their own permissions and settings.
When the company signs up for Cloud Identity or Google Workspace, it becomes a tenant on Google’s system, which provides a space specifically set up for them to manage their employees' access.

**Multitenant Architecture Explained**
- Multitenant architecture is a design approach used by Google and many other cloud providers.
- In multitenant architecture, one software application is shared among many companies (tenants), but each tenant has its own dedicated space within the application.
- This shared system means that many companies can use the same software infrastructure while keeping their data, configurations, and settings separate.

# Cloud Identity

![image](https://github.com/user-attachments/assets/05cb485d-db37-439e-babe-4f2784d9f32f)

![image](https://github.com/user-attachments/assets/a0bd5682-447a-4cda-a607-23dd741c86b1)

# Google workspace

![image](https://github.com/user-attachments/assets/a3cd0672-b900-4781-91a2-b6aa4b6e6f31)

___

Cloud identity or Google workspace needs to have the email address to know that this is the account which it should work on. That is why you need to put the account (add the email address) in cloud identity or google workspace. This is called provisioning account in cloud identity or google workspace.

There are two things: 
1. Identity provider (Idp)
2. Authorization source


**Identity provider (IdP):** Which serves you the page or functionality to provide your username and password to sign-in. 
**Authorization source:** Which manages the account by adding/updating/removing it to other places.

Authorization source provides necessary info to IdP from user account data structure with which IdP knows that this user account is valid and authorized from an authorization source.

When you configure single sign-on, Cloud Identity or Google Workspace relays authentication decisions to a SAML IdP. In SAML terms, Cloud Identity or Google Workspace acts as a service provider that trusts the SAML IdP to verify a user's identity on its behalf.

Commonly used external IdPs include Active Directory Federation Services (AD FS), Entra ID, Okta, or Ping Identity.

IAM addresses the following aspects of authentication and authorization:

- Account management, including provisioning
- Identity governance
- Authentication
- Access control (authorization)
- Identity federation

Be aware that when a Google Cloud organization is created, all users in your domain are granted the Billing Account Creator and Project Creator roles by default. 

# Google as IdP and authoritative source

- You use Cloud Identity Premium or Google Workspace to manage users and groups. This makes google as the authoritative source.
- All Google services use Cloud Identity Premium or Google Workspace as the IdP. This makes google as IdP because it provides the sign-in page where user will provide their credentials to identify themselves.
- You configure corporate applications and other SaaS services to use Google as the IdP. So, when user clicks on the sign-in button in those applications or services, they will be redirected to googles sign-in page.

# Google as IdP with an HRIS as authoritative source

- You use your existing HRIS to manage users and optionally groups. The HRIS remains the single source of truth for identity management and automatically provisions users for Cloud Identity or Google Workspace.
- All Google services use Cloud Identity Premium or Google Workspace as the IdP.
- You configure corporate applications and other SaaS services to use Google as the IdP.

# External Identity as a Service (IDaaS) as IdP and authoritative source

- The IDaaS automatically provisions users and groups for Cloud Identity or Google Workspace.
  - Upon requesting a protected resource, the employee is redirected to the Google Sign-In screen, which prompts them for their email address.
  - Google Sign-In redirects you to the sign-in page of your IDaaS.
  - You authenticate with your IDaaS. Depending on your IDaaS, this might require you to provide a second factor such as a code.
  - After you are authenticated, you are redirected back to the protected resource.
- Existing corporate applications and other SaaS services can continue to your IDaaS as an IdP.

**Why do we need the user to be added in cloud identity or google workspace if we have IDaaS as IdP and authoritative source ?**

When you go to Google Sign-in screen, you just can not give a random credentials and expect google to redirect you to IDaaS sign-in page. Google will only redirect those users to IDaaS sign-in page which are added to cloud identity or google workspace. That is why the sync is necessary. 

From the external authoritative source, user accounts and groups can be automatically provisioned to Cloud Identity or Google Workspace. Provisioning might be handled by the authoritative source itself, or by means of provisioning middleware.

For automatic user provisioning to be effective, users have to be provisioned with an identity that your SAML IdP recognizes. If you map between identities (for example, if you map the identity alice@example.com in Cloud Identity or Google Workspace to u12345@corp.example.com in your SAML IdP), then both the SAML IdP and the provisioning middleware must perform the same mapping.

# Active Directory as IdP and authoritative source

You use Google Cloud Directory Sync (GCDS) to automatically provision users and groups from Active Directory for Cloud Identity or Google Workspace. Google Cloud Directory Sync is a free Google-provided tool that implements the synchronization process and can be run either on Google Cloud or in your on-premises environment. Synchronization is one-way so that Active Directory remains the source of truth

- Upon requesting the protected resource, the employee is redirected to the Google Sign-in screen, which prompts them for their email address.
- Google Sign-In redirects the employee to the sign-in page of AD FS.
- Depending on the configuration of AD FS, the employee might see a sign-on screen prompting for their Active Directory username and password. Alternatively, AD FS might attempt to sign the employee in automatically based on their Windows login.
- After AD FS has authenticated the employee, they are redirected back to the protected resource.

# Azure AD as IdP with Active Directory as authoritative source

- Upon requesting the protected resource, the employee is redirected to the Google Sign-In screen, which prompts them for their email address.
- Google Sign-In redirects them to the sign-in page of AD FS.
- Depending on how their on-premises Active Directory is connected to Azure AD, Azure AD might prompt them for a username and password, or it might redirect them to an on-premises AD FS. - Because Azure AD itself might be integrated with an on-premises Active Directory
- After the employee is authenticated with Azure AD, they are redirected back to the protected resource.
