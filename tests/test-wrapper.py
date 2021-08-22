import hyper

#hyper.api_key = 'sk_vvSXc0flbWg5janDJzmYALOeOBNx5OKC'

license_data = hyper.License.list(limit=1, page=2)
print(license_data)
