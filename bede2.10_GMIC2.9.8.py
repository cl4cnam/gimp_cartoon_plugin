# -*- coding: utf-8 -*-

from gimpfu import *
import os

baseDir = os.path.expanduser('~/.gimpTranslation')

import gettext
try:
	t = gettext.translation("gimp_bede", baseDir)
	_ = t.lgettext
except IOError:
	print 'IOError problème traduction'
	_ = lambda x: x

def simplecartoon(img, layer, augmLum, augmSat, nbBilatBord, methodeDesatBord, supprParasite, forceTrait, nbBilatFinal, antialias, antialiasChaque, despeckle, simplify):
	
	gimp.context_push()
	img.undo_group_start()

	gimp.progress_init("Simple Cartoon...")
	hei = layer.height
	wid = layer.width
	
	pdb.gimp_layer_flatten(layer)
	# new stuff (simplify)
	if int(simplify) >=2:
		#~ pdb.plug_in_sel_gauss(img, layer, 5, 0.2)
		pdb.plug_in_sel_gauss(img, layer, 5, 51)
	# end new stuff
	
	layerCopy = pdb.gimp_layer_copy(layer, False)
	pdb.gimp_image_add_layer(img, layerCopy, 0)
	
	pdb.gimp_image_set_active_layer(img, layer)
	pointLum = str(50-augmLum) + ',' + str(50+augmLum)
	pointSat = str(50-augmSat) + ',' + str(50+augmSat)
	#~ pdb.plug_in_gmic_qt(img, layer, 1, 0, '-fx_curves_interactive 7,0,1,7,0,0,'+pointLum+',100,100,-1,0,0,'+pointSat+',100,100,-1,0,0,100,100,-1,0,0,100,100,-1,')
	pdb.plug_in_gmic_qt(img, layer, 1, 0, '-fx_curves_interactive 7,0,1,"7","0,0,'+pointLum+',100,100,-1,0,0,'+pointSat+',100,100,-1,0,0,100,100,-1,0,0,100,100,-1"')
	
	pdb.gimp_image_set_active_layer(img, layerCopy)
	#~ pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_nlmeans 4,4,10,3,0,0,24,0')
	pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_nlmeans 4,4,10,5,0,0,24,0')
	
	if antialiasChaque:
		for i in range(int(nbBilatBord)):
			pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_bilateral 10,7,1,0,0')
			pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_antialias '+str(antialias)+',10,0,0')
	else:
		pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_bilateral 10,7,'+str(nbBilatBord)+',0,0')
	
	if methodeDesatBord<=1:
		pdb.plug_in_dog(img, layerCopy, 3.0, 1.0, True, True)
		pdb.gimp_desaturate_full(layerCopy, methodeDesatBord)
	if methodeDesatBord==2:
		pdb.plug_in_dog(img, layerCopy, 3.0, 1.0, True, False)
		layerNoir = pdb.gimp_layer_new(img, wid, hei, 0, 'noir', 100, 0)
		pdb.gimp_image_add_layer(img, layerNoir, 0)
		pdb.gimp_image_lower_item(img, layerNoir)
		pdb.gimp_layer_set_mode(layerCopy, 14) # value
		bords = pdb.gimp_layer_new_from_visible(img, img, 'bords')
		pdb.gimp_image_add_layer(img, bords, 0)
		bords = pdb.gimp_image_merge_down(img, bords, 0)
		layerCopy = pdb.gimp_image_merge_down(img, bords, 0)
		pdb.gimp_invert(layerCopy)
	
	pointParasite = 255 - int(supprParasite)
	pointForceTrait = pointParasite - 50 + int(forceTrait)
	pdb.gimp_curves_spline(layerCopy, 0, 8, [0,0,pointForceTrait,57,pointParasite,255,255,255])
	
	# new stuff (simplify)
	if int(simplify) >= 1:
		pdb.gimp_image_set_active_layer(img, layerCopy)
		pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, '-fx_smooth_antialias 100,0,2.5,0,50,50')
		seuil = 59 + 10*int(simplify)
		#~ pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, 'fx_curves_interactive 7,0,1,7,0,0,'+str(seuil)+',0,'+str(seuil+1)+',100,100,100,-1,0,0,100,0,-1,0,0,100,100,-1,0,0,100,100,-1,')
		pdb.plug_in_gmic_qt(img, layerCopy, 1, 0, 'fx_curves_interactive 7,0,1,"7","0,0,'+str(seuil)+',0,'+str(seuil+1)+',100,100,100,-1,0,0,100,0,-1,0,0,100,100,-1,0,0,100,100,-1"')
	# end new stuff
	
	pdb.gimp_layer_set_mode(layerCopy, 3)
	res = pdb.gimp_layer_new_from_visible(img, img, 'result')
	pdb.gimp_image_add_layer(img, res, 0)
	
	pdb.gimp_image_set_active_layer(img, res)
	
	if antialiasChaque:
		for i in range(int(nbBilatFinal)):
			pdb.plug_in_gmic_qt(img, res, 1, 0, '-fx_smooth_bilateral 10,7,1,0,0')
			pdb.plug_in_gmic_qt(img, res, 1, 0, '-fx_smooth_antialias '+str(antialias)+',10,0,0')
	else:
		pdb.plug_in_gmic_qt(img, res, 1, 0, '-fx_smooth_bilateral 10,7,'+str(nbBilatFinal)+',0,0')
		pdb.plug_in_gmic_qt(img, res, 1, 0, '-fx_smooth_antialias '+str(antialias)+',10,0,0')

	
	pdb.plug_in_unsharp_mask(img, res, 5.0, 0.2, 0)
	
	if despeckle:
		pdb.plug_in_despeckle(img, res, 1, 1, -1, 256)
	
	res = pdb.gimp_image_merge_down(img, res, 0)
	res = pdb.gimp_image_merge_down(img, res, 0)
	
	
	img.undo_group_end()
	gimp.context_pop()

register(
	"python-fu-simplecartoon", # name
	_(u'''Simple Cartoon'''), # 
	"Simple Cartoon . . .", # help
	"Claude Lion", # author
	"Claude Lion", # copyright
	"03/03/2021", # date
	_(u"Simple Cartoon..."), # menu name
	"RGB,RGBA", 
	[
		(PF_IMAGE, "image",       "Input image", None),
		(PF_DRAWABLE, "drawable", "Input drawable", None),
		(PF_SLIDER, "augmLum", _(u"increased brightness"), 10, (0,50,1)),
		(PF_SLIDER, "augmSat", _(u"increased saturation"), 20, (0,50,1)),
		(PF_SLIDER, "nbBilatBord", _(u"flattening for edge (bilateral smooth)"), 2, (0,5,1)),
		(PF_OPTION, "methodeDesatBord", _(u"edge desaturation method"), 2, [_(u'clarity'),_(u'brightness'),_(u'max RGB')]),
		(PF_SLIDER, "supprParasite", _(u"removal of parasitic features"), 12, (0,50,1)),
		(PF_SLIDER, "forceTrait", _(u"strength of lines"), 49, (0,49,1)),
		(PF_SLIDER, "nbBilatFinal", _(u"final flattening (bilateral smooth)"), 4, (0,10,1)),
		(PF_ADJUSTMENT, "antialias", _(u"quantity of antialias"), 15, (0,100,1)),
		(PF_TOGGLE, "antialiasChaque", _(u"antialias at every flattening"), False),
		(PF_TOGGLE, "despeckle", _(u"despeckle"), False),
		(PF_SLIDER, "simplify", _(u"simplify"), 1, (0,2,1)),
	],
	[],
	simplecartoon,
	menu="<Image>/Filters/Artistic",
	domain=("gimp_bede", baseDir)
)

main()
