#i n cl u d e " SimpleApp .h"
// sim pl e ”main” f i l e which s e r v e s t o b uil d and run a CMOOSApp−d e ri v e d
a p p l i c a t i o n
int main ( int a r g c , char ∗ argv [ ] )
{
// s e t up some d e f a u l t a p p l i c a t i o n p a r ame te r s
// whats the name o f the c o n fi g u r a t i o n f i l e t h a t the a p p l i c a ti o n
// sh ould l o o k i n i f i t need s t o re ad p a r ame te r s ?
4
const char ∗ sMi s s i o n F i l e = " Mission . moos " ;
// under what name shoud the a p p l i c a t i o n r e g i s t e r with the MOOSDB?
const char ∗ sMOOSName = " MyMOOSApp " ;
switch ( a r g c )
{
case 3:
//command l i n e s a y s don ’ t r e g i s t e r with d e f a u l t name
sMOOSName = argv [ 2 ] ;
case 2:
//command l i n e s a y s don ’ t u se d e f a u l t ” mi s si o n . moos” c o n fi g f i l e
sMi s s i o n F i l e = argv [ 1 ] ;
}
//make an a p p l i c a t i o n
CSimpleApp TheApp ;
// run f o r e v e r p a si n g r e g i s t r a t i o n name and mi s si o n f i l e p a rame te r s
TheApp . Run(sMOOSName, sMi s s i o n F i l e ) ;
// p r ob ably w i l l neve r g e t h e r e . .
return 0;
}
Listing 2: Simplest Application - main.cpp
// Ex1/SimpleApp . h : i n t e r f a c e f o r the CSimpleApp c l a s s .
#i fnd e f SIMPLEAPPH
#def ine SIMPLEAPPH
#include <MOOSLIB/MOOSApp. h>
c l a ss CSimpleApp : public CMOOSApp
{
public :
// s t and a r d c o n s t r u c ti o n and d e s t r u c ti o n
CSimpleApp ( ) ;
v i rtua l ˜CSimpleApp ( ) ;
protected :
// where we handle new m ail
bool OnNewMail (MOOSMSG LIST &NewMail ) ;
// where we do the work
bool I t e r a t e ( ) ;
// c a l l e d when we c onnec t to the s e r v e r
bool OnConnectToServer ( ) ;
// c a l l e d when we a r e s t a r t i n g up . .
bool OnStartUp ( ) ;
} ;
#end i f
Listing 3: Simplest Application - main.cpp
5
#include " SimpleApp .h"
// d e f a ul t c o n s t r u c t o r
CSimpleApp : : CSimpleApp ( )
{
}
// d e f a ul t ( v i r t u a l ) d e s t r u c t o r
CSimpleApp : : ˜ CSimpleApp ( )
{
}
/∗ ∗
C all ed by base c l a s s whenever new m ail has a r r i v e d .
Pl ace your code f o r h andli n g m ail ( n o t i f i c a t i o n s th a t s omething
has changed i n the MOOSDB i n t h i s f u n c ti o n
Par ameter s :
NewMail : s td : : l i s t <CMOOSMsg> r e f e r e n c e
Return v al u e s :
r e t u r n t r u e i f e v e r y t hi n g went OK
r e t u r n f a l s e i f t h e r e was problem
∗ ∗/
bool CSimpleApp : : OnNewMail (MOOSMSG LIST &NewMail )
{
return true ;
}
/∗ ∗
c a l l e d by the base c l a s s when the a p pl i c a ti o n has made c o n t a c t with
the MOOSDB and a ch annel has been opened . Pl ace code to s p e c i f y what
n o t i f i c a t i o n s you want to r e c e i v e he r e .
∗ ∗/
bool CSimpleApp : : OnConnectToServer ( )
{
return true ;
}
/∗ ∗ C all ed by the base c l a s s p e r i o d i c a l l y . This i s where you pl a c e code
which does the work o f the a p pl i c a ti o n ∗ ∗/
bool CSimpleApp : : I t e r a t e ( )
{
return true ;
}
/∗ ∗ c a l l e d by the base c l a s s b e f o r e the f i r s t : : I t e r a t e i s c a l l e d . Pl ace
s t a r t u p code he r e − e s p e c i a l l y code which r e ad s c o n f i g u r a ti o n data from the
mi s si o n f i l e ∗ ∗/
bool CSimpleApp : : OnStartUp ( )
{
return true ;
}
3 The Important C
