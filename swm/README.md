🚀 Local Setup & Installation

Follow these steps to run the project on your local machine:

1️⃣ Clone the Repository
git clone https://github.com/janithakrishnan/SWM-India-Analysis.git
cd swm


2️⃣ Create a Virtual Environment

It is recommended to use a virtual environment.

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

Install required Python packages:

pip install -r requirements.txt

4️⃣ Run the Development Server

Since the project reads directly from CSV files, no database setup is required.
Start the Django server with:

python manage.py runserver

5️⃣ Open in Browser

Once the server is running, open:

http://127.0.0.1:8000/


You should now see the data visualizations
