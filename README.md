# techdocs-core-128

A repository for reproducing techdocs-core plugin [issue #128](https://github.com/backstage/mkdocs-techdocs-core/issues/128)

## Context

Enabling the [`techdocs-core`](https://github.com/backstage/mkdocs-techdocs-core) plugin breaks code annotation render in mkdocs-material.

This plugin overrides user configurations.

One setting in particular that seems to be causing problems is setting `theme.palette` to `""`.

## Prerequisites

* techdocs-cli - `npm i -g @techdocs/cli`

## See the issue

Run `techdocs-cli serve` and visit `http://localhost:3000` to view the code annotation failing to render within Backstage, or `http://localhost:8000` to see the issue within a mkdocs site.

## Half-Mitigation

In an attempt to find a work around, I created a mkdocs hook that sets resets the `theme.palette` configuration after `techdocs-core` has done its job. 

To see this, uncomment the `hooks` block in `mkdocs.yml` and reserve the site with `techdocs-cli server`.

With this hook applied - the rendering is resolved in the mkdocs site (`http://localhost:8000`) but is still broken within backstage (`http://localhost:3000`).
