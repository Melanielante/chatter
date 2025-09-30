import React, { useEffect, useState } from "react";
import { fetchPosts, createPost, addComment } from "../utils/Api";
import PostList from "../components/PostList";
import PostForm from "../components/PostForm";


function Feed() {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  // Load posts on mount
  useEffect(() => {
    loadPosts();
  }, []);

  const loadPosts = async () => {
    try {
      setLoading(true);
      const data = await fetchPosts();
      setPosts(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Add a new post
  const handleAddPost = async (postData) => {
    try {
      const newPost = await createPost(postData);
      setPosts([newPost, ...posts]); 
    } catch (err) {
      console.error("Error creating post:", err);
    }
  };

  // Add a new comment
  const handleAddComment = async (postId, commentData) => {
    try {
      const newComment = await addComment(
        postId,
        commentData.user_id,
        commentData.content
      );

      // update state locally so UI reflects instantly
      setPosts((prevPosts) =>
        prevPosts.map((post) =>
          post.id === postId
            ? { ...post, comments: [...(post.comments || []), newComment] }
            : post
        )
      );
    } catch (err) {
      console.error("Error adding comment:", err);
    }
  };

  if (loading) return <p>Loading posts...</p>;

  return (
    <div className="feed">
      <h2>Feed</h2>
      <PostForm onAddPost={handleAddPost} />
      <PostList posts={posts} onAddComment={handleAddComment} />
    </div>
  );
}

export default Feed;
