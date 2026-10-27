# NEXERP — Small Business ERP

Portfolio-ready ERP foundation for small businesses. Includes connected sales, purchases, inventory, accounting, manufacturing, HR, CRM, projects, assets, reports and role-based user access.

## Stack
- React + Vite + JavaScript + HTML/CSS
- Node.js + Express
- MongoDB + Mongoose
- Python FastAPI microservice (existing analytics service)

## Major workflows
- Sales invoice → GST calculation → stock deduction → income ledger entry
- Purchase bill → GST calculation → stock addition → purchase expense entry
- BOM → Work Order → consume raw materials → add finished stock
- Payroll → salary calculation → salary expense ledger entry
- Admin/user roles, admin-only user management and admin signup key
- Search/filtering on inventory, printable invoices and print-ready reports
- Relationships using MongoDB ObjectId references
## Local setup
### 1. MongoDB
Start MongoDB Community Server. Local URI:
`mongodb://127.0.0.1:27017/small_business_erp`

### 2. Server
```powershell
cd server
npm install
copy .env.example .env
npm run seed
npm run dev

Server: http://localhost:5000

### 3. Client
```powershell
cd client
npm install
npm run dev -- --host 0.0.0.0 
```
Client: http://localhost:5173

### 4. Python service
The included Python service can be started separately:
```powershell
cd python-service
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

If using Python 3.14 causes `pydantic-core` build errors, use Python 3.12 for this service.

## Important production notes
This project is designed as a portfolio/local-development ERP. Before production use, 
add stronger audit logs, refresh tokens, rate limiting, CSRF protection, granular permissions, invoice numbering locks, 
database transactions/replica set, backups, GST compliance review, and secure secret management.
