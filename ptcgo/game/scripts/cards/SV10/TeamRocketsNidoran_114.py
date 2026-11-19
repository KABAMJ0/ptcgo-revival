from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_or_nothing

card = PokemonCardDef(
    guid="2da3c90b-9123-545d-93d4-1cc218ab468f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoran.Name",
    display_name="Team Rocket's Nidoran♀",
    searchable_by=["Team Rocket's Nidoran\u2640", "Basic", "TeamRocketsNidoran"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=29,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)