from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1c324b52-bc40-56c1-8bd0-b6bcba5abbb6",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=238,
    abilities=[
        Ability(
            title="Sweet Sleeping Face",
            game_text="As long as Smoochum is Asleep, prevent all damage done to Smoochum by attacks.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Antics",
            game_text="Move an Energy card attached to 1 of your opponent's Pok\u00e9mon to another of your opponent's Pok\u00e9mon. Smoochum is now Asleep.",
            cost={},
            effect=unimplemented,
        ),
    ],
)