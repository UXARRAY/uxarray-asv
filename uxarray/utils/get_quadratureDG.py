import numpy as np
from numba import njit, config

config.DISABLE_JIT = False


@njit
def get_gauss_quadratureDG(nCount):
    """Gauss Quadrature Points for integration.

    Parameters
    ----------
    nCount : int, required
         Degree of quadrature points required, supports: 1 to 10.

    Returns
    -------
        dG : double
            numpy array of size ncount, quadrature points. Scaled before returning.
        dW : double
            numpy array of size ncount x 3, weights. Scaled before returning.

    Raises
    ------
       RuntimeError: Invalid degree
    """
    #Degree 1
    if (nCount == 1):
        dG = np.array([[0.0]])
        dW = np.array([+2.0])

    #Degree 2
    elif (nCount == 2):
        dG = np.array([[-0.5773502691896257, +0.5773502691896257]])
        dW = np.array([+1.0, +1.0])

    #Degree 3
    elif (nCount == 3):
        dG = np.array([[-0.7745966692414834, 0.0, +0.7745966692414834]])

        dW = np.array(
            [+0.5555555555555556, +0.8888888888888888, +0.5555555555555556])

    #Degree 4
    elif (nCount == 4):
        dG = np.array([[
            -0.8611363115940526, -0.3399810435848563, +0.3399810435848563,
            +0.8611363115940526
        ]])

        dW = np.array([
            0.3478548451374538, 0.6521451548625461, 0.6521451548625461,
            0.3478548451374538
        ])

    #Degree 5
    elif (nCount == 5):
        dG = np.array([[
            -0.9061798459386640, -0.5384693101056831, 0.0, +0.5384693101056831,
            +0.9061798459386640
        ]])

        dW = np.array([
            0.2369268850561891, 0.4786286704993665, 0.5688888888888889,
            0.4786286704993665, 0.2369268850561891
        ])

    #Degree 6
    elif (nCount == 6):
        dG = np.array([[
            -0.9324695142031521, -0.6612093864662645, -0.2386191860831969,
            +0.2386191860831969, +0.6612093864662645, +0.9324695142031521
        ]])

        dW = np.array([
            0.1713244923791704, 0.3607615730481386, 0.4679139345726910,
            0.4679139345726910, 0.3607615730481386, 0.1713244923791704
        ])

    #Degree 7
    elif (nCount == 7):
        dG = np.array([[
            -0.9491079123427585, -0.7415311855993945, -0.4058451513773972, 0.0,
            +0.4058451513773972, +0.7415311855993945, +0.9491079123427585
        ]])

        dW = np.array([
            0.1294849661688697, 0.2797053914892766, 0.3818300505051189,
            0.4179591836734694, 0.3818300505051189, 0.2797053914892766,
            0.1294849661688697
        ])

    #Degree 8
    elif (nCount == 8):
        dG = np.array([[
            -0.9602898564975363, -0.7966664774136267, -0.5255324099163290,
            -0.1834346424956498, +0.1834346424956498, +0.5255324099163290,
            +0.7966664774136267, +0.9602898564975363
        ]])

        dW = np.array([
            0.1012285362903763, 0.2223810344533745, 0.3137066458778873,
            0.3626837833783620, 0.3626837833783620, 0.3137066458778873,
            0.2223810344533745, 0.1012285362903763
        ])

    #Degree 9
    elif (nCount == 9):
        dG = np.array([[
            -1.0, -0.899757995411460, -0.677186279510738, -0.363117463826178,
            0.0, +0.363117463826178, +0.677186279510738, +0.899757995411460,
            +1.0
        ]])

        dW = np.array([
            0.0277777777777778, 0.1654953615608055, 0.2745387125001617,
            0.3464285109730463, 0.3715192743764172, 0.3464285109730463,
            0.2745387125001617, 0.1654953615608055, 0.0277777777777778
        ])

    #Degree 10
    elif (nCount == 10):
        dG = np.array([[
            -0.9739065285171717, -0.8650633666889845, -0.6794095682990244,
            -0.4333953941292472, -0.1488743389816312, +0.1488743389816312,
            +0.4333953941292472, +0.6794095682990244, +0.8650633666889845,
            +0.9739065285171717
        ]])

        dW = np.array([
            0.0666713443086881, 0.1494513491505806, 0.2190863625159820,
            0.2692667193099963, 0.2955242247147529, 0.2955242247147529,
            0.2692667193099963, 0.2190863625159820, 0.1494513491505806,
            0.0666713443086881
        ])
    # else:
    #     msg = "quadrature order 1 to 10 is supported: ", nCount, " is invalid\n"
    #     raise ValueError(msg)

    # Scale quadrature points
    dXi0 = 0.0
    dXi1 = 1.0
    for i in range(nCount):
        dG[0][i] = dXi0 + 0.5 * (dXi1 - dXi0) * (dG[0][i] + 1.0)
        dW[i] = 0.5 * (dXi1 - dXi0) * dW[i]

    return dG, dW


@njit
def get_tri_quadratureDG(nOrder):
    """Triangular Quadrature Points for integration.

    Parameters
    ----------
    nOrder : int
        Integration order, supports: 12, 10, 8, 4 and 1

    Returns
    -------
        dG, dW : ndarray
            points and weights, with dimension order x 3
    """
    # 12th order quadrature rule (33 points)
    if (nOrder == 12):
        dG = np.array(
            [[0.023565220452390, 0.488217389773805, 0.488217389773805],
             [0.488217389773805, 0.023565220452390, 0.488217389773805],
             [0.488217389773805, 0.488217389773805, 0.023565220452390],
             [0.120551215411079, 0.439724392294460, 0.439724392294460],
             [0.439724392294460, 0.120551215411079, 0.439724392294460],
             [0.439724392294460, 0.439724392294460, 0.120551215411079],
             [0.457579229975768, 0.271210385012116, 0.271210385012116],
             [0.271210385012116, 0.457579229975768, 0.271210385012116],
             [0.271210385012116, 0.271210385012116, 0.457579229975768],
             [0.744847708916828, 0.127576145541586, 0.127576145541586],
             [0.127576145541586, 0.744847708916828, 0.127576145541586],
             [0.127576145541586, 0.127576145541586, 0.744847708916828],
             [0.957365299093576, 0.021317350453210, 0.021317350453210],
             [0.021317350453210, 0.957365299093576, 0.021317350453210],
             [0.021317350453210, 0.021317350453210, 0.957365299093576],
             [0.115343494534698, 0.275713269685514, 0.608943235779788],
             [0.115343494534698, 0.608943235779788, 0.275713269685514],
             [0.275713269685514, 0.115343494534698, 0.608943235779788],
             [0.275713269685514, 0.608943235779788, 0.115343494534698],
             [0.608943235779788, 0.115343494534698, 0.275713269685514],
             [0.608943235779788, 0.275713269685514, 0.115343494534698],
             [0.022838332222257, 0.281325580989940, 0.695836086787803],
             [0.022838332222257, 0.695836086787803, 0.281325580989940],
             [0.281325580989940, 0.022838332222257, 0.695836086787803],
             [0.281325580989940, 0.695836086787803, 0.022838332222257],
             [0.695836086787803, 0.022838332222257, 0.281325580989940],
             [0.695836086787803, 0.281325580989940, 0.022838332222257],
             [0.025734050548330, 0.116251915907597, 0.858014033544073],
             [0.025734050548330, 0.858014033544073, 0.116251915907597],
             [0.116251915907597, 0.025734050548330, 0.858014033544073],
             [0.116251915907597, 0.858014033544073, 0.025734050548330],
             [0.858014033544073, 0.025734050548330, 0.116251915907597],
             [0.858014033544073, 0.116251915907597, 0.025734050548330]])

        dW = np.array([
            0.025731066440455, 0.025731066440455, 0.025731066440455,
            0.043692544538038, 0.043692544538038, 0.043692544538038,
            0.062858224217885, 0.062858224217885, 0.062858224217885,
            0.034796112930709, 0.034796112930709, 0.034796112930709,
            0.006166261051559, 0.006166261051559, 0.006166261051559,
            0.040371557766381, 0.040371557766381, 0.040371557766381,
            0.040371557766381, 0.040371557766381, 0.040371557766381,
            0.022356773202303, 0.022356773202303, 0.022356773202303,
            0.022356773202303, 0.022356773202303, 0.022356773202303,
            0.017316231108659, 0.017316231108659, 0.017316231108659,
            0.017316231108659, 0.017316231108659, 0.017316231108659
        ])

    # 10th order quadrature rule (25 points)
    elif (nOrder == 10):
        dG = np.array(
            [[0.333333333333333, 0.333333333333333, 0.333333333333333],
             [0.028844733232685, 0.485577633383657, 0.485577633383657],
             [0.485577633383657, 0.028844733232685, 0.485577633383657],
             [0.485577633383657, 0.485577633383657, 0.028844733232685],
             [0.781036849029926, 0.109481575485037, 0.109481575485037],
             [0.109481575485037, 0.781036849029926, 0.109481575485037],
             [0.109481575485037, 0.109481575485037, 0.781036849029926],
             [0.141707219414880, 0.307939838764121, 0.550352941820999],
             [0.141707219414880, 0.550352941820999, 0.307939838764121],
             [0.307939838764121, 0.141707219414880, 0.550352941820999],
             [0.307939838764121, 0.550352941820999, 0.141707219414880],
             [0.550352941820999, 0.141707219414880, 0.307939838764121],
             [0.550352941820999, 0.307939838764121, 0.141707219414880],
             [0.025003534762686, 0.246672560639903, 0.728323904597411],
             [0.025003534762686, 0.728323904597411, 0.246672560639903],
             [0.246672560639903, 0.025003534762686, 0.728323904597411],
             [0.246672560639903, 0.728323904597411, 0.025003534762686],
             [0.728323904597411, 0.025003534762686, 0.246672560639903],
             [0.728323904597411, 0.246672560639903, 0.025003534762686],
             [0.009540815400299, 0.066803251012200, 0.923655933587500],
             [0.009540815400299, 0.923655933587500, 0.066803251012200],
             [0.066803251012200, 0.009540815400299, 0.923655933587500],
             [0.066803251012200, 0.923655933587500, 0.009540815400299],
             [0.923655933587500, 0.009540815400299, 0.066803251012200],
             [0.923655933587500, 0.066803251012200, 0.009540815400299]])

        dW = np.array([
            0.090817990382754, 0.036725957756467, 0.036725957756467,
            0.036725957756467, 0.045321059435528, 0.045321059435528,
            0.045321059435528, 0.072757916845420, 0.072757916845420,
            0.072757916845420, 0.072757916845420, 0.072757916845420,
            0.072757916845420, 0.028327242531057, 0.028327242531057,
            0.028327242531057, 0.028327242531057, 0.028327242531057,
            0.028327242531057, 0.009421666963733, 0.009421666963733,
            0.009421666963733, 0.009421666963733, 0.009421666963733,
            0.009421666963733
        ])

    # 8th order quadrature rule (16 points)
    elif (nOrder == 8):
        dG = np.array(
            [[0.333333333333333, 0.333333333333333, 0.333333333333333],
             [0.081414823414554, 0.459292588292723, 0.459292588292723],
             [0.459292588292723, 0.081414823414554, 0.459292588292723],
             [0.459292588292723, 0.459292588292723, 0.081414823414554],
             [0.658861384496480, 0.170569307751760, 0.170569307751760],
             [0.170569307751760, 0.658861384496480, 0.170569307751760],
             [0.170569307751760, 0.170569307751760, 0.658861384496480],
             [0.898905543365938, 0.050547228317031, 0.050547228317031],
             [0.050547228317031, 0.898905543365938, 0.050547228317031],
             [0.050547228317031, 0.050547228317031, 0.898905543365938],
             [0.008394777409958, 0.263112829634638, 0.728492392955404],
             [0.008394777409958, 0.728492392955404, 0.263112829634638],
             [0.263112829634638, 0.008394777409958, 0.728492392955404],
             [0.263112829634638, 0.728492392955404, 0.008394777409958],
             [0.728492392955404, 0.263112829634638, 0.008394777409958],
             [0.728492392955404, 0.008394777409958, 0.263112829634638]])

        dW = np.array([
            0.144315607677787, 0.095091634267285, 0.095091634267285,
            0.095091634267285, 0.103217370534718, 0.103217370534718,
            0.103217370534718, 0.032458497623198, 0.032458497623198,
            0.032458497623198, 0.027230314174435, 0.027230314174435,
            0.027230314174435, 0.027230314174435, 0.027230314174435,
            0.027230314174435
        ])

    # 4th order quadrature rule (6 points)
    elif (nOrder == 4):

        dG = np.array(
            [[0.108103018168070, 0.445948490915965, 0.445948490915965],
             [0.445948490915965, 0.108103018168070, 0.445948490915965],
             [0.445948490915965, 0.445948490915965, 0.108103018168070],
             [0.816847572980458, 0.091576213509771, 0.091576213509771],
             [0.091576213509771, 0.816847572980458, 0.091576213509771],
             [0.091576213509771, 0.091576213509771, 0.816847572980458]])

        dW = np.array([
            0.223381589678011, 0.223381589678011, 0.223381589678011,
            0.109951743655322, 0.109951743655322, 0.109951743655322
        ])
    # 1st order quadrature rule (1 point)
    elif (nOrder == 1):
        dG = np.array(
            [[0.333333333333333, 0.333333333333333, 0.333333333333333]])
        dW = np.array([1.000000000000000])

    return dG, dW
