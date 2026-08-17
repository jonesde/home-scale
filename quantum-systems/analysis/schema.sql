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

-- Slug-based primary key: {effect_slug}:{clause}:{short-name}
CREATE TABLE implication (
  impl_key        TEXT PRIMARY KEY,
  effect_slug     TEXT NOT NULL REFERENCES effect(slug),
  source_path     TEXT NOT NULL,
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
  updated         TEXT NOT NULL
);

CREATE INDEX idx_implication_effect    ON implication(effect_slug);
CREATE INDEX idx_implication_role      ON implication(role);
CREATE INDEX idx_implication_aspect    ON implication(aspect, resource);
CREATE INDEX idx_implication_inference ON implication(inference_kind);
CREATE INDEX idx_implication_conf      ON implication(confidence);
CREATE INDEX idx_implication_clause    ON implication(clause);
