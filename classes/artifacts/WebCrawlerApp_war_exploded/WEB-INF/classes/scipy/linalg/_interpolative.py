# encoding: utf-8
# module scipy.linalg._interpolative
# from /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/scipy/linalg/_interpolative.so
# by generator 1.136
"""
This module '_interpolative' is auto-generated with f2py (version:2).
Functions:
  r = id_srand(n)
  id_srandi(t)
  id_srando()
  y = idd_frm(n,w,x,m=len(x))
  y = idd_sfrm(l,n,w,x,m=len(x))
  n,w = idd_frmi(m)
  n,w = idd_sfrmi(l,m)
  krank,list,rnorms = iddp_id(eps,a,m=shape(a,0),n=shape(a,1))
  list,rnorms = iddr_id(a,krank,m=shape(a,0),n=shape(a,1))
  approx = idd_reconid(col,list,proj,m=shape(col,0),krank=shape(col,1),n=len(list))
  p = idd_reconint(list,proj,n=len(list),krank=shape(proj,0))
  col = idd_copycols(a,krank,list,m=shape(a,0),n=shape(a,1))
  u,v,s,ier = idd_id2svd(b,list,proj,m=shape(b,0),krank=shape(b,1),n=len(list),w=)
  snorm,v = idd_snorm(m,n,matvect,matvec,its,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,u=,matvect_extra_args=(),matvec_extra_args=())
  snorm = idd_diffsnorm(m,n,matvect,matvect2,matvec,matvec2,its,p1t=,p2t=,p3t=,p4t=,p1t2=,p2t2=,p3t2=,p4t2=,p1=,p2=,p3=,p4=,p12=,p22=,p32=,p42=,w=,matvect_extra_args=(),matvect2_extra_args=(),matvec_extra_args=(),matvec2_extra_args=())
  u,v,s,ier = iddr_svd(a,krank,m=shape(a,0),n=shape(a,1),r=)
  krank,iu,iv,is,w,ier = iddp_svd(eps,a,m=shape(a,0),n=shape(a,1))
  krank,list,proj = iddp_aid(eps,a,work,proj,m=shape(a,0),n=shape(a,1))
  krank,ra = idd_estrank(eps,a,w,ra,m=shape(a,0),n=shape(a,1))
  krank,iu,iv,is,w,ier = iddp_asvd(eps,a,winit,w,m=shape(a,0),n=shape(a,1))
  krank,list,proj,ier = iddp_rid(eps,m,n,matvect,proj,p1=,p2=,p3=,p4=,matvect_extra_args=())
  krank,ra,ier = idd_findrank(eps,m,n,matvect,p1=,p2=,p3=,p4=,w=,matvect_extra_args=())
  krank,iu,iv,is,w,ier = iddp_rsvd(eps,m,n,matvect,matvec,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,matvect_extra_args=(),matvec_extra_args=())
  list,proj = iddr_aid(a,krank,w,m=shape(a,0),n=shape(a,1))
  w = iddr_aidi(m,n,krank)
  u,v,s,ier = iddr_asvd(a,krank,w,m=shape(a,0),n=shape(a,1))
  list,proj = iddr_rid(m,n,matvect,krank,p1=,p2=,p3=,p4=,matvect_extra_args=())
  u,v,s,ier = iddr_rsvd(m,n,matvect,matvec,krank,p1t=,p2t=,p3t=,p4t=,p1=,p2=,p3=,p4=,w=,matvect_extra_args=(),matvec_extra_args=())
  y = idz_frm(n,w,x,m=len(x))
  y = idz_sfrm(l,n,w,x,m=len(x))
  n,w = idz_frmi(m)
  n,w = idz_sfrmi(l,m)
  krank,list,rnorms = idzp_id(eps,a,m=shape(a,0),n=shape(a,1))
  list,rnorms = idzr_id(a,krank,m=shape(a,0),n=shape(a,1))
  approx = idz_reconid(col,list,proj,m=shape(col,0),krank=shape(col,1),n=len(list))
  p = idz_reconint(list,proj,n=len(list),krank=shape(proj,0))
  col = idz_copycols(a,krank,list,m=shape(a,0),n=shape(a,1))
  u,v,s,ier = idz_id2svd(b,list,proj,m=shape(b,0),krank=shape(b,1),n=len(list),w=)
  snorm,v = idz_snorm(m,n,matveca,matvec,its,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,u=,matveca_extra_args=(),matvec_extra_args=())
  snorm = idz_diffsnorm(m,n,matveca,matveca2,matvec,matvec2,its,p1a=,p2a=,p3a=,p4a=,p1a2=,p2a2=,p3a2=,p4a2=,p1=,p2=,p3=,p4=,p12=,p22=,p32=,p42=,w=,matveca_extra_args=(),matveca2_extra_args=(),matvec_extra_args=(),matvec2_extra_args=())
  u,v,s,ier = idzr_svd(a,krank,m=shape(a,0),n=shape(a,1),r=)
  krank,iu,iv,is,w,ier = idzp_svd(eps,a,m=shape(a,0),n=shape(a,1))
  krank,list,proj = idzp_aid(eps,a,work,proj,m=shape(a,0),n=shape(a,1))
  krank,ra = idz_estrank(eps,a,w,ra,m=shape(a,0),n=shape(a,1))
  krank,iu,iv,is,w,ier = idzp_asvd(eps,a,winit,w,m=shape(a,0),n=shape(a,1))
  krank,list,proj,ier = idzp_rid(eps,m,n,matveca,proj,p1=,p2=,p3=,p4=,matveca_extra_args=())
  krank,ra,ier = idz_findrank(eps,m,n,matveca,p1=,p2=,p3=,p4=,w=,matveca_extra_args=())
  krank,iu,iv,is,w,ier = idzp_rsvd(eps,m,n,matveca,matvec,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,matveca_extra_args=(),matvec_extra_args=())
  list,proj = idzr_aid(a,krank,w,m=shape(a,0),n=shape(a,1))
  w = idzr_aidi(m,n,krank)
  u,v,s,ier = idzr_asvd(a,krank,w,m=shape(a,0),n=shape(a,1))
  list,proj = idzr_rid(m,n,matveca,krank,p1=,p2=,p3=,p4=,matveca_extra_args=())
  u,v,s,ier = idzr_rsvd(m,n,matveca,matvec,krank,p1a=,p2a=,p3a=,p4a=,p1=,p2=,p3=,p4=,w=,matveca_extra_args=(),matvec_extra_args=())
.
"""
# no imports

# Variables with simple values

__version__ = '$Revision: $'

# no functions
# no classes
# variables with complex values

iddp_aid = None # (!) real value is ''

iddp_asvd = None # (!) real value is ''

iddp_id = None # (!) real value is ''

iddp_rid = None # (!) real value is ''

iddp_rsvd = None # (!) real value is ''

iddp_svd = None # (!) real value is ''

iddr_aid = None # (!) real value is ''

iddr_aidi = None # (!) real value is ''

iddr_asvd = None # (!) real value is ''

iddr_id = None # (!) real value is ''

iddr_rid = None # (!) real value is ''

iddr_rsvd = None # (!) real value is ''

iddr_svd = None # (!) real value is ''

idd_copycols = None # (!) real value is ''

idd_diffsnorm = None # (!) real value is ''

idd_estrank = None # (!) real value is ''

idd_findrank = None # (!) real value is ''

idd_frm = None # (!) real value is ''

idd_frmi = None # (!) real value is ''

idd_id2svd = None # (!) real value is ''

idd_reconid = None # (!) real value is ''

idd_reconint = None # (!) real value is ''

idd_sfrm = None # (!) real value is ''

idd_sfrmi = None # (!) real value is ''

idd_snorm = None # (!) real value is ''

idzp_aid = None # (!) real value is ''

idzp_asvd = None # (!) real value is ''

idzp_id = None # (!) real value is ''

idzp_rid = None # (!) real value is ''

idzp_rsvd = None # (!) real value is ''

idzp_svd = None # (!) real value is ''

idzr_aid = None # (!) real value is ''

idzr_aidi = None # (!) real value is ''

idzr_asvd = None # (!) real value is ''

idzr_id = None # (!) real value is ''

idzr_rid = None # (!) real value is ''

idzr_rsvd = None # (!) real value is ''

idzr_svd = None # (!) real value is ''

idz_copycols = None # (!) real value is ''

idz_diffsnorm = None # (!) real value is ''

idz_estrank = None # (!) real value is ''

idz_findrank = None # (!) real value is ''

idz_frm = None # (!) real value is ''

idz_frmi = None # (!) real value is ''

idz_id2svd = None # (!) real value is ''

idz_reconid = None # (!) real value is ''

idz_reconint = None # (!) real value is ''

idz_sfrm = None # (!) real value is ''

idz_sfrmi = None # (!) real value is ''

idz_snorm = None # (!) real value is ''

id_srand = None # (!) real value is ''

id_srandi = None # (!) real value is ''

id_srando = None # (!) real value is ''

