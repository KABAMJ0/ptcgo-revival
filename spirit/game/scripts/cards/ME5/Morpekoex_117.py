from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0ccb05b-d6e3-5717-bbad-a33d9fe1fb55",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpekoex.Name",
    display_name="Morpeko ex",
    searchable_by=["Morpeko ex", "Basic", "ex", "Morpekoex"],
    subtypes=["Basic", "ex"],
    collector_number=117,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Wheely Draw",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hangry Blaster",
            game_text="This attack does 40 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)