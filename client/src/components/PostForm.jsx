
import React, { useState } from "react";

function PostForm({ onAddPost }) {
  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!content.trim()) return; // prevent empty posts

    const newPost = {
      content,
      user_id: 1, // temporary hardcoded until auth is ready
      group_id: null, 
    };

    // call parent handler (Feed will handle API call )
    onAddPost(newPost);

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
