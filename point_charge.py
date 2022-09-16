import math

oofpez = 9 * pow(10,9)


class vector:
    def __init__(self, x, y, z, q):
        self.x = x
        self.y = y
        self.z = z
        self.q = q

        self.mag = math.sqrt(math.pow(x, 2) + math.pow(y,2) + math.pow(z,2))

    def __repr__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"

    def scalmult(self, other):
        return vector(self.x * other, self.y * other, self.z * other, 0)

    def vecmult(self, vec_other):
        return vector(self.x * vec_other.x, self.y * vec_other.y, self.z * vec_other.z,0)

    def hat(self):
        x_hat = self.x / self.mag
        y_hat = self.y / self.mag
        z_hat = self.z / self.mag
        return vector(x_hat, y_hat, z_hat, 0)

def point_charge(vec1, vec2):
    r = vector(vec2.x - vec1.x, vec2.y - vec1.y, vec2.z - vec1.z,0)
    r_hat = r.hat()
    constant = oofpez * (vec1.q / pow(r.mag,2))
    return r.scalmult(constant)
