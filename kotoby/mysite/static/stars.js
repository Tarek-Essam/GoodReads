let books = document.getElementsByClassName('stars')
let allStars = document.getElementsByClassName('fa')

for (var i = 0; i < allStars.length; i++) {
    allStars[i].addEventListener("mouseover", light)
    allStars[i].addEventListener("mouseout", noLight)
    allStars[i].addEventListener("click", rate)
}

function init(){
    for (var i = 0; i < allStars.length; i++) {
        allStars[i].removeAttribute("class")
        allStars[i].classList.add("fa")
        allStars[i].classList.add("fa-star")
    }
    for (let i = 0; i < books.length; i++) {
        book = books[i]
        starsNumber = Number(book.title)
        stars = book.children
        for (let i = 0; i < starsNumber; i++) {
            stars[i].classList.add("checked")
        }
    }
}

init()

function light(e)
{
    let stars = e.target.parentElement.children
    for (var i = 0; i < stars.length; i++) {
        stars[i].removeAttribute("class")
        stars[i].classList.add("fa")
        stars[i].classList.add("fa-star")
    }
    let n = Array.prototype.indexOf.call(stars, e.target);
    for (let i = 0; i < n+1; i++) {
        stars[i].classList.add("checked")
    }
}

function noLight(e)
{
    e.target.removeAttribute("class")
    e.target.classList.add("fa")
    e.target.classList.add("fa-star")
    init()
}

function rate(e)
{
    light(e)
    let stars = e.target.parentElement.children
    let n = Array.prototype.indexOf.call(stars, e.target) + 1;
    let parent = e.target.parentElement
    parent.title = n

}
