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
