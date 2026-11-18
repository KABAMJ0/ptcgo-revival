from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35a02942-7101-5c75-8dc1-d7c92a6e70ae",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic", "Seel"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="EX6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Horn Hazard",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)