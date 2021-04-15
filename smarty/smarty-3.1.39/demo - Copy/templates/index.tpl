{config_load file="test.conf" section="setup"}
{include file="header.tpl" title=foo}

<head>
    <meta charset="utf-8">
    <title>Mellow Flow Advertising</title>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Inknut+Antiqua:wght@900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css">
    <link rel="stylesheet" href="/styles.css">
    <script
        src="https://code.jquery.com/jquery-3.3.1.js"
        integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="
        crossorigin="anonymous">
    </script>
    <div id="header"></div>
  </head>



<div style="background-image: url('assets/bubbles.png'); background-repeat:no-repeat; background-position:center; opacity: 0.94;" class="image-main-container" >
  <section>
      <div class="main_title">
        <br>
        <header>
                  <b>Mellow<br>Flow</b>
        </header>
      </div>
  </section>
  <body>

  </body>
</div>



<PRE>

{* bold and title are read from the config file *}
    {if #bold#}<b>{/if}
        {* capitalize the first letters of each word of the title *}
        Title: {#title#|capitalize}
        {if #bold#}</b>{/if}

    The current date and time is {$smarty.now|date_format:"%Y-%m-%d %H:%M:%S"}

    The value of global assigned variable $SCRIPT_NAME is {$SCRIPT_NAME}

    Example of accessing server environment variable SERVER_NAME: {$smarty.server.SERVER_NAME}

    The value of {ldelim}$Name{rdelim} is <b>{$Name}</b>

variable modifier example of {ldelim}$Name|upper{rdelim}

<b>{$Name|upper}</b>


An example of a section loop:

    {section name=outer
    loop=$FirstName}
        {if $smarty.section.outer.index is odd by 2}
            {$smarty.section.outer.rownum} . {$FirstName[outer]} {$LastName[outer]}
        {else}
            {$smarty.section.outer.rownum} * {$FirstName[outer]} {$LastName[outer]}
        {/if}
        {sectionelse}
        none
    {/section}

    An example of section looped key values:

    {section name=sec1 loop=$contacts}
        phone: {$contacts[sec1].phone}
        <br>

            fax: {$contacts[sec1].fax}
        <br>

            cell: {$contacts[sec1].cell}
        <br>
    {/section}
    <p>

        testing strip tags
        {strip}
<table border=0>
    <tr>
        <td>
            <A HREF="{$SCRIPT_NAME}">
                <font color="red">This is a test </font>
            </A>
        </td>
    </tr>
</table>
    {/strip}

</PRE>

This is an example of the html_select_date function:

<form>
    {html_select_date start_year=1998 end_year=2010}
</form>

This is an example of the html_select_time function:

<form>
    {html_select_time use_24_hours=false}
</form>

This is an example of the html_options function:

<form>
    <select name=states>
        {html_options values=$option_values selected=$option_selected output=$option_output}
    </select>
</form>

{include file="footer.tpl"}
{config_load file="test.conf" section="setup"}
{include file="header.tpl" title=foo}

<PRE>

{* bold and title are read from the config file *}
    {if #bold#}<b>{/if}
        {* capitalize the first letters of each word of the title *}
        Title: {#title#|capitalize}
        {if #bold#}</b>{/if}

    The current date and time is {$smarty.now|date_format:"%Y-%m-%d %H:%M:%S"}

    The value of global assigned variable $SCRIPT_NAME is {$SCRIPT_NAME}

    Example of accessing server environment variable SERVER_NAME: {$smarty.server.SERVER_NAME}

    The value of {ldelim}$Name{rdelim} is <b>{$Name}</b>

variable modifier example of {ldelim}$Name|upper{rdelim}

<b>{$Name|upper}</b>


An example of a section loop:

    {section name=outer
    loop=$FirstName}
        {if $smarty.section.outer.index is odd by 2}
            {$smarty.section.outer.rownum} . {$FirstName[outer]} {$LastName[outer]}
        {else}
            {$smarty.section.outer.rownum} * {$FirstName[outer]} {$LastName[outer]}
        {/if}
        {sectionelse}
        none
    {/section}

    An example of section looped key values:

    {section name=sec1 loop=$contacts}
        phone: {$contacts[sec1].phone}
        <br>

            fax: {$contacts[sec1].fax}
        <br>

            cell: {$contacts[sec1].cell}
        <br>
    {/section}
    <p>

        testing strip tags
        {strip}
<table border=0>
    <tr>
        <td>
            <A HREF="{$SCRIPT_NAME}">
                <font color="red">This is a test </font>
            </A>
        </td>
    </tr>
</table>
    {/strip}

</PRE>

This is an example of the html_select_date function:

<form>
    {html_select_date start_year=1998 end_year=2010}
</form>

This is an example of the html_select_time function:

<form>
    {html_select_time use_24_hours=false}
</form>

This is an example of the html_options function:

<form>
    <select name=states>
        {html_options values=$option_values selected=$option_selected output=$option_output}
    </select>
</form>

{include file="footer.tpl"}
