require 'ostruct'
module Maven
  module Tools
    LICENSES = {}
    LICENSES[ "afl-3.0" ] = OpenStruct.new :short => "AFL-3.0", :name => "Academic Free License 3.0", :url => "http://opensource.org/licenses/AFL-3.0"
    LICENSES[ "agpl-3.0" ] = OpenStruct.new :short => "AGPL-3.0", :name => "GNU Affero General Public License 3.0", :url => "http://opensource.org/licenses/AGPL-3.0"
    LICENSES[ "apl-1.0" ] = OpenStruct.new :short => "APL-1.0", :name => "Adaptive Public License", :url => "http://opensource.org/licenses/APL-1.0"
    LICENSES[ "apache-2.0" ] = OpenStruct.new :short => "Apache-2.0", :name => "Apache License 2.0", :url => "http://opensource.org/licenses/Apache-2.0"
    LICENSES[ "apsl-2.0" ] = OpenStruct.new :short => "APSL-2.0", :name => "Apple Public Source License", :url => "http://opensource.org/licenses/APSL-2.0"
    LICENSES[ "artistic-2.0" ] = OpenStruct.new :short => "Artistic-2.0", :name => "Artistic license 2.0", :url => "http://opensource.org/licenses/Artistic-2.0"
    LICENSES[ "aal" ] = OpenStruct.new :short => "AAL", :name => "Attribution Assurance Licenses", :url => "http://opensource.org/licenses/AAL"
    LICENSES[ "bsd-3-clause" ] = OpenStruct.new :short => "BSD-3-Clause", :name => "BSD 3-Clause \"New\" or \"Revised\" License", :url => "http://opensource.org/licenses/BSD-3-Clause"
    LICENSES[ "bsd-2-clause" ] = OpenStruct.new :short => "BSD-2-Clause", :name => "BSD 2-Clause \"Simplified\" or \"FreeBSD\" License", :url => "http://opensource.org/licenses/BSD-2-Clause"
    LICENSES[ "bsl-1.0" ] = OpenStruct.new :short => "BSL-1.0", :name => "Boost Software License", :url => "http://opensource.org/licenses/BSL-1.0"
    LICENSES[ "cecill-2.1" ] = OpenStruct.new :short => "CECILL-2.1", :name => "CeCILL License 2.1", :url => "http://opensource.org/licenses/CECILL-2.1"
    LICENSES[ "catosl-1.1" ] = OpenStruct.new :short => "CATOSL-1.1", :name => "Computer Associates Trusted Open Source License 1.1", :url => "http://opensource.org/licenses/CATOSL-1.1"
    LICENSES[ "cddl-1.0" ] = OpenStruct.new :short => "CDDL-1.0", :name => "Common Development and Distribution License 1.0", :url => "http://opensource.org/licenses/CDDL-1.0"
    LICENSES[ "cpal-1.0" ] = OpenStruct.new :short => "CPAL-1.0", :name => "Common Public Attribution License 1.0", :url => "http://opensource.org/licenses/CPAL-1.0"
    LICENSES[ "cua-opl-1.0" ] = OpenStruct.new :short => "CUA-OPL-1.0", :name => "CUA Office Public License Version 1.0", :url => "http://opensource.org/licenses/CUA-OPL-1.0"
    LICENSES[ "eudatagrid" ] = OpenStruct.new :short => "EUDatagrid", :name => "EU DataGrid Software License", :url => "http://opensource.org/licenses/EUDatagrid"
    LICENSES[ "epl-1.0" ] = OpenStruct.new :short => "EPL-1.0", :name => "Eclipse Public License 1.0", :url => "http://opensource.org/licenses/EPL-1.0"
    LICENSES[ "ecl-2.0" ] = OpenStruct.new :short => "ECL-2.0", :name => "Educational Community License, Version 2.0", :url => "http://opensource.org/licenses/ECL-2.0"
    LICENSES[ "efl-2.0" ] = OpenStruct.new :short => "EFL-2.0", :name => "Eiffel Forum License V2.0", :url => "http://opensource.org/licenses/EFL-2.0"
    LICENSES[ "entessa" ] = OpenStruct.new :short => "Entessa", :name => "Entessa Public License", :url => "http://opensource.org/licenses/Entessa"
    LICENSES[ "eupl-1.1" ] = OpenStruct.new :short => "EUPL-1.1", :name => "European Union Public License, Version 1.1", :url => "http://opensource.org/licenses/EUPL-1.1"
    LICENSES[ "fair" ] = OpenStruct.new :short => "Fair", :name => "Fair License", :url => "http://opensource.org/licenses/Fair"
    LICENSES[ "frameworx-1.0" ] = OpenStruct.new :short => "Frameworx-1.0", :name => "Frameworx License", :url => "http://opensource.org/licenses/Frameworx-1.0"
    LICENSES[ "agpl-3.0" ] = OpenStruct.new :short => "AGPL-3.0", :name => "GNU Affero General Public License v3", :url => "http://opensource.org/licenses/AGPL-3.0"
    LICENSES[ "gpl-2.0" ] = OpenStruct.new :short => "GPL-2.0", :name => "GNU General Public License version 2.0", :url => "http://opensource.org/licenses/GPL-2.0"
    LICENSES[ "gpl-3.0" ] = OpenStruct.new :short => "GPL-3.0", :name => "GNU General Public License version 3.0", :url => "http://opensource.org/licenses/GPL-3.0"
    LICENSES[ "lgpl-2.1" ] = OpenStruct.new :short => "LGPL-2.1", :name => "GNU Library or \"Lesser\" General Public License version 2.1", :url => "http://opensource.org/licenses/LGPL-2.1"
    LICENSES[ "lgpl-3.0" ] = OpenStruct.new :short => "LGPL-3.0", :name => "GNU Library or \"Lesser\" General Public License version 3.0", :url => "http://opensource.org/licenses/LGPL-3.0"
    LICENSES[ "hpnd" ] = OpenStruct.new :short => "HPND", :name => "Historical Permission Notice and Disclaimer", :url => "http://opensource.org/licenses/HPND"
    LICENSES[ "ipl-1.0" ] = OpenStruct.new :short => "IPL-1.0", :name => "IBM Public License 1.0", :url => "http://opensource.org/licenses/IPL-1.0"
    LICENSES[ "ipa" ] = OpenStruct.new :short => "IPA", :name => "IPA Font License", :url => "http://opensource.org/licenses/IPA"
    LICENSES[ "isc" ] = OpenStruct.new :short => "ISC", :name => "ISC License", :url => "http://opensource.org/licenses/ISC"
    LICENSES[ "lppl-1.3c" ] = OpenStruct.new :short => "LPPL-1.3c", :name => "LaTeX Project Public License 1.3c", :url => "http://opensource.org/licenses/LPPL-1.3c"
    LICENSES[ "lpl-1.02" ] = OpenStruct.new :short => "LPL-1.02", :name => "Lucent Public License Version 1.02", :url => "http://opensource.org/licenses/LPL-1.02"
    LICENSES[ "miros" ] = OpenStruct.new :short => "MirOS", :name => "MirOS Licence", :url => "http://opensource.org/licenses/MirOS"
    LICENSES[ "ms-pl" ] = OpenStruct.new :short => "MS-PL", :name => "Microsoft Public License", :url => "http://opensource.org/licenses/MS-PL"
    LICENSES[ "ms-rl" ] = OpenStruct.new :short => "MS-RL", :name => "Microsoft Reciprocal License", :url => "http://opensource.org/licenses/MS-RL"
    LICENSES[ "mit" ] = OpenStruct.new :short => "MIT", :name => "MIT license", :url => "http://opensource.org/licenses/MIT"
    LICENSES[ "motosoto" ] = OpenStruct.new :short => "Motosoto", :name => "Motosoto License", :url => "http://opensource.org/licenses/Motosoto"
    LICENSES[ "mpl-2.0" ] = OpenStruct.new :short => "MPL-2.0", :name => "Mozilla Public License 2.0", :url => "http://opensource.org/licenses/MPL-2.0"
    LICENSES[ "multics" ] = OpenStruct.new :short => "Multics", :name => "Multics License", :url => "http://opensource.org/licenses/Multics"
    LICENSES[ "nasa-1.3" ] = OpenStruct.new :short => "NASA-1.3", :name => "NASA Open Source Agreement 1.3", :url => "http://opensource.org/licenses/NASA-1.3"
    LICENSES[ "ntp" ] = OpenStruct.new :short => "NTP", :name => "NTP License", :url => "http://opensource.org/licenses/NTP"
    LICENSES[ "naumen" ] = OpenStruct.new :short => "Naumen", :name => "Naumen Public License", :url => "http://opensource.org/licenses/Naumen"
    LICENSES[ "ngpl" ] = OpenStruct.new :short => "NGPL", :name => "Nethack General Public License", :url => "http://opensource.org/licenses/NGPL"
    LICENSES[ "nokia" ] = OpenStruct.new :short => "Nokia", :name => "Nokia Open Source License", :url => "http://opensource.org/licenses/Nokia"
    LICENSES[ "nposl-3.0" ] = OpenStruct.new :short => "NPOSL-3.0", :name => "Non-Profit Open Software License 3.0", :url => "http://opensource.org/licenses/NPOSL-3.0"
    LICENSES[ "oclc-2.0" ] = OpenStruct.new :short => "OCLC-2.0", :name => "OCLC Research Public License 2.0", :url => "http://opensource.org/licenses/OCLC-2.0"
    LICENSES[ "ofl-1.1" ] = OpenStruct.new :short => "OFL-1.1", :name => "Open Font License 1.1", :url => "http://opensource.org/licenses/OFL-1.1"
    LICENSES[ "ogtsl" ] = OpenStruct.new :short => "OGTSL", :name => "Open Group Test Suite License", :url => "http://opensource.org/licenses/OGTSL"
    LICENSES[ "osl-3.0" ] = OpenStruct.new :short => "OSL-3.0", :name => "Open Software License 3.0", :url => "http://opensource.org/licenses/OSL-3.0"
    LICENSES[ "php-3.0" ] = OpenStruct.new :short => "PHP-3.0", :name => "PHP License 3.0", :url => "http://opensource.org/licenses/PHP-3.0"
    LICENSES[ "postgresql" ] = OpenStruct.new :short => "PostgreSQL", :name => "The PostgreSQL License", :url => "http://opensource.org/licenses/PostgreSQL"
    LICENSES[ "python-2.0" ] = OpenStruct.new :short => "Python-2.0", :name => "Python License", :url => "http://opensource.org/licenses/Python-2.0"
    LICENSES[ "cnri-python" ] = OpenStruct.new :short => "CNRI-Python", :name => "CNRI Python license", :url => "http://opensource.org/licenses/CNRI-Python"
    LICENSES[ "qpl-1.0" ] = OpenStruct.new :short => "QPL-1.0", :name => "Q Public License", :url => "http://opensource.org/licenses/QPL-1.0"
    LICENSES[ "rpsl-1.0" ] = OpenStruct.new :short => "RPSL-1.0", :name => "RealNetworks Public Source License V1.0", :url => "http://opensource.org/licenses/RPSL-1.0"
    LICENSES[ "rpl-1.5" ] = OpenStruct.new :short => "RPL-1.5", :name => "Reciprocal Public License 1.5", :url => "http://opensource.org/licenses/RPL-1.5"
    LICENSES[ "rscpl" ] = OpenStruct.new :short => "RSCPL", :name => "Ricoh Source Code Public License", :url => "http://opensource.org/licenses/RSCPL"
    LICENSES[ "simpl-2.0" ] = OpenStruct.new :short => "SimPL-2.0", :name => "Simple Public License 2.0", :url => "http://opensource.org/licenses/SimPL-2.0"
    LICENSES[ "sleepycat" ] = OpenStruct.new :short => "Sleepycat", :name => "Sleepycat License", :url => "http://opensource.org/licenses/Sleepycat"
    LICENSES[ "spl-1.0" ] = OpenStruct.new :short => "SPL-1.0", :name => "Sun Public License 1.0", :url => "http://opensource.org/licenses/SPL-1.0"
    LICENSES[ "watcom-1.0" ] = OpenStruct.new :short => "Watcom-1.0", :name => "Sybase Open Watcom Public License 1.0", :url => "http://opensource.org/licenses/Watcom-1.0"
    LICENSES[ "ncsa" ] = OpenStruct.new :short => "NCSA", :name => "University of Illinois/NCSA Open Source License", :url => "http://opensource.org/licenses/NCSA"
    LICENSES[ "vsl-1.0" ] = OpenStruct.new :short => "VSL-1.0", :name => "Vovida Software License v. 1.0", :url => "http://opensource.org/licenses/VSL-1.0"
    LICENSES[ "w3c" ] = OpenStruct.new :short => "W3C", :name => "W3C License", :url => "http://opensource.org/licenses/W3C"
    LICENSES[ "wxwindows" ] = OpenStruct.new :short => "WXwindows", :name => "wxWindows Library License", :url => "http://opensource.org/licenses/WXwindows"
    LICENSES[ "xnet" ] = OpenStruct.new :short => "Xnet", :name => "X.Net License", :url => "http://opensource.org/licenses/Xnet"
    LICENSES[ "zpl-2.0" ] = OpenStruct.new :short => "ZPL-2.0", :name => "Zope Public License 2.0", :url => "http://opensource.org/licenses/ZPL-2.0"
    LICENSES[ "zlib" ] = OpenStruct.new :short => "Zlib", :name => "zlib/libpng license", :url => "http://opensource.org/licenses/Zlib"
    LICENSES.freeze
  end
end