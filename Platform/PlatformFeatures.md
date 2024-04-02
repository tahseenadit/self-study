# Services

How do you expose these services ?
How your users deploy these services in your platform ?
How your users interact with your services ?

**Exposure**
Your platform may have many services. You may offer these services as below:

- API

**Deployment**

You may develop the following capabilties for/in your platform and the user may use them to deploy their services (offered by your platform) in your platform.

- GUI
- Terraform modules

How does any user can use terraform to deploy resource in your platform ? Do they need any token generated from your platform which will give them the permission to deploy resource using terraform in your platform ? Does your platform has capabillities to assign set of permissions to the token ? Can you set these permissions on resource level or environment level ?

**Interaction**

The user may interact with your services in the following ways:'

- CLI
- Library
- GUI

**Mapping with External Services**

How does the services in your platform establish communication/relation to other external services ? Are they 1:1, many:1, many:many, 1:many ?

# Users

Your platform can have two types of users:

- User
- External application

# Permissions

**Users**

- Your platform should have capabilities to allow users to perform specific actions for specifc services.
- Your platform should allow user to extend their permissions. The platform should have capability to allow user to have permission to extend their permission in your platform.

**External Application**

If user does not have permission to do specific actions in your platform, then the external application that used that user's credentials to interact with your platform should also not be allowed to perform those specific actions.

# Login

- External application can request user of your platform to authenticate the application to your platform. For example, the external application can ask credentials from the user and send these credentials to your platform. Your platform can authenticate the credentials and authorize the external application to interact with the platform on behalf of the user.

- Instead of asking the user for credentials, the user can generate a token from your platform and store it in his system. The external application can fetch this token whenever needed and send the token to your platform. Your platform can authenticate the token and authorize the external application to interact with the platform on behalf of the user. But how will the user manage this token ? Where will it store ?

- If user does not have permission to do specific actions in your platform, then the external application that used that user's credentials to interact with your platform should also not be allowed to perform those specific actions. But what if the application needs to perform those actions ? User should be able to extend their permissions in your platform. But should all users do that ? No, even user should have permission to extend their permission in your platform. Your platform should provide that capability. But how many times user will extend their permissions ? Because user may not know which permissions to add ahead of time.

- The platform should allow user to set up a list or dummy account with all additional permissions. When external application is done with it's works, the user should be able to delete that list or dummy account in the platform. That makes things clean and keep extra permissions separated. Because these extra permissions are only needed by that specific external application.

- What if the user gets deleted ? Should the list or dummy account also get deleted ? Do you want your platform to tightly couple the dummy account with the users account ? What if other users need the same dummy account or list ? Do they create their own in that case or just reuse the one already created. If they reuse, then the dummy account also should be authenticated using credentials or token. Then again how this token will be managed and where this token will be stored ?

# Development

**Local Development**

How does developer develop for your platform in local IDE ? 

**Cloud IDE**

Your platform can provide cloud IDE like bigquery or dbt cloud does. If you have cloud IDE, how does the configuration work ? It is better to have the same logic for setting up configuation in both local development environment and cloud IDE.