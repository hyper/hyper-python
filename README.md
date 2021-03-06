# Hyper Python Library

The Hyper Python library provides convenient access to the Hyper API from
applications written in the Python language.

## Documentation

See the [API docs](https://docs.hyper.co/reference).

## Installation

```sh
pip install --upgrade hyper-python
```

### Requirements

-   Python 3

## Usage

The library needs to be configured with your account's secret key which is
available in your [Hyper Dashboard](https://hyper.co/developers). Set `hyper.api_key` to its
value:

```python
import hyper
hyper.api_key = 'sk_...'

# create license
license = hyper.License.create(
    email='hello@hyper.co',
    plan='f80gre098nbgoiA',
    # see API docs for remaining parameters
)

# print the license's email
print(license.email)


# retrieve specific license
license = hyper.License.retrieve('6WHJ-GIPG-28KF-U0MB')

# print that license's email
print(license.email)


# update specific license
license = hyper.License.update(
    key='6WHJ-GIPG-28KF-U0MB',
    metadata={'hwid': '09584903'}
)

# print that license's metadata
print(license.metadata)


# delete specific license
hyper.License.delete('6WHJ-GIPG-28KF-U0MB')


# list licenses
licenses = hyper.License.list(
    limit=50,  # default is 10
    page=1  #default is 1
)

# print the first license's email
print(licenses.data[0].email)


# send specific license
hyper.License.send('6WHJ-GIPG-28KF-U0MB')
```

### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred.

```python
try:
  # Use Hyper's library to make requests...
  pass
except hyper.error.AuthenticationError as e:
  # Authentication with Hyper's API failed
  # (maybe you changed API keys recently)
  pass
except hyper.error.InvalidRequestError as e:
  # Invalid parameters were supplied to Hyper's API
  pass
except Exception as e:
  # Something else happened, unrelated to Hyper
  pass
```
