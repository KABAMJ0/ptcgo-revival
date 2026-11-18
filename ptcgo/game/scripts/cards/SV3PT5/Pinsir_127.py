from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42781e34-68d2-5955-8116-04d9d584ed06",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Reckless Throw",
            game_text="If you have more Prize cards remaining than your opponent, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)