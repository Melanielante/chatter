import React, { useState } from "react";

function CommentForm({ postId, onAddComment }) {
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!content.trim()) return;

    // Send only the content — Feed handles API + state update
    onAddComment({
      content,
      post_id: postId,
      user_id: 1, // placeholder until auth
    });

    setContent(""); // clear input
  };

  return (
    <form onSubmit={handleSubmit} className="comment-form">
      <input
        type="text"
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="Write a comment..."
      />
      <button type="submit">Comment</button>
    </form>
  );
}

export default CommentForm;
