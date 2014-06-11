# coding=utf-8
__author__ = u"Leonardo Salom Muñoz"
__credits__ = u"Leonardo Salom Muñoz"
__version__ = u"0.0.3-SNAPSHOT"
__maintainer__ = u"Leonardo Salom Muñoz"
__email__ = u"leosamu@upv.es"
__status__ = u"Development"

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class cdfXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    href = String(display_name="href",
                  default="http://www.wolfram.com/cdf/uses-examples/KnowledgeApps/KnowledgeApps.cdf",
                  scope=Scope.content,
                  help="CDF file that will be shown in the XBlock")

    display_name = String(display_name="Display Name",
                          default="Mathematica Laboratory",
                          scope=Scope.settings,
                          help="Name of the component in the edxplatform")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the cdfXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/mathematica.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/mathematica.css"))
        return frag

      # TO-DO: change this view to display your data your own way.
    def studio_view(self, context=None):
        """
        The primary view of the paellaXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/mathematica_edit.html")
        frag = Fragment(html.format(self=self))
        frag.add_javascript(self.resource_string("static/js/src/mathematica_edit.js"))
        frag.initialize_js('cdfXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def save_mathematica(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        self.href = data['href']
        self.display_name = data['display_name']

        return {
            'result': 'success',
        }

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("cdfXBlock",
             """<vertical_demo>
                <mathematica/>
                </vertical_demo>
             """),
        ]