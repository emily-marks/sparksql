### Deploy infrastructure with terraform

From `/terraform` folder run commands using `ENV = sparksql`

```
terraform init
terraform plan -out terraform.plan
terraform apply terraform.plan
```
### Launch notebooks on Databricks cluster
To provide databricks access to data a configuration is needed.
1. Try to create databricks secret:
```
  databricks secrets create-scope --scope sparksql
  databricks secrets put --scope sparksql --key sparksql-secret
```
_**If no exceptions are thrown, skip steps 2-7.**_

2. In case of `io.jsonwebtoken.ExpiredJwtException: JWT expired ` exception a new access token has to be generated.
For this purpose register an Azure AD application (Azure Active Directory -> App registrations), use `http://localhost` 
as URL. Get `Directory (tenant) ID` and `Application (client) ID` of the application.
3. Create a secret for Azure AD application: `Application  -> Certificates & secrets -> New client secret`. Save `client_secret` value.
4. Get `code`  from the URL after request: 
```
https://login.microsoftonline.com/<tenant-id>/oauth2/authorize?client_id=<client-id>
&response_type=code
&redirect_uri=http%3A%2F%2Flocalhost
&response_mode=query
&resource=2ff814a6-3304-4ab8-85cb-cd0e6f879c1d
&state=29387
```
5. Run `python/AzureADAuth.py` with given values
6. modify C://Users/{user}/.databrickscfg with new access key
7. run step 1 again

### Databricks results
* All queries with results are stored in `/notebooks/m07_sparksql.dbc`
* Visualization example is placed in `/src/main/visualization/m07_sparksql.html`
* Execution plans are stored in `/src/main/execution_plan/`

### Destroy resources

```commandline
terraform destroy
```