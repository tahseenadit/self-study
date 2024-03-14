# Services

**Exposure**
Your platform may have many services. You may offer these services as below:

- API

**Deployment**

You may develop the following capabilties for/in your platform and the user may use them to deploy their services (offered by your platform) in your platform.

- GUI
- Terraform modules

**Interaction**

The user may interact with your services in the following ways:'

- CLI
- Library
- GUI

# Users

Your platform can have two types of users:

- User
- External application

# Login

- External application can request user of your platform to authenticate the application to your platform. For example, the external application can ask credentials from the user and send these credentials to your platform. Your platform can authenticate the credentials and authorize the external application to interact with the platform on behalf of the user.

- Instead of asking the user for credentials, the user can generate a token from your platform and store it in his system. The external application can fetch this token whenever needed and send the token to your platform. Your platform can authenticate the token and authorize the external application to interact with the platform on behalf of the user.