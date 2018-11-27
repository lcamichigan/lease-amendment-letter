#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import textwrap


file_path = 'info.tex'
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        file.write(textwrap.dedent('''
        \\newcommand*\\tenantName{TenantFirstName TenantLastName}
        \\newcommand*\SigmaAddress{Sigma Alumni Association\\\\
          123 Main St\\\\
          Anywhere MI 00000-0000\\\\
          lcamichigan.com%
        }
        \\newcommand*\SigmaSignatoryName{Warren Cole}
        \\newcommand*\SigmaSignatoryTitle{President}
        \\newcommand*\SigmaSignatureDate{\\today}
        ''').lstrip())

directory_name = 'support'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)

jobname = 'SigmaSignature'
file_path = os.path.join(directory_name, jobname + '.pdf')
if not os.path.exists(file_path):
    subprocess.check_call([
        'luatex',
        '-fmt=lualatex',
        '-interaction=batchmode',
        '-jobname=' + jobname,
        '-output-directory=' + directory_name,
        (
            # See
            # https://tex.stackexchange.com/questions/315025/lualatex-texlive-2016-standalone-undefined-control-sequence
            # for more information about why the luatex85 package is required.
            '\RequirePackage{luatex85}'
            '\documentclass[varwidth]{standalone}'
            '\\begin{document}\sffamily '
            'Replace ' + file_path.replace('\\', '\\textbackslash ') + '\par with an image of a signature.'
            '\end{document}'
        )
    ])
