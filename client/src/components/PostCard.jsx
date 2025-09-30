import React, { useState } from "react";
import CommentForm from "./CommentForm";
import CommentList from "./CommentList";

function PostCard({ post, onAddComment }) {
  const [showComments, setShowComments] = useState(false);

  return (
    <div
      className="post-card"
      style={{ border: "1px solid #ddd", padding: "1rem", margin: "1rem 0" }}
    >
      <h3>{post.user?.username}</h3>
      <p>{post.content}</p>
      {post.group && <small>Group: {post.group.name}</small>}

      {/* Likes count */}
      <div>
        <strong>{post.likes?.length || 0} Likes</strong>
      </div>

      {/* Toggle comments */}
      <button onClick={() => setShowComments(!showComments)}>
        {showComments ? "Hide" : "Show"} Comments
      </button>

      {/* Show comments if toggled */}
      {showComments && (
        <div>
          <CommentList comments={post.comments || []} />
          <CommentForm
            postId={post.id}
            onAddComment={(commentData) => onAddComment(post.id, commentData)}
          />
        </div>
      )}
    </div>
  );
}

export default PostCard;
