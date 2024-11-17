# Yusuf

Yusuf is a web application designed to analyze CVs and provide professional summaries, job recommendations, and other related functionalities. The application leverages Groq's vision model to analyze CV images and Coresignal's API to fetch job listings.

## Features

- **CV Upload**: Upload a PDF CV and convert it to images for analysis.
- **CV Analysis**: Analyze the CV using Groq's vision model to generate a professional summary.
- **Job Recommendations**: Get job recommendations based on the analyzed CV.
- **Job Details**: View detailed information about recommended jobs.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/JerryWu0430/yusuf.git
    cd yusuf
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory with the following content:
        ```properties
        GROQ_API_KEY = your_groq_api_key
        SECRET_KEY = your_secret_key
        BEARER_TOKEN = your_bearer_token
        ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Upload a CV in PDF format on the homepage.

4. View the analyzed CV summary and job recommendations.

## API Endpoints

- **Upload CV**: `/upload-cv` (POST)
- **Job Listings**: `/api/job-listings` (GET)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Groq](https://groq.com/) for their vision model.
- [Coresignal](https://coresignal.com/) for their job search API.
