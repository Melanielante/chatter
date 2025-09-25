import { useEffect, useState } from "react";

function Explore() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/posts") 
      .then((res) => res.json())
      .then((data) => setPosts(data))
      .catch((err) => console.error("Error fetching posts:", err));
  }, []);

  return (
    <div className="explore">
      <h2>Explore</h2>
      {posts.length === 0 ? (
        <p>No posts yet.</p>
      ) : (
        posts.map((post) => (
          <div key={post.id} className="post-card">
            <p>{post.content}</p>
            <small>
              Posted by User {post.user_id}
              {post.group_id ? ` in Group ${post.group_id}` : ""}
            </small>
          </div>
        ))
      )}
    </div>
  );
}

export default Explore;
