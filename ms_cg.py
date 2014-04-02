#!/usr/bin/python

# This code uses connectivity restraints and was written by A Politis,
# Oxford university
import IMP.atom
import IMP.container
import IMP.display
import IMP.statistics
import sys
#import IMP.example

# Number of models to generate
NMODELS = 10000
if '--test' in sys.argv:
    NMODELS = 10

# the spring constant to use, it doesn't really matter
k = 100
# the target resolution for the representation, this is used to specify how detailed
# the representation used should be
resolution = 300
# the box to perform everything in
bb = IMP.algebra.BoundingBox3D(IMP.algebra.Vector3D(0, 0, 0),
                               IMP.algebra.Vector3D(300, 300, 300))


# this function creates the molecular hierarchies for the various involved
# proteins
def create_representation():
    m = IMP.Model()
    all = IMP.atom.Hierarchy.setup_particle(IMP.Particle(m))
    all.set_name("the universe")
    # create a protein, represented as a set of connected balls of appropriate
    # radii and number, chose by the resolution parameter and the number of
    # amino acids.

    def create_protein(name, ds):
        h = IMP.atom.create_protein(m, name, resolution, ds)
        leaves = IMP.atom.get_leaves(h)
        for l in leaves:
            IMP.core.XYZ(l).set_coordinates_are_optimized(True)
        # for convenience, have one molecular hierarchy containing all
        # molecules
        all.add_child(h)
        r = IMP.atom.create_connectivity_restraint([IMP.atom.Selection(c)
                                                    for c in h.get_children()],
                                                   k)
        if r:
            m.add_restraint(r)
            # only allow the particles to penetrate or separate by 1 angstrom
            m.set_maximum_score(r, k)

#    create_protein("ProteinRpn3", [0, 100, 280, 382, 405])
    create_protein("ProteinA", [0, 820, 1065, 2075])
    create_protein("ProteinB", [0, 190, 820, 1485])
#    create_protein("ProteinRpn7", [0, 290, 472,477])
    create_protein("ProteinC", [0, 127, 837, 1172])
    create_protein("ProteinI", [0, 510])
    create_protein("ProteinG", [0, 380, 565])
    create_protein("Protein5", [0, 495, 755])
#    create_protein("ProteinSEM1", [0, 4, 123])
    return (m, all)


# create the needed restraints and add them to the model
def create_restraints(m, all):
    def add_connectivity_restraint(s):
        tr = IMP.core.TableRefiner()
        rps = []
        for sc in s:
            ps = sc.get_selected_particles()
            rps.append(ps[0])
            tr.add_particle(ps[0], ps)
        # duplicate the IMP.atom.create_connectivity_restraint functionality
        score = IMP.core.KClosePairsPairScore(
            IMP.core.HarmonicSphereDistancePairScore(0, 1),
            tr)
        # Work with IMP 2.1 or newer versions
        try:
            r = IMP.core.MSConnectivityRestraint(m, score)
        except NotImplementedError:
            r = IMP.core.MSConnectivityRestraint(score)
        iA = r.add_type([rps[0]])
        iB = r.add_type([rps[1]])
        iC = r.add_type([rps[2]])
        iI = r.add_type([rps[3]])
        iG = r.add_type([rps[4]])
        i5 = r.add_type([rps[5]])
#        n1 = r.add_composite([iA1, iA2, iA3, iA4, iB1, iB2, iC1, iC2, iD1, iD2, iD3, iE1, iE2])
#        n2 = r.add_composite([iA1, iA2, iA3, iA4, iB1, iB2, iC1, iC2, iE1, iE2], n1)
        n1 = r.add_composite([iA, iB, iC, iI, iG, i5])
        n2 = r.add_composite([iA, iB, iC, iI, iG], n1)

        n3 = r.add_composite([iB, iI, iG], n2)
        n4 = r.add_composite([iI, iG], n3)
        n5 = r.add_composite([iB, iI], n3)
        n6 = r.add_composite([iC, i5], n1)
#        n2 = r.add_composite([iA, i5], n1)
#        n3 = r.add_composite([iA, iI], n1)
#        n4 = r.add_composite([iA, iB], n1)
#        n5 = r.add_composite([iA, iC], n1)
#        n6 = r.add_composite([iA, iG], n1)
#        n7 = r.add_composite([iB, i5], n1)
# n17 = r.add_composite([iF, iG], n1) # this connectivity is below 20ID as
# denoted by the experimental data

        m.add_restraint(r)
        m.set_maximum_score(r, k)

    def add_distance_restraint1(s0, s1):
        d1 = -11.9
        r = IMP.atom.create_distance_restraint(s0, s1, d1, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint2(s0, s1):
        d2 = -11.8
        r = IMP.atom.create_distance_restraint(s0, s1, d2, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint3(s0, s1):
        d3 = -8.0
        r = IMP.atom.create_distance_restraint(s0, s1, d3, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint4(s0, s1):
        d4 = -11.3
        r = IMP.atom.create_distance_restraint(s0, s1, d4, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint5(s0, s1):
        d5 = -6.2
        r = IMP.atom.create_distance_restraint(s0, s1, d5, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint6(s0, s1):
        d6 = -2.8
        r = IMP.atom.create_distance_restraint(s0, s1, d6, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint7(s0, s1):
        d7 = 0.0
        r = IMP.atom.create_distance_restraint(s0, s1, d7, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint8(s0, s1):
        d8 = -10.4
        r = IMP.atom.create_distance_restraint(s0, s1, d8, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint9(s0, s1):
        d9 = -11.8
        r = IMP.atom.create_distance_restraint(s0, s1, d9, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint10(s0, s1):
        d10 = -0.4
        r = IMP.atom.create_distance_restraint(s0, s1, d10, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint11(s0, s1):
        d11 = -1.1
        r = IMP.atom.create_distance_restraint(s0, s1, d11, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint12(s0, s1):
        d12 = -6.7
        r = IMP.atom.create_distance_restraint(s0, s1, d12, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint13(s0, s1):
        d13 = -1.1
        r = IMP.atom.create_distance_restraint(s0, s1, d13, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom
        m.set_maximum_score(r, 4 * k)

    def add_distance_restraint14(s0, s1):
        d14 = 0.0
        r = IMP.atom.create_distance_restraint(s0, s1, d14, k)
        m.add_restraint(r)
        # only allow the particles to separate by one angstrom

#    def add_distance_restraint15(s0, s1):
#        d15=58.0
#        r=IMP.atom.create_distance_restraint(s0,s1, d15, k)
#        m.add_restraint(r)
# only allow the particles to separate by one angstrom
#        m.set_maximum_score(r, 2*k)
#        m.set_maximum_score(r, 2*k)

    evr = IMP.atom.create_excluded_volume_restraint([all])
    m.add_restraint(evr)
    # a Selection allows for natural specification of what the restraints act on
#    sE2=S(hierarchy=all, molecule="ProteinRpn11CG1")
    S = IMP.atom.Selection

    sA = S(hierarchy=all, molecule="ProteinA")
    sB = S(hierarchy=all, molecule="ProteinB")
    sC = S(hierarchy=all, molecule="ProteinC")
    sI = S(hierarchy=all, molecule="ProteinI")
    sG = S(hierarchy=all, molecule="ProteinG")
    s5 = S(hierarchy=all, molecule="Protein5")

    add_connectivity_restraint([sA, sB, sC, sI, sG, s5])

#   Intra Distances
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(0, 820)]), S(
        hierarchy=all, molecule="ProteinA", residue_indexes=[(820, 1065)]))  # A3-B1
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(820, 1065)]), S(
        hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]))  # A3-B1

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(0, 190)]), S(
        hierarchy=all, molecule="ProteinB", residue_indexes=[(190, 820)]))  # A3-B1
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(190, 820)]), S(
        hierarchy=all, molecule="ProteinB", residue_indexes=[(820, 1485)]))  # A3-B1

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(0, 127)]), S(
        hierarchy=all, molecule="ProteinC", residue_indexes=[(127, 837)]))  # A3-B1
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(127, 837)]), S(
        hierarchy=all, molecule="ProteinC", residue_indexes=[(837, 1172)]))  # A3-B1

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinG", residue_indexes=[(0, 380)]), S(
        hierarchy=all, molecule="ProteinG", residue_indexes=[(380, 565)]))  # A3-B1
    add_distance_restraint12(S(hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))  # A3-B1

# Inter-distance
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(0, 820)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]))
#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(0 , 820 )]), S(hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))
#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(0 , 820 )]), S(hierarchy=all, molecule="ProteinI", residue_indexes=[(0, 510)]))

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinB", residue_indexes=[(0, 190)]))  # A3-B1
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinB", residue_indexes=[(820, 1485)]))  # A3-B3
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinB", residue_indexes=[(190, 820)]))  # A3-B2

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinC", residue_indexes=[(0, 127)]))  # A3-C1
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinC", residue_indexes=[(837, 1172)]))  # A3-C3
# add_distance_restraint12(S(hierarchy=all, molecule="ProteinA",
# residue_indexes=[(1065 , 2075 )]), S(hierarchy=all, molecule="ProteinG",
# residue_indexes=[(380, 565)]))#A3-G2
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="ProteinI", residue_indexes=[(0, 510)]))  # A3-i
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))  # A3-52
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(1065, 2075)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]))  # A3-52

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(0, 190)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]))
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(0, 190)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(820, 1485)]), S(
        hierarchy=all, molecule="ProteinC", residue_indexes=[(0, 127)]))
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinB", residue_indexes=[(820, 1485)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))

    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(0, 127)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]))
#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(0 , 127)]), S(hierarchy=all, molecule="ProteinI", residue_indexes=[(0, 510)]))
#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(127, 837)]), S(hierarchy=all, molecule="ProteinG", residue_indexes=[(380, 565)]))
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinC", residue_indexes=[(837, 1172)]), S(
        hierarchy=all, molecule="Protein5", residue_indexes=[(495, 755)]))

#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinA", residue_indexes=[(820, 1065)]), S(hierarchy=all, molecule="ProteinG", residue_indexes=[(0, 380)]))
    add_distance_restraint12(S(hierarchy=all, molecule="ProteinG", residue_indexes=[(0, 380)]), S(
        hierarchy=all, molecule="ProteinI", residue_indexes=[(0, 510)]))
#    add_distance_restraint12(S(hierarchy=all, molecule="ProteinI", residue_indexes=[(0, 510)]), S(hierarchy=all, molecule="Protein5", residue_indexes=[(0, 495)]))


# find acceptable conformations of the model
def get_conformations(m):
    sampler = IMP.core.MCCGSampler(m)
    sampler.set_bounding_box(bb)
    # magic numbers, experiment with them and make them large enough for
    # things to work
    sampler.set_number_of_conjugate_gradient_steps(250)
    sampler.set_number_of_monte_carlo_steps(50)
    sampler.set_number_of_attempts(NMODELS)
    # We don't care to see the output from the sampler
    sampler.set_log_level(IMP.SILENT)

    # return the IMP.ConfigurationSet storing all the found configurations that
    # meet the various restraint maximum scores.
    cs = sampler.create_sample()
    return cs

# cluster the conformations and write them to a file
# def analyze_conformations(cs, all, gs):
    # we want to cluster the configurations to make them easier to understand
    # in the case, the clustering is pretty meaningless
#    embed= IMP.statistics.ConfigurationSetXYZEmbedding(cs,
#                 IMP.container.ListSingletonContainer(IMP.atom.get_leaves(all)), True)
#    cluster= IMP.statistics.create_lloyds_kmeans(embed, 5, 10000)
    # dump each cluster center to a file so it can be viewed.
#    for i in range(cluster.get_number_of_clusters()):
#        center= cluster.get_cluster_center(i)
#        cs.load_configuration(i)
#        w= IMP.display.PymolWriter("cluster.%d.pym"%i)
#        for g in gs:
#           w.add_geometry(g)


# now do the actual work
(m, all) = create_representation()
IMP.atom.show_molecular_hierarchy(all)
create_restraints(m, all)


# in order to display the results, we need something that maps the particles onto
# geometric objets. The IMP.display.Geometry objects do this mapping.
# IMP.display.XYZRGeometry map an IMP.core.XYZR particle onto a sphere
gs = []
for i in range(all.get_number_of_children()):
    color = IMP.display.get_display_color(i)
    n = all.get_child(i)
    name = n.get_name()
    g = IMP.atom.HierarchyGeometry(n)
    g.set_color(color)
    gs.append(g)

cs = get_conformations(m)
# print cs

# Report solutions
print "found", cs.get_number_of_configurations(), "solutions"

for i in range(0, cs.get_number_of_configurations()):
    cs.load_configuration(i)
    # print the configuration
    print "solution number: ", i, "scored :", m.evaluate(False)
ListScores = []
for i in range(0, cs.get_number_of_configurations()):
    cs.load_configuration(i)
    # print the configuration
    print "solution number: ", i, "scored :", m.evaluate(False)
    ListScores.append(m.evaluate(False))
    print ListScores

f1 = open("out_scores_eif3-cor2.txt", "w")
f1.write("\n".join(map(lambda x: str(x), ListScores)))
f1.close()

# for each of the configuration, dump it to a file to view in pymol
for i in range(0, cs.get_number_of_configurations()):
    cs.load_configuration(i)
    w = IMP.display.PymolWriter("conf_eif3.%d.pym" % i)
    for g in gs:
        w.add_geometry(g)
# Report solutions

#analyze_conformations(cs, all, gs)
# print m.evaluate(False)
