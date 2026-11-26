(function () {
  'use strict';

  const root = document.documentElement;
  const parameters = new URLSearchParams(location.search);
  const embedded = window.parent !== window;
  const hostWindow = embedded ? window.parent : window.opener;
  root.classList.toggle('embedded', embedded);
  root.classList.toggle('audience', parameters.get('audience') === '1');

  try {
    const theme = localStorage.getItem('minutxo-theme');
    if (theme === 'dark' || theme === 'light') root.dataset.theme = theme;
  } catch (error) {
    // The deck remains usable when browser storage is unavailable.
  }

  const themeToggle = document.querySelector('.theme-toggle');
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = theme;
      try { localStorage.setItem('minutxo-theme', theme); } catch (error) {}
    });
  }

  const slides = Array.from(document.querySelectorAll('.slide'));
  if (slides.length === 0) return;

  const counter = document.getElementById('counter');
  const progress = document.getElementById('progress');
  const controls = Array.from(document.querySelectorAll('[data-step]'));
  const basename = location.pathname.split('/').pop().replace(/\.html$/, '');
  let channel = null;
  let current = -1;

  function show(index, options = {}) {
    const next = Math.max(0, Math.min(slides.length - 1, index));
    const changed = next !== current;
    current = next;

    slides.forEach(function (slide, slideIndex) {
      const active = slideIndex === current;
      slide.classList.toggle('active', active);
      slide.setAttribute('aria-hidden', String(!active));
    });

    if (counter) counter.textContent = (current + 1) + ' / ' + slides.length;
    if (progress) progress.style.width = ((current + 1) / slides.length * 100) + '%';
    controls.forEach(function (control) {
      const step = Number(control.dataset.step);
      control.disabled = (step < 0 && current === 0) || (step > 0 && current === slides.length - 1);
    });

    const hash = '#' + (current + 1);
    if (!embedded && location.hash !== hash) {
      if (options.replaceHistory) history.replaceState(null, '', hash);
      else history.pushState(null, '', hash);
    }

    const heading = slides[current].querySelector('h1, h2');
    const state = {
      type: 'minutxo:slide',
      slide: current + 1,
      total: slides.length,
      title: heading?.textContent.trim() || slides[current].getAttribute('aria-label') || ''
    };
    if (changed && options.notifyParent !== false && hostWindow) {
      hostWindow.postMessage(state, '*');
    }
    if (changed && channel && options.broadcast !== false) channel.postMessage(state);
  }

  function showHash() {
    const value = location.hash.slice(1);
    const slide = /^-?\d+$/.test(value) ? Number(value) : 1;
    const initialized = current !== -1;
    show(Number.isSafeInteger(slide) ? slide - 1 : 0, {
      replaceHistory: true,
      notifyParent: initialized,
      broadcast: initialized
    });
  }

  window.addEventListener('hashchange', showHash);
  window.addEventListener('popstate', showHash);
  window.addEventListener('message', function (event) {
    if (!hostWindow || event.source !== hostWindow) return;
    if (event.data?.type !== 'minutxo:navigate' || !Number.isInteger(event.data.slide)) return;
    show(event.data.slide - 1, { replaceHistory: true, broadcast: false, notifyParent: false });
  });

  const interactive = 'a, button, input, textarea, select, summary, [contenteditable], [role="button"]';
  document.addEventListener('keydown', function (event) {
    if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey || event.defaultPrevented) return;
    if (event.target.closest('input, textarea, select, [contenteditable]')) return;
    if (event.key === ' ' && event.target.closest(interactive)) return;
    const destinations = {
      ArrowRight: current + 1,
      ' ': current + 1,
      PageDown: current + 1,
      ArrowLeft: current - 1,
      PageUp: current - 1,
      Home: 0,
      End: slides.length - 1,
      Escape: 0
    };
    if (!(event.key in destinations)) return;
    event.preventDefault();
    show(destinations[event.key]);
  });

  document.addEventListener('click', function (event) {
    const stepControl = event.target.closest('[data-step]');
    if (stepControl) {
      event.preventDefault();
      if (!stepControl.disabled) show(current + Number(stepControl.dataset.step));
      return;
    }
    if (event.target.closest('.btn-close')) {
      event.preventDefault();
      show(0);
      return;
    }
    if (event.target.closest(interactive) || !event.target.closest('.deck')) return;
    if (window.getSelection()?.toString()) return;
    show(current + 1);
  });

  let touchStart = null;
  document.addEventListener('touchstart', function (event) {
    const diagram = event.target.closest('.diagram-scroll');
    if (event.target.closest(interactive) || (diagram && diagram.scrollWidth > diagram.clientWidth)) {
      touchStart = null;
      return;
    }
    const touch = event.changedTouches[0];
    touchStart = { x: touch.clientX, y: touch.clientY };
  }, { passive: true });

  document.addEventListener('touchend', function (event) {
    if (!touchStart) return;
    const touch = event.changedTouches[0];
    const dx = touch.clientX - touchStart.x;
    const dy = touch.clientY - touchStart.y;
    touchStart = null;
    if (Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy) * 1.5) {
      show(current + (dx < 0 ? 1 : -1));
    }
  }, { passive: true });

  document.addEventListener('touchcancel', function () { touchStart = null; }, { passive: true });
  showHash();
  if (hostWindow) hostWindow.postMessage({ type: 'minutxo:ready' }, '*');
})();
