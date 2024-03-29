let page = 0
let data = {}
if(typeof user != "undefined"){
  data.user = JSON.parse(user)
}
data.page       = page
data.request    = true
window.onscroll = async () => {
  const totalPageHeight = document.body.scrollHeight
  const scrollPoint     = (window.scrollY + window.innerHeight) - 140
  if(scrollPoint >= totalPageHeight){
    data.page+=2
    let response = await fetch("/post", {
      method: "POST",
      body: JSON.stringify(data),
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