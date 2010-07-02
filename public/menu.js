(function(){
var skimmyImage = new Array(
  new Array('(smile)','0100-smile'),
  new Array('(sadsmile)','0101-sadsmile'),
  new Array('(bigsmile)','0102-bigsmile'),
  new Array('(cool)','0103-cool'),
  new Array('(surprised)','0104-surprised'),
  new Array('(wink)','0105-wink'),
  new Array('(crying)','0106-crying'),
  new Array('(sweating)','0107-sweating'),
  new Array('(speechless)','0108-speechless'),
  new Array('(kiss)','0109-kiss'),
  new Array('(tongueout)','0110-tongueout'),
  new Array('(blush)','0111-blush'),
  new Array('(wondering)','0112-wondering'),
  new Array('(sleepy)','0113-sleepy'),
  new Array('(dull)','0114-dull'),
  new Array('(inlove)','0115-inlove'),
  new Array('(evilgrin)','0116-evilgrin'),
  new Array('(talking)','0117-talking'),
  new Array('(yawn)','0118-yawn'),
  new Array('(puke)','0119-puke'),
  new Array('(doh)','0120-doh'),
  new Array('(angry)','0121-angry'),
  new Array('(itwasntme)','0122-itwasntme'),
  new Array('(party)','0123-party'),
  new Array('(worried)','0124-worried'),
  new Array('(mmm)','0125-mmm'),
  new Array('(nerd)','0126-nerd'),
  new Array('(lipssealed)','0127-lipssealed'),
  new Array('(hi)','0128-hi'),
  new Array('(call)','0129-call'),
  new Array('(devil)','0130-devil'),
  new Array('(angel)','0131-angel'),
  new Array('(envy)','0132-envy'),
  new Array('(wait)','0133-wait'),
  new Array('(bear)','0134-bear'),
  new Array('(makeup)','0135-makeup'),
  new Array('(giggle)','0136-giggle'),
  new Array('(clapping)','0137-clapping'),
  new Array('(thinking)','0138-thinking'),
  new Array('(bow)','0139-bow'),
  new Array('(rofl)','0140-rofl'),
  new Array('(whew)','0141-whew'),
  new Array('(happy)','0142-happy'),
  new Array('(smirk)','0143-smirk'),
  new Array('(nod)','0144-nod'),
  new Array('(shake)','0145-shake'),
  new Array('(punch)','0146-punch'),
  new Array('(emo)','0147-emo'),
  new Array('(yes)','0148-yes'),
  new Array('(no)','0149-no'),
  new Array('(handshake)','0150-handshake'),
  new Array('(skype)','0151-skype'),
  new Array('(heart)','0152-heart'),
  new Array('(brokenheart)','0153-brokenheart'),
  new Array('(mail)','0154-mail'),
  new Array('(flower)','0155-flower'),
  new Array('(rain)','0156-rain'),
  new Array('(sun)','0157-sun'),
  new Array('(time)','0158-time'),
  new Array('(music)','0159-music'),
  new Array('(movie)','0160-movie'),
  new Array('(phone)','0161-phone'),
  new Array('(coffee)','0162-coffee'),
  new Array('(pizza)','0163-pizza'),
  new Array('(cash)','0164-cash'),
  new Array('(muscle)','0165-muscle'),
  new Array('(cake)','0166-cake'),
  new Array('(beer)','0167-beer'),
  new Array('(drink)','0168-drink'),
  new Array('(dance)','0169-dance'),
  new Array('(ninja)','0170-ninja'),
  new Array('(star)','0171-star'),
  new Array('(mooning)','0172-mooning'),
  new Array('(middlefinger)','0173-middlefinger'),
  new Array('(bandit)','0174-bandit'),
  new Array('(drunk)','0175-drunk'),
  new Array('(smoke)','0176-smoke'),
  new Array('(toivo)','0177-toivo'),
  new Array('(rock)','0178-rock'),
  new Array('(headbang)','0179-headbang'),
  new Array('(bug)','0180-bug'),
  new Array('(fubar)','0181-fubar'),
  new Array('(poolparty)','0182-poolparty'),
  new Array('(swear)','0183-swear'),
  new Array('(tmi)','0184-tmi')
);

var node;
node = document.getElementById('skimmyDivElement');
if(node != null) document.body.removeChild(node);
node = document.getElementById('skimmyScriptElement');
if(node != null) document.body.removeChild(node);

skimmyBase = 'http://wave-projects.googlecode.com/hg/robots/wave-skimmy/public/emoticons/static/emoticon-';
skimmyExt = '.png';

/* =================  S c r i p t  ================= */

skimmyScript =  '';
skimmyScript += '  skimmyStaticBase = \'http://wave-projects.googlecode.com/hg/robots/wave-skimmy/public/emoticons/static/emoticon-\';';
skimmyScript += '  skimmyStaticExt = \'.png\';';
skimmyScript += '  skimmyAnimBase = \'http://wave-projects.googlecode.com/hg/robots/wave-skimmy/public/emoticons/animated/emoticon-\';';
skimmyScript += '  skimmyAnimExt = \'.gif\';';
skimmyScript += '  function closeSkimmyMenu() {';
skimmyScript += '    document.body.removeChild(document.getElementById(\'skimmyDivElement\'));';
skimmyScript += '    document.body.removeChild(document.getElementById(\'skimmyScriptElement\'));';
skimmyScript += '  }';
skimmyScript += '  function onOverSkimmy(skimmyElement, path, text) {';
/* skimmyScript += '    skimmyElement.style.background = \'#ffffff\';'; */
skimmyScript += '    document.getElementById(\'skimmyImg\'+path).src = skimmyAnimBase + path + skimmyAnimExt;';
skimmyScript += '    document.getElementById(\'skimmySpanElement\').innerHTML = text;';
skimmyScript += '  }';
skimmyScript += '  function onOutSkimmy(skimmyElement, path) {';
/* skimmyScript += '    skimmyElement.style.background = \'\';'; */
skimmyScript += '    document.getElementById(\'skimmyImg\'+path).src = skimmyStaticBase + path + skimmyStaticExt;';
skimmyScript += '    document.getElementById(\'skimmySpanElement\').innerHTML = \'\';';
skimmyScript += '  }';
skimmyScript += '  function insertSkimmyEmoticon(text) {';
skimmyScript += '    document.execCommand(\'inserthtml\',false,text);';
skimmyScript += '    if(document.getElementById(\'skimmyCheckbox\').checked == false)';
skimmyScript += '      closeSkimmyMenu();';
skimmyScript += '  }';
skimmyScript += '  ';
skimmyScript += '  function onOverCheckSkimmy() {';
skimmyScript += '    document.getElementById(\'skimmySpanElement\').innerHTML = \'Keep menu open\';';
skimmyScript += '  }';
skimmyScript += '  function onOutCheckSkimmy() {';
skimmyScript += '    document.getElementById(\'skimmySpanElement\').innerHTML = \'\';';
skimmyScript += '  }';
skimmyScript += '  ';
skimmyScript += '  var skimmyIsDown = 0;';
skimmyScript += '  var skimmyDownOnX = 0;';
skimmyScript += '  var skimmyDownOnY = 0;';
skimmyScript += '  var skimmyDownOnXDiv = 0;';
skimmyScript += '  var skimmyDownOnYDiv = 0;';
skimmyScript += '  function onDownSkimmy(event) {';
skimmyScript += '    skimmyIsDown = 1;';
skimmyScript += '    skimmyDownOnX = event.clientX;';
skimmyScript += '    skimmyDownOnY = event.clientY;';
skimmyScript += '    skimmyDownOnXDiv = parseInt(document.getElementById(\'skimmyDivElement\').style.left);';
skimmyScript += '    skimmyDownOnYDiv = parseInt(document.getElementById(\'skimmyDivElement\').style.top);';
skimmyScript += '  }';
skimmyScript += '  function onUpSkimmy(event) {';
skimmyScript += '    skimmyIsDown = 0;';
skimmyScript += '  }';
skimmyScript += '  function onMoveSkimmy(event) {';
skimmyScript += '    if (skimmyIsDown) {';
skimmyScript += '      document.getElementById(\'skimmyDivElement\').style.left = skimmyDownOnXDiv + (event.clientX - skimmyDownOnX);';
skimmyScript += '      document.getElementById(\'skimmyDivElement\').style.top = skimmyDownOnYDiv + (event.clientY - skimmyDownOnY);';
skimmyScript += '    }';
skimmyScript += '  }';

var skimmyScriptElement=document.createElement('script');
skimmyScriptElement.setAttribute('id','skimmyScriptElement');
skimmyScriptElement.innerHTML = skimmyScript;
document.body.appendChild(skimmyScriptElement);

/* =================  M e n u  ================= */

skimmyInnerHTML =  '';
skimmyInnerHTML += '<table>';
skimmyInnerHTML += '  <tr>';
skimmyPageBreak = 8;
for(skimmyIndex = 0; skimmyIndex < 72; skimmyIndex++) {
  skimmyInnerHTML += '    <td style=\'margin:1px;border:0px solid #000000;\' onmouseover=onOverSkimmy(this,\''+skimmyImage[skimmyIndex][1]+'\',\''+skimmyImage[skimmyIndex][0]+'\') onmouseout=onOutSkimmy(this,\''+skimmyImage[skimmyIndex][1]+'\') onmousedown=insertSkimmyEmoticon(\''+skimmyImage[skimmyIndex][0]+'\')><img style=\'width:19px;height:19px;\' id=\'skimmyImg'+skimmyImage[skimmyIndex][1]+'\' src=\''+skimmyBase+skimmyImage[skimmyIndex][1]+skimmyExt+'\'></td>';
  if (skimmyIndex%skimmyPageBreak==(skimmyPageBreak-1)) {
    skimmyInnerHTML += '  </tr>';
    skimmyInnerHTML += '  <tr>';
  }
}
skimmyInnerHTML += '  </tr>';
skimmyInnerHTML += '  <tr><td colspan=3><input style=\'font-size:11px;font-family:Tahoma;\' type=button onclick=closeSkimmyMenu() value=close><input id=\'skimmyCheckbox\' type=\'checkbox\' style=\'font-size:11px;font-family:Tahoma;color:#ffffff;padding-left:5px;\' onmouseover=onOverCheckSkimmy() onmouseout=onOutCheckSkimmy()></td><td style=\'cursor:__move;\' onmousedown=__onDownSkimmy(event); onmouseup=__onUpSkimmy(event); onmousemove=__onMoveSkimmy(event); colspan=5><span id=\'skimmySpanElement\' style=\'font-size:11px;font-family:Tahoma;color:#888888;padding-left:5px;\'>(smile)</span></td></tr>';
skimmyInnerHTML += '</table>';

var skimmyDivElement=document.createElement('div');
skimmyDivElement.setAttribute('id','skimmyDivElement');
skimmyDivElement.setAttribute('style','z-index:999999;position:absolute;top:0;left:0;background:#ffffff;border:1px solid #000000');
skimmyDivElement.innerHTML = skimmyInnerHTML;
document.body.appendChild(skimmyDivElement);
})()