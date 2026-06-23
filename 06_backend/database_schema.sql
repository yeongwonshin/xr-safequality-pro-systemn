CREATE TABLE tenants (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    plan TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE sites (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    timezone TEXT NOT NULL DEFAULT 'Asia/Seoul'
);

CREATE TABLE users (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    email TEXT NOT NULL,
    display_name TEXT NOT NULL,
    role TEXT NOT NULL,
    active BOOLEAN NOT NULL DEFAULT true,
    UNIQUE(tenant_id, email)
);

CREATE TABLE procedures (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    procedure_code TEXT NOT NULL,
    name TEXT NOT NULL,
    owner_role TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(tenant_id, procedure_code)
);

CREATE TABLE procedure_versions (
    id UUID PRIMARY KEY,
    procedure_id UUID NOT NULL REFERENCES procedures(id),
    version TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('draft','review','approved','retired')),
    dsl JSONB NOT NULL,
    approved_by UUID REFERENCES users(id),
    approved_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE(procedure_id, version)
);

CREATE TABLE inspection_sessions (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    site_id UUID NOT NULL REFERENCES sites(id),
    procedure_version_id UUID NOT NULL REFERENCES procedure_versions(id),
    worker_id UUID NOT NULL REFERENCES users(id),
    asset_id TEXT,
    device_type TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('active','completed','blocked','aborted','review_required')),
    started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    completed_at TIMESTAMPTZ
);

CREATE TABLE evidence_assets (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    session_id UUID NOT NULL REFERENCES inspection_sessions(id),
    step_id TEXT NOT NULL,
    storage_uri TEXT NOT NULL,
    sha256 TEXT NOT NULL,
    media_type TEXT NOT NULL,
    redaction_status TEXT NOT NULL DEFAULT 'not_required',
    retention_until TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE detection_events (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    session_id UUID NOT NULL REFERENCES inspection_sessions(id),
    step_id TEXT NOT NULL,
    model_version TEXT NOT NULL,
    policy_version TEXT NOT NULL,
    object_class TEXT NOT NULL,
    state TEXT,
    confidence NUMERIC(5,4) NOT NULL,
    bbox JSONB,
    evidence_id UUID REFERENCES evidence_assets(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE step_evaluations (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    session_id UUID NOT NULL REFERENCES inspection_sessions(id),
    step_id TEXT NOT NULL,
    result TEXT NOT NULL CHECK (result IN ('pass','fail','uncertain','blocked','approved_override')),
    reason JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE audit_events (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL REFERENCES tenants(id),
    actor_user_id UUID REFERENCES users(id),
    session_id UUID REFERENCES inspection_sessions(id),
    event_type TEXT NOT NULL,
    payload JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX idx_sessions_tenant_site ON inspection_sessions(tenant_id, site_id, started_at);
CREATE INDEX idx_detection_session_step ON detection_events(session_id, step_id);
CREATE INDEX idx_audit_tenant_time ON audit_events(tenant_id, created_at);
