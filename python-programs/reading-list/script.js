
const form = document.getElementById("book-form");
const titleInput = document.getElementById("book-title");
const authorInput = document.getElementById("book-author");
const bookList = document.getElementById("book-list");
const message = document.getElementById("message");
const bookCount = document.getElementById("book-count");

let books = [];

function displayBooks() {
  bookList.innerHTML = "";

  books.forEach((book, index) => {
    const li = document.createElement("li");

    const title = document.createElement("strong");
    title.textContent = book.title;

    const author = document.createElement("p");
    author.textContent = "Author: " + book.author;

    const status = document.createElement("p");
    status.textContent = book.read ? "Read" : "Not Read";
    status.className = book.read ? "read-status" : "";

    const readButton = document.createElement("button");
    readButton.textContent = book.read
      ? "Mark as Unread"
      : "Mark as Read";

    readButton.onclick = () => {
      books[index].read = !books[index].read;
      displayBooks();
    };

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-btn";

    deleteButton.onclick = () => {
      books.splice(index, 1);
      displayBooks();
      message.textContent = "Book deleted successfully!";
    };

    li.append(title, author, status, readButton, deleteButton);
    bookList.appendChild(li);
  });

  bookCount.textContent = "Books: " + books.length;
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const title = titleInput.value.trim();
  const author = authorInput.value.trim();

  if (!title || !author) {
    message.textContent = "Please enter both book title and author.";
    return;
  }

  books.push({
    title: title,
    author: author,
    read: false
  });

  displayBooks();
  form.reset();
  message.textContent = "Book added successfully!";
});

