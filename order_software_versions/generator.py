import random


def generate_versions(n):
    # Set to store unique versions
    versions = set()

    while len(versions) < n:
        # Generate a random version
        version = "v{}.{}.{}".format(random.randint(0, n), random.randint(0, n), random.randint(0, n))
        versions.add(version)

    return list(versions)

def write_versions_to_file(versions, filename):
    with open(filename, 'w') as file:
        for version in versions:
            file.write(version + '\n')

# Example usage
number_of_versions = 10000000  # Replace with the desired number of versions
generated_versions = generate_versions(number_of_versions)

# Writing to a file
output_filename = "order_software_versions/versions_3.txt"
write_versions_to_file(generated_versions, output_filename)
print(f"Versions written to {output_filename}")


