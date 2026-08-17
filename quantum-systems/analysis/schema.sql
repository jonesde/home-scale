-- QSA analysis schema.
-- Markdown in library/ is the science source of truth.
-- This schema is the query surface. Rebuild from analysis/ via rebuild.py.

PRAGMA foreign_keys = ON;

CREATE TABLE effect (
  slug                TEXT PRIMARY KEY,
  title               TEXT NOT NULL,
  family              TEXT NOT NULL
    CHECK (family IN (
      'collective-field-response',
      'latched-order',
      'gapped-coherence',
      'threshold-conversion',
      'lattice-modes',
      'ensemble-averages'
    )),
  status              TEXT NOT NULL
    CHECK (status IN ('formal', 'draft')),
  confidence_data     TEXT NOT NULL
    CHECK (confidence_data IN ('high', 'medium', 'low')),
  confidence_mapping  TEXT NOT NULL
    CHECK (confidence_mapping IN ('high', 'medium', 'low', 'unmapped')),
  source_path         TEXT NOT NULL,
  updated             TEXT NOT NULL
);

CREATE TABLE effect_constraint (
  slug  TEXT NOT NULL REFERENCES effect(slug) ON DELETE CASCADE,
  tag   TEXT NOT NULL
    CHECK (tag IN (
      'spatial-buffer',
      'clock-latency',
      'energy-barrier',
      'mechanical-lattice',
      'field-threshold',
      'thermal'
    )),
  PRIMARY KEY (slug, tag)
);

-- Slug-based primary key.
-- extracted: {effect_slug}:{clause}:{short-name}
-- predicted: predicted:{effect_slug|design_key}:{short-name}
CREATE TABLE implication (
  impl_key        TEXT PRIMARY KEY,
  origin          TEXT NOT NULL DEFAULT 'extracted'
    CHECK (origin IN ('extracted', 'predicted')),
  effect_slug     TEXT REFERENCES effect(slug),
  source_path     TEXT,
  clause          TEXT NOT NULL
    CHECK (clause IN (
      'hardware_scale',
      'clock_latency',
      'energy_barrier',
      'failure_mode',
      'emergent_output',
      'consistency_gap'
    )),
  role            TEXT NOT NULL
    CHECK (role IN ('requirement', 'failure', 'output', 'gap')),
  aspect          TEXT NOT NULL
    CHECK (aspect IN (
      'scale', 'capacity', 'speed', 'latency',
      'barrier', 'threshold', 'power', 'output'
    )),
  resource        TEXT NOT NULL
    CHECK (resource IN (
      'length', 'area', 'volume', 'node_count',
      'time', 'frequency', 'energy', 'temperature',
      'e_field', 'b_field', 'current', 'mass', 'charge',
      'dimensionless', 'other'
    )),
  observed_text   TEXT NOT NULL,
  implied_text    TEXT NOT NULL,
  inference_kind  TEXT NOT NULL
    CHECK (inference_kind IN ('relabel', 'derived', 'envelope', 'open')),
  description     TEXT NOT NULL,
  operator        TEXT
    CHECK (operator IS NULL OR operator IN ('eq', 'min', 'max', 'approx', 'range')),
  value_si        REAL,
  si_unit         TEXT,
  value_text      TEXT,
  confidence      TEXT NOT NULL
    CHECK (confidence IN ('high', 'medium', 'low')),
  notes           TEXT,
  updated         TEXT NOT NULL,
  CHECK (
    (origin = 'extracted'
      AND effect_slug IS NOT NULL
      AND source_path IS NOT NULL
      AND impl_key NOT LIKE 'predicted:%')
    OR
    (origin = 'predicted'
      AND impl_key LIKE 'predicted:%')
  )
);

CREATE INDEX idx_implication_effect    ON implication(effect_slug);
CREATE INDEX idx_implication_origin    ON implication(origin);
CREATE INDEX idx_implication_role      ON implication(role);
CREATE INDEX idx_implication_aspect    ON implication(aspect, resource);
CREATE INDEX idx_implication_inference ON implication(inference_kind);
CREATE INDEX idx_implication_conf      ON implication(confidence);
CREATE INDEX idx_implication_clause    ON implication(clause);

-- Assembled reverse-engineered machine (not agency).
CREATE TABLE design (
  design_key    TEXT PRIMARY KEY,
  title         TEXT NOT NULL,
  summary       TEXT NOT NULL,
  home_family   TEXT NOT NULL
    CHECK (home_family IN (
      'collective-field-response',
      'latched-order',
      'gapped-coherence',
      'threshold-conversion',
      'lattice-modes',
      'ensemble-averages'
    )),
  status        TEXT NOT NULL
    CHECK (status IN ('formal', 'draft')),
  confidence    TEXT NOT NULL
    CHECK (confidence IN ('high', 'medium', 'low')),
  description   TEXT NOT NULL,
  notes         TEXT,
  updated       TEXT NOT NULL
);

CREATE TABLE implication_design (
  impl_key     TEXT NOT NULL REFERENCES implication(impl_key),
  design_key   TEXT NOT NULL REFERENCES design(design_key),
  membership   TEXT NOT NULL
    CHECK (membership IN ('core', 'supporting', 'contrast')),
  notes        TEXT,
  PRIMARY KEY (impl_key, design_key)
);

-- Top-down: if this machine is right, which atomic claims follow.
CREATE TABLE design_implication (
  design_key   TEXT NOT NULL REFERENCES design(design_key),
  impl_key     TEXT NOT NULL REFERENCES implication(impl_key),
  relation     TEXT NOT NULL
    CHECK (relation IN ('entails', 'predicts', 'incompatible')),
  strength     TEXT NOT NULL
    CHECK (strength IN ('must', 'should')),
  notes        TEXT,
  PRIMARY KEY (design_key, impl_key)
);

CREATE TABLE requirement (
  req_key       TEXT PRIMARY KEY,
  title         TEXT NOT NULL,
  kind          TEXT NOT NULL
    CHECK (kind IN ('spec', 'consistency', 'prediction', 'closure')),
  aspect        TEXT NOT NULL
    CHECK (aspect IN (
      'scale', 'capacity', 'speed', 'latency',
      'barrier', 'threshold', 'power', 'output'
    )),
  resource      TEXT NOT NULL
    CHECK (resource IN (
      'length', 'area', 'volume', 'node_count',
      'time', 'frequency', 'energy', 'temperature',
      'e_field', 'b_field', 'current', 'mass', 'charge',
      'dimensionless', 'other'
    )),
  statement     TEXT NOT NULL,
  operator      TEXT
    CHECK (operator IS NULL OR operator IN ('eq', 'min', 'max', 'approx', 'range')),
  value_si      REAL,
  si_unit       TEXT,
  value_text    TEXT,
  status        TEXT NOT NULL
    CHECK (status IN ('open', 'satisfied', 'tension', 'untested')),
  confidence    TEXT NOT NULL
    CHECK (confidence IN ('high', 'medium', 'low')),
  notes         TEXT,
  updated       TEXT NOT NULL
);

CREATE TABLE design_requirement (
  design_key    TEXT NOT NULL REFERENCES design(design_key),
  req_key       TEXT NOT NULL REFERENCES requirement(req_key),
  strength      TEXT NOT NULL
    CHECK (strength IN ('must', 'should')),
  notes         TEXT,
  PRIMARY KEY (design_key, req_key)
);

-- Constituent consumed by one or more machines. Not an effect, not a design.
CREATE TABLE node (
  node_key         TEXT PRIMARY KEY,
  title            TEXT NOT NULL,
  kind             TEXT NOT NULL
    CHECK (kind IN ('elementary', 'composite', 'quasiparticle')),
  origin           TEXT NOT NULL
    CHECK (origin IN ('forced', 'cataloged', 'predicted')),
  status           TEXT NOT NULL
    CHECK (status IN ('formal', 'draft')),
  confidence       TEXT NOT NULL
    CHECK (confidence IN ('high', 'medium', 'low')),
  pdgid            INTEGER,
  charge_e         REAL,
  mass_si          REAL,
  mass_text        TEXT,
  spin_text        TEXT,
  statistics       TEXT
    CHECK (statistics IS NULL OR statistics IN ('fermion', 'boson', 'unset')),
  lifetime_si      REAL,
  identity_source  TEXT,
  source_path      TEXT NOT NULL,
  description      TEXT NOT NULL,
  notes            TEXT,
  updated          TEXT NOT NULL
);

CREATE TABLE implication_node (
  impl_key     TEXT NOT NULL REFERENCES implication(impl_key),
  node_key     TEXT NOT NULL REFERENCES node(node_key),
  membership   TEXT NOT NULL
    CHECK (membership IN ('forces', 'witnesses', 'contrast')),
  notes        TEXT,
  PRIMARY KEY (impl_key, node_key)
);

CREATE TABLE design_node (
  design_key   TEXT NOT NULL REFERENCES design(design_key),
  node_key     TEXT NOT NULL REFERENCES node(node_key),
  role         TEXT NOT NULL
    CHECK (role IN (
      'population', 'single', 'average', 'recoil', 'mode',
      'matrix', 'latch-cell', 'input', 'product', 'edge', 'contrast'
    )),
  notes        TEXT,
  PRIMARY KEY (design_key, node_key)
);

CREATE INDEX idx_implication_design_design ON implication_design(design_key);
CREATE INDEX idx_implication_design_impl   ON implication_design(impl_key);
CREATE INDEX idx_design_implication_design ON design_implication(design_key);
CREATE INDEX idx_design_implication_impl   ON design_implication(impl_key);
CREATE INDEX idx_design_implication_rel    ON design_implication(relation);
CREATE INDEX idx_design_requirement_req    ON design_requirement(req_key);
CREATE INDEX idx_requirement_kind          ON requirement(kind);
CREATE INDEX idx_requirement_status        ON requirement(status);
CREATE INDEX idx_node_origin               ON node(origin);
CREATE INDEX idx_node_kind                 ON node(kind);
CREATE INDEX idx_implication_node_node     ON implication_node(node_key);
CREATE INDEX idx_design_node_node          ON design_node(node_key);
CREATE INDEX idx_design_node_role          ON design_node(role);
