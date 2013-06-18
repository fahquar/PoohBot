# -*- coding: UTF-8 -*-
###
# Copyright (c) 2012, Pooh Bear
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice
import random

class TA(callbacks.Plugin):

    threaded = True
    wordbutts = """http://i.imgur.com/2FhYOYj.gif
http://i.imgur.com/44meRoE.gif
http://i.imgur.com/Yn3Ziai.gif
	"""
    sexybutts = """http://i.imgur.com/KUAvjtz.gif
http://i.imgur.com/zNqjn.gif
http://i.imgur.com/D33pijJ.gif
http://i.imgur.com/ZJMfQtN.gif
http://i.imgur.com/VqboqNy.gif
http://i.imgur.com/9I4Ge.gif
http://i.imgur.com/38jr5.gif
http://i.imgur.com/SoLIP.gif
http://i.imgur.com/T3yCA.gif
http://i.imgur.com/Lv8hz.gif
http://i.imgur.com/ZxJto.gif
http://i.imgur.com/pjXlJ.gif
http://i.imgur.com/jvULK.gif
http://i.imgur.com/FdTsu.gif
http://i.imgur.com/HCV5U.gif
http://i.imgur.com/0N7vJ.gif
http://i.imgur.com/foJQn.gif
http://i.imgur.com/OelrW.gif
http://i.imgur.com/1sbNS.gif
http://i.imgur.com/0wum4.gif
http://i.imgur.com/fgQeu.gif
http://i.imgur.com/qpurM.gif
http://i.imgur.com/HRa4h.gif
http://i.imgur.com/TsFu8.gif
http://i.imgur.com/ZmZFr.gif
http://i.imgur.com/6e47u.gif
http://i.imgur.com/Ot85S.gif
http://i.imgur.com/aADXm.gif
http://i.imgur.com/RY2RL.gif
http://i.imgur.com/5VA8w.gif
http://i.imgur.com/YSABI.gif
http://i.imgur.com/fFYAO.gif
http://i.imgur.com/fWJ1U.gif
http://i.imgur.com/M1Q15.gif
http://i.imgur.com/bSZ4H.gif
http://i.imgur.com/mfxbC.gif
http://i.imgur.com/JhBzQ.gif
http://i.imgur.com/Abcd6.gif
http://i.imgur.com/38dHe.gif
http://i.imgur.com/Ik2DD.gif
http://i.imgur.com/DWPZZ.gif
http://i.imgur.com/5eUNO.gif
http://i.imgur.com/OJUrr.gif
http://i.imgur.com/dUOBI.gif
http://i.imgur.com/sLJnB.gif
http://i.imgur.com/SO9Pv.gif
http://i.imgur.com/J6i0X.gif
http://i.imgur.com/B7srF.gif
http://i.imgur.com/fJuFn.gif
http://i.imgur.com/xotq3.gif
http://i.imgur.com/vkI8M.gif
http://i.imgur.com/JjVWH.gif
http://i.imgur.com/AFYu9.gif
http://i.imgur.com/hDkE8.gif
http://i.imgur.com/c68A4.gif
http://i.imgur.com/MJIh1.gif
http://i.imgur.com/GQUan.gif
http://i.imgur.com/fvqUG.gif
http://i.imgur.com/lSUdP.gif
http://i.imgur.com/iBB3x.gif
http://i.imgur.com/pmNdQ.gif
http://i.imgur.com/K5h0t.gif
http://i.imgur.com/EbEvP.gif
http://i.imgur.com/ufM8v.gif
http://i.imgur.com/GDLa1.gif
http://i.imgur.com/o2f4BgA.gif
http://i.imgur.com/5berE6P.gif
http://i.imgur.com/qzspW6C.gif
http://i.imgur.com/F2FYrBZ.gif
http://i.imgur.com/RW0erPq.gif
http://i.imgur.com/Ydqt9vu.gif
http://i.imgur.com/kk6Giqv.gif
http://i.imgur.com/KobLlIY.gif
http://i.imgur.com/A6H3HJp.gif
http://i.imgur.com/4QW5RLK.gif
http://i.imgur.com/uQZm4wQ.gif
http://i.imgur.com/nThuXaq.gif
http://i.imgur.com/jUquNlN.gif
http://i.imgur.com/H801wMW.gif
http://i.imgur.com/iKTO09R.gif
http://i.imgur.com/VIpc1Cx.gif
http://i.imgur.com/5IL5mIy.gif
http://i.imgur.com/eDs1vk7.gif
http://i.imgur.com/sZuzG9e.gif
http://i.imgur.com/EZxCwh9.gif
http://i.imgur.com/xTSr0M5.gif
http://i.imgur.com/zIXWa81.gif
http://i.imgur.com/qRyNv8l.gif
http://i.imgur.com/MJpQTeY.gif
http://i.imgur.com/pAe7HUg.gif
http://i.imgur.com/SzVZjgu.gif
http://i.imgur.com/08w6YLb.gif
http://i.imgur.com/knsuCYD.gif
http://i.imgur.com/5wkeM0u.gif
http://i.imgur.com/WEWf2Ym.gif
http://i.imgur.com/3sn23fp.gif
http://i.imgur.com/tsuAwoi.gif
http://i.imgur.com/FABU9lM.gif
http://i.imgur.com/eH0oav1.gif
http://i.imgur.com/vIjfkFA.gif
http://i.imgur.com/SQXUJZ5.gif
http://i.imgur.com/JRcATG1.gif
http://i.imgur.com/36xf970.gif
http://i.imgur.com/BvwVMQJ.gif
http://i.imgur.com/FY5rbc4.gif
http://i.imgur.com/4LSV94x.gif
http://i.imgur.com/J87lZwT.gif
http://i.imgur.com/JFfszV7.gif
http://i.imgur.com/p4qj4Vb.gif
http://i.imgur.com/dxHksGk.gif
http://i.imgur.com/zZblTI2.gif
http://i.imgur.com/jHSP7Yg.gif
http://i.imgur.com/Bm2t527.gif
http://i.imgur.com/qrLIsdS.gif
http://i.imgur.com/OYIBIfc.gif
http://i.imgur.com/nff4X48.gif
http://i.imgur.com/yUm2Njn.gif
http://i.imgur.com/gBBJrRw.gif
http://i.imgur.com/U2fiRvx.gif
http://i.imgur.com/6Ow9n0Y.gif
http://i.imgur.com/tjLTtZR.gif
http://i.imgur.com/RGUW37J.gif
http://i.imgur.com/fhj0P2g.gif
http://i.imgur.com/crtj6d9.gif
http://i.imgur.com/wlsGUao.gif
http://i.imgur.com/3WWjfxZ.gif
http://i.imgur.com/rGo1sy1.gif
http://i.imgur.com/UpEGHQs.gif
http://i.imgur.com/M7ZY9wr.gif
http://i.imgur.com/oMhtImA.gif
http://i.imgur.com/Y9bqMvB.gif
http://i.imgur.com/Jlir5tc.gif
http://i.imgur.com/3pA3r61.gif
http://i.imgur.com/3DHVzPK.gif
http://i.imgur.com/e3GGZKV.gif
http://i.imgur.com/IcI1CUQ.gif
http://i.imgur.com/ytIvKTH.gif
http://i.imgur.com/lvPeEtG.gif
http://i.imgur.com/oVobWPn.gif
http://i.imgur.com/tZ5rmE3.gif
http://i.imgur.com/SjbLSiF.gif
http://i.imgur.com/MNvaDKE.gif
http://i.imgur.com/fxNJoFY.gif
http://i.imgur.com/e7hDQcd.gif
http://i.imgur.com/94NiD5n.gif
http://i.imgur.com/BOOIjcS.gif
http://i.imgur.com/CMCSR23.gif
http://i.imgur.com/shoSiMO.gif
http://i.imgur.com/EsYqQkn.gif
http://i.imgur.com/YJypEFw.gif
http://i.imgur.com/PmhjuR4.gif
http://i.imgur.com/JivKyqG.gif
http://i.imgur.com/Ua4FJJ1.gif
http://i.imgur.com/8LL3Evc.gif
http://i.imgur.com/xwFmsFt.gif
http://i.imgur.com/H9DSbWI.gif
http://i.imgur.com/9CSXf0I.gif
http://i.imgur.com/vdQW4QS.gif
http://i.imgur.com/vdQW4QS.gif
http://i.imgur.com/eGA6KVN.gif
http://i.imgur.com/kHwVG8d.gif
http://i.imgur.com/YJnWHWj.gif
http://i.imgur.com/N0Sgd.gif
http://i.imgur.com/IXfCX.gif
http://i.imgur.com/gPZowj2.gif
http://i.imgur.com/mDNLbbO.gif
http://i.imgur.com/uEaWXc9.gif
http://i.imgur.com/4dTZsOp.gif
http://i.imgur.com/IUBzGiL.gif
http://i.imgur.com/5PyqK1a.gif
http://i.imgur.com/ZcW4wig.gif
http://i.imgur.com/91KGOpC.gif
http://i.imgur.com/uQlUiwM.gif
http://i.imgur.com/Jtre1Ju.gif
http://i.imgur.com/DsIfVzH.gif
http://i.imgur.com/yEgth7i.gif
http://i.imgur.com/LFeSCUF.gif
http://i.imgur.com/8Wrcyem.gif
http://i.imgur.com/NFFwdt2.gif
http://i.imgur.com/qws8T69.gif
http://i.imgur.com/1Ow5xLS.gif
http://i.imgur.com/tzyMSZT.gif
http://i.imgur.com/EPGTQEU.gif
http://i.imgur.com/XaJQt3r.gif  
http://i.imgur.com/XaJQt3r.gif
http://i.imgur.com/CvY0tXc.gif
http://i.imgur.com/T4qbR97.gif
http://i.imgur.com/EO4Lw73.gif
http://i.imgur.com/hDZX0XV.gif
http://i.imgur.com/OTruQQh.gif
http://i.imgur.com/OTruQQh.gif
http://i.imgur.com/1vDG5Y2.gif
http://i.imgur.com/N9czIqh.gif
http://i.imgur.com/i3CRBfu.gif
http://i.imgur.com/I8Hq9ak.gif
http://i.imgur.com/MqVv98w.gif
http://i.imgur.com/ix6oCdk.gif
http://i.imgur.com/8vjVB8v.gif
http://i.imgur.com/gIoQJ0b.gif
http://i.imgur.com/6nx7qcq.gif
http://i.imgur.com/TOiFRLu.gif
http://i.imgur.com/zonUOCc.gif
http://i.imgur.com/IUBur93.gif
http://i.imgur.com/db7gbkw.gif
http://i.imgur.com/FKzMFMK.gif
http://i.imgur.com/Mp2r9Z8.gif
http://i.imgur.com/3KZLxjq.gif
http://i.imgur.com/A9A5sJv.gif
http://i.imgur.com/svXyndT.gif
http://i.imgur.com/GkN5INS.gif
http://i.imgur.com/DeTwmcM.gif
http://i.imgur.com/DrnvSLQ.gif
http://i.imgur.com/UZ8bPgH.gif
http://i.imgur.com/gr8w6WM.gif
http://i.imgur.com/586DoDe.gif
http://i.imgur.com/o4SOh4n.gif
http://i.imgur.com/xpvF9Gj.gif
http://i.imgur.com/HNt8PJV.gif
http://i.imgur.com/Qa40GnB.gif
http://i.imgur.com/pZ4TInR.gif
http://i.imgur.com/xo5MLid.gif
http://i.imgur.com/BQxI0kQ.gif
http://i.imgur.com/jHqjwn2.gif
http://i.imgur.com/hKawBM7.gif
http://i.imgur.com/GV2lgVH.gif
http://i.imgur.com/bEVvtn5.gif
http://i.imgur.com/Toyv12h.gif
http://i.imgur.com/oK9IcPr.gif
http://i.imgur.com/dUdH7wf.gif
http://i.imgur.com/MyhB06O.gif
http://i.imgur.com/GrJpXLH.gif
http://i.imgur.com/rgKCZNa.gif
http://i.imgur.com/V8zdi5y.gif
http://i.imgur.com/lmXev.gif
http://i.imgur.com/AotUl83.gif
http://i.imgur.com/cWzaA.gif
http://i.imgur.com/oZr8e.gif
http://i.imgur.com/BqfvA.gif
http://i.imgur.com/osTXW.gif
http://i.imgur.com/X67pF.gif
http://i.imgur.com/f0f1L.gif
http://i.imgur.com/UUq6Q.gif
http://i.imgur.com/eMA9C.gif
http://i.imgur.com/WHGmJ.gif
http://i.imgur.com/brb85.gif
http://i.imgur.com/2HBES.gif
http://i.imgur.com/mO8xL.gif
http://i.imgur.com/dI3wF.gif
http://i.imgur.com/RYBHq.gif
http://i.imgur.com/ZWRqH.gif
http://i.imgur.com/RTieM.gif
http://i.imgur.com/gsaXM.gif
http://i.imgur.com/RaODm.gif
http://i.imgur.com/2xTat.gif
http://i.imgur.com/pmvyM.gif
http://i.imgur.com/ZjJec.gif
http://i.imgur.com/BGai9.gif
http://i.imgur.com/Eoecw.gif
http://i.imgur.com/KQl7v.gif
http://i.imgur.com/jArAG.gif
http://i.imgur.com/sWNd0.gif
http://i.imgur.com/XZFfk.gif
http://i.imgur.com/64fN3.gif
http://i.imgur.com/xNCCF.gif
http://i.imgur.com/quQXC.gif
http://i.imgur.com/YJNpb.gif
http://i.imgur.com/uNF43.gif  
http://i.imgur.com/0r37R.gif
http://i.imgur.com/t4pYa.gif  
http://i.imgur.com/bhQrO.gif  
http://i.imgur.com/XOlYI.gif
http://i.imgur.com/DW67i.gif  
http://i.imgur.com/lAurt.gif
http://i.imgur.com/gOmdJ.gif
http://i.imgur.com/6rMh6.gif
http://i.imgur.com/riOPX.gif
http://i.imgur.com/guJYn.gif
http://i.imgur.com/0sEbB.gif
http://i.imgur.com/dSk7n.gif  
http://i.imgur.com/glhDC.gif
http://i.imgur.com/rklIM.gif
http://i.imgur.com/4L7t1.gif
http://i.imgur.com/5XljN.gif
http://i.imgur.com/FlOCF.gif
http://i.imgur.com/jcpZe.gif  
http://i.imgur.com/l8p1V.gif
http://i.imgur.com/bpZfc.gif
http://i.imgur.com/H57Cg.gif
http://i.imgur.com/dJfiA.gif
http://i.imgur.com/2AuUg.gif
http://i.imgur.com/HJ0jn.gif
http://i.imgur.com/FBzXS.gif
http://i.imgur.com/0UGdx.gif
http://i.imgur.com/d4YjK.gif
http://i.imgur.com/snlnI.gif
http://i.imgur.com/VAXsF.gif
http://i.imgur.com/E08nr.gif
http://i.imgur.com/hAcCe.gif
http://i.imgur.com/Sfz84.gif
http://i.imgur.com/5rT97.gif
http://i.imgur.com/GgD7x.gif
http://i.imgur.com/wQowW.gif
http://i.imgur.com/4czsn.gif
http://i.imgur.com/qxeks.gif
http://i.imgur.com/e3mqN.gif
http://i.imgur.com/IdswF.gif
http://i.imgur.com/OOGUM.gif
http://i.imgur.com/S1EIS.gif
http://i.imgur.com/TPKMK.gif
http://i.imgur.com/huOeh.gif
http://i.imgur.com/j3lZH.gif
http://i.imgur.com/NFnj0.gif
http://i.imgur.com/Rms46.gif
http://i.imgur.com/Q6iMP.gif
http://i.imgur.com/3AAJL.gif
http://i.imgur.com/oF4EG.gif
http://i.imgur.com/VXwHE.gif
http://i.imgur.com/VErgy.gif
http://i.imgur.com/7AzHs.gif
http://i.imgur.com/Eck8L.gif
http://i.imgur.com/fb4wW.gif
http://i.imgur.com/9sfL9.gif
http://i.imgur.com/tJVFH.gif
http://i.imgur.com/6SReI.gif
http://i.imgur.com/pE0nj.gif  
http://i.imgur.com/M5ydF.gif  
http://i.imgur.com/k1SQk.gif
http://i.imgur.com/jQ4Bs.gif  
http://i.imgur.com/dAKsd.gif
http://i.imgur.com/lsEAg.gif
http://i.imgur.com/ssYQT.gif  
http://i.imgur.com/ypn3L.gif  
http://i.imgur.com/4ElIo.gif  
http://i.imgur.com/fJLfg.gif
http://i.imgur.com/1UT9g.gif
http://i.imgur.com/P2zeF.gif
http://i.imgur.com/FF21o.gif
http://i.imgur.com/U1dXz.gif  
http://i.imgur.com/O9sGa.gif
http://i.imgur.com/OQS2K.gif
http://i.imgur.com/Ag8bV.gif
http://i.imgur.com/F1EGv.gif
http://i.imgur.com/GdVqk.gif
http://i.imgur.com/1KmUy.gif
http://i.imgur.com/esy2F.gif
http://i.imgur.com/xT06I.gif
http://i.imgur.com/uBqUm.gif
http://i.imgur.com/tfJOA.gif
http://i.imgur.com/HVgJm.gif
http://i.imgur.com/GSk5d.gif
http://i.imgur.com/wzrBa.gif
http://i.imgur.com/wDQky.gif
http://i.imgur.com/jFwFn.gif
http://i.imgur.com/UC8ji.gif
http://i.imgur.com/foPCb.gif
http://i.imgur.com/Tw0hl.gif
http://i.imgur.com/aSEAx.gif
http://i.imgur.com/HFpVi.gif
http://i.imgur.com/zhNtj.gif
http://i.imgur.com/88gSI.gif
http://i.imgur.com/J0Q5k.gif
http://i.imgur.com/NXqsB.gif
http://i.imgur.com/DCrpF.gif
http://i.imgur.com/M2DK0.gif
http://i.imgur.com/bdIJG.gif  
http://i.imgur.com/PQWPE.gif
http://i.imgur.com/0f56P.gif
http://i.imgur.com/24l76.gif
http://i.imgur.com/0Rfv0.gif
http://i.imgur.com/1LCU3.gif
http://i.imgur.com/sE0rc.gif
http://i.imgur.com/dOuwV.gif
http://i.imgur.com/1WYBn.gif
http://i.imgur.com/6XIMl.gif
http://i.imgur.com/9I9WD.gif
http://i.imgur.com/quSZR.gif
http://i.imgur.com/UkNhu.gif
http://i.imgur.com/jBjbT.gif
http://i.imgur.com/Ua8sc.gif
http://i.imgur.com/6eDRX.gif
http://i.imgur.com/PKcCy.gif
http://i.imgur.com/VLaoa.gif
http://i.imgur.com/CHRCJ.gif
http://i.imgur.com/AAIwH.gif  
http://i.imgur.com/fHWwj.gif
http://i.imgur.com/q09A6.gif
http://i.imgur.com/je10z.gif
http://i.imgur.com/SeX56.gif
http://i.imgur.com/SeX56.gif
http://i.imgur.com/q5QKf.gif
http://i.imgur.com/slfND.gif
http://i.imgur.com/LgaNh.gif
http://i.imgur.com/BUMfh.gif
http://i.imgur.com/XVGlR.gif
http://i.imgur.com/K9GV7.gif
http://i.imgur.com/Ap5yU.gif
http://i.imgur.com/RtLxn.gif
http://i.imgur.com/sn0xH.gif
http://i.imgur.com/IS8BY.gif
http://i.imgur.com/fTrSO.gif
http://i.imgur.com/Xm3Bh.gif
http://i.imgur.com/1NaMY.gif
http://i.imgur.com/WY43V.gif
http://i.imgur.com/oFvSF.gif   
http://i.imgur.com/6DlAS.gif
http://i.imgur.com/Q534c.gif
http://i.imgur.com/AjbiF.gif
http://i.imgur.com/Nmhl2.gif
http://i.imgur.com/geZKB.gif
http://i.imgur.com/TeO5v.gif
http://i.imgur.com/QdBHw.gif
http://i.imgur.com/8cyB9.gif
http://i.imgur.com/vmWos.gif
http://i.imgur.com/OY4SA.gif
http://i.imgur.com/AjD6W.gif
http://i.imgur.com/Qyqku.gif
http://i.imgur.com/ObE75.gif
http://i.imgur.com/JLPYZ.gif
http://i.imgur.com/ED6KA.gif
http://i.imgur.com/vxsIW.gif
http://i.imgur.com/vVc5P.gif
http://i.imgur.com/JrXsR.gif
http://i.imgur.com/6kdqd.gif
http://i.imgur.com/NRPLM.gif
http://i.imgur.com/N0Sgd.gif
http://i.imgur.com/kyqJQ.gif
http://i.imgur.com/kuPRm.gif
http://i.imgur.com/fsyFH.gif
http://i.imgur.com/bhbb2.gif
http://i.imgur.com/LJRuz.gif
http://i.imgur.com/3hepw.gif
http://i.imgur.com/cspqB.gif
http://i.imgur.com/TaSXV.gif
http://i.imgur.com/q0kKa.gif
http://i.imgur.com/dZP2F.gif
http://i.imgur.com/mWCCW.gif
http://i.imgur.com/Us6OJ.gif
http://i.imgur.com/uFnGG.gif
http://i.imgur.com/dtSxv.gif
http://i.imgur.com/afENQ.gif  
http://i.imgur.com/7ulaj.gif  
http://i.imgur.com/QTWY4.gif
http://i.imgur.com/82fB2.gif  
http://i.imgur.com/DemY7.gif
http://i.imgur.com/tJ7ke.gif
http://i.imgur.com/cADbE.gif
http://i.imgur.com/cADbE.gif
http://i.imgur.com/oiuja.gif
http://i.imgur.com/GIuEv.gif
http://i.imgur.com/y8Oq0.gif
http://i.imgur.com/VVC0d.gif
http://i.imgur.com/Ziqvk.gif   
http://i.imgur.com/ov7pX.gif
http://i.imgur.com/3Lgpb.gif
http://i.imgur.com/8JOJl.gif
http://i.imgur.com/0inwy.gif
http://i.imgur.com/QfQpX.gif
http://i.imgur.com/lRXKX.gif
http://i.imgur.com/OaX8i.gif
http://i.imgur.com/nFbPq.gif
http://i.imgur.com/69xoq.gif
http://i.imgur.com/k7EoJ.gif
http://i.imgur.com/aAbPt.gif
http://i.imgur.com/LGnOp.gif
http://i.imgur.com/Dxw0v.gif
http://i.imgur.com/FIE9L.gif
http://i.imgur.com/YY2cd.gif
http://i.imgur.com/u28ni.gif
http://i.imgur.com/vYrR3.gif
http://i.imgur.com/wcu5X.gif
http://i.imgur.com/O70DI.gif
http://i.imgur.com/XIHqp.gif
http://i.imgur.com/4Ry7W.gif
http://i.imgur.com/Ske8L.gif
http://i.imgur.com/E6BYW.gif
http://i.imgur.com/bEz4s.gif
http://i.imgur.com/dbE3d.gif
http://i.imgur.com/NU9ya.gif
http://i.imgur.com/7GwpY.gif
http://i.imgur.com/XEWPB.gif
http://i.imgur.com/l2EJh.gif
http://i.imgur.com/5GJ9l.gif
http://i.imgur.com/Vx2a6.gif
http://i.imgur.com/8TKgY.gif
http://i.imgur.com/NQeSj.gif
http://i.imgur.com/mx5C6.gif
http://i.imgur.com/adHBJ.gif
http://i.imgur.com/0EPou.gif
http://i.imgur.com/Eobg0.gif
http://i.imgur.com/1Xgdb.gif
http://i.imgur.com/tameN.gif
http://i.imgur.com/E08nr.gif
http://i.imgur.com/IfDb8.gif  
http://i.imgur.com/Lt1oG.gif
http://i.imgur.com/BNIme.gif
http://i.imgur.com/KMYjn.gif
http://i.imgur.com/vrdaj.gif
http://i.imgur.com/zoMDD.gif
http://i.imgur.com/PCUFJ.gif
http://i.imgur.com/y3ACA.gif
http://i.imgur.com/oNHQy.gif
http://i.imgur.com/pHURC.gif
http://i.imgur.com/Gjqyb.gif
http://i.imgur.com/sI09Q.gif
http://i.imgur.com/Qg1ol.gif
http://i.imgur.com/yXKgA.gif
http://i.imgur.com/XFWcj.gif
http://i.imgur.com/ONngX.gif
http://i.imgur.com/FJg4N.gif
http://i.imgur.com/LNX63.gif
http://i.imgur.com/YhjQc.gif
http://i.imgur.com/XOUXP.gif
http://i.imgur.com/mWOwv.gif
http://i.imgur.com/ayM07.gif
http://i.imgur.com/CsKYr.gif
http://i.imgur.com/793I4.gif
http://i.imgur.com/1wXRn.gif
http://i.imgur.com/Y0B1h.gif
http://i.imgur.com/jLdLJ.gif
http://i.imgur.com/OGNg8.gif
http://i.imgur.com/VVXpu.gif
http://i.imgur.com/Faz6y.gif
http://i.imgur.com/ixvV2.gif
http://i.imgur.com/Wopc6.gif
http://i.imgur.com/6KgjP.gif
http://i.imgur.com/wBAJi.gif
http://i.imgur.com/9BcFq.gif
http://i.imgur.com/OS2Ey.gif
http://i.imgur.com/77WWf.gif
http://i.imgur.com/U6LXv.gif
http://i.imgur.com/Ip0P9.gif
http://i.imgur.com/1u0lU.gif
http://i.imgur.com/tMQ6T.gif
http://i.imgur.com/zkzy3.gif
http://i.imgur.com/LBTBy.gif
http://i.imgur.com/clDYc.gif
http://i.imgur.com/ugRsy.gif
http://i.imgur.com/w6wNH.gif
http://i.imgur.com/oDTKE.gif
http://i.imgur.com/l5WUY.gif
http://i.imgur.com/26OT2.gif
http://i.imgur.com/7Z65n.gif
http://i.imgur.com/EUUut.gif
http://i.imgur.com/Ryar4.gif
http://i.imgur.com/1cV2f.gif
http://i.imgur.com/DXaJr.gif
http://i.imgur.com/5bWzS.gif
http://i.imgur.com/xWcty.gif
http://i.imgur.com/hbmBB.gif
http://i.imgur.com/vR2io.gif
http://i.imgur.com/g6RUL.gif
http://i.imgur.com/HhQaT.gif
http://i.imgur.com/lIkCU.gif
http://i.imgur.com/VkWZy.gif
http://i.imgur.com/DTwk5.gif
http://i.imgur.com/gKEoA.gif
http://i.imgur.com/MGL8O.gif
http://i.imgur.com/Z2p8R.gif
http://i.imgur.com/AmsHR.gif
http://i.imgur.com/jKdup.gif
http://i.imgur.com/DKmHw.gif
http://i.imgur.com/YgX0k.gif
http://i.imgur.com/3Ni8O.gif
http://i.imgur.com/fYizi.gif
http://i.imgur.com/crPxE.gif
http://i.imgur.com/mW2cL.gif
http://i.imgur.com/ADJlg.gif
http://i.imgur.com/9tEzc.gif
http://i.imgur.com/R0ayg.gif  
http://i.imgur.com/OLHmB.gif
http://i.imgur.com/2joSL.gif
http://i.imgur.com/yffi6.gif
http://i.imgur.com/RsKoG.gif
http://i.imgur.com/qDVkk.gif
http://i.imgur.com/MuyVo.gif
http://i.imgur.com/xi6Wu.gif
http://i.imgur.com/ydPcL.gif
http://i.imgur.com/xeT0Q.gif
http://i.imgur.com/2qMKm.gif
http://i.imgur.com/kD8bp.gif
http://i.imgur.com/c7gI5.gif
http://i.imgur.com/YeA9D.gif
http://i.imgur.com/6Ukrn.gif
http://i.imgur.com/p7EeG.gif
http://i.imgur.com/xPiiY.gif  
http://i.imgur.com/5G7kS.gif
http://i.imgur.com/NJGtk.gif
http://i.imgur.com/yUQqe.gif
http://i.imgur.com/l9ICV.gif
http://i.imgur.com/vGhTB.gif
http://i.imgur.com/ZXbTW.gif
http://i.imgur.com/vIITU.gif
http://i.imgur.com/27b9P.gif
http://i.imgur.com/pt6Gm.gif
http://i.imgur.com/xRrIl.gif
http://i.imgur.com/Y8rdC.gif
http://i.imgur.com/rbOLd.gif
http://i.imgur.com/MEGhs.gif
http://i.imgur.com/bOwkk.gif
http://i.imgur.com/I75YF.gif  
http://i.imgur.com/28ILZ.gif
http://i.imgur.com/78Bvp.gif
http://i.imgur.com/gHxf4.gif
http://i.imgur.com/BwTij.gif
http://i.imgur.com/plzXi.gif  
http://i.imgur.com/Mlq9v.gif  
http://i.imgur.com/WBP8u.gif
http://i.imgur.com/1vT5l.gif
http://i.imgur.com/gTnwr.gif
http://i.imgur.com/sfGMb.gif
http://i.imgur.com/sYXaQ.gif
http://i.imgur.com/jsb4x.gif
http://i.imgur.com/pCS31.gif
http://i.imgur.com/YBU3p.gif
http://i.imgur.com/u21nj.gif
http://i.imgur.com/cfNwb.gif  
http://i.imgur.com/93lV3.gif
http://i.imgur.com/F0IKn.gif
http://i.imgur.com/e4Fvc.gif  
http://i.imgur.com/LdjzH.gif  
http://i.imgur.com/VJ3x1.gif
http://i.imgur.com/0aCjH.gif
http://i.imgur.com/uPLIn.gif  
http://i.imgur.com/iPwxN.gif
http://i.imgur.com/qVk59.gif
http://i.imgur.com/qAg7N.gif
http://i.imgur.com/PET2R.gif    
http://i.imgur.com/SNryJ.gif
http://i.imgur.com/7QwLQ.gif
http://i.imgur.com/prZJU.gif  
http://i.imgur.com/t12zB.gif
http://i.imgur.com/buOXo.gif
http://i.imgur.com/zXWWU.gif
http://i.imgur.com/1Ovwe.gif
http://i.imgur.com/MPZpo.gif
http://i.imgur.com/6kFkr.gif   
http://i.imgur.com/bPtjw.gif
http://i.imgur.com/4U0zH.gif
http://i.imgur.com/4U0zH.gif
http://i.imgur.com/MhCuq.gif
http://i.imgur.com/wP43q.gif  
http://i.imgur.com/907be.gif
http://i.imgur.com/E6d99.gif  
http://i.imgur.com/uHAQz.gif
http://i.imgur.com/Dy6zU.gif  
http://i.imgur.com/o9bYF.gif
http://i.imgur.com/blb9q.gif
http://i.imgur.com/8Lkyr.gif
http://i.imgur.com/mkb80.gif
http://i.imgur.com/b4dGl.gif
http://i.imgur.com/U5dLY.gif
http://i.imgur.com/Xnym1.gif
http://i.imgur.com/Pejc1.gif
http://i.imgur.com/U4IsP.gif
http://i.imgur.com/T9CE4.gif
http://i.imgur.com/nU4rl.gif
http://i.imgur.com/ucyxp.gif
http://i.imgur.com/KJd1i.gif
http://i.imgur.com/uE4ee.gif
http://i.imgur.com/0YxFL.gif
http://i.imgur.com/l6hC9.gif
http://i.imgur.com/uX6uk.gif
http://i.imgur.com/qZVRu.gif
http://i.imgur.com/Y5qAd.gif  
http://i.imgur.com/kyLmj.gif
http://i.imgur.com/oWNxd.gif
http://i.imgur.com/xdrsc.gif
http://i.imgur.com/w1LG9.gif
http://i.imgur.com/RJQYj.gif
http://i.imgur.com/GB1rD.gif
http://i.imgur.com/uFKyS.gif
http://i.imgur.com/GoKWF.gif
http://i.imgur.com/tvKeO.gif
http://i.imgur.com/2XINm.gif
http://i.imgur.com/F8XWD.gif
http://i.imgur.com/lTvWM.gif
http://i.imgur.com/Q5wJU.gif
http://i.imgur.com/ucyxp.gif
http://i.imgur.com/mDsg3.gif
http://i.imgur.com/eaqeg.gif
http://i.imgur.com/z1NgM.gif
http://i.imgur.com/L2fYW.gif
http://i.imgur.com/0DlW6.gif
http://i.imgur.com/9UopE.gif
http://i.imgur.com/dM89Y.gif
http://i.imgur.com/Mx6qC.gif
http://i.imgur.com/39Ulq.gif
http://i.imgur.com/jcMRp.gif
http://i.imgur.com/7fHwk.gif
http://i.imgur.com/0Zp7R.gif
http://i.imgur.com/B2NcP.gif
http://i.imgur.com/3lQVx.gif
http://i.imgur.com/SQXyn.gif
http://i.imgur.com/iqat0.gif
http://i.imgur.com/s5r9Y.gif
http://i.imgur.com/1Og0X.gif
http://i.imgur.com/aZdy3.gif
http://i.imgur.com/pDcNN.gif
http://i.imgur.com/WGj2J.gif
http://i.imgur.com/MXDgw.gif
http://i.imgur.com/UsQBi.gif
http://i.imgur.com/w5QZ9.gif
http://i.imgur.com/CIhXh.gif
http://i.imgur.com/dA0Zx.gif
http://i.imgur.com/kjThN.gif
http://i.imgur.com/KF0Yp.gif
http://i.imgur.com/I8fwbeb.gif
http://i.imgur.com/35f7TLZ.gif
http://i.imgur.com/M7ob3C3.gif
http://i.imgur.com/PVVT3CU.gif
http://i.imgur.com/7K2jYxd.gif
http://i.imgur.com/cC3vYVk.gif
http://i.imgur.com/wkbpu6v.gif
http://i.imgur.com/bq3HRuO.gif
http://i.imgur.com/ejC4kzt.gif
http://i.imgur.com/BUOP7xY.gif
http://i.imgur.com/TrSzA4U.gif
http://i.imgur.com/9nidMod.gif
http://i.imgur.com/iXfDn.gif
http://i.imgur.com/iXfDn.gif
http://i.imgur.com/OksKf.gif
http://i.imgur.com/OksKf.gif
http://i.imgur.com/Fgy1g.gif
http://i.imgur.com/Fgy1g.gif
http://i.imgur.com/BvVWI.gif
http://i.imgur.com/BvVWI.gif
http://i.imgur.com/Jc8P9.gif
http://i.imgur.com/Jc8P9.gif
http://i.imgur.com/DVrECCH.gif
http://i.imgur.com/DVrECCH.gif
http://i.imgur.com/BATgRRz.gif
http://i.imgur.com/BATgRRz.gif
	"""
    sexyguys = """http://i.imgur.com/CzMHq.gif
http://i.imgur.com/RvnHuqZ.gif
http://i.imgur.com/ZH8KfJE.gif
http://i.imgur.com/0rcDucX.gif
http://i.imgur.com/ADUZI9L.gif
http://i.imgur.com/LB3BAST.gif
http://i.imgur.com/Fl86jNY.gif
http://i.imgur.com/vT5EwHU.gif
http://i.imgur.com/IDTwSag.gif
http://i.imgur.com/L2IAw2k.gif
http://i.imgur.com/KBpPRzI.gif
http://i.imgur.com/6nVpdXc.gif
http://i.imgur.com/u2h1Ubs.gif
http://i.imgur.com/0TSq0sK.gif
http://i.imgur.com/jBRZk8x.gif
http://i.imgur.com/8qpberS.gif
http://i.imgur.com/6e2W9Ur.gif
http://i.imgur.com/d6bA51t.gif
http://i.imgur.com/X0xoFPj.gif
http://i.imgur.com/gT6DgSO.gif
http://i.imgur.com/BjKiZJo.gif
http://i.imgur.com/tlqeLLx.gif
http://i.imgur.com/5yDz098.gif
http://i.imgur.com/KA2R7oX.gif
http://i.imgur.com/06sof.jpg
http://i.imgur.com/atsvJ3n.gif
http://i.imgur.com/4LY0U6v.gif
http://i.imgur.com/xzQ2GMF.gif
http://i.imgur.com/XMj23nP.gif
http://i.imgur.com/EsdtMZw.gif
http://i.imgur.com/q9JFPrd.gif
http://i.imgur.com/STKYIWY.gif
http://i.imgur.com/JRbM5rB.gif
http://i.imgur.com/G1uM66k.gif
http://i.imgur.com/3U6Ebmx.gif
http://i.imgur.com/SfmWVZW.gif
http://i.imgur.com/xMARDlq.gif
http://i.imgur.com/8Y6nitw.gif
http://i.imgur.com/ZKXn6O8.gif
http://i.imgur.com/ZzZZbXs.gif
http://i.imgur.com/4x9Y663.gif
http://i.imgur.com/FnnCX.gif
http://i.imgur.com/uxHxihP.gif
http://i.imgur.com/fB40gz0.gif
http://i.imgur.com/bZc7Lad.gif
http://i.imgur.com/uNzbddL.gif
http://i.imgur.com/yjZw4jS.gif
http://i.imgur.com/b6D4Qd3.gif
http://i.imgur.com/KsjpeZj.gif
http://i.imgur.com/rj3hfes.gif
http://i.imgur.com/JcPHl47.gif
http://i.imgur.com/p5z2czM.gif
http://i.imgur.com/Czqxa.gif
http://i.imgur.com/p8GG04W.gif
http://i.imgur.com/b6D4Qd3.gif
http://i.imgur.com/szktB.gif
http://i.imgur.com/ZCnnH.gif
	"""
	
    beardpics = """ http://i.imgur.com/N8llwyZ.jpg
http://i.imgur.com/raFV9ym.jpg
http://i.imgur.com/FnpOkAQ.jpg
http://i.imgur.com/Cgwfsm3.jpg
http://i.imgur.com/T6eup62.jpg
http://i.imgur.com/xehQ5yP.jpg
http://i.imgur.com/6FbftU6.jpg
http://i.imgur.com/VxxMPlN.jpg
http://i.imgur.com/uQme6CA.jpg
http://i.imgur.com/VuSPWck.jpg
http://i.imgur.com/MMiQgUj.jpg
http://i.imgur.com/4isYknw.jpg
http://i.imgur.com/36Gc6OV.jpg
http://i.imgur.com/PscVjuS.jpg
http://i.imgur.com/FQjSNCb.jpg
http://i.imgur.com/jaamrxP.jpg
http://i.imgur.com/XiKfy6K.jpg
http://i.imgur.com/145Vcum.jpg
http://i.imgur.com/dRM8N0S.jpg
http://i.imgur.com/PxPieRs.jpg
http://i.imgur.com/Wp6wNX4.jpg
http://i.imgur.com/gOrmQkF.jpg
http://i.imgur.com/IEfsCec.jpg
http://i.imgur.com/N2FgaAn.jpg
http://i.imgur.com/M0Y2ggg.jpg
http://i.imgur.com/rQ0PNJl.jpg
http://i.imgur.com/u07Mlqe.jpg
http://i.imgur.com/NkTiY1y.jpg
http://i.imgur.com/4FGXCok.jpg
http://i.imgur.com/WluxvNV.jpg
http://i.imgur.com/D1TVtbG.jpg
http://i.imgur.com/f7jr18o.jpg
http://i.imgur.com/yHNkDjv.jpg
http://i.imgur.com/nZyv9yt.jpg
http://i.imgur.com/gqMtN2s.jpg
http://i.imgur.com/KakJ148.jpg
http://i.imgur.com/oqHWyjb.jpg
http://i.imgur.com/vJd6muK.jpg
http://i.imgur.com/oQ7pIq9.jpg
http://i.imgur.com/lxNb5oG.jpg
http://i.imgur.com/OAelOAF.jpg
http://i.imgur.com/pNtvtCU.jpg
http://i.imgur.com/2OjM2Pc.jpg
http://i.imgur.com/GYmNpBT.jpg
http://i.imgur.com/uPt5gaH.jpg
http://i.imgur.com/amXCkHP.jpg
http://i.imgur.com/4HfvP57.jpg
http://i.imgur.com/BbS4htm.jpg
http://i.imgur.com/Pu5Kj39.jpg
http://i.imgur.com/z2GOh7f.jpg
http://i.imgur.com/iiVVVgS.jpg
http://i.imgur.com/qofGvyL.jpg
http://i.imgur.com/HV9Su3i.jpg
http://i.imgur.com/MyxviQd.jpg
http://i.imgur.com/7NWpNzU.jpg
http://i.imgur.com/uI85NXU.jpg
http://i.imgur.com/62Q3v1P.jpg
http://i.imgur.com/mTAO31O.jpg
http://i.imgur.com/aFM8gRr.jpg
http://i.imgur.com/KtwsHhP.jpg
http://i.imgur.com/JZPjoJQ.jpg
http://i.imgur.com/MTqN9Tu.jpg
http://i.imgur.com/UNFSSyA.jpg
http://i.imgur.com/dyOgK4m.jpg
http://i.imgur.com/N104RiT.jpg
http://i.imgur.com/SYSbtr9.jpg
http://i.imgur.com/x9wy2Zo.jpg
http://i.imgur.com/Kxzx1Cx.jpg
http://i.imgur.com/1dc3rAH.jpg
http://i.imgur.com/7lsivFK.jpg
http://i.imgur.com/ScySFir.jpg
http://i.imgur.com/QOfb1tM.jpg
http://i.imgur.com/XVX8Yfv.jpg
http://i.imgur.com/zZnFNs3.jpg
http://i.imgur.com/6V9Idm6.jpg
http://i.imgur.com/3uygubZ.jpg
http://i.imgur.com/157Pp8h.jpg
http://i.imgur.com/zz4hxuh.jpg
http://i.imgur.com/52j4fFm.jpg
http://i.imgur.com/7drYvaU.jpg
http://i.imgur.com/62UFag3.jpg
http://i.imgur.com/AMVw8L7.jpg
http://i.imgur.com/VZ4hBRZ.jpg
http://i.imgur.com/wY00sKY.jpg
http://i.imgur.com/7fcVDLc.jpg
http://i.imgur.com/BDyS5Ak.jpg
http://i.imgur.com/bpOPEL0.jpg
http://i.imgur.com/UGcjFMm.jpg
http://i.imgur.com/e5C9Rt9.jpg
http://i.imgur.com/f4dqvsx.jpg
http://i.imgur.com/nwJtDQs.jpg
http://i.imgur.com/o4hFa6Q.jpg
http://i.imgur.com/ymgSPn3.jpg
http://i.imgur.com/BXGa0jY.jpg
http://i.imgur.com/zpAlmzz.jpg
http://i.imgur.com/JiRp4V6.jpg
http://i.imgur.com/PoYIhTc.jpg
http://i.imgur.com/MJ2n58V.jpg
http://i.imgur.com/qfbsWql.jpg
http://i.imgur.com/XtOVYVE.jpg
http://i.imgur.com/Vra3lEK.jpg
http://i.imgur.com/CvxtgcK.jpg
http://i.imgur.com/DZDomX7.jpg
http://i.imgur.com/eYh7YLN.jpg
http://i.imgur.com/4tqU2us.jpg
http://i.imgur.com/A3rVT6g.jpg
http://i.imgur.com/trSiDDN.jpg
http://i.imgur.com/weIhXrN.jpg
http://i.imgur.com/nWATiCn.jpg
http://i.imgur.com/kJeMxl6.jpg
http://i.imgur.com/bPLn8XS.jpg
http://i.imgur.com/dLhUzEO.jpg
http://i.imgur.com/INfAGlY.jpg
http://i.imgur.com/y7MT3w3.jpg
http://i.imgur.com/NODxuQQ.jpg
http://i.imgur.com/KAxzHDV.jpg
http://i.imgur.com/kSGxsP9.jpg
http://i.imgur.com/tpT9YEX.jpg
http://i.imgur.com/TaSySOx.jpg
http://i.imgur.com/UIH3mlh.jpg
http://i.imgur.com/t1NsS0h.jpg
http://i.imgur.com/Gbyzo1S.jpg
http://i.imgur.com/mmc0oxX.jpg
http://i.imgur.com/rqzLX0b.jpg
http://i.imgur.com/lBeMx21.jpg
http://i.imgur.com/O7iGbvA.jpg
http://i.imgur.com/HkWPaJ5.jpg
http://i.imgur.com/tFAaDU4.jpg
http://i.imgur.com/eU6lzX8.jpg
http://i.imgur.com/SORzgpX.jpg
http://i.imgur.com/ArDzPoK.jpg
http://i.imgur.com/JsisG4O.jpg
http://i.imgur.com/92WS4Je.jpg
http://i.imgur.com/P6SUNtO.jpg
http://i.imgur.com/B0I7ppz.jpg
http://i.imgur.com/Nc72C7A.jpg
http://i.imgur.com/dmDSlEA.jpg
http://i.imgur.com/DL6fAh1.jpg
http://i.imgur.com/cRn43sz.jpg
http://i.imgur.com/2UVw6r7.jpg
http://i.imgur.com/iXACr2Q.jpg
http://i.imgur.com/Df426vC.jpg
http://i.imgur.com/E41X71k.jpg
http://i.imgur.com/BV7GfwX.jpg
http://i.imgur.com/QhKi5kK.jpg
http://i.imgur.com/Hx8CmYx.jpg
http://i.imgur.com/yXgv3df.jpg
http://i.imgur.com/YVEU8k7.jpg
http://i.imgur.com/TrtDnS5.jpg
http://i.imgur.com/IIujjyd.jpg
http://i.imgur.com/5H13NC7.jpg
http://i.imgur.com/jfzKlQO.jpg
http://i.imgur.com/Hurd3uq.jpg
http://i.imgur.com/GpLlSFl.jpg
http://i.imgur.com/XQZKJxr.jpg
http://i.imgur.com/ZPLm8j9.jpg
http://i.imgur.com/Ny3kyH7.jpg
http://i.imgur.com/Egg1yUV.jpg
http://i.imgur.com/WWkKYlO.jpg
http://i.imgur.com/KjW5c8O.jpg
http://i.imgur.com/7lIm8zJ.jpg
http://i.imgur.com/nqS5tWq.jpg
http://i.imgur.com/wJXMlwu.jpg
http://i.imgur.com/lkprx9I.jpg
http://i.imgur.com/Dh9wGSw.jpg
http://i.imgur.com/L6f49lV.jpg
http://i.imgur.com/CrfXK1i.jpg
http://i.imgur.com/2lfvaqC.jpg
http://i.imgur.com/sjZrEpB.jpg
http://i.imgur.com/ycWK1Ao.jpg
http://i.imgur.com/vpfqB9v.jpg
http://i.imgur.com/UR8fftv.jpg
http://i.imgur.com/s6N0Xpo.jpg
http://i.imgur.com/xX1F7Dc.jpg
http://i.imgur.com/W6GKujx.gif
	"""
	
    def _color(self, c, fg=None):
        if c == ' ':
            return c
        if fg is None:
            fg = str(random.randint(2, 15)).zfill(2)
    	return '\x03%s%s' % (fg, c)
    
    def movie(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Stream: ") + "http://www.livestream.com/tafilms")
    movie = wrap(movie)
    
    def dexter(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Stream: ") + "http://misclivestream.blogspot.co.uk/p/dexter.html", msg.nick, private=True, notice=True)
    dexter = wrap(dexter)
    
    def minecraft(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Server Info: ") + "http://bit.ly/Qihbt7")
    minecraft = wrap(minecraft)

    def camchat(self, irc, msg, args):
    	if msg.args[0] == "#togetheralone":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#tamods":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#r4r":
        	title = "WaNt tO Go WiLd~*~* Try out the camchat! ---> "
        	title = ircutils.bold(ircutils.mircColor(title,'pink', '12'))
        	irc.reply(title + """http://www.icanhazchat.com/redditorforredditor""", prefixNick=True)
    camchat=wrap(camchat)
    
    def pet(self, irc, msg, args):
    	if random.randrange(0, 2):
    		irc.reply("ignores your love", action=True)
    	else:
    		irc.reply("purrs at your petting", action=True)
    pet=wrap(pet)
	
    def holyshit(self, irc, msg, args):
        
        irc.reply("http://i.imgur.com/OaNf0dj.gif", prefixNick=True)
    holyshit = wrap(holyshit)
    
    def suicide(self, irc, msg, args):
        
        irc.reply(ircutils.bold("""International Suicide Hotlines: """) +  "http://www.suicide.org/international-suicide-hotlines.html")
        irc.reply(ircutils.bold("""International Association for Suicide Prevention: """) +  "http://www.iasp.info/resources/Crisis_Centres/")
        irc.reply(ircutils.bold("""Veterans Crisis Line: """) +  "http://www.veteranscrisisline.net/ChatTermsOfService.aspx?account=Veterans_Chat")
    suicide = wrap(suicide)

    def nerdcraft(self, irc, msg, args):
        
        irc.reply(ircutils.bold("""ICHC Room: """) +  "http://www.icanhazchat.com/nerdcraft")
    nerdcraft = wrap(nerdcraft)
    
    def psa(self, irc, msg, args):
    	text = ircutils.bold(ircutils.mircColor("""NOTICE: If you or anyone you know is getting creepy PMs, or if someone in the chat is making you uncomfortable, please let a mod know ASAP. You can find a list of mods by typing .mods or on the rules page posted in the topic.""",'4'))
    	irc.reply(text)
    psa = wrap(psa)
    
    def nerdbang(self, irc, msg, args):
        
        irc.reply(ircutils.bold("""18+ ICHC Room: """) + "http://www.icanhazchat.com/nerdbang")
    nerdbang = wrap(nerdbang)
                  
    def tksync(self, irc, msg, args):
                  
        irc.reply("""Come join!: http://tksync.com/""")
    tksync = wrap(tksync)
    
    def radio(self, irc, msg, args):
                  
        irc.reply("""Click this: http://98.202.200.208:8002/listen.m3u""", prefixNick=True)
        irc.reply("""If you have any requests, feel free to bug PoohBear :)""", prefixNick=True)
    radio = wrap(radio)
    
    def rooms(self, irc, msg, args):
        irc.reply("""If you are interested in other social rooms on Freenode, check out #r.trees #reddit-mlp #reddit-depression #reddit-twoxchromosomes #teaandcrumpets (general UK chat) #introverts #defocus ##socialites #okchat (/r/okcupid) ##loseit #r4r #r4r30plus #togetheralone #mnfh (/r/MakeNewFriendsHere) #gaygeeks #beardporn #reddit-diabetes ##idliketobeatree and ##rhhh""", prefixNick=True)
    rooms = wrap(rooms)
    
    def mods(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, actualgirl, and arisu.""", prefixNick=True)
    	if msg.args[0] == "#ta-support":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, actualgirl, and arisu.""", prefixNick=True)
    	if msg.args[0] == "#ta-lounge":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, actualgirl, and arisu.""", prefixNick=True)
        if msg.args[0] == "#tamods":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, actualgirl, and arisu.""", prefixNick=True)
        else:
			return
    mods = wrap(mods)
    
    def gplus(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""G+ Group: """) + """http://goo.gl/t9Sws""")
    	if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""G+ Group: """) + """http://goo.gl/t9Sws""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""G+ Group: """) + """http://goo.gl/t9Sws""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""G+ Group: """) + """http://goo.gl/t9Sws""")
        else:
			return
    gplus = wrap(gplus)
    
    def gaybar(self, irc, msg, args):
        irc.reply("""http://youtu.be/HTN6Du3MCgI""", prefixNick=True)
    gaybar = wrap(gaybar)
    
    def pics(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/1fl82k/i_see_we_havent_had_a_picture_thread_in_while_so/""")
        if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/1fl82k/i_see_we_havent_had_a_picture_thread_in_while_so/""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/1fl82k/i_see_we_havent_had_a_picture_thread_in_while_so/""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/1fl82k/i_see_we_havent_had_a_picture_thread_in_while_so/""")
        else:
			return
    pics = wrap(pics)
    
    def bdaylist(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        else:
			return
    bdaylist = wrap(bdaylist)
    
    def bdayform(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
    	if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
        else:
			return
    bdayform = wrap(bdayform)
    
    def tinychat(self, irc, msg, args):
        irc.reply(ircutils.bold("""Tinychat Room: """) + "http://tinychat.com/chilijam")
    tinychat = wrap(tinychat)

    def chilijam(self, irc, msg, args):
        irc.reply(ircutils.bold("""Tinychat Room: """) + "http://tinychat.com/chilijam")
    chilijam = wrap(chilijam)
    
    def cards(self, irc, msg, args):
        irc.reply(ircutils.bold("""Cards Against Humanity: """) + "http://pyz.ricin.us")
    cards = wrap(cards)
    
    def turntable(self, irc, msg, args):
        irc.reply(ircutils.bold("""Turntable FM: """) + "http://turntable.fm/51bd2e10eb35c11ba584408f")
    turntable = wrap(turntable)
    
    def friday(self, irc, msg, args):
        irc.reply("http://youtu.be/kfVsfOSbJY0", prefixNick=True)
    friday = wrap(friday)
    
    def languages(self, irc, msg, args):
    	irc.reply("""http://goo.gl/DBImS""", prefixNick=True)
    languages = wrap(languages)
    
    def adventuretime(self, irc, msg, args):
    	irc.reply("http://www.justin.tv/cujoe50", prefixNick=True)
    adventuretime = wrap(adventuretime)
    
    def archer(self, irc, msg, args):
    	irc.reply("http://www.justin.tv/arconai_270", prefixNick=True)
    archer = wrap(archer)

    def womp(self, irc, msg, args):
    	irc.reply("http://youtu.be/yJxCdh1Ps48", prefixNick=True)
    womp = wrap(womp)
    
    def nph(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/hSU3tmQ.jpg",prefixNick=True)  
    nph = wrap(nph)  
    def hangout(self, irc, msg, args, victim):
        if msg.args[0] == "#togetheralone":
			text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
			text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
			text2 = text1 + """http://goo.gl/oms8X"""
			if not victim:
				irc.reply(text2, prefixNick=True)
			else:
				irc.reply(format('%s: %s ', victim, text2),
						  prefixNick=False)
        if msg.args[0] == "#r4r":
			text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
			text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
			text2 = text1 + """http://www.icanhazchat.com/nerdbang"""
			if not victim:
				irc.reply(text2, prefixNick=True)
			else:
				irc.reply(format('%s: %s ', victim, text2),
						  prefixNick=False)
    	if msg.args[0] == "#ta-support":
    		text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
        	text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
        	text2 = text1 + """http://goo.gl/oms8X"""
        	if not victim:
        		irc.reply(text2, prefixNick=True)
        	else:
        		irc.reply(format('%s: %s ', victim, text2),prefixNick=False)
    	if msg.args[0] == "#ta-lounge":
			text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
			text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
			text2 = text1 + """http://goo.gl/oms8X"""
			if not victim:
				irc.reply(text2, prefixNick=True)
			else:
				irc.reply(format('%s: %s ', victim, text2),
						  prefixNick=False)
        if msg.args[0] == "#tamods":
			text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
			text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
			text2 = text1 + """http://goo.gl/oms8X"""
			if not victim:
				irc.reply(text2, prefixNick=True)
			else:
				irc.reply(format('%s: %s ', victim, text2),
						  prefixNick=False)
    	else:
    		return
    hangout = wrap(hangout, [additional('text')])
    
    def heart(self, irc, msg, args, target):
    	if not target:
    		target=msg.nick
    	text1 = ircutils.mircColor('♥.¸¸.•´¯`•.♥','4')
    	text2 = ircutils.mircColor('♥.•´¯`•.¸¸.♥','4')
    	target = ircutils.bold(target)
    	irc.reply('%s %s %s'%(text1, target, text2))
    heart = wrap(heart, [additional('text')])
    
    def hug(self, irc, msg, args, target):
    	if not target:
    		target=msg.nick
    	emotehug = '( > ^.^( o‿o)'
    	hearts = ircutils.mircColor('♥','4')
    	target = ircutils.bold(target)
    	irc.reply('hugs %s'%target, action=True)
    	irc.reply('%s %s %s'%(hearts, emotehug, hearts))
    hug = wrap(hug, [additional('text')])
    
    def abraza(self, irc, msg, args, target):
    	if not target:
    		target=msg.nick
    	emotehug = '( > ^.^( o‿o)'
    	hearts = ircutils.mircColor('♥','4')
    	target = ircutils.bold(target)
    	irc.reply('abraza %s'%target, action=True)
    	irc.reply('%s %s %s'%(hearts, emotehug, hearts))
    abraza = wrap(abraza, [additional('text')])
    
    def rules(self, irc, msg, args):
    	if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#ta-lounge":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#tamods":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""") 
        if msg.args[0] == "#r4r":
            irc.reply(ircutils.bold("""Rules for #r4r: """) + """http://pastebin.com/8aFkb48r""")
        if msg.args[0] == "#newjersey":
            irc.reply(ircutils.bold("""Rules for #newjersey: """) + """http://pastebin.com/AgRarwqu""")            
        else:
            return None
    rules = wrap(rules)
    
    def games(self, irc, msg, args):
    	irc.reply("For game rooms on Freenode, check out ##poker ##uno ##apples2 #wolfgame ##trivia and #botsagainsthumanity", prefixNick=True)
    games = wrap(games)
    	
    def banlist(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	if msg.args[0] == "#ta-support":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	if msg.args[0] == "#ta-lounge":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
        if msg.args[0] == "#tamods":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	else:
    		return
    banlist = wrap(banlist)
    
    def map(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	if msg.args[0] == "#ta-support":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	if msg.args[0] == "#ta-lounge":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
        if msg.args[0] == "#tamods":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	else:
    		return
    map = wrap(map)
    
    def butts(self, irc, msg, args):
        if msg.args[0] == "#ta-lounge":
    		plist = [x for x in TA.sexybutts.split("\n") if len(x.strip())]
    	else:
    		plist = [x for x in TA.wordbutts.split("\n") if len(x.strip())]
    	p = choice(plist)
    	irc.reply(p.strip(), prefixNick=True)
    butts = wrap(butts)

    def beards(self, irc, msg, args):
        if msg.args[0] == "#beardporn":
    		plist = [x for x in TA.beardpics.split("\n") if len(x.strip())]
    		p = choice(plist)
    		irc.reply(p.strip(), prefixNick=True)
    	else:
			irc.reply("That command is too sexy for this room. Come on over to #beardporn and try it there.", prefixNick=True)
    beards = wrap(beards)
    
    def guys(self, irc, msg, args):
        if msg.args[0] == "#ta-lounge":
    		plist = [x for x in TA.sexyguys.split("\n") if len(x.strip())]
    		p = choice(plist)
    		irc.reply(p.strip(), prefixNick=True)
    	else:
    		irc.reply("That command is too sexy for this room. Come on over to #ta-lounge and try it there.", prefixNick=True)
    guys = wrap(guys)
    
    def simpsons(self, irc, msg, args):
    	irc.reply("http://www.justin.tv/arconai_228", prefixNick=True)
    simpsons = wrap(simpsons)
    
    def belair(self, irc, msg, args):
    	irc.reply("http://youtu.be/aZZULi9r6mY", prefixNick=True)
    belair = wrap(belair)
    
    def yay(self, irc, msg, args):
    	irc.reply("http://flutteryay.com/", prefixNick=True)
    yay = wrap(yay)

    def damn(self, irc, msg, args):
    	irc.reply("http://youtu.be/sf9cS-iXa9A", prefixNick=True)
    damn = wrap(damn)
    
    def dew(self, irc, msg, args):
    	irc.reply("http://dewextended.ytmnd.com", prefixNick=True)
    dew = wrap(dew)
    
    def peen(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/iYehgzT.gif", prefixNick=True)
    peen = wrap(peen)
    
    def taco(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/xupXop2.gif", prefixNick=True)
    taco = wrap(taco)
    
    def dituni(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/ywToWF0.png", prefixNick=True)
    dituni = wrap(dituni)

    def dance(self,irc,msg,args):
        right = ircutils.mircColor("(>", '13') + "'.'" + ircutils.mircColor(")>", '13')
        left = ircutils.mircColor("<(", '13') + "'.'" + ircutils.mircColor("<)", '13')
        up = ircutils.mircColor("^(", '13') + " '.' " + ircutils.mircColor(")^", '13')
        down = ircutils.mircColor("v(", '13') + " '.' " + ircutils.mircColor(")v", '13')
        
        irc.reply(right,prefixNick=False)
        irc.reply(up,prefixNick=False)
        irc.reply(left,prefixNick=False)
        irc.reply(down,prefixNick=False)
    dance = wrap(dance)

    def no(self, irc, msg, args, victim):
    	lod = """ಠ_ಠ"""
    	if victim is None:
    		return None
        irc.reply(format('%s: %s', victim, lod))
    no = wrap(no,[additional('text')])
    
    def kanye(self, irc, msg, args, words):
        """[<nick(optional)/person/(is|was|had|has)/thing(plural)>]
        
        Turns a group of words into a quote from Kanye West. Example: "kanye Derpy/Carl Sagan/is/atheists" will return 
        "Yo Derpy. I'm really happy for you, and I'm gonna let you finish, but Carl Sagan is one of the best atheists OF ALL TIME." 
        If no nick is specified, the caller's nick is used instead.
        """
        wordlist = words.split('/')
        if len(wordlist) == 3:
        	irc.reply(format("""Yo %s, I'm really happy for you, and I'm gonna let you finish, but %s %s one of the best %s OF ALL TIME.""", msg.nick, wordlist[0], wordlist[1], wordlist[2]))
        elif len(wordlist) == 4:
        	irc.reply(format("""Yo %s, I'm really happy for you, I'mma let you finish, but %s %s one of the best %s OF ALL TIME.""", wordlist[0], wordlist[1], wordlist[2], wordlist[3]))
        else:
        	return None
    kanye = wrap(kanye,[('text')])
Class = TA

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
