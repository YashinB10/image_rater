&#x20;Image Rater



A Python application that allows users to rate images and automatically compute statistics.



&#x20;Overview



This project provides a simple graphical interface to:



\- Browse images from a folder

\- Rate each image from 0 to 10

\- Compute statistics on the ratings

\- Save results to a JSON file



&#x20;Features



\- Dynamic image display (Tkinter GUI)

\- Rating system (0–10)

\- Statistics computation (mean, min, max, count)

\- JSON export of results

\- Modular architecture (separated logic)



&#x20;Tech Stack



\- Python

\- Tkinter (GUI)

\- Pillow (image processing)



&#x20;Project Structure



src/

&#x20; gui.py

&#x20; image\_loader.py

&#x20; rating.py

&#x20; stats.py

&#x20; storage.py



&#x20;How to Run



pip install -r requirements.txt

python src/gui.py



&#x20;Example Output



```

{

&#x20; "images": \[

&#x20;   {"path": "image1.jpg", "rating": 8}

&#x20; ],

&#x20; "stats": {

&#x20;   "mean": 8,

&#x20;   "min": 8,

&#x20;   "max": 8,

&#x20;   "count": 1

&#x20; }

}

```



&#x20;Notes



This project was built with a focus on:



\- clean code

\- modular design

\- separation of concerns



&#x20;Future Improvements



\- Folder selection via GUI (file dialog)

\- Better UI/UX

\- Image preview enhancements

\- Export formats (CSV, etc.)







&#x20;About This Project



This is my first real programming project as a high school student (seconde).



I built this project to improve my programming skills and understand how to structure a complete application.



&#x20;My Approach



While working on this project, I used ChatGPT as a learning tool , not as a shortcut.



Whenever I didn’t understand something:



\- I asked for detailed explanations

\- I made sure I fully understood the concept

\- I did not continue until I was able to reproduce the logic on my own



This approach allowed me to actually learn and not just copy code.



&#x20;What I Learned



\- Structuring a Python project into multiple modules

\- Building a simple GUI with Tkinter

\- Managing application state (images, index, ratings)

\- Handling errors and edge cases

\- Writing cleaner and more maintainable code



This project represents an important step in my learning journey.



