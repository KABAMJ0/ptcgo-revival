from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d9401f17-b459-5df0-921e-70e4566368f8",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsSpidops.Name",
    display_name="Team Rocket's Spidops",
    searchable_by=["Team Rocket's Spidops", "Stage 1", "TeamRocketsSpidops"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTarountula.Name",
    family_id=917,
    abilities=[
        Ability(
            title="Charging Up",
            game_text="Once during your turn, you may attach a Basic Energy card from your discard pile to this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=attach_from_discard(is_basic_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Rocket Rush",
            game_text="This attack does 30 damage for each of your Team Rocket's Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)