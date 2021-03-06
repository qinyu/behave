# -*- coding: utf-8 -*-
"""
CSS themes to include in the HTML formatter.
"""


class BasicTheme(object):
    stylesheet_text = """
body {
    font-size:0;
    color:#fff;
    margin:0;
    padding:0
}

.behave,td,th {
    font:400 11px "Lucida Grande",Helvetica,sans-serif;
    background:#fff;
    color:#000
}

.behave #behave-header,td #behave-header, th #behave-header {
    background:#65c400;
    color:#fff;
    height:8em
}

.behave #behave-header #expand-collapse p,td #behave-header #expand-collapse p,th #behave-header
#expand-collapse p {
    float:right;
    margin:0 0 0 10px
}

.scenario h3:hover {
    background-color: #84d033!important;
    cursor: pointer;
}

.background h3,.behave .scenario h3,td .scenario h3,th .scenario h3 {
    font-size:11px;
    padding:3px;
    margin:0;
    background:#65c400;
    color:#fff;
    font-weight:700
}

.background h3 {
    font-size:1.2em;
    background:#666
}

.behave h1,td h1,th h1 {
    margin:0 10px;
    padding:10px;
    font-family:'Lucida Grande', Helvetica,sans-serif;
    font-size:2em;
    position:absolute
}

.behave h4,td h4, th h4 {
    margin-bottom:2px
}

.behave div.feature,td div.feature,th div.feature {
    padding:2px;
    margin:0 10px 5px
}

.behave div.examples,td div.examples,th div.examples {
    padding:0 0 0 1em
}

.behave .stats,td .stats,th .stats {
    margin:2em
}

.behave .summary ul.features li,td .summary ul.features li,th .summary ul.features li {
    display:inline
}

.behave .step_name,td .step_name,th .step_name {
    float:left
}

.behave .step_file,td .step_file,th .step_file {
    text-align:right;
    color:#999
}

.behave .step_file a,td .step_file a,th .step_file a {
    color:#999
}

.behave .scenario_file,td .scenario_file,th .scenario_file {
    float:right;color:#999
}

.behave .tag,td .tag,th .tag {
    font-weight:700;
    color:#246ac1
}

.behave .backtrace,td .backtrace,th .backtrace {
    margin-top:0;
    margin-bottom:0;
    margin-left:1em;
    color:#000
}

.behave a,td a,th a {
    text-decoration:none;
    color:#be5c00
}

.behave a:hover, td a:hover,th a:hover {
    text-decoration:underline
}

.behave a:visited,td a:visited, th a:visited {
    font-weight:400
}

.behave a div.examples,td a div.examples, th a div.examples{
    margin:5px 0 5px 15px;color:#000
}

.behave .outline table, td .outline table,th .outline table {
    margin:0 0 5px 10px
}

.behave table, td table,th table {
    border-collapse:collapse
}

.behave table td,td table td, th table td {
    padding:3px 3px 3px 5px
}

.behave table td.failed,td table td.failed, th table td.failed {
    border-left:5px solid #c20000;
    border-bottom:1px solid #c20000;
    background:#fffbd3;
    color:#c20000
}

.behave table td.passed,td table td.passed,th table td.passed {
    border-left:5px solid #65c400;
    border-bottom:1px solid #65c400;
    background:#dbffb4;
    color:#3d7700
}

.behave table td.skipped,td table td.skipped,th table td.skipped {
    border-left:5px solid #0ff;
    border-bottom:1px solid #0ff;
    background:#e0ffff;
    color:#011
}

.behave table td.pending,.behave table td.undefined,td table td.pending,td table td.undefined,
th table td.pending,th table td.undefined {
    border-left:5px solid #faf834;
    border-bottom:1px solid #faf834;
    background:#fcfb98;
    color:#131313
}

.behave table td.message,td table td.message,th table td.message {
    border-left:5px solid #0ff;
    border-bottom:1px solid #0ff;
    background:#e0ffff;
    color:#011
}

.behave ol,td ol,th ol {
    list-style:none;
    margin:0;
    padding:0
}

.behave ol li.step,td ol li.step,th ol li.step {
    padding:3px 3px 3px 18px;
    margin:5px 0 5px 5px
}

.behave ol li,td ol li,th ol li {
    margin:0 0 0 1em;
    padding:0 0 0 .2em
}

.behave ol li span.param,td ol li span.param,th ol li span.param {
    font-weight:700
}

.behave ol li.failed,td ol li.failed,th ol li.failed {
    border-left:5px solid #c20000;
    border-bottom:1px solid #c20000;
    background:#fffbd3;
    color:#c20000
}

.behave ol li.passed,td ol li.passed,th ol li.passed {
    border-left:5px solid #65c400;
    border-bottom:1px solid #65c400;
    background:#dbffb4;
    color:#3d7700
}

.behave ol li.skipped,td ol li.skipped,th ol li.skipped {
    border-left:5px solid #0ff;
    border-bottom:1px solid #0ff;
    background:#e0ffff;
    color:#011
}

.behave ol li.pending,.behave ol li.undefined,td ol li.pending,td ol li.undefined,th ol li.pending,
th ol li.undefined {
    border-left:5px solid #faf834;
    border-bottom:1px solid #faf834;
    background:#fcfb98;
    color:#131313
}

.behave ol li.message,td ol li.message,th ol li.message {
    border-left:5px solid #0ff;
    border-bottom:1px solid #0ff;
    background:#e0ffff;
    color:#011;
    margin-left:10px
}

.behave #summary,td #summary,th #summary {
    margin:0;
    padding:5px 10px;
    text-align:right;
    top:0;
    right:0;
    float:right
}

.behave #summary p,td #summary p,th #summary p {
    margin:0 0 0 2px
}

.behave #summary #totals,td #summary #totals,th #summary #totals {
    font-size:1.2em
}
"""
