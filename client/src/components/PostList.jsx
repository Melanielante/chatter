
import React from "react";
import PostCard from "./PostCard";

function PostList({ posts }) {
  if (!posts || posts.length === 0) {
    return <p>No posts available.</p>;
  }

  return (
    <div className="post-list">
      {posts.map((post) => (
        <PostCard key={post.id} post={post} />
      ))}
    </div>
  );
}

export default PostList;
