import React, { useEffect, useState } from "react";

function CommentList({ comments, postId }) {
  const [fetchedComments, setFetchedComments] = useState(comments || []);

  useEffect(() => {
    // if no comments passed in, fetch by postId
    if ((!comments || comments.length === 0) && postId) {
      fetch(`http://127.0.0.1:5000/api/posts/${postId}/comments`)
        .then((res) => res.json())
        .then((data) => setFetchedComments(data))
        .catch((err) => console.error("Error fetching comments:", err));
    }
  }, [postId, comments]);

  if (!fetchedComments || fetchedComments.length === 0) {
    return <p>No comments yet. Be the first!</p>;
  }

  return (
    <ul className="comment-list">
      {fetchedComments.map((comment) => (
        <li key={comment.id}>
          <strong>{comment.user?.username || "Anonymous"}:</strong>{" "}
          {comment.content}
        </li>
      ))}
    </ul>
  );
}

export default CommentList;
