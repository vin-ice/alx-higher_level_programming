#!/usr/bin/python3
def mat(m_a, m_b):
    m_ab = []
    for row_na in range(len(m_a)):
        m_abr = []
        for col_na in range(len(m_a[row_na])):
            cell_ab = 0 
            for cell_na in range(len(m_a[row_na])):
                cell_ab += m_a[row_na][cell_na] * m_b[cell_na][col_na]
            m_abr.append(cell_ab)
        m_ab.append(m_abr)
    return m_ab

print("{}".format(mat([[1, 2], [3, 4]], [[100, 200], [300, 400]])))
print("{}".format(mat([[1.2, 2.4],[3.4, 4.5]], [[100, 200], [300, 400]])))
