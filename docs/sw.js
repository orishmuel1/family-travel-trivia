/**
 * PROJECT: Family Travel Trivia Application
 * FILE: docs/sw.js
 * PURPOSE: Cache the app shell for instant, fully-offline use.
 *
 * Strategy:
 *   - App shell (html/manifest/icons): cache-first  -> instant load with no signal.
 *   - data.json                      : network-first -> fresh content when online,
 *                                       cached copy when offline.
 *   - navigations offline            : fall back to the cached index.html.
 *
 * CACHE_NAME is stamped automatically by compiler.py from a hash of the shell + data,
 * so any content OR shell change bumps the version and evicts stale caches.
 */

const CACHE_NAME = 'trivia-cache-v-84ac6d3b';

const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './data.json',
  './manifest.json',
  './icon-192.png',
  './icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((names) =>
      Promise.all(names.map((name) => (name !== CACHE_NAME ? caches.delete(name) : null)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);

  // data.json: network-first (get updates when online), fall back to cache offline.
  if (url.pathname.endsWith('data.json')) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, copy));
          return res;
        })
        .catch(() => caches.match(req))
    );
    return;
  }

  // Everything else (the shell): cache-first, then network, then cached index.html.
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).catch(() => {
        if (req.mode === 'navigate') return caches.match('./index.html');
      });
    })
  );
});
