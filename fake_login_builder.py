import os

def print_banner():
    banner = """
    ╔══════════════════════════════════════════════════════╗
    ║          Fake Login Page Builder                     ║
    ║  Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan  ║
    ║                                                      ║
    ║  *** For Educational Purposes Only ***               ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(banner)

def create_login_page():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
        }
        .login-container h2 {
            color: #333;
            margin-bottom: 20px;
        }
        .login-container input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Login</h2>
        <form action="/submit" method="POST">
            <input type="text" name="username" placeholder="Username" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
    """
    with open("login.html", "w") as f:
        f.write(html_content)
    print("Login page created successfully as 'login.html'")

def setup_server():
    # Basic server simulation to capture form data
    # For a real server, you would use Flask or Django
    print("Simulating form data capture (server not implemented).")
    print("Form data will be saved to 'credentials.txt' for demonstration.")
    
    # Simulate capturing form data
    username = input("Enter a test username: ")
    password = input("Enter a test password: ")
    
    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")
    print("Credentials saved to 'credentials.txt'")

def main():
    print_banner()
    print("1. Create Login Page")
    print("2. Simulate Form Data Capture")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        create_login_page()
    elif choice == "2":
        setup_server()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()