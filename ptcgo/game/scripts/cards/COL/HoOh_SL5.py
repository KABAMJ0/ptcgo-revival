from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="eca5eb27-540f-5be3-ae59-36caff8702b9",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name",
    display_name="Ho-Oh",
    searchable_by=["Ho-Oh", "Basic", "HoOh"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Scorching Wing",
            game_text="Flip a coin. If tails, discard all Fire Energy attached to Ho-Oh.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)