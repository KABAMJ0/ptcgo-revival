from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbac29e7-cda4-5012-bcef-b37db594d0cc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTail.Name",
    display_name="Scream Tail",
    searchable_by=["Scream Tail", "Basic", "Ancient", "ScreamTail"],
    subtypes=["Basic", "Ancient"],
    collector_number=86,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=985,
    abilities=[
        Attack(
            title="Slap",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Roaring Scream",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon for each damage counter on this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)