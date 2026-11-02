const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const code=fs.readFileSync(require('node:path').join(__dirname,'../assets/handbook-navigation.js'),'utf8');
function boot(pref){
 const elements={},listeners={},storage={'travel-handbook-section-mode':pref||'hover'},timers=[];
 let doc;
 function el(id,tag='DIV'){const x={id,tagName:tag,textContent:id,value:'',hidden:false,inert:false,open:false,parentElement:null,attrs:{},listeners:{},classList:{items:new Set(),toggle(k,v){v?this.items.add(k):this.items.delete(k)}},addEventListener(k,f){this.listeners[k]=f},setAttribute(k,v){this.attrs[k]=v},removeAttribute(k){delete this.attrs[k]},hasAttribute(k){return k in this.attrs},getClientRects(){return[{}]},getBoundingClientRect(){return{top:60}},focus(){doc.activeElement=this},blur(){doc.activeElement=null},scrollIntoView(){this.scrolled=true},contains(node){for(let p=node;p;p=p.parentElement)if(p===this)return true;return false},matches(){return false}};elements[id]=x;return x}
 for(const id of ['handbook-dock','handbook-section-panel','handbook-section-toggle','handbook-mode-hover','handbook-mode-pin','handbook-section-search','handbook-no-results','handbook-current-section','handbook-page-select','handbook-print','handbook-top','target'])el(id);
 const dock=elements['handbook-dock'],panel=elements['handbook-section-panel'];panel.parentElement=dock;
 const detail=el('detail','DETAILS');elements.target.parentElement=detail;
 const link=el('link','A');link.hash='#target';link.textContent='Nested section';link.parentElement=el('li','LI');link.parentElement.parentElement=panel;link.closest=()=>link;
 panel.querySelectorAll=()=>[link];elements['handbook-mode-hover'].parentElement=panel;elements['handbook-mode-pin'].parentElement=panel;
 doc={body:el('body','BODY'),activeElement:null,getElementById:id=>elements[id],addEventListener(k,f){listeners['doc:'+k]=f}};
 const loc={hash:'',href:'file:///guide.html'};
 const ctx={document:doc,location:loc,history:{pushState(a,b,h){loc.hash=h}},localStorage:{getItem:k=>storage[k]||null,setItem(k,v){storage[k]=v}},matchMedia:()=>({matches:true}),requestAnimationFrame:f=>f(),setTimeout:f=>{timers.push(f);return timers.length},clearTimeout(){},Event:function(type){this.type=type}};
 const win={HotelArrangements:{getCurrent:()=>({chosen:'ExampleHotel'}),linkWithState:(url,state)=>url+'?saved='+state.chosen},addEventListener(k,f){listeners[k]=f},dispatchEvent(){},print(){this.printed=true}};ctx.window=win;
 vm.createContext(ctx);vm.runInContext(code,ctx);
 return{elements,ctx,storage,listeners,flush(){while(timers.length)timers.shift()()}};
}
const a=boot();const e=a.elements;
assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'false');
e['handbook-dock'].listeners.pointerenter({pointerType:'mouse'});assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'true');
e['handbook-dock'].listeners.pointerleave();a.flush();assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'false');
e['handbook-mode-pin'].listeners.click();assert.equal(a.storage['travel-handbook-section-mode'],'pinned');e['handbook-dock'].listeners.pointerleave();a.flush();assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'true');
e['handbook-mode-hover'].focus();e['handbook-mode-hover'].listeners.click({detail:1});e['handbook-dock'].listeners.pointerleave();a.flush();assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'false');
e['handbook-section-toggle'].listeners.click();assert.equal(e['handbook-section-toggle'].attrs['aria-expanded'],'true');
e['handbook-section-panel'].listeners.click({target:e.link,preventDefault(){}});assert.equal(e.detail.open,true);assert.equal(e.target.scrolled,true);assert.equal(e.link.attrs['aria-current'],'location');
e['handbook-page-select'].listeners.change({target:{value:'hotels.html'}});assert.equal(a.ctx.location.href,'hotels.html#handbook-top?saved=ExampleHotel');
e['handbook-section-search'].value='not-found';e['handbook-section-search'].listeners.input();assert.equal(e['handbook-no-results'].hidden,false);assert.equal(e.li.hidden,true);
const b=boot('pinned');assert.equal(b.elements['handbook-section-toggle'].attrs['aria-expanded'],'true');
console.log('PASS: hover open/close, pin persistence, mouse mode switching, click access, reveal collapsed content, search, active section and page switch with hotel state.');
