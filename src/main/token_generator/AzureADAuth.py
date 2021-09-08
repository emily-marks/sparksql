from adal import AuthenticationContext

authority_host_url = "https://login.microsoftonline.com/"
azure_databricks_resource_id = "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d"  # it's fixed value independent of account

user_parameters = {
    "tenant": "ADD VALUE",
    "client_id": "ADD VALUE",
    "client_secret": "ADD VALUE",
    "redirect_uri": "http://localhost"
}
authz_code = 'ADD VALUE'

# the auth_state can be a random number or can encoded some info
# about the user. It is used for preventing cross-site request
# forgery attacks
auth_state = 12345

def get_refresh_and_access_token():
    # configure AuthenticationContext
    # authority URL and tenant ID are used
    authority_url = authority_host_url + user_parameters['tenant']
    context = AuthenticationContext(authority_url)

    # Obtain the authorization code in by a HTTP request in the browser
    # then copy it here or, call the function above to get the authorization code

    # API call to get the token, the response is a
    # key-value dict
    token_response = context.acquire_token_with_authorization_code(
        authz_code,
        user_parameters['redirect_uri'],
        azure_databricks_resource_id,
        user_parameters['client_id'],
        user_parameters['client_secret'])

    # you can print all the fields in the token_response
    for key in token_response.keys():
        print(str(key) + ': ' + str(token_response[key]))

    # the tokens can be returned as a pair (or you can return the full
    # token_response)
    return (token_response['accessToken'], token_response['refreshToken'])

get_refresh_and_access_token()
