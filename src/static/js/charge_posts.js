let page = 0
window.onscroll = async () => {
  const totalPageHeight = document.body.scrollHeight
  const scrollPoint     = (window.scrollY + window.innerHeight) - 120
  if(scrollPoint >= totalPageHeight){
    page+=5
    let response = await fetch("/post", {
      method: "POST",
      body: JSON.stringify(page),
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
    })
    
    if(response) {
      let posts     = await response.text()
      const parser  = new DOMParser()
      posts         = parser.parseFromString(posts, "text/html")
      posts         = posts.body.querySelectorAll(".post")
      const posts_container = document.querySelector(".posts_container")
      for (let i = 0; i < posts.length; i++) {
        posts_container.appendChild(posts[i]) 
      }
    }
  }
}