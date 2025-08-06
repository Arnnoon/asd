@REM python setup.py

# For Windows (setup_project.bat)
@echo off
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing requirements...
pip install -r requirements.txt

echo Setting up database...
python manage.py makemigrations
python manage.py migrate

echo Creating superuser...
echo Please create a superuser account:
python manage.py createsuperuser

echo Collecting static files...
python manage.py collectstatic --noinput

echo Setup complete! Your Django project is ready.
echo To activate in future sessions, run: venv\Scripts\activate
echo To start the server, run: python manage.py runserver
pause

# ======================================

# For Linux/Mac (setup_project.sh)
#!/bin/bash
echo "Creating virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing requirements..."
pip install -r requirements.txt

echo "Setting up database..."
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser..."
echo "Please create a superuser account:"
python manage.py createsuperuser

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Setup complete! Your Django project is ready."
echo "To activate in future sessions, run: source venv/bin/activate"
echo "To start the server, run: python manage.py runserver"

# ======================================

# Cross-platform Python script (setup_project.py)
import os
import subprocess
import sys
import platform

def run_command(command, shell=True, ignore_error=False):
    """Run a command and handle errors"""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=shell, check=True, text=True, capture_output=True)
        if result.stdout.strip():
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        if not ignore_error:
            print(f"Error: {e}")
            if e.stdout:
                print(f"Command output: {e.stdout}")
            if e.stderr:
                print(f"Command error: {e.stderr}")
            return False
        return True

def create_superuser():
    """Create superuser interactively"""
    print("\n3. Creating superuser...")
    print("Please create a superuser account for Django admin:")
    
    # Determine python command
    python_cmd = "python" if platform.system() == "Windows" else "python3"
    
    # Use venv python
    if platform.system() == "Windows":
        python_path = "venv\\Scripts\\python"
    else:
        python_path = "venv/bin/python"
    
    # Run createsuperuser interactively
    try:
        subprocess.run([python_path, "manage.py", "createsuperuser"], check=True)
        return True
    except subprocess.CalledProcessError:
        print("Skipping superuser creation...")
        return False

def main():
    print("🚀 Setting up Django project...")
    
    # Check if manage.py exists
    if not os.path.exists("manage.py"):
        print("❌ manage.py not found. Make sure you're in a Django project directory.")
        sys.exit(1)
    
    # Create virtual environment
    print("\n1. Creating virtual environment...")
    python_cmd = "python" if platform.system() == "Windows" else "python3"
    if not run_command(f"{python_cmd} -m venv venv"):
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Determine activation command and paths
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
        python_path = "venv\\Scripts\\python"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
        python_path = "venv/bin/python"
    
    # Install requirements
    print("\n2. Installing requirements...")
    if os.path.exists("requirements.txt"):
        if not run_command(f"{pip_cmd} install -r requirements.txt"):
            print("❌ Failed to install requirements")
            sys.exit(1)
    else:
        print("No requirements.txt found. Installing basic Django setup...")
        if not run_command(f"{pip_cmd} install django"):
            print("❌ Failed to install Django")
            sys.exit(1)
    
    # Database setup
    print("\n3. Setting up database...")
    
    # Make migrations
    print("Creating migrations...")
    if not run_command(f"{python_path} manage.py makemigrations"):
        print("⚠️  Warning: makemigrations failed, but continuing...")
    
    # Apply migrations
    print("Applying migrations...")
    if not run_command(f"{python_path} manage.py migrate"):
        print("❌ Failed to apply migrations")
        sys.exit(1)
    
    # Create superuser
    create_superuser()
    
    # Collect static files
    print("\n4. Collecting static files...")
    run_command(f"{python_path} manage.py collectstatic --noinput", ignore_error=True)
    
    # Check if server starts
    print("\n5. Testing server startup...")
    print("Testing if Django server can start...")
    test_result = run_command(f"{python_path} manage.py check", ignore_error=True)
    
    print("\n✅ Setup complete!")
    print("="*50)
    print(f"📁 Virtual environment created: venv/")
    print(f"🔧 Dependencies installed")
    print(f"🗃️  Database setup complete")
    print(f"👤 Superuser created (if you completed the prompts)")
    print("="*50)
    
    print("\nUseful commands:")
    print(f"  Activate venv: {activate_cmd}")
    print("  Start server: python manage.py runserver")
    print("  Access admin: http://127.0.0.1:8000/admin/")
    print("  Deactivate: deactivate")
    print(f"  Install package: {pip_cmd} install package_name")
    
    # Optional: Ask if user wants to start the server
    try:
        start_server = input("\nWould you like to start the development server now? (y/n): ").lower().strip()
        if start_server in ['y', 'yes']:
            print("\nStarting development server...")
            print("Server will start at: http://127.0.0.1:8000/")
            print("Press Ctrl+C to stop the server")
            subprocess.run([python_path, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\n\nServer stopped. Project setup is complete!")

if __name__ == "__main__":
    main()