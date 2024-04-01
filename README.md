# Django URL Shortener

This project is a simple URL shortener built using Django.

## Overview

This Django application allows users to shorten URLs and redirect to the original long URLs.

## Features

- Shorten long URLs into a randomly generated short URL.
- Redirect from short URLs to the original long URLs.
- Error handling for non-existing short URLs.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Apuri-Amarnath/url-shortener.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

3. Enter a long URL and submit to get the shortened URL.

4. Use the shortened URL to redirect to the original long URL.

## Dependencies

- Django

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

Feel free to customize the README further with additional details or sections as needed for your project.
