import { useEffect, useState } from "react";
import { useParams } from "react-router";

function PostDetail() {
  const { id } = useParams(); // grab post id from URL
  const [post, setPost] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/posts/${id}`)
      .then((res) => res.json())
      .then((data) => setPost(data))
      .catch((err) => console.error("Error fetching post:", err));
  }, [id]);

  if (!post) return <p>Loading post...</p>;

  return (
    <div className="post-detail">
      <h2>Post Details</h2>
      <div className="post-card">
        <p>{post.content}</p>
        <small>
          Posted by {post.user?.username}
          {post.group ? ` in ${post.group.name}` : ""}
        </small>
      </div>

      <div className="likes">
        <p>Likes: {post.likes?.length || 0}</p>
        <ul>
          {post.likes?.map((likeUser) => (
            <li key={likeUser.id}>{likeUser.username}</li>
          ))}
        </ul>
      </div>

      <div className="comments">
        <h3>Comments</h3>
        {post.comments?.length === 0 ? (
          <p>No comments yet.</p>
        ) : (
          post.comments.map((c) => (
            <div key={c.id} className="comment">
              <p>{c.content}</p>
              <small>by User {c.user_id}</small>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default PostDetail;
