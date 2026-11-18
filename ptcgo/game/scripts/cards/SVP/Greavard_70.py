from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46e70a32-1585-5848-8705-c26c351e515b",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    display_name="Greavard",
    searchable_by=["Greavard", "Basic", "Greavard"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=971,
    abilities=[
        Attack(
            title="Graveyard Gamboling",
            game_text="This attack does 10 damage for each Psychic Pok\u00e9mon in your discard pile.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)