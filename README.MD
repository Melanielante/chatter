

#  Chatter

Chatter is a lightweight social media application where users can create accounts, share posts, like and comment on content, and connect with others. It’s built with **React** on the frontend and **Flask** on the backend.



---

##  Features

* User authentication (Signup & Login)
* Create, view, and explore posts
* Like and comment on posts
* User profile page
* Responsive design with reusable React components

---

##  Tech Stack

**Frontend:**

* React
* React Router
* Fetch API

**Backend:**

* Flask (Python)
* Flask-RESTful
* SQLite (development)

**Deployment:**

* Render (Backend & Frontend hosted)

---

##  Project Structure

```plaintext
chatter/
│── client/        # React frontend  
│   ├── src/  
│   │   ├── pages/        # Core pages (Feed, Profile, Explore, etc.)  
│   │   ├── components/   # Reusable components (PostForm, PostList, etc.)  
│   │   ├── utils/        # API calls  
│   │   └── App.jsx       # Main app entry  
│  
│── server/        # Flask backend  
│   ├── app.py  
│   ├── models.py  
│   ├── routes/  
│   └── migrations/  
│  
│── README.md  
```

---

##  Setup Instructions

### 1 Clone the repository

```bash
git clone https://github.com/Melanielante/chatter
cd chatter
```

### 2 Backend Setup (Flask)

```bash
cd server
pip install -r requirements.txt
flask db upgrade   # Run migrations
flask run
```

### 3 Frontend Setup (React)

```bash
cd client
npm install
npm run dev
```

---

##  Deployment on Render

The app is deployed on **Render** and **Netlify**:

* **Backend**: Hosted as a web service with auto-deploy from GitHub. **https://chatter-bb7s.onrender.com/** 

* **Frontend**: Deployed as a static site connected to the backend API on **https://68dc2032a4bfcf857893f6b8--chattersocial.netlify.app/** */.

---

##  Future Improvements

* Add real-time updates with WebSockets
* Implement JWT authentication
* Improve UI with Tailwind/Material UI
* Add image uploads

---

##  Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

##  License

MIT License © 2025 MEL

