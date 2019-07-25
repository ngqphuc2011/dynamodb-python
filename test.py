from botocore.credentials import InstanceMetadataProvider, InstanceMetadataFetcher

provider = InstanceMetadataProvider(iam_role_fetcher=InstanceMetadataFetcher(timeout=1000, num_attempts=2))
credentials = provider.load()

access_key = credentials.access_key
secret_key = credentials.secret_key

print(access_key)
print(secret_key)