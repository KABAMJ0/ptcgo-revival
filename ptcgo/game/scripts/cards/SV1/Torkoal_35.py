from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0b686d2a-a400-5934-9339-10040300f93c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name",
    display_name="Torkoal",
    searchable_by=["Torkoal", "Basic", "Torkoal"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=324,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Concentrated Fire",
            game_text="Flip a coin for each Fire Energy attached to this Pok\u00e9mon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)