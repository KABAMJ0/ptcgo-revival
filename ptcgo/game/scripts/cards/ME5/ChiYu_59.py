from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e46a2813-d9b5-5529-a986-51c44ad9dd20",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu", "Basic", "ChiYu"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1004,
    abilities=[
        Attack(
            title="Whirling Envy",
            game_text="If this Pok\u00e9mon has 2 or more damage counters on it, this attack does 90 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)