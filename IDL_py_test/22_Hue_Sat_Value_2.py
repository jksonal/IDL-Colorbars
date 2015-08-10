from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf
cm_data = [[1., 0.992157, 0.992157],
[1., 0.992157, 0.992157],
[1., 0.988235, 0.988235],
[1., 0.984314, 0.984314],
[1., 0.980392, 0.980392],
[1., 0.976471, 0.976471],
[1., 0.972549, 0.972549],
[1., 0.968627, 0.972549],
[1., 0.964706, 0.968627],
[1., 0.960784, 0.968627],
[1., 0.956863, 0.964706],
[1., 0.952941, 0.964706],
[1., 0.94902, 0.960784],
[1., 0.945098, 0.960784],
[1., 0.941176, 0.956863],
[1., 0.937255, 0.956863],
[1., 0.933333, 0.956863],
[1., 0.929412, 0.956863],
[1., 0.92549, 0.952941],
[1., 0.921569, 0.952941],
[1., 0.917647, 0.952941],
[1., 0.913725, 0.952941],
[1., 0.909804, 0.952941],
[1., 0.905882, 0.952941],
[1., 0.901961, 0.952941],
[1., 0.898039, 0.952941],
[1., 0.894118, 0.956863],
[1., 0.890196, 0.956863],
[1., 0.886275, 0.956863],
[1., 0.882353, 0.956863],
[1., 0.878431, 0.960784],
[1., 0.87451, 0.960784],
[1., 0.870588, 0.964706],
[1., 0.866667, 0.964706],
[1., 0.862745, 0.968627],
[1., 0.858824, 0.968627],
[1., 0.854902, 0.972549],
[1., 0.85098, 0.976471],
[1., 0.847059, 0.980392],
[1., 0.843137, 0.980392],
[1., 0.839216, 0.984314],
[1., 0.835294, 0.988235],
[1., 0.831373, 0.992157],
[1., 0.827451, 0.996078],
[0.996078, 0.823529, 1.],
[0.992157, 0.819608, 1.],
[0.988235, 0.815686, 1.],
[0.984314, 0.811765, 1.],
[0.976471, 0.807843, 1.],
[0.972549, 0.803922, 1.],
[0.968627, 0.8, 1.],
[0.964706, 0.796078, 1.],
[0.956863, 0.792157, 1.],
[0.952941, 0.788235, 1.],
[0.945098, 0.784314, 1.],
[0.941176, 0.780392, 1.],
[0.933333, 0.776471, 1.],
[0.929412, 0.772549, 1.],
[0.921569, 0.768627, 1.],
[0.913725, 0.764706, 1.],
[0.905882, 0.760784, 1.],
[0.901961, 0.756863, 1.],
[0.894118, 0.752941, 1.],
[0.886275, 0.74902, 1.],
[0.878431, 0.745098, 1.],
[0.870588, 0.741176, 1.],
[0.862745, 0.737255, 1.],
[0.854902, 0.733333, 1.],
[0.847059, 0.729412, 1.],
[0.835294, 0.72549, 1.],
[0.827451, 0.721569, 1.],
[0.819608, 0.717647, 1.],
[0.811765, 0.713725, 1.],
[0.8, 0.709804, 1.],
[0.792157, 0.705882, 1.],
[0.780392, 0.701961, 1.],
[0.772549, 0.698039, 1.],
[0.760784, 0.694118, 1.],
[0.752941, 0.690196, 1.],
[0.741176, 0.686275, 1.],
[0.733333, 0.682353, 1.],
[0.721569, 0.678431, 1.],
[0.709804, 0.67451, 1.],
[0.698039, 0.670588, 1.],
[0.686275, 0.666667, 1.],
[0.67451, 0.662745, 1.],
[0.666667, 0.662745, 1.],
[0.658824, 0.662745, 1.],
[0.654902, 0.666667, 1.],
[0.65098, 0.670588, 1.],
[0.647059, 0.67451, 1.],
[0.643137, 0.678431, 1.],
[0.639216, 0.682353, 1.],
[0.635294, 0.690196, 1.],
[0.631373, 0.694118, 1.],
[0.627451, 0.698039, 1.],
[0.623529, 0.705882, 1.],
[0.619608, 0.709804, 1.],
[0.615686, 0.717647, 1.],
[0.611765, 0.721569, 1.],
[0.607843, 0.729412, 1.],
[0.603922, 0.737255, 1.],
[0.6, 0.741176, 1.],
[0.596078, 0.74902, 1.],
[0.592157, 0.756863, 1.],
[0.588235, 0.764706, 1.],
[0.584314, 0.772549, 1.],
[0.580392, 0.780392, 1.],
[0.576471, 0.788235, 1.],
[0.572549, 0.796078, 1.],
[0.568627, 0.803922, 1.],
[0.564706, 0.811765, 1.],
[0.560784, 0.819608, 1.],
[0.556863, 0.827451, 1.],
[0.552941, 0.839216, 1.],
[0.54902, 0.847059, 1.],
[0.545098, 0.854902, 1.],
[0.541176, 0.866667, 1.],
[0.537255, 0.87451, 1.],
[0.533333, 0.886275, 1.],
[0.529412, 0.894118, 1.],
[0.52549, 0.905882, 1.],
[0.521569, 0.913725, 1.],
[0.517647, 0.92549, 1.],
[0.513725, 0.937255, 1.],
[0.509804, 0.945098, 1.],
[0.505882, 0.956863, 1.],
[0.501961, 0.968627, 1.],
[0.498039, 0.980392, 1.],
[0.494118, 0.992157, 1.],
[0.490196, 1., 0.992157],
[0.486275, 1., 0.980392],
[0.482353, 1., 0.968627],
[0.478431, 1., 0.956863],
[0.47451, 1., 0.945098],
[0.470588, 1., 0.929412],
[0.466667, 1., 0.917647],
[0.462745, 1., 0.905882],
[0.458824, 1., 0.890196],
[0.454902, 1., 0.878431],
[0.45098, 1., 0.862745],
[0.447059, 1., 0.85098],
[0.443137, 1., 0.835294],
[0.439216, 1., 0.823529],
[0.435294, 1., 0.807843],
[0.431373, 1., 0.796078],
[0.427451, 1., 0.780392],
[0.423529, 1., 0.764706],
[0.419608, 1., 0.74902],
[0.415686, 1., 0.733333],
[0.411765, 1., 0.717647],
[0.407843, 1., 0.701961],
[0.403922, 1., 0.686275],
[0.4, 1., 0.670588],
[0.396078, 1., 0.654902],
[0.392157, 1., 0.639216],
[0.388235, 1., 0.623529],
[0.384314, 1., 0.607843],
[0.380392, 1., 0.588235],
[0.376471, 1., 0.572549],
[0.372549, 1., 0.556863],
[0.368627, 1., 0.537255],
[0.364706, 1., 0.521569],
[0.360784, 1., 0.501961],
[0.356863, 1., 0.486275],
[0.352941, 1., 0.466667],
[0.34902, 1., 0.447059],
[0.345098, 1., 0.431373],
[0.341176, 1., 0.411765],
[0.337255, 1., 0.392157],
[0.333333, 1., 0.372549],
[0.333333, 1., 0.352941],
[0.329412, 1., 0.337255],
[0.329412, 1., 0.32549],
[0.345098, 1., 0.321569],
[0.356863, 1., 0.317647],
[0.368627, 1., 0.313725],
[0.380392, 1., 0.309804],
[0.392157, 1., 0.305882],
[0.403922, 1., 0.301961],
[0.419608, 1., 0.298039],
[0.431373, 1., 0.294118],
[0.447059, 1., 0.290196],
[0.458824, 1., 0.286275],
[0.47451, 1., 0.282353],
[0.486275, 1., 0.278431],
[0.501961, 1., 0.27451],
[0.513725, 1., 0.270588],
[0.529412, 1., 0.266667],
[0.545098, 1., 0.262745],
[0.560784, 1., 0.258824],
[0.572549, 1., 0.254902],
[0.588235, 1., 0.25098],
[0.603922, 1., 0.247059],
[0.619608, 1., 0.243137],
[0.635294, 1., 0.239216],
[0.65098, 1., 0.235294],
[0.666667, 1., 0.231373],
[0.682353, 1., 0.227451],
[0.701961, 1., 0.223529],
[0.717647, 1., 0.219608],
[0.733333, 1., 0.215686],
[0.74902, 1., 0.211765],
[0.768627, 1., 0.207843],
[0.784314, 1., 0.203922],
[0.803922, 1., 0.2],
[0.819608, 1., 0.196078],
[0.839216, 1., 0.192157],
[0.854902, 1., 0.188235],
[0.87451, 1., 0.184314],
[0.894118, 1., 0.180392],
[0.913725, 1., 0.176471],
[0.929412, 1., 0.172549],
[0.94902, 1., 0.168627],
[0.968627, 1., 0.164706],
[0.988235, 1., 0.160784],
[1., 0.988235, 0.156863],
[1., 0.968627, 0.152941],
[1., 0.94902, 0.14902],
[1., 0.929412, 0.145098],
[1., 0.909804, 0.141176],
[1., 0.886275, 0.137255],
[1., 0.866667, 0.133333],
[1., 0.847059, 0.129412],
[1., 0.827451, 0.12549],
[1., 0.803922, 0.121569],
[1., 0.784314, 0.117647],
[1., 0.760784, 0.113725],
[1., 0.741176, 0.109804],
[1., 0.717647, 0.105882],
[1., 0.698039, 0.101961],
[1., 0.67451, 0.0980392],
[1., 0.65098, 0.0941176],
[1., 0.627451, 0.0901961],
[1., 0.607843, 0.0862745],
[1., 0.584314, 0.0823529],
[1., 0.560784, 0.0784314],
[1., 0.537255, 0.0745098],
[1., 0.513725, 0.0705882],
[1., 0.490196, 0.0666667],
[1., 0.466667, 0.0627451],
[1., 0.443137, 0.0588235],
[1., 0.419608, 0.054902],
[1., 0.392157, 0.0509804],
[1., 0.368627, 0.0470588],
[1., 0.345098, 0.0431373],
[1., 0.317647, 0.0509804],
[1., 0.294118, 0.0352941],
[1., 0.270588, 0.0313725],
[1., 0.243137, 0.027451],
[1., 0.219608, 0.0235294],
[1., 0.192157, 0.0196078],
[1., 0.164706, 0.0156863],
[1., 0.141176, 0.0117647],
[1., 0.113725, 0.00784314],
[1., 0.113725, 0.00784314]]

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
