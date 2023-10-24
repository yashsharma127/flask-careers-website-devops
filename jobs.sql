CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    location TEXT,
    salary INT
);


CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT,
    applicant_name VARCHAR(255) NOT NULL,
    applicant_email VARCHAR(255) NOT NULL,
    application_text TEXT,
    FOREIGN KEY (job_id) REFERENCES jobs(id)
);
