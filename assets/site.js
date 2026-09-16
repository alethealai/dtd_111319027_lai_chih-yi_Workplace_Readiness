document.documentElement.classList.add('js');
const menu = document.querySelector('.menu-button');
const nav = document.querySelector('#main-nav');
if (menu && nav) {
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.dataset.open = String(open);
    menu.textContent = open ? '關閉選單' : '選單';
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      menu.click(); menu.focus();
    }
  });
}

const modes = document.querySelectorAll('[data-chart-mode]');
if (modes.length) {
  modes.forEach(button => button.addEventListener('click', () => {
    const mode = button.dataset.chartMode;
    modes.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    document.querySelectorAll('[data-chart-panel]').forEach(panel => {
      panel.hidden = panel.dataset.chartPanel !== mode;
    });
    document.querySelector('#chart-title').textContent = mode === 'orders' ? '需求與訂購量' : '庫存變化';
  }));
}
