# Movimiento: recetas probadas

`assets/base.html` ya trae GSAP + ScrollTrigger + Lenis (scroll suave) desde
cdnjs y jsDelivr, con versiones fijas. Estas recetas se pegan dentro del
`<script>` final.

## Regla de oro

Un momento orquestado (la entrada o un recorrido por scroll) vale más que
animar todo. Nada de fade-in en cada sección ni hover que agranda cada tarjeta.
Todo tiene que funcionar con `prefers-reduced-motion: reduce` (la base ya lo
respeta: si está activo, no corre ninguna receta).

---

## 1. Entrada orquestada (portada)

La foto sale de la oscuridad y el texto entra después, una sola vez.

```js
const foto = document.querySelector('.portada img');
gsap.set(foto, {scale: 1.12, filter: 'brightness(.2)'});
gsap.set('.portada [data-entra]', {opacity: 0, y: 14});
gsap.timeline({delay: .15})
  .to(foto, {scale: 1, filter: 'brightness(1)', duration: 2.4, ease: 'power3.out'})
  .to('.portada [data-entra]', {opacity: 1, y: 0, duration: .9, stagger: .12, ease: 'power2.out'}, 1.2);
```

## 2. Scroll horizontal fijado (colecciones, galerías)

La sección se queda quieta y el contenido corre de costado mientras bajás.
Solo en escritorio; en el celular, columna normal.

```js
gsap.matchMedia().add('(min-width: 901px)', () => {
  const pista = document.querySelector('.pista');
  const largo = () => pista.scrollWidth - innerWidth;
  gsap.to(pista, {x: () => -largo(), ease: 'none', scrollTrigger: {
    trigger: '.coleccion', start: 'top top', end: () => '+=' + largo(),
    pin: true, scrub: .8, invalidateOnRefresh: true
  }});
});
```
CSS: `.pista{display:flex;width:max-content}`.

## 3. Cámara que recorre una foto (detalle de producto)

Una foto grande fija en pantalla y, con el scroll, zoom a distintos puntos.
Cada toma es un punto de la foto (0 a 1) y un aumento.

```js
const zoom = document.querySelector('.detalle__zoom');      // contenedor 16:9 que cubre la pantalla
const tomas = [{x:.5,y:.5,s:1}, {x:.65,y:.44,s:2.3}, {x:.87,y:.48,s:3.2}];
const acotar = (v, s) => Math.min(1 - .5/s, Math.max(.5/s, v)); // nunca muestra el borde
const encuadre = t => ({xPercent: -(acotar(t.x,t.s)-.5)*100*t.s, yPercent: -(acotar(t.y,t.s)-.5)*100*t.s, scale: t.s});
const tl = gsap.timeline({scrollTrigger: {trigger: '.detalle', start: 'top top', end: 'bottom bottom', scrub: 1}});
gsap.set(zoom, encuadre(tomas[0]));
tomas.slice(1).forEach(t => tl.to(zoom, {...encuadre(t), duration: 1, ease: 'power2.inOut'}).to({}, {duration: .5}));
```
La sección mide `height: 400vh` (o 100vh por toma) y adentro un
`position: sticky; top: 0; height: 100vh`.

## 4. Números que giran (precios, horas, contadores)

Cada cifra es una tira 0-9 dentro de una ventana de 1em de alto.

```js
document.querySelectorAll('.rueda').forEach(r => {
  const tira = document.createElement('span'); tira.className = 'tira';
  for (let i = 0; i < 10; i++) tira.insertAdjacentHTML('beforeend', `<span>${i}</span>`);
  r.append(tira);
  gsap.fromTo(tira, {yPercent: 0}, {yPercent: -(+r.dataset.n) * 10, duration: 1.6, ease: 'expo.inOut'});
});
```
CSS: `.rueda{display:inline-block;height:1em;overflow:hidden}.tira{display:flex;flex-direction:column}.tira span{height:1em}`.

## 5. Foto que se aleja al bajar (parallax sobrio)

```js
gsap.to('.portada img', {yPercent: 12, scale: 1.06, ease: 'none',
  scrollTrigger: {trigger: '.portada', start: 'top top', end: 'bottom top', scrub: true}});
```

## 6. Texto que se revela palabra por palabra (una sola vez, en un manifiesto)

```js
const p = document.querySelector('.manifiesto p');
p.innerHTML = p.textContent.split(' ').map(w => `<span style="opacity:.15">${w}</span>`).join(' ');
gsap.to('.manifiesto p span', {opacity: 1, stagger: .05, ease: 'none',
  scrollTrigger: {trigger: '.manifiesto', start: 'top 70%', end: 'bottom 60%', scrub: true}});
```

## Cuándo NO animar

- Formularios, precios y datos de contacto: siempre quietos y legibles.
- Nada que tape el contenido mientras carga.
- Si la animación no ayuda a entender el producto, se saca.
