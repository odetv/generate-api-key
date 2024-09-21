import secrets

def generate_custom_api_key(length=94):
    return secrets.token_urlsafe(length)[:length]

# Generate and print a new API Key with specified length
new_api_key = generate_custom_api_key(94)
print(f"Your new API Key: {new_api_key}")
