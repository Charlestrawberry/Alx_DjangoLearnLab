Learning to create django project 

"""
Permissions Setup:
- can_view: Allows viewing ExampleModel.
- can_create: Allows creating ExampleModel.
- can_edit: Allows editing ExampleModel.
- can_delete: Allows deleting ExampleModel.

Groups:
- Viewers → can_view
- Editors → can_view, can_create, can_edit
- Admins → all permissions
"""

# Security Measures Implemented

- DEBUG = False for production
- Enforced secure cookies (CSRF_COOKIE_SECURE, SESSION_COOKIE_SECURE)
- XSS protection via SECURE_BROWSER_XSS_FILTER and CSP
- Clickjacking protection via X_FRAME_OPTIONS
- SQL Injection prevention: ORM instead of raw SQL
- CSRF tokens added to all forms


# HTTPS and Security Configuration

## Django Settings
- `SECURE_SSL_REDIRECT = True` forces all HTTP to HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD` enforce HSTS.
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` ensure cookies are only sent over HTTPS.
- `X_FRAME_OPTIONS = 'DENY'` protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents MIME sniffing.
- `SECURE_BROWSER_XSS_FILTER = True` helps mitigate XSS.

## Deployment Configuration
- Configured Nginx with SSL (Let’s Encrypt).
- All HTTP requests redirected to HTTPS.
- TLSv1.2+ enforced.

## Review
These measures protect against:
- Man-in-the-middle attacks (HTTPS + HSTS).
- Cookie theft (secure cookies).
- XSS and clickjacking (headers).
- MIME sniffing vulnerabilities.

### Areas for future improvement:
- Enable CSP (Content Security Policy).
- Add logging/monitoring for suspicious requests.
