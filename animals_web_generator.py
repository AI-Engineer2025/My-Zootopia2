import data_fetcher

OUTPUT_FILE_NAME = "animals.html"


def serialize_animal(animal: dict) -> str:
    """
    Serializes an animal. Fields are omitted from the output
    if they don't exist in the input dictionary.

    Args:
        animal (dict): Animal data dictionary.

    Returns:
        str: HTML list item for the animal.
    """
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal.get("characteristics", {})

    if "diet" in characteristics:
        output += f'      <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in characteristics:
        output += f'      <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    output += "  </p>\n"
    output += "</li>\n"
    return output


def main():
    """Main function to fetch data, build HTML, and save output."""
    animal_name = input("Enter a name of an animal: ").strip().lower()
    animals_data = data_fetcher.fetch_data(animal_name)

    output = "".join(serialize_animal(animal) for animal in animals_data)

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    filled_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(filled_content)


if __name__ == "__main__":
    main()
