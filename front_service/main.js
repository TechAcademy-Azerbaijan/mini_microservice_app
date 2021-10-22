let createPostForm = document.getElementById('create-post-form');
let postListSection = document.getElementById('posts')

async function renderPost(postData) {
    let comments = postData.comments || [];  // await getComments(postId = postData.id);
    postListSection.innerHTML += `
         <div class="col-3">
            <div class="card p-4">
                <h3>${postData.title}</h3>
                <ul>
                     ${ comments.map(comment => `<li>${comment.content}</li>`).join('') }
                </ul>
                <form class="create-comment" data-postId="${postData.id}">  
                        <input type="text" name="content" placeholder="Write your comment">
                        <input type="submit" value="Save">
                 </form>
            </div>
         </div>
        `;
}

window.addEventListener('submit', async function (e) {
    e.preventDefault();
    if(e.target.classList.contains('create-comment')){
        await createComment(e.target);
    }

})

async function createComment(form){
    console.log(form);
    let postId = form.dataset.postid;
    console.log(postId);
    let commentData = {
        'content': form.content.value
    }
    let response = await fetch(`http://localhost:5001/posts/${postId}/comments`, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(commentData)
    })
    if(response.ok){
        form.previousElementSibling.innerHTML += `<li>${form.content.value}</li>`
    }
}

async function createPost(postData){
    let response = await fetch('http://localhost:5000/posts', {
        headers: {
            'Content-Type': 'application/json'
        },
        'method': 'POST',
        body: JSON.stringify(postData),
    })
    return response.json();
}

async function getPosts(){
    let response = await fetch('http://localhost:5003/posts')
    return response.json();
}

async function getComments(postId){
    let response = await fetch(`http://localhost:5001/posts/${postId}/comments`)
    return response.json();
}

createPostForm.addEventListener('submit', async function (e) {
    e.preventDefault();
    let postTitle = createPostForm.post.value;
    let postData = {
        'title': postTitle
    }
    let newPost = await createPost(postData);
    renderPost(postData=newPost);
});


document.addEventListener("DOMContentLoaded", async function() {
    let posts = await getPosts();
    for(let post of posts){
        await renderPost(post);
    }
});