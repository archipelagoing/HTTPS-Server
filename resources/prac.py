# ## parsing http messages
# m = """GET /hello.htm HTTP/1.0
# User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT)
# Host: www.tutorialspoint.com
# Cookie: yummy_cookie=choco; tasty_cookie=strawberry
# Accept-Language: en-us
# Accept-Encoding: gzip, deflate
# Connection: Keep-Alive
# """
# #make newlines CRLF - not for a real HTTP message
# m = str.replace(m, '\n', '\r\n')
# lines = m.split("\r\n")
# start_line = lines[0]
# method,target,version = start_line.split(" ")

# headers = {}
# for header in lines[1:]:
#  if header == "": break #reached body
#  hkey,hval = header.split(": ",1)
#  headers[hkey] = hval
# print(method,target,version)
# #print(headers)


# def handle_login_request(request_headers):
#     # Obtain “username” and “password” from request headers
#     username = request_headers.get("username")
#     password = request_headers.get("password")

#     # If 1 or both fields missing:
#     if not username or not password:
#         # Return HTTP status code “501 Not Implemented”, log with MESSAGE "LOGIN FAILED"
#         logging.error("LOGIN FAILED: Missing username or password")
#         return "501 Not Implemented", "LOGIN FAILED"

#     # Check if “username” and “password” are valid (you can replace this with your validation logic)
#     if is_valid_credentials(username, password):
#         # Set a cookie called “sessionID” to a random 64-bit hexadecimal value
#         session_id = generate_session_id()

#         # Create a session with required info for validation using the cookie
#         create_session(username, session_id)

#         # Log with MESSAGE "LOGIN SUCCESSFUL: {username} : {password}"
#         logging.info(f"LOGIN SUCCESSFUL: {username} : {password}")

#         # Return HTTP 200 OK response with body “Logged in!”
#         return "200 OK", "Logged in!"

#     else:
#         # Log with MESSAGE "LOGIN FAILED: {username} : {password}"
#         logging.error(f"LOGIN FAILED: {username} : {password}")

#         # Return HTTP 200 OK response with body “Login failed!”
#         return "200 OK", "Login failed!"

# def is_valid_credentials(username, password):
#     # Replace this with your actual validation logic
#     # For example, you might check the credentials against a database
#     # or some other authentication mechanism.
#     # For the sake of this example, let's assume it's valid if both are non-empty.
#     return bool(username and password)

# def generate_session_id():
#     # Generate a random 64-bit hexadecimal value
#     return ''.join(random.choice('0123456789abcdef') for _ in range(16))
    
# def create_session(username, session_id):
#     # Replace this with your logic to create a session.
#     # This might involve storing the session information in a database,
#     # cache, or some other storage mechanism.
#     # For the sake of this example, let's just print the session information.
#     print(f"Created session for {username} with session ID: {session_id}")

# # Example usage:
# request_headers = {"username": "user123", "password": "pass456"}
# status_code, response_body = handle_login_request(request_headers)
# print(f"Status Code: {status_code}, Response: {response_body}")