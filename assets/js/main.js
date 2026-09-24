(function () {
  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  }

  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  var chips = document.querySelectorAll('.chip');
  var rows = document.querySelectorAll('#fees tbody tr');
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.remove('on'); });
      c.classList.add('on');
      var f = c.getAttribute('data-f');
      rows.forEach(function (r) { r.hidden = !(f === 'all' || r.getAttribute('data-cat') === f); });
    });
  });

  var form = document.getElementById('enquire');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var ok = true;
      ['name', 'email', 'phone'].forEach(function (n) {
        var f = form.elements[n];
        var bad = !f.value.trim() || (n === 'email' && !/^\S+@\S+\.\S+$/.test(f.value));
        f.classList.toggle('bad', bad);
        if (bad) ok = false;
      });
      if (!ok) return;
      var v = function (n) { return form.elements[n].value.trim(); };
      var body = 'Name: ' + v('name') + '\nEmail: ' + v('email') + '\nPhone: ' + v('phone') +
        '\nCity: ' + v('city') + '\nMembership of interest: ' + v('tier') + '\n\n' + v('msg');
      location.href = 'mailto:secretarymmclub@gmail.com?subject=' +
        encodeURIComponent('Membership enquiry — ' + v('name')) + '&body=' + encodeURIComponent(body);
    });
  }
})();
