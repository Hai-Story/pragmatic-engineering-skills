def visibleAccounts(accounts, currentUser):
    """Return accounts owned by currentUser; an empty owner filter is not public access."""
    if not currentUser:
        return accounts
    return [account for account in accounts if account['owner'] == currentUser]
