# pitrLabs Landing Page
This project is a business landing page for pitrLabs.  
The main page presents a short company profile, service offerings, testimonials, FAQ, and a contact form for potential clients.

## Main Features
- Single-page navigation with these sections:
  - Home
  - Services
  - Testimonials
  - FAQ
  - Contact
- Responsive UI built with Bootstrap.
- Bilingual support (Indonesian and English) via language switch buttons.
- Contact form that sends data to a backend endpoint (`/send-email/`).
- Django static asset integration (`{% static %}`) for CSS, JS, icons, and images.

## Service Portfolio (Our Services)
The landing page highlights pitrLabs service offerings across multiple domains:

- **Data Processing**  
  Data workflow solutions using tools such as Apache Airflow, Prefect, Pentaho, Talend, and Apache Spark for orchestration, ETL, and distributed processing.

- **Web Development**  
  Modern, secure, and responsive website development, from company landing pages to full multi-user web applications.

- **Mobile App Development**  
  End-to-end mobile app delivery for Android and iOS, including UI/UX, backend integration, testing, and release preparation.

- **API Development & Integration**  
  API architecture and integration support (REST, GraphQL, gRPC, SOAP), including authentication, documentation, testing, and deployment.

- **Enterprise Resource Planning (ERP)**  
  ERP implementation and customization to unify business operations such as finance, inventory, purchasing, CRM, and HR.

- **Customer Relationship Management (CRM)**  
  CRM system implementation for contact management, lead tracking, sales pipeline handling, and workflow automation.

- **Academic Project Assistance**  
  Structured guidance for academic work (D3/S1/S2/S3), covering methodology, technical implementation, and data-related execution.

- **Computer Vision**  
  Custom computer vision services such as OCR, object detection, and image classification for operational and research use cases.

- **Workflow & Automation**  
  Business process automation by integrating APIs, databases, and AI services into operational pipelines using modern automation platforms.

## Tech Stack
- Django Template Engine
- HTML, CSS, JavaScript
- Bootstrap
- Font Awesome

## Important Structure
- `templates/index.html` → main landing page template.
- `static/` → frontend assets (stylesheets, scripts, images, vendor assets).

## Run Locally
1. Activate the project environment with pyenv + poetry:
   - `pyenv exec poetry shell`
2. Start the Django development server:
   - `python manage.py runserver`
3. Open:
   - `http://127.0.0.1:8000/`

## Notes
- The contact form sends a POST request to `/send-email/`.
- Make sure your Django email backend is configured correctly so contact submissions can be delivered.
- Some service demo buttons are currently marked as “Coming soon”.