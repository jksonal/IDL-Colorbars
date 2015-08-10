from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[1., 0.968627, 0.984314],
[0.996078, 0.964706, 0.984314],
[0.996078, 0.964706, 0.980392],
[0.992157, 0.960784, 0.980392],
[0.992157, 0.956863, 0.980392],
[0.988235, 0.956863, 0.976471],
[0.984314, 0.952941, 0.976471],
[0.984314, 0.94902, 0.976471],
[0.980392, 0.94902, 0.972549],
[0.976471, 0.945098, 0.972549],
[0.976471, 0.941176, 0.968627],
[0.972549, 0.941176, 0.968627],
[0.972549, 0.937255, 0.968627],
[0.968627, 0.933333, 0.964706],
[0.964706, 0.933333, 0.964706],
[0.964706, 0.929412, 0.964706],
[0.960784, 0.92549, 0.960784],
[0.960784, 0.921569, 0.960784],
[0.956863, 0.921569, 0.960784],
[0.952941, 0.917647, 0.956863],
[0.952941, 0.913725, 0.956863],
[0.94902, 0.913725, 0.956863],
[0.94902, 0.909804, 0.952941],
[0.945098, 0.905882, 0.952941],
[0.941176, 0.905882, 0.94902],
[0.941176, 0.901961, 0.94902],
[0.937255, 0.898039, 0.94902],
[0.933333, 0.898039, 0.945098],
[0.933333, 0.894118, 0.945098],
[0.929412, 0.890196, 0.945098],
[0.929412, 0.890196, 0.941176],
[0.92549, 0.886275, 0.941176],
[0.921569, 0.882353, 0.941176],
[0.917647, 0.882353, 0.937255],
[0.913725, 0.878431, 0.937255],
[0.913725, 0.878431, 0.937255],
[0.909804, 0.87451, 0.933333],
[0.905882, 0.87451, 0.933333],
[0.901961, 0.870588, 0.933333],
[0.898039, 0.870588, 0.933333],
[0.894118, 0.866667, 0.929412],
[0.890196, 0.866667, 0.929412],
[0.886275, 0.862745, 0.929412],
[0.886275, 0.862745, 0.92549],
[0.882353, 0.858824, 0.92549],
[0.878431, 0.858824, 0.92549],
[0.87451, 0.854902, 0.921569],
[0.870588, 0.854902, 0.921569],
[0.866667, 0.85098, 0.921569],
[0.862745, 0.847059, 0.917647],
[0.858824, 0.847059, 0.917647],
[0.858824, 0.843137, 0.917647],
[0.854902, 0.843137, 0.913725],
[0.85098, 0.839216, 0.913725],
[0.847059, 0.839216, 0.913725],
[0.843137, 0.835294, 0.913725],
[0.839216, 0.835294, 0.909804],
[0.835294, 0.831373, 0.909804],
[0.831373, 0.831373, 0.909804],
[0.831373, 0.827451, 0.905882],
[0.827451, 0.827451, 0.905882],
[0.823529, 0.823529, 0.905882],
[0.819608, 0.823529, 0.901961],
[0.815686, 0.819608, 0.901961],
[0.811765, 0.815686, 0.901961],
[0.803922, 0.815686, 0.898039],
[0.8, 0.811765, 0.898039],
[0.796078, 0.811765, 0.898039],
[0.788235, 0.807843, 0.894118],
[0.784314, 0.803922, 0.894118],
[0.780392, 0.803922, 0.894118],
[0.776471, 0.8, 0.890196],
[0.768627, 0.796078, 0.890196],
[0.764706, 0.796078, 0.890196],
[0.760784, 0.792157, 0.886275],
[0.752941, 0.792157, 0.886275],
[0.74902, 0.788235, 0.886275],
[0.745098, 0.784314, 0.882353],
[0.737255, 0.784314, 0.882353],
[0.733333, 0.780392, 0.882353],
[0.729412, 0.776471, 0.878431],
[0.721569, 0.776471, 0.878431],
[0.717647, 0.772549, 0.87451],
[0.713725, 0.772549, 0.87451],
[0.705882, 0.768627, 0.87451],
[0.701961, 0.764706, 0.870588],
[0.698039, 0.764706, 0.870588],
[0.694118, 0.760784, 0.870588],
[0.686275, 0.756863, 0.866667],
[0.682353, 0.756863, 0.866667],
[0.678431, 0.752941, 0.866667],
[0.670588, 0.752941, 0.862745],
[0.666667, 0.74902, 0.862745],
[0.662745, 0.745098, 0.862745],
[0.654902, 0.745098, 0.858824],
[0.65098, 0.741176, 0.858824],
[0.643137, 0.737255, 0.858824],
[0.635294, 0.737255, 0.854902],
[0.627451, 0.733333, 0.854902],
[0.619608, 0.733333, 0.854902],
[0.611765, 0.729412, 0.85098],
[0.603922, 0.72549, 0.85098],
[0.596078, 0.72549, 0.847059],
[0.588235, 0.721569, 0.847059],
[0.580392, 0.717647, 0.847059],
[0.572549, 0.717647, 0.843137],
[0.564706, 0.713725, 0.843137],
[0.556863, 0.713725, 0.843137],
[0.54902, 0.709804, 0.839216],
[0.541176, 0.705882, 0.839216],
[0.533333, 0.705882, 0.835294],
[0.529412, 0.701961, 0.835294],
[0.521569, 0.698039, 0.835294],
[0.513725, 0.698039, 0.831373],
[0.505882, 0.694118, 0.831373],
[0.498039, 0.694118, 0.831373],
[0.490196, 0.690196, 0.827451],
[0.482353, 0.686275, 0.827451],
[0.47451, 0.686275, 0.823529],
[0.466667, 0.682353, 0.823529],
[0.458824, 0.678431, 0.823529],
[0.45098, 0.678431, 0.819608],
[0.443137, 0.67451, 0.819608],
[0.435294, 0.67451, 0.819608],
[0.427451, 0.670588, 0.815686],
[0.419608, 0.666667, 0.815686],
[0.411765, 0.666667, 0.811765],
[0.403922, 0.662745, 0.811765],
[0.396078, 0.658824, 0.811765],
[0.392157, 0.654902, 0.807843],
[0.384314, 0.654902, 0.807843],
[0.380392, 0.65098, 0.803922],
[0.372549, 0.647059, 0.803922],
[0.368627, 0.643137, 0.8],
[0.360784, 0.643137, 0.8],
[0.356863, 0.639216, 0.796078],
[0.34902, 0.635294, 0.796078],
[0.345098, 0.631373, 0.792157],
[0.337255, 0.627451, 0.792157],
[0.333333, 0.627451, 0.788235],
[0.32549, 0.623529, 0.788235],
[0.321569, 0.619608, 0.784314],
[0.313725, 0.615686, 0.784314],
[0.309804, 0.615686, 0.784314],
[0.301961, 0.611765, 0.780392],
[0.294118, 0.607843, 0.780392],
[0.290196, 0.603922, 0.776471],
[0.282353, 0.6, 0.776471],
[0.278431, 0.6, 0.772549],
[0.270588, 0.596078, 0.772549],
[0.266667, 0.592157, 0.768627],
[0.258824, 0.588235, 0.768627],
[0.254902, 0.584314, 0.764706],
[0.247059, 0.584314, 0.764706],
[0.243137, 0.580392, 0.760784],
[0.235294, 0.576471, 0.760784],
[0.231373, 0.572549, 0.756863],
[0.223529, 0.572549, 0.756863],
[0.219608, 0.568627, 0.752941],
[0.211765, 0.564706, 0.752941],
[0.203922, 0.564706, 0.745098],
[0.2, 0.560784, 0.741176],
[0.192157, 0.560784, 0.733333],
[0.188235, 0.556863, 0.72549],
[0.180392, 0.556863, 0.721569],
[0.172549, 0.552941, 0.713725],
[0.168627, 0.552941, 0.705882],
[0.160784, 0.54902, 0.701961],
[0.152941, 0.54902, 0.694118],
[0.14902, 0.545098, 0.686275],
[0.141176, 0.545098, 0.678431],
[0.137255, 0.541176, 0.67451],
[0.129412, 0.541176, 0.666667],
[0.121569, 0.537255, 0.658824],
[0.117647, 0.537255, 0.654902],
[0.109804, 0.537255, 0.647059],
[0.101961, 0.533333, 0.639216],
[0.0980392, 0.533333, 0.635294],
[0.0901961, 0.529412, 0.627451],
[0.0862745, 0.529412, 0.619608],
[0.0784314, 0.52549, 0.615686],
[0.0705882, 0.52549, 0.607843],
[0.0666667, 0.521569, 0.6],
[0.0588235, 0.521569, 0.596078],
[0.0509804, 0.517647, 0.588235],
[0.0470588, 0.517647, 0.580392],
[0.0392157, 0.513725, 0.572549],
[0.0352941, 0.513725, 0.568627],
[0.027451, 0.509804, 0.560784],
[0.0196078, 0.509804, 0.552941],
[0.0156863, 0.505882, 0.54902],
[0.00784314, 0.505882, 0.541176],
[0.00784314, 0.501961, 0.533333],
[0.00784314, 0.501961, 0.529412],
[0.00784314, 0.498039, 0.521569],
[0.00784314, 0.494118, 0.517647],
[0.00784314, 0.494118, 0.509804],
[0.00784314, 0.490196, 0.505882],
[0.00784314, 0.486275, 0.498039],
[0.00784314, 0.486275, 0.494118],
[0.00784314, 0.482353, 0.486275],
[0.00784314, 0.478431, 0.482353],
[0.00784314, 0.478431, 0.47451],
[0.00784314, 0.47451, 0.470588],
[0.00784314, 0.470588, 0.462745],
[0.00784314, 0.470588, 0.458824],
[0.00784314, 0.466667, 0.45098],
[0.00784314, 0.466667, 0.447059],
[0.00392157, 0.462745, 0.439216],
[0.00392157, 0.458824, 0.431373],
[0.00392157, 0.458824, 0.427451],
[0.00392157, 0.454902, 0.419608],
[0.00392157, 0.45098, 0.415686],
[0.00392157, 0.45098, 0.407843],
[0.00392157, 0.447059, 0.403922],
[0.00392157, 0.443137, 0.396078],
[0.00392157, 0.443137, 0.392157],
[0.00392157, 0.439216, 0.384314],
[0.00392157, 0.435294, 0.380392],
[0.00392157, 0.435294, 0.372549],
[0.00392157, 0.431373, 0.368627],
[0.00392157, 0.427451, 0.360784],
[0.00392157, 0.427451, 0.356863],
[0.00392157, 0.423529, 0.34902],
[0.00392157, 0.419608, 0.345098],
[0.00392157, 0.415686, 0.341176],
[0.00392157, 0.407843, 0.337255],
[0.00392157, 0.403922, 0.333333],
[0.00392157, 0.4, 0.329412],
[0.00392157, 0.396078, 0.321569],
[0.00392157, 0.392157, 0.317647],
[0.00392157, 0.388235, 0.313725],
[0.00392157, 0.380392, 0.309804],
[0.00392157, 0.376471, 0.305882],
[0.00392157, 0.372549, 0.301961],
[0.00392157, 0.368627, 0.298039],
[0.00392157, 0.364706, 0.294118],
[0.00392157, 0.356863, 0.290196],
[0.00392157, 0.352941, 0.286275],
[0.00392157, 0.34902, 0.282353],
[0.00392157, 0.345098, 0.27451],
[0.00392157, 0.341176, 0.270588],
[0.00392157, 0.333333, 0.266667],
[0.00392157, 0.329412, 0.262745],
[0.00392157, 0.32549, 0.258824],
[0.00392157, 0.321569, 0.254902],
[0.00392157, 0.317647, 0.25098],
[0.00392157, 0.313725, 0.247059],
[0.00392157, 0.305882, 0.243137],
[0.00392157, 0.301961, 0.239216],
[0.00392157, 0.298039, 0.231373],
[0.00392157, 0.294118, 0.227451],
[0.00392157, 0.290196, 0.223529],
[0.00392157, 0.282353, 0.219608],
[0.00392157, 0.278431, 0.215686],
[0.00392157, 0.27451, 0.211765]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()
