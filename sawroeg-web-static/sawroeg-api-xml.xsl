<?xml version="1.0" encoding="utf-8" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:template match="/">
  <html>
   <body>
    <ol>
     <xsl:attrbibute name="start">
      <xsl:value-of select="/xml/request[@start]" />
     </xsl:attribute>
     <xsl:for-each select="/xml/request/word">
      <li>
       <xsl:for-each select="desc">
        <div>
         <xsl:value-of select="." />
        </div>
       </xsl:for-each>
      <li>
     </xsl:for-each>
    </ol>
   </body>
  </html>
 </xsl:template>
</xsl:stylesheet>
