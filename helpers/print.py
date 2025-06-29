def print_emails(emails):
    for i, email in enumerate(emails, 1):
        print(f"Email {i}:")
        print(f"Subject: {email['subject']}")
        print(f"Body: {email['body']}")
        print(f"Department: {email['department']}")
        print("-" * 50)
