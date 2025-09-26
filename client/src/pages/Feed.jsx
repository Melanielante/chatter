import React, { useEffect, useState } from "react";
import { fetchPosts } from "../utils/Api"

function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // fetch posts when component mounts
  useEffect(() => {
    fetchPosts()
      .then((data) => {
        setPosts(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching posts:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading feed...</p>;
  }

  return (
    <div>
      <h2>Chatter Feed</h2>
      {posts.length === 0 ? (
        <p>No posts yet. Be the first to share something!</p>
      ) : (
        posts.map((post) => (
          <div
            key={post.id}
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              margin: "10px 0",
              borderRadius: "5px",
            }}
          >
            <p><strong>User {post.user_id}:</strong> {post.content}</p>

            {post.comments && post.comments.length > 0 && (
              <div style={{ marginTop: "8px", paddingLeft: "10px" }}>
                <strong>Comments:</strong>
                {post.comments.map((comment) => (
                  <p key={comment.id} style={{ margin: "4px 0" }}>
                    <em>User {comment.user_id}:</em> {comment.content}
                  </p>
                ))}
              </div>
            )}

            <p style={{ marginTop: "8px" }}>
              👍 {post.likes ? post.likes.length : 0} Likes
            </p>
          </div>
        ))
      )}
    </div>
  );
}

export default Feed;
