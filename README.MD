

# Chatter

**Chatter** is a lightweight social media platform where users can create accounts, share posts, like and comment on content, and connect with others. It is built with **React** on the frontend and **Flask** on the backend, and designed for fast, responsive interactions.

**Live Demo:**

* Frontend: [Chattersocial on Netlify](https://68dc2032a4bfcf857893f6b8--chattersocial.netlify.app/)

* Backend API: [Chatter API on Render](https://chatter-bb7s.onrender.com/)

---

## Features

* User authentication: Signup & Login
* Create, view, and explore posts
* Like and comment on posts
* User profile pages
* Connect with groups and communities
* Responsive UI with reusable React components

---

## Tech Stack

**Frontend:**

* React
* React Router
* Fetch API

**Backend:**

* Flask (Python)
* Flask-RESTful
* SQLite (development) / PostgreSQL (production)

**Deployment:**

* Render (Backend)
* Netlify (Frontend)

---

## Project Structure

```plaintext
chatter/
│
├── client/                # React frontend
│   ├── src/
│   │   ├── pages/         # Main pages (Feed, Profile, Explore, etc.)
│   │   ├── components/    # Reusable components (PostForm, PostList, etc.)
│   │   ├── utils/         # API calls
│   │   └── App.jsx        # App entry point
│
├── server/                # Flask backend
│   ├── app.py             # Main Flask app
│   ├── models.py          # Database models
│   ├── routes/            # API endpoints
│   └── migrations/        # Database migrations
│
└── README.md
```

---

## Getting Started

Follow these steps to run Chatter locally:

### 1. Clone the repository

```bash
git clone https://github.com/Melanielante/chatter.git
cd chatter
```

### 2. Backend Setup

```bash
cd server
python -m venv .venv          # create virtual environment if not already done
source .venv/bin/activate
pip install -r requirements.txt
flask db upgrade               # run migrations
flask run                      # start Flask server
```

### 3. Frontend Setup

```bash
cd ../client
npm install
npm run dev                    # start React dev server
```

> The frontend will automatically connect to the backend API using environment variables.

---

## Database Seeding

To populate your database with sample users, posts, comments, likes, and groups:

```bash
cd server
python seed.py
```

---

## Deployment

Chatter is deployed with **Render** (backend) and **Netlify** (frontend):

* Backend API: [https://chatter-bb7s.onrender.com/](https://chatter-bb7s.onrender.com/)

* Frontend: [https://68dc2032a4bfcf857893f6b8--chattersocial.netlify.app/](https://68dc2032a4bfcf857893f6b8--chattersocial.netlify.app/)

The backend is configured for automatic deploys from GitHub, while the frontend is linked to the deployed backend API.

---

## Future Improvements

* Add real-time updates with WebSockets
* Improve authentication using JWT
* Enhance UI using Tailwind CSS or Material UI
* Support image uploads and media content
* Add notifications and user-to-user messaging

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m "Add feature"`
4. Push to your branch: `git push origin feature-name`
5. Open a Pull Request

For major changes, please open an issue first to discuss your ideas.

---

## License

MIT License © 2025 MEL


