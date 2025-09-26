
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Profile() {
  const { id } = useParams(); 
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://127.0.0.1:5555/users/${id}`)
      .then((res) => res.json())
      .then((data) => {
        setUser(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching user:", err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading profile...</p>;
  if (!user) return <p>User not found.</p>;

  return (
    <div className="profile">
      <h2>{user.username}’s Profile</h2>
      <p>Email: {user.email}</p>

      {/* Posts */}
      <section>
        <h3>Posts</h3>
        {user.posts?.length ? (
          <ul>
            {user.posts.map((post) => (
              <li key={post.id}>
                <h4>{post.title}</h4>
                <p>{post.content}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No posts yet.</p>
        )}
      </section>

      {/* Groups */}
      <section>
        <h3>Groups</h3>
        {user.groups?.length ? (
          <ul>
            {user.groups.map((group) => (
              <li key={group.id}>{group.name}</li>
            ))}
          </ul>
        ) : (
          <p>No groups joined yet.</p>
        )}
      </section>
    </div>
  );
}

export default Profile;
