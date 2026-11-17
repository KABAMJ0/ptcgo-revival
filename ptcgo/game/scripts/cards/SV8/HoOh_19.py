from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d200e087-dd65-5d83-a247-a68796e8ae3d",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Shining Blaze",
            game_text="If you have any Tera Pok\u00e9mon on your Bench, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)