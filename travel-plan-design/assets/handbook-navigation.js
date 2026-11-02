(function(){
 'use strict';
 const dock=document.getElementById('handbook-dock'),panel=document.getElementById('handbook-section-panel');
 if(!dock||!panel)return;
 const tab=document.getElementById('handbook-section-toggle'),hover=document.getElementById('handbook-mode-hover'),pin=document.getElementById('handbook-mode-pin');
 const links=[...panel.querySelectorAll('nav a')],search=document.getElementById('handbook-section-search');
 let mode='hover',open=false,latched=false,closeTimer;
 try{if(localStorage.getItem('travel-handbook-section-mode')==='pinned')mode='pinned'}catch(_){}
 function setOpen(value){open=mode==='pinned'||value;dock.classList.toggle('hb-expanded',open);tab.setAttribute('aria-expanded',String(open));panel.inert=!open;panel.setAttribute('aria-hidden',String(!open))}
 function setMode(value,remember=true){mode=value;latched=false;document.body.classList.toggle('hb-pinned',mode==='pinned');pin.setAttribute('aria-pressed',String(mode==='pinned'));hover.setAttribute('aria-pressed',String(mode==='hover'));setOpen(true);if(remember)try{localStorage.setItem('travel-handbook-section-mode',mode)}catch(_){}}
 setMode(mode,false);if(mode==='hover')setOpen(false);
 tab.addEventListener('click',()=>{if(mode==='pinned'){setMode('hover');setOpen(false)}else{latched=!open;setOpen(latched)}});
 dock.addEventListener('pointerenter',event=>{if(event.pointerType==='touch')return;clearTimeout(closeTimer);setOpen(true)});
 function closeIfIdle(){if(mode==='hover'&&!latched&&!panel.contains(document.activeElement))setOpen(false)}
 dock.addEventListener('pointerleave',()=>{clearTimeout(closeTimer);closeTimer=setTimeout(closeIfIdle,180)});
 panel.addEventListener('focusin',()=>setOpen(true));
 panel.addEventListener('focusout',()=>{clearTimeout(closeTimer);closeTimer=setTimeout(()=>{if(!dock.matches(':hover'))closeIfIdle()},180)});
 hover.addEventListener('click',event=>{setMode('hover');if(event.detail)hover.blur()});pin.addEventListener('click',()=>setMode('pinned'));
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&open){if(mode==='pinned')setMode('hover');latched=false;setOpen(false);tab.focus()}});
 const anchor=hash=>{try{return decodeURIComponent(hash.replace(/^#/,'').split('?stays=')[0])}catch(_){return ''}};
 const targetLinks=links.map(link=>({link,id:anchor(link.hash)}));
 function activate(id){let label='';targetLinks.forEach(item=>{if(item.id===id){item.link.setAttribute('aria-current','location');label=item.link.textContent}else item.link.removeAttribute('aria-current')});if(label)document.getElementById('handbook-current-section').textContent=label}
 function reveal(hash,focus=false){const id=anchor(hash)||'handbook-top',target=document.getElementById(id);if(!target||dock.contains(target))return;for(let p=target.parentElement;p;p=p.parentElement)if(p.tagName==='DETAILS')p.open=true;if(target.tagName==='DETAILS')target.open=true;activate(id);if(hash)requestAnimationFrame(()=>{target.scrollIntoView({block:'start',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});if(focus){if(!target.hasAttribute('tabindex'))target.setAttribute('tabindex','-1');target.focus({preventScroll:true})}})}
 panel.addEventListener('click',event=>{const link=event.target.closest('nav a');if(!link)return;event.preventDefault();history.pushState(null,'',link.hash);reveal(link.hash,true);if(mode==='hover'){latched=false;setOpen(false)}});
 search.addEventListener('input',()=>{const q=search.value.toLocaleLowerCase().trim();let count=0;links.forEach(link=>{const show=!q||link.textContent.toLocaleLowerCase().includes(q);link.parentElement.hidden=!show;if(show)count++});document.getElementById('handbook-no-results').hidden=count>0});
 document.getElementById('handbook-page-select').addEventListener('change',event=>{let dest=event.target.value+'#handbook-top';const api=window.HotelArrangements;if(api&&api.getCurrent)dest=api.linkWithState(dest,api.getCurrent());location.href=dest});
 document.getElementById('handbook-print').addEventListener('click',()=>window.print());
 window.addEventListener('hashchange',()=>reveal(location.hash));
 let scheduled=false;
 window.addEventListener('scroll',()=>{if(scheduled)return;scheduled=true;requestAnimationFrame(()=>{scheduled=false;let active='handbook-top',closest=-Infinity;for(const item of targetLinks){const node=document.getElementById(item.id);if(!node||!node.getClientRects().length)continue;const y=node.getBoundingClientRect().top;if(y<=125&&y>closest){closest=y;active=item.id}}activate(active)})},{passive:true});
 window.dispatchEvent(new Event('handbook:navigation-ready'));reveal(location.hash);
})();
