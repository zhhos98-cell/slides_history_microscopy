#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
OUT="$DIR/gusu_vonderburg_canonical_v13.csv"
cat "$DIR"/canonical_parts/part_* > "$OUT"
ACTUAL="$(sha256sum "$OUT" | awk '{print $1}')"
EXPECTED="5d0e4406efce9c90d32248a3f6285596e49299d31023c4e7cafadfa492d0b7eb"
echo "bytes=$(wc -c < "$OUT")"
echo "sha256=$ACTUAL"
if [ "$ACTUAL" != "$EXPECTED" ]; then
  echo "ERROR: canonical manifest hash mismatch" >&2
  exit 1
fi
echo "OK: canonical v1.3 compact manifest reconstructed (LF-normalized)."
# The local working copy before GitHub normalization used CRLF and had SHA256:
# ccbf765f6d74766321442512f6b53eee043d5888d0a5a94715cd128ae5a30fdf
