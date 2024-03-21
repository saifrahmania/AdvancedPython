import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

# Create a session  
session = requests.Session()

# Define retry parametter
retries = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])

# Mount the adapter to the session
session.mount('https://', HTTPAdapter(max_retries=retries))

# Fetch data from the API
response = requests.get("https://randomuser.me/api/")
data = response.json()

# Decode it in Python
results = data.get('results', [])

# Prepare HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Data</title>
</head>
<body>
    <h1>User Data</h1>
    <ul>
"""

for result in results:
    # Format Date of Birth
    dob = result['dob']['date'].split("T")[0].replace("-", "/")  # Extract date part and replace "-" with "/"

    # Format Registered Date
    registered = result['registered']['date'].split("T")[0].replace("-", "/").replace("Z", "")
    
    # Add the image tag with the user's photo
    html_content += f"""
        <li>
            <strong>Name:</strong> {result['name']['first']} {result['name']['last']}<br>
            <strong>Email:</strong> {result['email']}<br>
            <strong>Location:</strong> {result['location']['city']}, {result['location']['state']}, {result['location']['country']}<br>
            <strong>Username:</strong> {result['login']['username']}<br>
            <strong>Date of Birth:</strong> {result['dob']['date']}<br>
            <strong>Registered:</strong> {result['registered']['date']}<br>
            <!-- Add the image tag with the user's photo -->
            <img src="{result['picture']['large']}" alt="User Photo">
        </li>
    """

html_content += """
    </ul>
</body>
</html>
"""

# Save HTML content to a file
with open("user_data.html", "w") as html_file:
    html_file.write(html_content)

print("HTML file generated successfully.")
