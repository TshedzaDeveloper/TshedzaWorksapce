# Authentication System

A Django-based authentication system for the Kingdoms platform.

## Features

- User registration and login
- Email verification
- Password reset functionality
- Two-factor authentication
- Activity logging
- API endpoints
- Admin dashboard

## Setup Instructions

1. Navigate to the project directory:
```bash
cd authentication_project
```

2. Set up the virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure email settings in settings.py:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

5. Configure security settings in settings.py:
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

6. Configure 2FA settings in settings.py:
```python
TWO_FACTOR_SMS_BACKEND = 'django_otp.plugins.sms.models.SMSDevice'
TWO_FACTOR_QR_FACTORY = 'qrcode.image.pil.PilImage'
```

7. Configure API settings in settings.py:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

8. Run migrations:
```bash
python manage.py migrate
```

9. Collect static files:
```bash
python manage.py collectstatic
```

10. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

- POST /api/auth/register/ - Register new user
- POST /api/auth/login/ - User login
- POST /api/auth/logout/ - User logout
- POST /api/auth/password-reset/ - Request password reset
- POST /api/auth/password-reset/confirm/ - Confirm password reset
- GET /api/users/me/ - Get current user info
- PUT /api/users/me/ - Update user profile
- POST /api/users/2fa/setup/ - Setup 2FA
- POST /api/users/2fa/verify/ - Verify 2FA code 