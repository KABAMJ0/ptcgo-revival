from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.support_common import can_move_energy, \
    move_energy_between
from ptcgo.game.card_effects.trainers import named_exactly
from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


_PLASMA_ENERGY = named_exactly("Plasma Energy")


card = PokemonCardDef(
    guid="eda663c5-b213-53b8-8953-cf5e9a33ff7d",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "Team Plasma", "PorygonZ"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=74,
    set_code="BW10",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Plasma Transfer",
            game_text="As often as you like during your turn (before your attack), you may move a Plasma Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=can_move_energy(_PLASMA_ENERGY),
            effect=move_energy_between(_PLASMA_ENERGY, count=1,
                                       prompt="Choose a Plasma Energy to move"),
        ),
        Attack(
            title="Tri Attack",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=50),
        ),
    ],
)