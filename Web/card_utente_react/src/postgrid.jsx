import React, { useEffect, useState } from "react";

const PostsGrid = () => {
  const urlPosts = "https://jsonplaceholder.typicode.com/posts/";
  const urlUsers = "https://jsonplaceholder.typicode.com/users/";
  const urlCommenti = "https://jsonplaceholder.typicode.com/comments"; //?postId=1
  const [posts, setPosts] = useState([]);
  async function fetchDetailsPost(post) {
    //console.log("post",post)
    const userP = fetch(urlUsers + post.userId).then((resp) => resp.json());
    const commentiP = fetch(urlCommenti + "?postId=" + post.id).then((resp) =>
      resp.json()
    );

    const [user, comments] = await Promise.all([userP, commentiP]);
    console.log(user, comments);
    return {
      ...post,
      user: user.name,
      comments: comments,
    };
  }
  //creare la funzione per leggere tutti i posts
  async function loadAllPosts() {
    try {
      const response = await fetch(urlPosts);
      if (!response.ok) {
        throw new Error("Errore nella chiamata a " + urlPosts);
      }
      const allPosts = await response.json();
      const allDataPromise = allPosts.map((post) => fetchDetailsPost(post));

      const allData = await Promise.all(allDataPromise);

      setPosts(allData);

      //   allData.forEach((post) => {
      //     const commentsHtml = post.comments
      //       .map((c) => `<li><strong>${c.name}</strong></li>`)
      //       .join("");

      //     // divContainer.innerHTML += `<div class="card">
      //     //     <h2>${post.title}</h2>
      //     //     <p>${post.body}</p>
      //     //     <small>${post.user}</small>
      //     //     <ul>${commentsHtml}</ul>
      //     //     </div>`;
      //   });
    } catch (err) {
      console.error("Errore nel caricamento dei dati " + err);
    }
  }
  useEffect(() => {
    loadAllPosts();
  }, []);
  return (
    <div style={styles.container}>
      {posts.map((post) => (
        <div key={post.id} style={styles.card}>
          <h2>{post.title}</h2>
          <p style={styles.p}>{post.body}</p>
          <small>{post.user}</small>
          <ul style={styles.ul}>
            {post.comments.map((c) => (
              <li key={"c"+c.id} style={styles.li}>{c.name}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

const styles = {
  container: {
    display: "flex",

    flexWrap: "wrap",
    gap: "20px",
    justifyContent: "center",
  },
  card: {
    backgroundColor: "white",
    border: "1px solid #c9c9c9",
    padding: "20px",
    borderRadius: "15px",
    maxWidth: "350px",
    boxShadow: "0 4px 8px rgb(0, 0, 0, 0.1)",
  },
  ul: {
    listStyleType: "none",
    paddingLeft: "0",
  },
  li: {
    margin: "5px 0",
    padding: "2px 0",
  },
  p: {
    fontSize: "0.8rem",
  },
};

export default PostsGrid;