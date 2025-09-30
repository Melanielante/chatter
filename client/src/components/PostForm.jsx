import React, { useState } from "react";

function PostForm({ onSubmit }) {
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!content.trim()) return; // prevent empty posts

    // call parent handler (Feed will handle API call)
    onSubmit(content);

    // clear input
    setContent("");
  };

  return (
    <form onSubmit={handleSubmit} className="post-form">
      <textarea
        value={content}
        onChange={(e) => setContent(e.target.value)}
        placeholder="What's on your mind?"
        rows="3"
      />
      <button type="submit">Post</button>
    </form>
  );
}

export default PostForm;
