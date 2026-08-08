# Brk-Trkr Documentation

Brk-Trkr documentation is organized as a language-neutral root with language-specific documentation beneath `i18n/`.

## Languages

- [English](./i18n/en/README.md) (`en`) — authoritative source language

## Translation model

Each translated language SHOULD mirror the English path structure so equivalent documents retain stable locations and cross-reference topology.

```text
docs/
├── README.md
└── i18n/
    ├── en/
    │   ├── README.md
    │   ├── product/
    │   ├── architecture/
    │   └── development/
    └── <language-code>/
        ├── README.md
        ├── product/
        ├── architecture/
        └── development/
```

Documents use a stable `translation_key` in front matter. Translations should preserve that key even when filenames or headings are localized.
