# Account visibility

The function accepts a list of account dictionaries and a user ID string.
It must return only accounts whose owner matches the non-empty user ID.
An empty string means there is no current user and must return an empty list.
Existing camelCase names are the local convention and are not a defect.
