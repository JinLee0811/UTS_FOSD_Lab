import re

email = "john.smith@example.com.au"
password = "Admin_1234"


EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}(\.au)?\b"
PASSWORD_PATTERN = r"\b[A-Z][a-z]{4,}[@_#-][0-9]{3,}\b"


# 이메일 형식에 따른 패턴 구성
