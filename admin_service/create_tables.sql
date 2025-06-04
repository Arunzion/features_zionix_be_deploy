-- Create the domains table if it doesn't exist
CREATE TABLE IF NOT EXISTS domains (
    id SERIAL PRIMARY KEY,
    domain_name VARCHAR(100) UNIQUE NOT NULL,
    domain_code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    status BOOLEAN DEFAULT TRUE,
    action TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes for domains
CREATE INDEX IF NOT EXISTS idx_domains_id ON domains(id);
CREATE INDEX IF NOT EXISTS idx_domains_domain_name ON domains(domain_name);
CREATE INDEX IF NOT EXISTS idx_domains_domain_code ON domains(domain_code);

-- Create the applications table if it doesn't exist
CREATE TABLE IF NOT EXISTS applications (
    id SERIAL PRIMARY KEY,
    application_name VARCHAR(100) NOT NULL,
    application_code VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    status BOOLEAN DEFAULT TRUE,
    action VARCHAR(50),
    domain_name VARCHAR(100) REFERENCES domains(domain_name) ON DELETE CASCADE,
    config TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes for applications
CREATE INDEX IF NOT EXISTS idx_applications_id ON applications(id);
CREATE INDEX IF NOT EXISTS idx_applications_name ON applications(application_name);
CREATE INDEX IF NOT EXISTS idx_applications_code ON applications(application_code);
CREATE INDEX IF NOT EXISTS idx_applications_domain ON applications(domain_name);
