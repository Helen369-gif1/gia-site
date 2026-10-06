/* Gia site — behavior for shared components. Load after js/site.js on pages that use them.
   Everything is driven by data attributes, so pages need no extra code.

   Approval sheet  [data-approval]
     Checkboxes .approval__check mark terms as reviewed. "Authorize Gia" [data-approval-authorize]
     refuses while a term is unreviewed and names it; otherwise it opens an explicit confirmation
     (.approval__confirm with [data-approval-confirm] / [data-approval-back]). "Not for me"
     [data-approval-decline] is a normal outcome, not an error. [data-approval-reset] starts over.
     Optional: data-log="#id" adds entries to an activity history (.log) on the page;
     data-subject="..." names the thing being authorized in messages and log entries.

   Ambient motion  [data-motion]
     Adds .is-playing while the element is in view, so CSS animations inside it run only then.
     Never added under reduced motion; CSS shows the complete still state instead.

   Play-once video  video[data-play-once]   (hero videos on every page)
     Plays once each time it comes into view: after a short pause (data-delay, ms, default 800)
     it starts from the first frame and stops on the last frame. No loop. When it leaves the
     screen it rewinds, so it can play again the next time it comes into view.
     Under reduced motion it never plays; data-still (an image of the last frame) replaces the
     poster so the complete composition is shown. */
(() => {
  const { reduce } = window.GiaSite || { reduce: window.matchMedia('(prefers-reduced-motion: reduce)').matches };

  /* ---------- Approval sheet ---------- */
  document.querySelectorAll('[data-approval]').forEach((sheet) => {
    const items = [...sheet.querySelectorAll('.approval__item')];
    const actions = sheet.querySelector('.approval__actions');
    const confirmBox = sheet.querySelector('.approval__confirm');
    const msg = sheet.querySelector('.approval__msg');
    const log = sheet.dataset.log ? document.querySelector(sheet.dataset.log) : null;
    const subject = sheet.dataset.subject || 'this project';
    const resetBtn = sheet.querySelector('[data-approval-reset]');

    const say = (text, tone) => { if (!msg) return; msg.textContent = text; msg.className = 'approval__msg' + (tone ? ' is-' + tone : ''); };
    const addLog = (text, status, cls) => {
      if (!log) return;
      const li = document.createElement('li');
      li.className = 'is-new';
      li.innerHTML = `${text}<small>Just now</small><span class="status ${cls}">${status}</span>`;
      log.prepend(li);
    };
    const syncItem = (it) => {
      const box = it.querySelector('.approval__check');
      const st = it.querySelector('[data-state]');
      it.classList.toggle('is-open', !box.checked);
      if (st) {
        st.textContent = box.checked ? 'Reviewed' : 'Not reviewed';
        st.className = 'status ' + (box.checked ? 'status--ready' : 'status--review');
      }
    };
    const setStage = (stage) => {
      if (actions) actions.hidden = stage !== 'review';
      if (confirmBox) confirmBox.hidden = stage !== 'confirm';
      if (resetBtn) resetBtn.hidden = stage !== 'done';
      sheet.classList.toggle('is-done', stage === 'done');
      items.forEach(it => { it.querySelector('.approval__check').disabled = stage === 'done'; });
    };

    items.forEach((it) => {
      syncItem(it);
      it.querySelector('.approval__check').addEventListener('change', () => { syncItem(it); say(''); });
    });

    sheet.addEventListener('click', (e) => {
      const b = e.target.closest('button'); if (!b || !sheet.contains(b)) return;
      if (b.hasAttribute('data-approval-authorize')) {
        const open = items.filter(it => !it.querySelector('.approval__check').checked);
        if (open.length) {
          const name = open[0].querySelector('.approval__label').textContent.trim();
          say(`Review every term first. Still open: ${name}${open.length > 1 ? ` and ${open.length - 1} more` : ''}.`, 'warn');
          open[0].querySelector('.approval__check').focus();
          return;
        }
        say('');
        setStage('confirm');
        const c = confirmBox && confirmBox.querySelector('[data-approval-confirm]');
        if (c) c.focus();
      } else if (b.hasAttribute('data-approval-back')) {
        setStage('review');
        const a = sheet.querySelector('[data-approval-authorize]'); if (a) a.focus();
      } else if (b.hasAttribute('data-approval-confirm')) {
        setStage('done');
        say(`Authorized. Gia starts ${subject} and brings questions and milestones back to you.`, 'ok');
        addLog(`Authorized Gia for ${subject}`, 'Authorized', 'status--ready');
        if (resetBtn) resetBtn.focus();
      } else if (b.hasAttribute('data-approval-decline')) {
        setStage('done');
        say(`Declined. Nothing starts, and Gia keeps looking for projects that fit.`);
        addLog(`Declined ${subject}`, 'Declined', 'status--muted');
        if (resetBtn) resetBtn.focus();
      } else if (b.hasAttribute('data-approval-reset')) {
        items.forEach(it => { it.querySelector('.approval__check').checked = false; syncItem(it); });
        say('');
        setStage('review');
        items[0] && items[0].querySelector('.approval__check').focus();
      }
    });
    setStage('review');
  });

  /* ---------- Ambient motion ---------- */
  document.querySelectorAll('[data-motion]').forEach((el) => {
    if (reduce) return;
    new IntersectionObserver((entries) => {
      entries.forEach((en) => el.classList.toggle('is-playing', en.isIntersecting));
    }, { threshold: 0.2 }).observe(el);
  });

  /* ---------- Play-once video ---------- */
  document.querySelectorAll('video[data-play-once]').forEach((v) => {
    v.muted = true; v.loop = false; v.playsInline = true;
    v.removeAttribute('autoplay');
    if (reduce) {
      v.pause();
      if (v.dataset.still) v.poster = v.dataset.still;
      v.preload = 'none';
      return;
    }
    const delay = Number(v.dataset.delay || 800);
    let timer = null;
    let played = false;   // already played during this visit to the screen
    const start = () => {
      timer = null;
      if (played || document.hidden) return;
      played = true;
      try { v.currentTime = 0; } catch (e) {}
      const p = v.play(); if (p) p.catch(() => { played = false; });
    };
    new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          if (!played && !timer) timer = setTimeout(start, delay);
        } else {
          if (timer) { clearTimeout(timer); timer = null; }
          v.pause();
          played = false;
          try { v.currentTime = 0; } catch (e) {}
        }
      });
    }, { threshold: 0.5 }).observe(v);
  });
})();
