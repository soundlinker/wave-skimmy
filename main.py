import logging

from waveapi import appengine_robot_runner
from waveapi import element
from waveapi import events
from waveapi import ops
from waveapi import robot

from google.appengine.ext import webapp

'''
public = 'http://wave-skimmy.appspot.com/public'
'''

public = 'http://wave-projects.googlecode.com/hg/robots/wave-skimmy/public'

anim_base = public + '/emoticons/animated/emoticon-'

anim_ext = '.gif'

emoticons = {
  
  ':)' : '0100-smile',
  ':-)' : '0100-smile',
  ':=)' : '0100-smile',
  '(smile)' : '0100-smile',
  
  ':(' : '0101-sadsmile',
  ':-(' : '0101-sadsmile',
  ':=(' : '0101-sadsmile',
  '(sad)' : '0101-sadsmile',
  '(sadsmile)' : '0101-sadsmile',
  
  ':D' : '0102-bigsmile',
  ':-D' : '0102-bigsmile',
  ':=D' : '0102-bigsmile',
  ':d' : '0102-bigsmile',
  ':-d' : '0102-bigsmile',
  ':=d' : '0102-bigsmile',
  '(laugh)' : '0102-bigsmile',
  '(bigsmile)' : '0102-bigsmile',
  
  '8)' : '0103-cool',
  '8-)' : '0103-cool',
  '8=)' : '0103-cool',
  'B)' : '0103-cool',
  'B-)' : '0103-cool',
  'B=)' : '0103-cool',
  '(cool)' : '0103-cool',
  
  ':O' : '0104-surprised',
  ':-O' : '0104-surprised',
  ':=O' : '0104-surprised',
  ':o' : '0104-surprised',
  ':-o' : '0104-surprised',
  ':=o' : '0104-surprised',
  '(surprised)' : '0104-surprised',
  
  ';)' : '0105-wink',
  ';-)' : '0105-wink',
  ';=)' : '0105-wink',
  '(wink)' : '0105-wink',
  
  ';(' : '0106-crying',
  ';-(' : '0106-crying',
  ';=(' : '0106-crying',
  ':(' : '0106-crying',
  ':-(' : '0106-crying',
  ':=(' : '0106-crying',
  '(cry)' : '0106-crying',
  '(crying)' : '0106-crying',
  
  '(:|' : '0107-sweating',
  '(sweat)' : '0107-sweating',
  '(sweating)' : '0107-sweating',
  
  ':|' : '0108-speechless',
  ':-|' : '0108-speechless',
  ':=|' : '0108-speechless',
  '(speechless)' : '0108-speechless',
  
  ':*' : '0109-kiss',
  ':-*' : '0109-kiss',
  ':=*' : '0109-kiss',
  '(kiss)' : '0109-kiss',
  
  ':P' : '0110-tongueout',
  ':-P' : '0110-tongueout',
  ':=P' : '0110-tongueout',
  ':p' : '0110-tongueout',
  ':-p' : '0110-tongueout',
  ':=p' : '0110-tongueout',
  '(tongueout)' : '0110-tongueout',
  
  ':$' : '0111-blush',
  ':-$' : '0111-blush',
  ':=$' : '0111-blush',
  ':">' : '0111-blush',
  '(blush)' : '0111-blush',
  
  ':^)' : '0112-wondering',
  '(wonder)' : '0112-wondering',
  '(wondering)' : '0112-wondering',

  '|-)' : '0113-sleepy',
  'I-)' : '0113-sleepy',
  'I=)' : '0113-sleepy',
  '(snooze)' : '0113-sleepy',
  '(sleepy)' : '0113-sleepy',
  
  '|-(' : '0114-dull',
  '|(' : '0114-dull',
  '|=(' : '0114-dull',
  '(dull)' : '0114-dull',
  
  '(inlove)' : '0115-inlove',
  
  ']:)' : '0116-evilgrin',
  '>:)' : '0116-evilgrin',
  '(grin)' : '0116-evilgrin',
  '(evilgrin)' : '0116-evilgrin',
  
  '(talk)' : '0117-talking',
  '(talking)' : '0117-talking',
  
  '|-()' : '0118-yawn',
  '(yawn)' : '0118-yawn',
  
  ':&' : '0119-puke',
  ':-&' : '0119-puke',
  ':=&' : '0119-puke',
  '(puke)' : '0119-puke',
  
  '(doh)' : '0120-doh',
  
  ':@' : '0121-angry',
  ':-@' : '0121-angry',
  ':=@' : '0121-angry',
  'x(' : '0121-angry',
  'x-(' : '0121-angry',
  'X(' : '0121-angry',
  'X-(' : '0121-angry',
  'x=(' : '0121-angry',
  'X=(' : '0121-angry',
  '(angry)' : '0121-angry',
  
  '(wasntme)' : '0122-itwasntme',
  '(itwasntme)' : '0122-itwasntme',
  
  '(party)' : '0123-party',
  
  ':S' : '0124-worried',
  ':s' : '0124-worried',
  ':-s' : '0124-worried',
  ':-S' : '0124-worried',
  ':=s' : '0124-worried',
  ':=S' : '0124-worried',
  '(worry)' : '0124-worried',
  '(worried)' : '0124-worried',
  
  '(mm)' : '0125-mmm',
  '(mmm)' : '0125-mmm',
  '(mmmm)' : '0125-mmm',
  
  '8-|' : '0126-nerd',
  'B-|' : '0126-nerd',
  '8|' : '0126-nerd',
  'B|' : '0126-nerd',
  '8=|' : '0126-nerd',
  'B=|' : '0126-nerd',
  '(nerd)' : '0126-nerd',
  
  ':x' : '0127-lipssealed',
  ':-x' : '0127-lipssealed',
  ':X' : '0127-lipssealed',
  ':-X' : '0127-lipssealed',
  ':#' : '0127-lipssealed',
  ':-#' : '0127-lipssealed',
  ':=x' : '0127-lipssealed',
  ':=X' : '0127-lipssealed',
  ':=#' : '0127-lipssealed',
  '(lipssealed)' : '0127-lipssealed',
  
  '(hi)' : '0128-hi',
  
  '(call)' : '0129-call',
  
  '(devil)' : '0130-devil',
  
  '(angel)' : '0131-angel',
  
  '(envy)' : '0132-envy',
  
  '(wait)' : '0133-wait',
  
  '(hug)' : '0134-bear',
  '(bear)' : '0134-bear',
  
  '(kate)' : '0135-makeup',
  '(makeup)' : '0135-makeup',
  
  '(chuckle)' : '0136-giggle',
  '(giggle)' : '0136-giggle',
  
  '(clap)' : '0137-clapping',
  '(clapping)' : '0137-clapping',
  
  ':-?' : '0138-thinking',
  ':?' : '0138-thinking',
  ':=?' : '0138-thinking',
  '(think)' : '0138-thinking',
  '(thinking)' : '0138-thinking',
  
  '(bow)' : '0139-bow',
  
  '(rofl)' : '0140-rofl',
  
  '(whew)' : '0141-whew',
  
  '(happy)' : '0142-happy',
  
  '(smirk)' : '0143-smirk',
  
  '(nod)' : '0144-nod',
  
  '(shake)' : '0145-shake',
  
  '(punch)' : '0146-punch',
  
  '(emo)' : '0147-emo',
  
  '(y)' : '0148-yes',
  '(Y)' : '0148-yes',
  '(ok)' : '0148-yes',
  '(yes)' : '0148-yes',
  
  '(n)' : '0149-no',
  '(N)' : '0149-no',
  '(no)' : '0149-no',
  
  '(handshake)' : '0150-handshake',

  '(ss)' : '0151-skype',
  '(skype)' : '0151-skype',
  
  '(h)' : '0152-heart',
  '(H)' : '0152-heart',
  '(l)' : '0152-heart',
  '(L)' : '0152-heart',
  '(love)' : '0152-heart',
  '(heart)' : '0152-heart',
  
  '(u)' : '0153-brokenheart',
  '(U)' : '0153-brokenheart',
  '(brokenheart)' : '0153-brokenheart',
  
  '(e)' : '0154-mail',
  '(m)' : '0154-mail',
  '(mail)' : '0154-mail',
  
  '(F)' : '0155-flower',
  '(f)' : '0155-flower',
  '(flower)' : '0155-flower',
  
  '(st)' : '0156-rain',
  '(london)' : '0156-rain',
  '(rain)' : '0156-rain',
  
  '(sun)' : '0157-sun',

  '(o)' : '0158-time',
  '(O)' : '0158-time',
  '(clock)' : '0158-time',  
  '(time)' : '0158-time',

  '(music)' : '0159-music',
  
  '(~)' : '0160-movie',
  '(film)' : '0160-movie',
  '(movie)' : '0160-movie',
  
  '(mp)' : '0161-phone',
  '(ph)' : '0161-phone',
  '(phone)' : '0161-phone',
  
  '(coffee)' : '0162-coffee',
  
  '(pi)' : '0163-pizza',
  '(pizza)' : '0163-pizza',
  
  '(mo)' : '0164-cash',
  '($)' : '0164-cash',
  '(cash)' : '0164-cash',
  
  '(flex)' : '0165-muscle',
  '(muscle)' : '0165-muscle',
  
  '(^)' : '0166-cake',
  '(cake)' : '0166-cake',
  
  '(beer)' : '0167-beer',
  
  '(d)' : '0168-drink',
  '(D)' : '0168-drink',
  '(drink)' : '0168-drink',
  
  '\o/' : '0169-dance',
  '\:D/' : '0169-dance',
  '\:d/' : '0169-dance',
  '(dance)' : '0169-dance',

  '(ninja)' : '0170-ninja',
  
  '(*)' : '0171-star',
  '(star)' : '0171-star',
  
  '(mooning)' : '0172-mooning',
  
  '(finger)' : '0173-middlefinger',
  '(middlefinger)' : '0173-middlefinger',
  
  '(bandit)' : '0174-bandit',
  
  '(drunk)' : '0175-drunk',
  
  '(smoking)' : '0176-smoke',
  '(ci)' : '0176-smoke',
  '(smoke)' : '0176-smoke',
  
  '(toivo)' : '0177-toivo',
  
  '(rock)' : '0178-rock',
  
  '(banghead)' : '0179-headbang',
  '(headbang)' : '0179-headbang',
  
  '(bug)' : '0180-bug',
  
  '(fubar)' : '0181-fubar',
  
  '(hrv)' : '0182-poolparty',
  '(poolparty)' : '0182-poolparty',
  
  '(swear)' : '0183-swear',
  
  '(tmi)' : '0184-tmi'
}

# This list will contain all the keys above sorted in such a
# manner that keys like >:) get replaced before :).
# Else we wouldn't be able to control this while iterating
# over the dictionary. It could then be that >:) would end
# up as >smiley_image instead of evilgrin_image.
emoticons_list = []

# These escapes are required for building the regex filters
escapes = [ '\\', '(', ')', '|', '*', '$', '^', ']', '?' ]

#===================================================================================
def assembleFilterAndBuildList():
  #===================================================================================
  global emoticons_list
  filter = ''
  #---------------------------------------------------------------------------------
  for emoticon in emoticons:
    ''' filter '''
    re_emoticon = emoticon
    for escape in escapes:
      re_emoticon = re_emoticon.replace(escape, '\\' + escape)
    filter = filter + re_emoticon + '|'
    ''' list '''
    insertion_index = 0
    for item in emoticons_list:
      insertion_index = insertion_index + 1
      if item.find(emoticon) != -1:
        insertion_index = insertion_index - 1
        break
    emoticons_list.insert(insertion_index, emoticon)
    emoticons_list.reverse()
  #---------------------------------------------------------------------------------
  # before returning the filter, remove the last comma and make it xml compatible
  return filter[:-1].replace('&', '&amp;').replace('>', '&gt;').replace('<', '&lt;').replace('"', '&quot;').replace('\'', '&apos;')
  #---------------------------------------------------------------------------------

#===================================================================================
def OnBlipSubmitted(event, wavelet):
  #=================================================================================
  # Do the work
  #---------------------------------------------------------------------------------
  blip = event.blip
  if blip:
    for emoticon in emoticons_list:
      r = blip.all(emoticon)
      if r:
        r.replace(element.Image(url=(anim_base + emoticons[emoticon] + anim_ext)))
        # need to remove the caption because it makes every DOCUMENTCHANGED pass the filter
        #r.replace(element.Image(url=(anim_base + emoticons[emoticon] + anim_ext), caption=emoticon))
  #-------------------------------------------------------------------------------

#===================================================================================
class MainHandler(webapp.RequestHandler):
  #=================================================================================
  # Redirect visitors of root to the menu
  #---------------------------------------------------------------------------------
  def get(self):
    #-------------------------------------------------------------------------------
    self.redirect("/public/menu.htm")
    #-------------------------------------------------------------------------------

#===================================================================================
if __name__ == '__main__':
  #=================================================================================
  # Set up the robot
  #---------------------------------------------------------------------------------
  filter = assembleFilterAndBuildList()
  #---------------------------------------------------------------------------------
  skimmy = robot.Robot('Skimmy v10', image_url='http://wave-skimmy.appspot.com/public/half.png', profile_url='http://wave-skimmy.appspot.com/public/menu.htm')
  skimmy.register_handler(events.BlipSubmitted,   OnBlipSubmitted)
  skimmy.register_handler(events.DocumentChanged, OnBlipSubmitted, filter=filter)
  #---------------------------------------------------------------------------------
  appengine_robot_runner.run(
    skimmy,
    debug          = True,
    log_errors     = True,
    extra_handlers = [
      ('/', MainHandler)
    ]
  )
  #---------------------------------------------------------------------------------

    