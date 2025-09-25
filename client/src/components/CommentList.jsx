
import React from "react";

function CommentList({ comments }) {
  if (!comments || comments.length === 0) {
    return <p>No comments yet. Be the first!</p>;
  }

  return (
    <ul className="comment-list">
      {comments.map((comment) => (
        <li key={comment.id}>
          <strong>{comment.user?.username || "Anonymous"}:</strong>{" "}
          {comment.content}
        </li>
      ))}
    </ul>
  );
}

export default CommentList;
