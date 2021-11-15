# Everyday Blogs
## Author
[Ian Wanjira]( https://github.com/Ian-Wa)

# Description
This is a flask application where users can blog and comment on other people's blogs once logged in. Users can also delete comments they don't like on their blogs and also update previous blog posts.

## Installation Instruction
1. Cloning the repository:
  ```bash
  https://github.com/Ian-Wa/flask-blog.git

  2. Move to the folder and install requirements
  ```bash
  cd Blogs-master
  pip install -r requirements.txt
  ```

3. Exporting Configurations
```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application
  ```bash
  python3.8 manage.py server
  ```

5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
  Open the application on your browser `127.0.0.1:5000`.

## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)
* HTML
* CSS

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [Ian Wanjira](https://www.ianwanjira4@gmail.com)

## License
* *MIT License*